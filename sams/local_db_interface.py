import sqlite3
import threading
from spotbot import logger

class LocalDbInterface:

    def __init__(self, local_db_file_name):
        # establish DB connection
        self.crit_section_lock = threading.Lock()
        self.db_file_name = local_db_file_name
        self.db_con = sqlite3.connect(database = self.db_file_name, isolation_level = "DEFERRED", check_same_thread = False)
        self.db_con.row_factory = sqlite3.Row
        self.db_cursor = self.db_con.cursor()
        logger.debug(f"local sqlite DB {self.db_file_name} connection established")


    def execute(self, sql, binds = {}):
        with self.crit_section_lock:
            self.db_cursor.execute(sql, binds)
            results = self.db_cursor.fetchall()
            self.db_con.commit()
        return results


    def execute_values(self, sql, records):
        with self.crit_section_lock:
            results = self.db_cursor.executemany(sql, records)
            self.db_con.commit()
        return results


    def close(self):
        self.db_cursor.close()
        self.db_con.close()
        logger.debug(f"local sqlite DB {self.db_file_name} connection closed")


if __name__ == "__main__":

    logger.info("starting unit tests")

    def _dump_result_set(rs):
        logger.info(f"dumping result set: {results}")
        for row in results:
            print(f"row[{row['record_id']}]: profiler name = {row['profiler_name']}, log_sequence = {row['log_sequence']}")


    import os
    local_db_file_name = "c:/4/spotbot.db"
    os.remove(local_db_file_name)

    ldbi = LocalDbInterface(local_db_file_name)

    import spotbot_profiler
    spotbot_profiler.create_local_db_objects(ldbi)

    # single insert test
    ldbi.execute("""
        INSERT INTO test_profiler_log (
            test_id,
            iteration,
            profiler_name,
            log_sequence,
            data_structure,
            record_modified_ts
        ) VALUES (
            1,
            :iteration,
            'matts profiler',
            1,
            '{some data structure}',
            'current time'
        )
    """, {
        "iteration": 99
    })
    #results = ldbi.execute("SELECT * FROM test_profiler_log")
    #_dump_result_set(results)

    # bulk insert test
    records = []
    for i in range(0, 500):
        records += [(1, 1, 'some prof', i, f'data struct {i}', f'current time {i}')]

    logger.info("bulk insert start")
    results = ldbi.execute_values("""
        INSERT INTO test_profiler_log (
            test_id,
            iteration,
            profiler_name,
            log_sequence,
            data_structure,
            record_modified_ts
        ) VALUES (?, ?, ?, ?, ?, ?)
        """, records
    )
    logger.info("bulk insert end")
    #results = ldbi.execute("SELECT * FROM test_profiler_log")
    #_dump_result_set(results)

    ldbi.close()
    logger.info("done")
