1. rename annotation_point to annotation_point_prod
2. create new annotation_point (PARTITIONED)
    DROP FK CONSTRAINST annotation_point_prod ???
    
4. populate new annotation_point FROM  annotation_point_prod
   where test_date >= ' ' and test_date <= ' '

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

### Issue - renaming the table automaticall get reflected in FK
column record_id in table tracking_point is used as FK in 
```
table                               constraint_name
annotation_tracking_jump              fk_atj_fprid
annotation_tracking_tunnel_recovery   fk_attr_fprid
annotation_tracking_early_termination fk_atet_fprid
annotation_tracking_lost_position     fk_atlp_fprid
```

remove foreign key constraint
```
ALTER TABLE your_tbl DROP constraint your_cnstrnt;
```
how to disable foreign key constraint in postgresql
```
ALTER TABLE tbl_StudentMarks DISABLE TRIGGER ALL;

I created the partitioned table in Postgres 15:

CREATE TABLE T (
	id bigserial NOT NULL,
        date DATE,
        ..., 
        primary key(record_id, test_date)
)PARTITION BY RANGE (test_date);

I added several partitions like this:
CREATE TABLE T_2020 PARTITION OF T for values from ('2020-01-01') to ('2021-01-01');
CREATE TABLE T_2021 PARTITION OF T for values from ('2021-01-01') to ('2022-01-01');

Question: is it guaraneed that the id (bigserial)  column will be unique across all partitions?
I see from metadata that there is just 1 sequence for T table created automatically for this bigserial column,
so there is no individual sequence per partition.
Does it mean that id column will be unique across all partitions?
