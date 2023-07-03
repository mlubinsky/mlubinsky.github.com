import json
import logging

class AnnotationParser:

    def __init__(self, db, db_cursor, test_package_id, report_date_root):
        self.logger = logging.getLogger("spotlight_etl.annotation_parser")
        self.db = db
        self.db_cursor = db_cursor
        self.test_package_id = test_package_id
        self.report_date_root = report_date_root

    def load_annotations(self):
    ############################        
        self.logger.info("load_annotations begin")

        self.logger.info("scanning for annotation json files")
        self.db_cursor.execute("""
            SELECT file_id,
                   file_system_path
            FROM   file
            WHERE  test_package_id = %(test_package_id)s
               AND file_type = 'file'
               AND file_system_path LIKE %(log_pattern)s
            ORDER BY file_system_path
            """, {
                "test_package_id": self.test_package_id,
                "log_pattern": "%/annotations.json"
            }
        )
        for record in self.db_cursor.fetchall():
            annotation_file_id = record[0]
            annotation_file_name = self.report_date_root + record[1]
            self.logger.info("processing annotation_file " + str(annotation_file_id) + ": " + annotation_file_name)
            try:
                self.parse(annotation_file_id, annotation_file_name)
                self.db.commit()
            except Exception as e:
                self.db.rollback()
                self.logger.warn("annotation_parser exception: " + str(e))

        self.logger.info("load_annotations complete")

    def parse(self, annotation_file_id, annotation_file_name):
    #############################################################
        with open(annotation_file_name) as annotation_file:
            annotations = json.load(annotation_file)["annotations"]

        # the auto analysis side generating the input json is sometimes producing duplicate records, collect distinct ones to process
        distinct_annotations = []
        for annotation in annotations:
            if annotation not in distinct_annotations:
                distinct_annotations += [annotation]
        annotations = distinct_annotations

        for annotation in annotations:
            annotation_type = annotation["annotation_type"]

            # create header record
            self.db_cursor.execute("""
                INSERT INTO annotation_header (
                    annotation_type,
                    test_package_id,
                    subject,
                    annotation_text,
                    status,
                    jira_key
                ) VALUES (
                    %s,
                    %s,
                    %s,
                    ('[' || TO_CHAR(CURRENT_TIMESTAMP, 'YYYY-MM-DD HH24:MI TZ') || ' --- AUTO GENERATED]:' || CHR(13) || %s),
                    %s,
                    %s
                )
                RETURNING annotation_id
                """, (
                annotation_type,
                self.test_package_id,
                annotation["subject"],
                annotation["annotation_text"],
                "Closed" if annotation_type == "INFO" else "Pending Triage",
                annotation["jira_key"])
            )
            annotation_id = self.db_cursor.fetchone()[0]

            key_words = annotation["key_words"]
            if key_words is None:
                key_words = []

            if annotation_type == "INFO":
                key_words = ["AUTO GENERATED"] + key_words
            else:
                key_words = ["AUTO GENERATED", "PROFILER EXCEPTION"] + key_words

            for index, key_word in enumerate(key_words):
                self.db_cursor.execute("""
                    INSERT INTO annotation_key_word (
                        annotation_id,
                        key_word,
                        key_word_sequence
                    ) VALUES (%s, %s, %s)
                    """, (
                    annotation_id,
                    key_word,
                    index + 1)
                )

            selection_string = None
            nav_gps_log_id = None
            subject = annotation["subject"]

            if annotation_type in ["INFO", "NAV_GPS_LOG", "RAWBIN_HOST_LOG"]:

                # look up nav gps log id by path
                log_file_path = annotation_file_name.replace(self.report_date_root, "").replace("\\", "/")
                self.db_cursor.execute("""
                    SELECT MIN(h.log_id) log_id,
                           MIN(dut.device_label) device_label
                    FROM   file annotations_file
                           INNER JOIN file header_file ON
                                annotations_file.test_package_id = header_file.test_package_id
                                AND REPLACE(annotations_file.file_system_path, 'annotations.json', 'nav.decrypted.gps') = header_file.file_system_path
                           INNER JOIN nav_gps_log_header h ON
                                header_file.test_package_id = h.test_package_id
                                AND header_file.file_id = h.log_file_id
                           INNER JOIN device_under_test dut ON h.device_id = dut.device_id
                    WHERE  annotations_file.file_id = %(annotation_file_id)s
                    """, {"annotation_file_id": annotation_file_id}
                )
                rec = self.db_cursor.fetchone()
                nav_gps_log_id = rec[0]
                device_label = rec[1]
                if device_label is not None:
                    subject = device_label + " - " + subject

                selection_text = []
                for selection_range in annotation["selection_ranges"]:
                    line_start = selection_range["line_start"]
                    line_end = selection_range["line_end"]
                    self.db_cursor.execute("""
                        INSERT INTO annotation_nav_gps_line_range (
                            annotation_id,
                            log_line_start,
                            log_line_end
                        ) VALUES (%s, %s, %s)
                        """, (
                        annotation_id,
                        line_start,
                        line_end)
                    )

                    if line_start == line_end:
                        selection_text += [str(line_start)]
                    else:
                        selection_text += [str(line_start) + "-" + str(line_end)]
                selection_string = ", ".join(selection_text)

            self.db_cursor.execute("""
                UPDATE annotation_header
                SET    selection_string = %s,
                       nav_gps_log_id = %s,
                       subject = %s
                WHERE  annotation_id = %s
                """, (selection_string, nav_gps_log_id, subject, annotation_id)
            )

            self.logger.info("created " + annotation_type + " annotation with ID " + str(annotation_id))
