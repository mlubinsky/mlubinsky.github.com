```
CREATE TABLE tracking_point_part ( ... )
ALTER TABLE tracking_point RENAME TO tracking_point_prod; 
ALTER TABLE tracking_point_part RENAME TO tracking_point;

issue above : after renaming the table FK into renamed table from other tables are automatically started to point into renamed table!!!

CREATE TABLE annotation_tracking_lost_position (
	selection_id        BIGSERIAL PRIMARY KEY,
	annotation_id       BIGINT NOT NULL,
	tracking_header_id  BIGINT NOT NULL,
	fix_point_record_id BIGINT NOT NULL
);

ALTER TABLE annotation_tracking_lost_position ADD CONSTRAINT fk_atlp_aid FOREIGN KEY (annotation_id) REFERENCES annotation_header(annotation_id);
ALTER TABLE annotation_tracking_lost_position ADD CONSTRAINT fk_atlp_thid FOREIGN KEY (tracking_header_id) REFERENCES tracking_header(header_id);
ALTER TABLE annotation_tracking_lost_position ADD CONSTRAINT fk_atlp_fprid FOREIGN KEY (fix_point_record_id) REFERENCES tracking_point(record_id);
CREATE INDEX i_atlp_aid ON annotation_tracking_lost_position(annotation_id);
```

### db/function/delete_test_package.sql
  NEW LINE:
 
	DELETE FROM tracking_point WHERE test_package_id = p_test_package_id;

### db/function/generate_tracking.sql
```
BEGIN

	-- remove any existing tracking test records for this report date
  ### NEW LINE !
	DELETE FROM tracking_point WHERE test_package_id = p_test_package_id; 

	DELETE FROM tracking_header
	WHERE  header_id IN (
		SELECT tracking_header.header_id
		FROM   test_header
			   INNER JOIN tracking_header ON test_header.test_id = tracking_header.test_id
		WHERE  test_header.test_package_id = p_test_package_id
	);
```


### db/function/generate_tracking_point_data.sql
```
BEGIN

	-- generate and store off tracking test point data
	INSERT INTO tracking_point (
		header_id,
		fix_utc,
		latitude,
		longitude,
		fix_point_geom,
		meas_eval_2d_error,
		dynamic_tracking_2d_error,
		meters_from_last_fix,
		seconds_from_last_fix,
		test_package_id
	)
	WITH log_ids AS (
		SELECT tracking_header.header_id,
			   tracking_header.nmea_log_id,
			   tracking_header.meas_eval_log_id,
			   tracking_header.dynamic_tracking_error_log_id,
			   test_header.test_package_id
		FROM   test_header
			   INNER JOIN tracking_header ON test_header.test_id = tracking_header.test_id
		WHERE  test_header.test_package_id = p_test_package_id
	)
```
### db/table/tracking_point.sql
```
CREATE TABLE tracking_point (
	record_id                     BIGSERIAL PRIMARY KEY,
	header_id                     BIGINT,
	fix_utc                       TIME,
  ...
	test_package_id               BIGINT NOT NULL
);

ALTER TABLE tracking_point ADD CONSTRAINT fk_tp_hid FOREIGN KEY (header_id) REFERENCES tracking_header(header_id);
ALTER TABLE tracking_point ADD CONSTRAINT fk_tp_tpid FOREIGN KEY (test_package_id) REFERENCES test_package(test_package_id);
```
