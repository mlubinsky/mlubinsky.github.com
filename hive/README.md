### Header

SET hive.cli.print.header=true;

### Order by positional

SET hive.groupby.orderby.position.alias=true;

### See Hive settings

hive -e "SET;" | grep <Search-String> 


### Timestamp + interval

https://stackoverflow.com/questions/73264703/hive-how-to-add-dynamic-interval-from-the-column


## If CTE is used many times then better to materialize it:

SET hive.default.fileformat=Orc; 

SET hive.optimize.cte.materialize.threshold=2;


###  Issue
```
select  count(*)  from A where date_key = '2022-07-12' 
Result: 0

But slightly modified query  gives  another result:

select date_key, count(*) from A where date_key > '2022-07-10'  group by date_key;
Result:
2022-07-12	2281097
	
It usually happens when the metadata is not available for that date_key with hive. Try running this:
	
ANALYZE TABLE hive_table PARTITION(partitioned_col) COMPUTE STATISTICS

The  first query output is usually pulled from metadata and second query needs processing.	
 
ANALYZE TABLE solved this issue.

set hive.compute.query.using.stats=false

Doing this would ensure that hive wouldn't use the stats/cache that it has but to run the map reduce job to calculate the counts. Would be handy to use when adding/pointing new partitions to an existing table.
if you are inserting the data into the table directly, hive auto generates the new stats using the setting below.

set hive.stats.autogather=true

use this only for adhoc queries when in need. Analyze table is still a standard way to get the counts updated
```
#### Repair

```
GRANT SELECT ON TABLE a TO ROLE public;

set hive.msck.path.validation=ignore;
msck repair table my_schema.my_table;

```


MSCK REPAIR TABLE

emrfs synch  https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emrfs-cli-reference.html

### Hive UDF
https://stackoverflow.com/questions/13940498/how-to-create-a-hive-udf-for-all-sessions

```
CREATE FUNCTION sbschema.roku_get_business_channel_id as 'com.roku.dea.hive.udfs.BusinessChannelUdf' USING JAR 's3://roku-dea-dev/sandbox/mlubinsky/hiveUdf.jar';

aws s3 cp hiveUdf.jar s3://roku-dea-dev/sandbox/mlubinsky/

DESCRIBE FUNCTION EXTENDED sbschema.roku_get_business_channel_id;
```

### Avro
column which contains array of strings
```
{ 
  "name":"parameters",  
  "type": { 
      "type": "array",
      "items": "string"
   } 
}
```


### Add column in the middle

first add the column user_id to the table with below command:

ALTER TABLE table_name ADD COLUMNS (user_id BIGINT);

To make user_id column as the first column in your table use change column with FIRST clause:

 ALTER TABLE table_name CHANGE COLUMN user_id user_id BIGINT first;

Use AFTER instead of FIRST if you want to move the specified column after any other column. Like say, I want to move DOB column AFTER  user_id column:

ALTER TABLE table_name CHANGE COLUMN dob dob date AFTER user_id;

Please note that this commands changes metadata only. 
If you are moving columns, the data must already match the new schema or you must change it to match by some other means.

https://habr.com/ru/post/585460/

https://medium.com/swlh/hive-optimization-quick-refresher-5e596654bc1d
```
SET hive.execution.engine=tez;

Vectorization
SET hive.vectorized.execution=true;
SET hive.vectorized.execution.enabled=true;

Predicate push down
SET hive.optimize.ppd=true;

Join Optimizations
SET hive.auto.convert.join=true;
SET hive.auto.convert.join.noconditionaltask=true;

SMB Join
SET hive.auto.convert.sortmerge.join=true;
SET hive.optimize.bucketmapjoin=true;
SET hive.optimize.bucketmapjoin.sortedmerge=true;

If tables are bucketed and sorted SMB join should be converted to SMB Map-Join.
SKEWED TABLE
CREATE TABLE <table_name>(col1 STRING, col2 STRING)
SKEWED BY (col1) ON (col_val1, col_val2, col_val3) 
[STORED AS DIRECTORIES];

SKEWED JOIN
SET hive.optimize.skewjoin=true;
SET hive.skewjoin.key=500000;

Cost based optimization
SET hive.cbo.enable=true;
SET hive.compute.query.using.stats=true;
SET hive.stats.fetch.column.stats=true;
SET hive.stats.fetch.partition.stats=true;
```
https://tech.trivago.com/2019/01/30/a-new-functional-approach-to-complex-types-in-apache-hive/

https://stackoverflow.com/questions/69576832/how-to-use-hive-macro-to-reduce-boilerplate

https://stackoverflow.com/questions/69591239/problem-with-explode-in-hive-or-spark-query

## File formats: Avro, Parquet

pip install parquet-tools

https://pypi.org/project/parquet-tools/

DuckDB for parquet

https://duckdb.org/docs/data/parquet.  https://duckdb.org/2021/06/25/querying-parquet.html

https://parquet.apache.org/documentation/latest/


https://medium.com/swlh/insights-into-parquet-storage-ac7e46b94ffe

parquet-tools meta hdfs://host:port/<location>/file1

<https://habr.com/ru/company/mailru/blog/504952/> Avro, Parquet, ...

<https://habr.com/ru/post/530422/> protobuf vs Avro

pip install pyorc. https://pypi.org/project/pyorc/

https://github.com/uber/petastorm. Parquet format. 

reading parquet from python: https://duckdb.org/2021/06/25/querying-parquet.html

Convert avro to JSON
```
curl -O http://central.maven.org/maven2/org/apache/avro/avro-tools/1.8.1/avro-tools-1.8.1.jar

java -jar avro-tools-1.8.1.jar tojson --pretty [job_output].avro > output.json
```

### 2 ways to insert into partition table
```
INSERT INTO zipcodes PARTITION(state='FL') VALUES 
(891,'US','TAMPA',33605);
```
Here it’s mandatory to keep the partition column as the last column.

```
INSERT INTO zipcodes PARTITION(state) VALUES 
(891,'US','TAMPA',33605,'FL');
```

### zip file processing

https://cwiki.apache.org/confluence/display/Hive/CompressedStorage

load data local inpath '/home/hdfs/employee_gz.gz' into table employee_gz;

```
echo {a..c}{1..100} | xargs -n 100 | tr ' ' '|'  | \
hdfs dfs -put - /user/hive/warehouse/mytable/data.txt

create external table mytable
(
    col58   string
   ,col64   string
   ,col65   string
)
row format serde 'org.apache.hadoop.hive.serde2.RegexSerDe'
with serdeproperties ("input.regex" = "^(?:([^|]*)\\|){58}(?:([^|]*)\\|){6}([^|]*)\\|.*$")
stored as textfile
location '/user/hive/warehouse/mytable'
;
```
Another example
http://alvincjin.blogspot.com/2014/11/hive-load-csvgz-files.html
```
CREATE TABLE csv_table (line STRING)
ROW FORMAT DELIMITED FIELDS TERMINATED BY '\t' 
LINES TERMINATED BY '\n'
tblproperties ("skip.header.line.count"="1");
 
LOAD DATA LOCAL INPATH '/tmp/weblogs/20090603-access.log.gz' INTO TABLE csv_table;

SET hive.exec.compress.output=true;
SET io.seqfile.compression.type=BLOCK; -- NONE/RECORD/BLOCK
INSERT OVERWRITE TABLE csv_table_sequence SELECT * FROM csv_table;
```
https://github.com/bernhard-42/spark-unzip

since it is not splittable, every zipfile will be read by exactly one mapper (low parallelism)

https://stackoverflow.com/questions/43094458/creating-external-table-from-compressed-gz-format-files-without-selecting-all

http://cutler.io/2012/07/hadoop-processing-zip-files-in-mapreduce/

https://github.com/bernhard-42/spark-unzip

https://stackoverflow.com/questions/56158947/processing-loading-huge-gzip-file-into-hive
	
## Struct
	Select STRUCT is NULL is always false.

### Array of structures  :

select array(named_struct("person_id","1","first_name","ooo"));

Answer:
	[{"person_id":"1","first_name":"ooo"}]

### How to insert NULL in struct
	
	https://issues.apache.org/jira/browse/HIVE-4022
	
Given table T with 3 columns:
```
C1 string
C2 struct<c2_a:array<string>, c2_c:string>
C3 array<struct<c3_a:string, c3_b:string>>	

insert into T
select 'c1_val',
	named_struct(
	   'c2_a',array(cast (null as string)),
	   'c2_c',cast (null as string)
	),
	 array(named_struct(
	        'c3_a',cast (null as string) ,
	        'c3_b',cast (null as string))
	 ) 
from z_dummy;
```
 



### Explode and LATERAL VIEW

```
select col1, explode(split(col2,'\\s')) from table_name;

SemanticException [Error 10081]: UDTF's are not supported outside the SELECT clause, nor nested in expressions
```
 solution
 ```
 select s.code, exp.splitted
  from sample_07 s
  lateral view explode(split('asdfa adsfa asdaf asdfad','\\s')) exp as splitted
  
  
  
 SELECT employee_id, employee_name, employee_telephone, employee_date, addr_city, addr_street, addr_zipcode, dept_name, dept_director, dept_budget

FROM employee

LATERAL VIEW json_tuple (employee.json, 'id', 'name', 'telephone', 'date', 'address', 'department') emp AS employee_id, employee_name, employee_telephone, employee_date, employee_address, employee_department

LATERAL VIEW json_tuple (emp.employee_address, 'city', 'street', 'zipcode') addr AS addr_city, addr_street, addr_zipcode

LATERAL VIEW json_tuple (emp.employee_department, 'name', 'director', 'budget') dept AS dept_name, dept_director, dept_budget 
  
  
```

Another example of lateral view/explode:
```
select
 lat.* from (select 0) t
 lateral view
 explode(array('A','B','C')) lat
```

#### important: SET hive.map.aggr=false;
```
SET hive.map.aggr=false;

WITH A AS (
SELECT 1 as id, array(
                     'subbrand_cbs',
                     'subbrand_nickelodeon',
                     'subbrand_mtv',
                     'subbrand_bet',
                     'subbrand_comedycentral',
                     'subbrand_smithsonian'
                    ) as tags
UNION ALL
SELECT 2 as id, array( 'nikelsonseries_roku', 'nikelson2series_roku' )  as tags
UNION ALL
SELECT 3 as id, array('nickelodeon', '123_movie_roku') as tags
)

SELECT A.id, A.tags,
concat_ws(' ',
  collect_set(
         CASE
            WHEN tag LIKE 'subbrand_%' THEN SUBSTR(tag,10)
            ELSE NULL
         END
    )
)
as provider_sub_brand

FROM A LATERAL VIEW OUTER EXPLODE(tags) t as tag
 GROUP BY A.id, A.tags
```


#### How to parse JSON array:
```
WITH T as
(
  SELECT
  'key1' as key,
  '[{"website":"baidu.com","name":" Baidu "},{"website":"google.com","name":" Google "}]' as value
  UNION ALL
  SELECT
  'key2' as key,
  '[{"website":"yandex.com","name":" YANDEX "}]' as value
)
select
key,
tmp
FROM T 
LATERAL VIEW
explode(
        split(
            regexp_replace(
                regexp_replace(
                  value,
                  '\\[|\\]',
                  ''
                ),
             '\\}\\,\\{',
             '\\}\\;\\{'
            ),
         '\\;'
        )
       ) tmp_t as tmp
```
 Result:
 ```
 key1	{"website":"baidu.com","name":" Baidu "}
 key1	{"website":"google.com","name":" Google "}
 key2	{"website":"yandex.com","name":" YANDEX "}
 ```
 Issue: the result above is not good: use json_tuple or get_json_object() to convert the json in 2 separate columns: website and name
 
 Solution: use GET_JSON_OBJECT
``` 
 WITH T as
(
  SELECT
  'key1' as key,
  '[{"website":"baidu.com","name":" Baidu "},{"website":"google.com","name":" Google "}]' as value
  UNION ALL
  SELECT
  'key2' as key,
  '[{"website":"yandex.com","name":" YANDEX "}]' as value
)
select
key,
GET_JSON_OBJECT(tmp,'$.website') as website,
GET_JSON_OBJECT(tmp,'$.name') as name,
tmp
FROM T 
LATERAL VIEW
explode(
        split(
            regexp_replace(
                regexp_replace(
                  value,
                  '\\[|\\]',
                  ''
                ),
             '\\}\\,\\{',
             '\\}\\;\\{'
            ),
         '\\;'
        )
       ) tmp_t as tmp
```
Result
```

key1	baidu.com	 Baidu 	{"website":"baidu.com","name":" Baidu "}
key1	google.com	 Google 	{"website":"google.com","name":" Google "}
key2	yandex.com	 YANDEX 	{"website":"yandex.com","name":" YANDEX "}
```

### JSON processing: get_json _object and json_tuple()

https://community.cloudera.com/t5/Support-Questions/Complex-Json-transformation-using-Hive-functions/td-p/236476

#### json_tuple(string jsonStr,string k1,...,string kn)

json_tuple takes JSON string and a set of n keys, and returns a tuple of n values. This is a more efficient version of the get_json_object UDF because it can get multiple keys with just one call.

json_tuple() takes a set of keys and a JSON string. Then returns a tuple of values. 
The json_tuple() UDF uses the lateral view syntax in Hive, which enables json_tuple() to create a virtual table 
by applying the UDT function to each row of the original table. 
Complex JSONs become too unwieldy because of the repeated use of LATERAL VIEW. 
Furthermore, JSON_TUPLE can't handle nested JSONs.

https://docs.microsoft.com/en-us/azure/hdinsight/hadoop/using-json-in-hive
	
### MAP and STRUCT
	
	https://datadojo.dev/2020/06/07/working-with-complex-datatypes-in-hive/
```	
-- map example	
	SELECT 
	first_name, 
	grade["math"] AS math_grade 
FROM 
	students
 --- struct example	-- structs can be accessed through DOT (.). 
SELECT 
	first_name, 
	teacher.math AS math_teacher 
FROM 
	student
```
	

### Array of maps :

select array(map("language","string")) 

## DRUID and Hive REGEXP_EXTRACT()

How to match till 1st occurance of char:
https://stackoverflow.com/questions/2013124/regex-matching-up-to-the-first-occurrence-of-a-character

```
. stands as a wildcard for any one character, and the * means to repeat whatever came before it any number of times. 
In a .* regular expression, the Java single wildcard character is repeated, 
effectively making the .* regular expression operate the same way as the * wildcard does elsewhere in SQL.



select regexp_extract('foot,heyz,bar', 'ba[^,]+', 0)  -- bar
select regexp_extract('foot,heyz,bar', 'h[^,]+', 0)  -- heyz

select regexp_extract('foot,heyz,bhar', 'k[^,]+', 0)  -- exception because there is not k in the string!


     select   regexp_extract('foot,heyz,bar,' , 'ba.*?,', 0)  -- bar,
     UNION ALL
     select   regexp_extract('foot,heyz,bar,' , 'foo.*?,' , 0)  -- foot.
     UNION ALL
     select   regexp_extract('foot,heyz,bar,' , 'h.*?,', 0)  -- heys,



   select   regexp_extract('foot,heyz,bar,' , 'bar(.*?)([^,])', 0) - ERROR
   
   select   regexp_extract('foot,heyz,bar,' , 'bar(.*?,)', 0)    bar,
   select   regexp_extract('foot,heyz,bar,' , 'bar.*?,', 0)

    select   regexp_extract('foot,heyz,bar' , 'ba.*?[^,]', 0)  -- bar
    UNION ALL
    select   regexp_extract('foot,heyz,bar' , 'fo.*?[^,]', 0)  -- foo . - lost last char
    UNION ALL
    select   regexp_extract('foot,heyz,bar' , 'he.*?[^,]', 0)  -- hey . lost last char
    
    Add comma to the end of intput string:
    select   regexp_extract('foot,heyz,bar,' , 'foo.*?,[^,]', 0)  -- foot,h .  what is it exta chars , h



```
Get 2nd substring in comma separated list:
```
SELECT REGEXP_EXTRACT('sales,agent', '(.*),(.*)', 2) as last_name
Answer:
agent
```

Get substr started from pattern hey and ended by ,
```

  select   regexp_extract('foot,heyz,bar' , 'fo.*,', 0) 
  Answer: foot,heyz,
  
  select   regexp_extract('foot,heyz,bar' , 'fo.*?,', 0)
  Answer: foot,
  because ? makes search non-greedy !!!
   
 select   regexp_extract('foot,heyz,bar', 'hey.*,', 0)
 Answer: heyz
 
 
 select   regexp_extract('foot,heyz,bar,' , 'ba.*?,' , 0)
 Anser: bar:
```
But if there is the comma


### Group by 1

```
SET hive.groupby.orderby.position.alias=true;

SELECT
 CASE
    WHEN active_exp_map LIKE '%zJIBXrCs5#Control%' THEN 'zJIBXrCs5#Control'
    WHEN active_exp_map LIKE '%zJIBXrCs5#GroupA%' THEN 'zJIBXrCs5#GroupA'
    ELSE active_exp_map
 END as bucket,

 SUM(COALESCE(total_cores,0)) as sum_total_device_cores
FROM roku.agg_channel_cores_daily
where date_key between '2020-12-03' and '2020-12-17'
and active_exp_map like '%zJIBXrCs5%'
GROUP BY 1
```

## Drop external table with data
DROP deletes data for managed tables while it only deletes metadata for external ones

```
ALTER TABLE <table-name> SET TBLPROPERTIES('EXTERNAL'='False'); //changing the tbl properties to to make the table as internal
DROP TABLE  <table-name>; //now the table is internal if you drop the table data will be dropped automatically.
```


ALTER TABLE addresses_text SET TBLPROPERTIES ('external.table.purge'='false');

Create an external table to store the CSV data, configuring the table so you can drop it along with the data.
```

CREATE EXTERNAL TABLE IF NOT EXISTS names_text(
  a INT, b STRING)
  ROW FORMAT DELIMITED
  FIELDS TERMINATED BY ','
  STORED AS TEXTFILE
  LOCATION '/user/andrena'
  TBLPROPERTIES ('external.table.purge'='true');          
```
Run DROP TABLE on the external table.
```
DROP TABLE names_text;
```

#### SPLIT - generate array, SUBSTRING_INDEX
```
SELECT SUBSTRING_INDEX(“www.big.data.n.sql.com”, “.”, 2);
Results: http://www.big

select size(split('abcd efgh 1234',' '));
3

select split('abcd efgh 1234',' ')[0];;
abcd

select split('abcd efgh 1234',' ')[1];
efgh

select split('abcd efgh 1234',' ')[2]; 
1234
```

### Complex SQL with COLLECT_SET

https://stackoverflow.com/questions/43054742/hive-collect-set

### Etc
```
WITH E as     
(
      SELECT
        id,
        SUBSTR(CAST(start_date as string),1,10) as  start_date,
        SUBSTR(CAST(end_date   as string),1,10) as  end_date
      FROM  roku.dim_experiment
      WHERE  '2020-10-25' between SUBSTR(CAST(start_date as string),1,10)   and  SUBSTR(CAST(end_date   as string),1,10)
      AND client='player' AND is_active=1
)
SELECT
          device_id,
          concat_ws(',',collect_set(experiment_id)),
         concat_ws(',',collect_set(bucket_name)),
          '2020-10-25',
         '2020-10-25'
     FROM roku.fact_amoeba_allocation_events A
     JOIN E
     ON  E.id = A.experiment_id
     WHERE A.date_key <= '2020-10-25'
     AND A.date_key between E.start_date AND E.end_date
     GROUP BY A.device_id;
```
Plan optimized by CBO:

```
hive> EXPLAIN SELECT
          device_id,
          concat_ws(',',collect_set(experiment_id)),
         concat_ws(',',collect_set(bucket_name)),
          '2020-10-25',
         '2020-10-25'
     FROM roku.fact_amoeba_allocation_events A
     JOIN
     (
      SELECT
        id,
        SUBSTR(CAST(start_date as string),1,10) as  start_date,
        SUBSTR(CAST(end_date   as string),1,10) as  end_date
      FROM  roku.dim_experiment
      WHERE  '2020-10-25' between SUBSTR(CAST(start_date as string),1,10)   and  SUBSTR(CAST(end_date   as string),1,10)
      AND client='player' AND is_active=1
     ) E
    
     ON  E.id = A.experiment_id
     WHERE A.date_key <= '2020-10-25'
     AND A.date_key between E.start_date AND E.end_date
     GROUP BY A.device_id;
OK
Plan optimized by CBO.

Vertex dependency in root stage
Map 1 <- Map 3 (BROADCAST_EDGE)
Reducer 2 <- Map 1 (SIMPLE_EDGE)

Stage-0
  Fetch Operator
    limit:-1
    Stage-1
      Reducer 2
      File Output Operator [FS_15]
        Select Operator [SEL_14] (rows=3033438 width=300)
          Output:["_col0","_col1","_col2","_col3","_col4"]
          Group By Operator [GBY_13] (rows=3033438 width=300)
            Output:["_col0","_col1","_col2"],aggregations:["collect_set(VALUE._col0)","collect_set(VALUE._col1)"],keys:KEY._col0
          <-Map 1 [SIMPLE_EDGE]
            SHUFFLE [RS_12]
              PartitionCols:_col0
              Group By Operator [GBY_11] (rows=6066876 width=300)
                Output:["_col0","_col1","_col2"],aggregations:["collect_set(_col1)","collect_set(_col2)"],keys:_col0
                Select Operator [SEL_10] (rows=6066876 width=300)
                  Output:["_col0","_col1","_col2"]
                  Filter Operator [FIL_9] (rows=6066876 width=300)
                    predicate:_col3 BETWEEN _col5 AND _col6
                    Map Join Operator [MAPJOIN_20] (rows=54601889 width=300)
                      Conds:SEL_2._col1=RS_7._col0(Inner),HybridGraceHashJoin:true,Output:["_col0","_col1","_col2","_col3","_col5","_col6"]
                    <-Map 3 [BROADCAST_EDGE] vectorized
                      BROADCAST [RS_7]
                        PartitionCols:_col0
                        Select Operator [SEL_5] (rows=11 width=284)
                          Output:["_col0","_col1","_col2"]
                          Filter Operator [FIL_19] (rows=11 width=284)
                            predicate:('2020-10-25' BETWEEN substr(UDFToString(start_date), 1, 10) AND substr(UDFToString(end_date), 1, 10) and (client = 'player') and (is_active = 1) and id is not null)
                            TableScan [TS_3] (rows=430 width=284)
                              roku@dim_experiment,dim_experiment,Tbl:COMPLETE,Col:NONE,Output:["id","start_date","end_date","is_active","client"]
                    <-Select Operator [SEL_2] (rows=49638080 width=300)
                        Output:["_col0","_col1","_col2","_col3"]
                        Filter Operator [FIL_18] (rows=49638080 width=300)
                          predicate:experiment_id is not null
                          TableScan [TS_0] (rows=49638080 width=300)
                            roku@fact_amoeba_allocation_events,a,Tbl:PARTIAL,Col:NONE,Output:["device_id","experiment_id","bucket_name"]

Time taken: 5.944 seconds, Fetched: 43 row(s)

```
SIMPLE SQL: Plan not optimized by CBO.
```
hive> EXPLAIN
    > SELECT
    >     A.device_id,
    >     concat_ws(',',collect_set(A.experiment_id)),
    >     concat_ws(',',collect_set(A.bucket_name))
    > FROM roku.fact_amoeba_allocation_events A
    > JOIN
    > (
    >  SELECT
    >    id,
    >    SUBSTR(CAST(start_date as string),1,10) as  start_date,
    >    SUBSTR(CAST(end_date   as string),1,10) as  end_date
    >  FROM  roku.dim_experiment
    >  WHERE id = 'I5ut8NBtK'
    > ) E
    >
    > ON  E.id = A.experiment_id
    > WHERE A.date_key <= '2020-10-25'
    > AND A.date_key between E.start_date AND E.end_date
    > GROUP BY A.device_id;
OK
Plan not optimized by CBO.

Vertex dependency in root stage
Map 2 <- Map 1 (BROADCAST_EDGE)
Reducer 3 <- Map 2 (SIMPLE_EDGE)

Stage-0
  Fetch Operator
    limit:-1
    Stage-1
      Reducer 3
      File Output Operator [FS_21]
        Select Operator [SEL_20] (rows=3033438 width=300)
          Output:["_col0","_col1","_col2"]
          Group By Operator [GBY_19] (rows=3033438 width=300)
            Output:["_col0","_col1","_col2"],aggregations:["collect_set(VALUE._col0)","collect_set(VALUE._col1)"],keys:KEY._col0
          <-Map 2 [SIMPLE_EDGE]
            SHUFFLE [RS_18]
              PartitionCols:_col0
              Group By Operator [GBY_17] (rows=6066876 width=300)
                Output:["_col0","_col1","_col2"],aggregations:["collect_set(_col7)","collect_set(_col8)"],keys:_col3
                Select Operator [SEL_16] (rows=6066876 width=300)
                  Output:["_col3","_col7","_col8"]
                  Filter Operator [FIL_24] (rows=6066876 width=300)
                    predicate:_col12 BETWEEN _col17 AND _col18
                    Map Join Operator [MAPJOIN_27] (rows=54601889 width=300)
                      Conds:FIL_26.experiment_id=RS_13.'I5ut8NBtK'(Inner),HybridGraceHashJoin:true,Output:["_col3","_col7","_col8","_col12","_col17","_col18"]
                    <-Map 1 [BROADCAST_EDGE] vectorized
                      BROADCAST [RS_13]
                        PartitionCols:'I5ut8NBtK'
                        Select Operator [SEL_8] (rows=687 width=89)
                          Output:["_col1","_col2"]
                          Filter Operator [FIL_25] (rows=687 width=89)
                            predicate:(id = 'I5ut8NBtK')
                            TableScan [TS_6] (rows=1374 width=89)
                              roku@dim_experiment,dim_experiment,Tbl:COMPLETE,Col:NONE,Output:["id","start_date","end_date"]
                    <-Filter Operator [FIL_26] (rows=49638080 width=300)
                        predicate:experiment_id is not null
                        TableScan [TS_9] (rows=49638080 width=300)
                          roku@fact_amoeba_allocation_events,a,Tbl:PARTIAL,Col:NONE,Output:["device_id","experiment_id","bucket_name"]
```

### Settings

grep -r  -h "SET hive" *hql  . | sort | uniq

```
SET hive.exec.max.dynamic.partitions.pernode=1500;
SET hive.exec.max.dynamic.partitions=1500;
SET hive.cli.print.header=true;
SET hive.exec.compress.output=false;
SET hive.exec.reducers.max=1;
SET hive.execution.engine=tez;
SET hive.execution.engine={hive_engine};
SET hive.mapred.mode=false;

 SET hive.exec.compress.intermediate=true;
 SET hive.exec.compress.output=false;
 SET hive.exec.reducers.max=1;
      query = """SET hive.execution.engine=mr;
      
SET hive.exec.compress.output=false;
SET hive.exec.reducers.max=1;
SET hive.execution.engine=tez;
    max_r_update_partition_hql = """SET hive.mapred.mode=nonstrict;

SET hive.execution.engine={hive_engine};
SET hive.mapred.mode=false;
SET hive.mapred.mode=nonstrict;
  SET hive.exec.compress.output=false;
  SET hive.exec.dynamic.partition = true;
  SET hive.exec.dynamic.partition.mode = nonstrict;
  SET hive.exec.reducers.max=1;
  SET hive.execution.engine=mr;
  SET hive.execution.engine=tez;
  SET hive.map.aggr=false;
  SET hive.mapred.mode = nonstrict;
  return ('SET hive.cli.print.header=false;SHOW partitions {table_name};'.format(
  sql = '''SET hive.exec.dynamic.partition=true;
 
SET hive.auto.convert.join=false;
SET hive.auto.convert.join=true;
SET hive.cbo.enable = true;
SET hive.cbo.enable=false;
SET hive.cbo.enable=true;
SET hive.compute.query.using.stats = true;
SET hive.exec.compress.intermediate=true;
SET hive.exec.compress.output = true;
SET hive.exec.compress.output=false;
SET hive.exec.compress.output=true;
SET hive.exec.dynamic.partition.mode=nonstrict;
SET hive.exec.dynamic.partition=TRUE;
SET hive.exec.dynamic.partition=true;
SET hive.exec.max.dynamic.partitions.pernode = 1000;
SET hive.exec.max.dynamic.partitions.pernode= 9999;
SET hive.exec.max.dynamic.partitions.pernode=100;
SET hive.exec.max.dynamic.partitions.pernode=10;
SET hive.exec.max.dynamic.partitions.pernode=200;
SET hive.exec.max.dynamic.partitions.pernode=3000;
SET hive.exec.max.dynamic.partitions.pernode=300;
SET hive.exec.max.dynamic.partitions.pernode=50;
SET hive.exec.max.dynamic.partitions.pernode=99999;
SET hive.exec.max.dynamic.partitions= 9999;
SET hive.exec.max.dynamic.partitions=100;
SET hive.exec.max.dynamic.partitions=10;
SET hive.exec.max.dynamic.partitions=3000;
SET hive.exec.max.dynamic.partitions=50;
SET hive.exec.max.dynamic.partitions=99999;
SET hive.exec.parallel=false;
SET hive.exec.parallel=true;
SET hive.exec.reducers.bytes.per.reducer=2000000;
SET hive.exec.reducers.bytes.per.reducer=256000000;
SET hive.exec.reducers.max=10;
SET hive.exec.reducers.max=1;
SET hive.exec.reducers.max=256;
SET hive.exec.reducers.max=3000;
SET hive.exec.reducers.max=4096;
SET hive.exec.reducers.max=4;
SET hive.exec.reducers.max=512;
SET hive.exec.reducers.max=5;
SET hive.exec.stagingdir={{ params.staging_dir }};
SET hive.execution.engine = mr;
SET hive.execution.engine = tez;
SET hive.execution.engine=TEZ;
SET hive.execution.engine=mr;
SET hive.execution.engine=tez;
SET hive.fetch.task.conversion = none;
SET hive.groupby.orderby.position.alias=true;
SET hive.limit.query.max.table.partition = 1000000;
SET hive.limit.query.max.table.partition = 100000;
SET hive.limit.query.max.table.partition = 10000;
SET hive.limit.query.max.table.partition = 2000;
SET hive.limit.query.max.table.partition=-1;
SET hive.limit.query.max.table.partition=10000;
SET hive.limit.query.max.table.partition=100;
SET hive.limit.query.max.table.partition=186;
SET hive.limit.query.max.table.partition=200;
SET hive.limit.query.max.table.partition=250;
SET hive.limit.query.max.table.partition=3000;
SET hive.limit.query.max.table.partition=300;
SET hive.limit.query.max.table.partition=50;
SET hive.limit.query.max.table.partition=800;
SET hive.load.dynamic.partitions.thread=15;
SET hive.map.aggr=false;
SET hive.map.aggr=true;
SET hive.mapred.mode = nonstrict;
SET hive.mapred.mode='nonstrict';
SET hive.mapred.mode=false;
SET hive.mapred.mode=non-strict;
SET hive.mapred.mode=nonstrict;
SET hive.mapred.mode=nostrict;
SET hive.mapred.supports.subdirectories=TRUE;
SET hive.merge.size.per.task=12800000000;
SET hive.merge.smallfiles.avgsize=12800000000;
SET hive.merge.tezfiles=true;
SET hive.mv.files.thread=0;
SET hive.optimize.sort.dynamic.partition=true;
SET hive.optimize.union.remove=true;
SET hive.stats.autogather = true;
SET hive.stats.fetch.column.stats = true;
SET hive.stats.fetch.partition.stats = true;
SET hive.strict.checks.cartesian.product = FALSE;
SET hive.strict.checks.cartesian.product=false;
SET hive.strict.checks.large.query=false;
SET hive.tez.auto.reducer.parallelism=true ;
SET hive.tez.auto.reducer.parallelism=true;
SET hive.tez.container.size=2048;
SET hive.tez.container.size=4096;
SET hive.tez.container.size=5120;
SET hive.tez.container.size=6656;
SET hive.tez.container.size=7168;
SET hive.tez.container.size=8192;
SET hive.tez.java.opts=-Xmx1638m;
SET hive.tez.java.opts=-Xmx3275m;
SET hive.tez.java.opts=-Xmx3276m;
SET hive.tez.java.opts=-Xmx3600m;
SET hive.tez.java.opts=-Xmx3g;
SET hive.tez.java.opts=-Xmx4096m;
SET hive.tez.java.opts=-Xmx5734m;
SET hive.tez.java.opts=-Xmx6500m;
SET hive.tez.java.opts=-Xmx6550m;
SET hive.tez.java.opts=-Xmx6553m;
SET hive.vectorized.execution.enabled = true;
SET hive.vectorized.execution.enabled=FALSE;
SET hive.vectorized.execution.enabled=false;
SET hive.vectorized.execution.enabled=true;
SET hive.vectorized.execution.reduce.enabled = true;
SET hivevar:hr=HOUR(FROM_UNIXTIME(${partition_ts}));
SET hivevar:partition_ts=${ts}-28800;
SET hivevar:ts=unix_timestamp(regexp_replace('{{ ts }}', 'T',' '));
```

### Problem: if  no records in Hive partition then copy to Redshift will fail: 

FAILED: SemanticException [Error 10006]: Partition not found {date_key=2020-09-21}


Solution: 

step 1: add records with NULL values in Hive - this it will enforce the new partition/folder to be created

```
insert into agg_t
select a,b from fact_t
group by ...
union select {{dt}}, NULL, NULL
```
step 2: remove  records  with NULL from Hive -  with  hope what new partition/folder will not be removed

```
insert overwrite table 
				sbschema.roku_agg_product_contextual_offers_metrics_daily
				partition 	(date_key ) 
				SELECT * 	  
	FROM  sbschema.roku_agg_product_contextual_offers_metrics_daily
	WHERE date_key='2020-06-13' AND  product_id IS NOT  NULL; 
```    


 
I tried to use in dev env the Hive DELETE statement from Airflow:
```
  DELETE FROM  sbschema.roku_agg_product_contextual_offers_metrics_daily
WHERE date_key='2020-06-13' AND  product_id IS NULL;
```
and I got:
```
 {hive_hooks.py:235} INFO - FAILED: SemanticException [Error 10294]:
 Attempt to do update or delete using transaction manager that does not support these operations.
 

Yamini Santhanam 
Is your table set to transaction=true? That's all I can think of for now

Todd Studenicka  

you can try  insert overwrite the rows you want:
 insert overwrite table 
 sbschema.roku_agg_product_contextual_offers_metrics_daily
				partition 	(date_key ) 
SELECT * 	  
	FROM  sbschema.roku_agg_product_contextual_offers_metrics_daily
	WHERE date_key='2020-06-13' AND  product_id IS NOT  NULL; 

```

###  Using  CASCADE in ALTER TABLE ADD COLUMNS ...  

https://stackoverflow.com/questions/40582387/how-to-add-columns-to-existing-hive-partitioned-table/44837663

ALTER TABLE dbname.table_name ADD columns (column1 string,column2 string) CASCADE; 

This changes the columns of a table's metadata and cascades the same change to all the partition metadata.  
RESTRICT is the default, limiting column change only to table metadata.

### Presto  Druid Pinot Kudu
Presto  query execution rate that is three times faster than Hive.

<https://support.treasuredata.com/hc/en-us/articles/360001450928-Presto-Known-Limitations>

<https://imply.io/post/performance-benchmark-druid-presto-hive>

<https://imply.io/post/compare-apache-druid-to-vertica>

Druid is fast

https://druid.apache.org/docs/latest/querying/lookups.html . LOOKUPS in Druid

<https://medium.com/@leventov/comparison-of-the-open-source-olap-systems-for-big-data-clickhouse-druid-and-pinot-8e042a5ed1c7>


<https://blog.cloudera.com/benchmarking-time-series-workloads-on-apache-kudu-using-tsbs/> . Kudu

But Pinot is faster?
<https://pinot.apache.org/>

<https://engineering.linkedin.com/blog/2020/apache-pinot-030-update>

<https://eng.uber.com/engineering-sql-support-on-apache-pinot/>

### Impala SQL Engine

Impala — это популярный движок MPP с открытым исходным кодом и широким спектром возможностей в Cloudera Distribution Hadoop (CDH ) и CDP. Impala заслужила доверие рынка благодаря low-latency highly interactive SQL-запросам. Возможности Impala очень широки, Impala не только поддерживает Hadoop Distributed File System (HDFS — распределенную файловую систему Hadoop) с Parquet, Optimized Row Columnar (ORC — оптимизированный узел хранения), JavaScript Object Notation (JSON), Avro, и текстовые форматы, но также имеет встроенную поддержку Kudu, Microsoft Azure Data Lake Storage (ADLS) и Amazon Simple Storage Service (S3). Impala обладает высоким уровнем безопасности при помощи either sentry или ranger и, как известно, может поддерживать тысячи пользователей с кластерами из сотен узлов на многпетабайтных датасетах. Давайте же рассмотрим общую архитектуру Impala.



Для проверки работоспособности кластера Impala использует StateStore. Если узел Impala по какой-либо причине переходит в режим «оффлайн», то StateStore передаст сообщение об этом по всем узлам и пропустит недоступный узел. Служба каталога Impala управляет метаданными для всех инструкций SQL для всех узлов кластера. StateStore и служба каталогов обмениваются данными с хранилищем Hive MetaStore для размещения блоков и файлов, а затем передают метаданные рабочим узлам. При поступлении запроса он передается одному из многочисленных программ согласования, где выполняется компиляция и инициируется планирование. Фрагменты плана возвращаются, и программа согласования организует его выполнение. Промежуточные результаты передаются между службами Impala и затем возвращаются.

Такая архитектура идеально подходит для тех случаев, когда нам нужны витрины данных для бизнес-аналитики для получения ответов на запросы с низким временем задержки, как это обычно бывает в случаях с использованием ad-hoc, self-service и discovery types. При таком сценарии мы имеем клиентов сообщающих нам ответы на сложные запросы от менее одной секунды до пяти секунд. 

Для данных Internet of Things (IoT) и связанных с ними сценариях, Impala вместе со streaming решениями, такими как NiFi, Kafka или Spark Streaming, и соответствующими хранилищами данных, такими как Kudu, может обеспечить непрерывную конвейерную обработку со временем задержки менее чем десять секунд. Благодаря встроенным функциям чтения/записи на S3, ADLS, HDFS, Hive, HBase и многим другим, Impala является превосходным SQL-движком для использования при запуске кластера до 1000 узлов, и более 100 триллионов строк в таблицах или датасетах размером в 50BP и более. 

### Hive LLAP

«Live Long And Process» или «Long Delay Analytics Processing», также известная как LLAP, является механизмом выполнения под управлением Hive, который поддерживает длительные процессы используя одни и те же ресурсы для кэширования и обработки. Этот механизм обработки дает нам ответ от SQL с очень низким временем задержки, так как у нас нет времени на запуск запрашиваемых ресурсов.



Кроме того, LLAP обеспечивает и устанавливает контроль над исполнением политики безопасности, поэтому вся работа LLAP для пользователя прозрачна, что помогает Hive конкурировать по показателям производительности рабочих нагрузок даже с наиболее популярными и традиционно используемыми средствами хранения данных на сегодняшний день.

Hive LLAP предлагает самый развитый движок SQL в экосистеме больших данных. Hive LLAP создан для огромного количества данных, предоставляя пользователям широкие возможности хранилища данных Enterprise Data Warehouse (EDW), которое поддерживает преобразование данных больших объемов, выполнение долгих запросов или тяжелых SQL запросов с сотней join-ов. Hive поддерживает materialized views, суррогатные ключи и различные ограничения, аналогичные традиционным реляционным системам управления базами данных, включая встроенное кэширование для получения запроса результатов и запросов данных. Hive LLAP может уменьшить нагрузку от повторяющихся запросов сократив время ответа до доли секунды. Hive LLAP может поддерживать федеративные запросы на HDFS (распределенную файловую систему Hadoop) и о object stores, а также потоковую передачу в реальном времени, работая с Kafka и Druid. 

Таким образом Hive LLAP идеально подходит в качестве решения Enterprise Data Warehouse (EDW ), в котором мы будем вынуждены столкнуться с большим количеством длительных запросов, требующих крупных преобразований или множественных join-ов между таблицами и большими датасетами. Благодаря технологии кэширования, включенной в Hive LLAP, у нас появились клиенты, которые могут сделать join 330 миллиардов записей с 92 миллиардами других записей с partition key или без него и получить результат за секунды. 

### AWS EMR
<https://aws.amazon.com/premiumsupport/knowledge-center/logs-hive-queries-amazon-emr/>

### Size Path
https://medium.com/@gomzvicky/finding-total-size-of-hive-databases-data-d2ce8fa96cbf

https://medium.com/@gomzvicky/finding-hdfs-paths-of-hive-tables-a42dcab161d7

### Books

Architecting Modern Data Platforms: A Guide to Enterprise Hadoop at Scale: December 5, 2018
<https://www.amazon.com/Architecting-Modern-Data-Platforms-Enterprise-ebook/dp/B07L9JDXM8/>

Hadoop Application Architectures: Designing Real-World Big Data Applications (I have this Kindle book)
<https://www.amazon.com/Hadoop-Application-Architectures-Real-World-Applications/dp/1491900083/>

The Enterprise Big Data Lake: Delivering the Promise of Big Data and Data Science 
<https://www.amazon.com/Enterprise-Big-Data-Lake-Delivering-ebook/dp/B07NY44RKR/>


### Hive Macro

https://tech.trivago.com/2019/01/30/a-new-functional-approach-to-complex-types-in-apache-hive/

https://developpaper.com/macro-an-often-overlooked-weapon-in-hive/

<https://dwgeek.com/working-with-hive-macros-syntax-and-examples.html/>

```
DROP TEMPORARY MACRO IF EXISTS isNumber;

CREATE TEMPORARY MACRO isNumber (input INT)
CASE
WHEN CAST(input AS INT) IS NULL THEN 'NO' else 'YES'
END
;

SELECT isNumber(100), isNumber("123"), isNumber("12sd");

DROP TEMPORARY MACRO IF EXISTS current_time_preferred_format;

CREATE TEMPORARY MACRO current_time_preferred_format(input string) 
CASE 
    WHEN UPPER(input) = "DEFAULT"
    THEN FROM_UNIXTIME( unix_timestamp(), "yyyy-MM-dd'T'HH:mm:ss.sss")
ELSE
    FROM_UNIXTIME( unix_timestamp(), input)
END
;

```

### CREATE TABLE ... COMPLEX DATA TYPE

https://acadgild.com/blog/hive-complex-data-types-with-examples

create table Temperature(date string,city string,MyTemp array<double>) row format delimited fields terminated by ‘\t’ collection items terminated by ‘,’;

### Reusable HQL
<https://stackoverflow.com/questions/40750439/hive-can-one-extract-common-options-for-reuse-in-other-scripts/40783621#40783621>

``hive -i config.hql -f script_A.hql``

```
hive -f a.hql
wait $! 
hive -f b.hql
wait $! 
```
### Map explode

SELECT explode(str_to_map('e1:t1&e2:t2&e3:t3','&',':'))


### FIND_IN_SET( string search_string, string source_string_list )

The FIND_IN_SET function searches for the search string in the source_string_list and returns the position of the first occurrence in the source string list. Here the source string list should be comma delimited one. It returns 0 if the first argument contains comma.
Example: FIND_IN_SET('ha','hao,mn,hc,ha,hef') returns 4


### Lateral VIEW explode map_keys
```
SELECT id, buckets, single_bucket
FROM roku.dim_experiment
LATERAL VIEW explode(map_keys(buckets)) exp_buckets AS single_bucket
LIMIT 10 ;
```

```
  create table sbschema.roku_t1 (x int, y int,  active_exp_map string);
  insert into sbschema.roku_t1 values
  (1, 1, "a:1&b:2&a:1"),
  (1, 2, "b:2&c:3"),
  (2, 1, "c:1&d:2&c:1"),
  (2, 2, "c:1");
  
 
select * from sbschema.roku_t1 lateral view explode(str_to_map(active_exp_map,  "&", ":")) a AS experiment_id, bucket;

 duplicates gone:
 
 	x	y	 active_exp_map	a.experiment_id	a.bucket
 	1	1	a:1&b:2&a:1     a	1
 	1	1	a:1&b:2&a:1  	b	 2
 	1	2	b:2&c:3	        b	2
 	1	2	b:2&c:3	        c	3
 	2	1	c:1&d:2&c:1	    c	1
 	2	1	c:1&d:2&c:1	    d	2
 	2	2	c:1	            c	1
```

### sort_array
```
WITH T as (
SELECT 1 as dev_id, 'a:1&b:2' as a, 10 as cnt
UNION ALL
SELECT 1 as dev_id, 'a:1&b:2' as a, 11 as cnt
UNION ALL
SELECT 2 as dev_id, 'b:2&a:1' as a, 12 as cnt
)
SELECT
     S.a_sorted,
     SUM(S.cnt)
FROM
(
     SELECT cnt,   concat_ws('&', sort_array(split(a, '&')) ) as a_sorted
     FROM T
) S
GROUP BY a_sorted
```
build active_exp_map from fact_amoeba_alloc_Events
```
CREATE EXTERNAL TABLE IF NOT EXISTS sbschema.roku_tmp2
(
 dev_id STRING,
 e STRING,
 b STRING
)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY '\t'
COLLECTION ITEMS TERMINATED BY ','
MAP KEYS TERMINATED BY ':'
STORED AS textfile
LOCATION 's3://roku-dea-dev/sand-box/roku-data-warehouse/roku/dimensions/tmp2'
;


INSERT INTO sbschema.roku_tmp2
SELECT 1 as dev_id, 'c' as e, '1' as b
UNION ALL
SELECT 1 as dev_id, 'b' as e, '2' as b
UNION ALL
SELECT 1 as dev_id, 'b' as e, '2' as b
UNION ALL
SELECT 2 as dev_id, 'b' as e, '2' as b
);

-- build active_exp_map with sorted content
SELECT
     dev_id,
     concat_ws('&', sort_array(collect_set(e || ':' || b)))
FROM sbschema.roku_tmp2
GROUP BY dev_id
```
Output:
```
1	b:2&c:1
2	b:2
```

### collect_set and concat_ws 
<https://stackoverflow.com/questions/61038050/hive-how-to-eliminate-the-duplicated-substrings>
```
select t.i, concat_ws('&',collect_set(e.val)) as grouped_s
  from T t 
       lateral view outer explode(split(t.s,'&')) e as val
 group by t.i; 
``` 
<https://dwgeek.com/apache-hive-group_concat-alternative-example.html/>
```
collect_set(col)  Returns a set of objects with duplicate elements eliminated.
collect_list(col)  Returns a list of objects with duplicates.
concat_ws(string SEP, array<string>);
 
  create table t1 (x int, s string);
  insert into t1 values 
  (1, "one"), 
  (3, "three"), 
  (2, "two"), 
  (1, "one"),
  (1, "four"), 
  (3, "five"), 
  (2, "six"), 
  (7, "seven");

 SELECT x,
        count(*) as num_of_rows, 
        concat_ws(',' , collect_set(s)) as group_con 
 FROM t1 group by x;
 
x num_of_rows group_con
1    3                 one,four
2    2                 two,six
3    2                 three,five
7    1                 seven
```

<https://stackoverflow.com/questions/48178027/hive-aggregate-function-for-merging-arrays>
```
select key, collect_set(explodedvalue) from (
  select key, explodedvalue from table_above lateral view explode(value) e as explodedvalue
) t group by key;
```
<https://github.com/brndnmtthws/facebook-hive-udfs/blob/master/src/main/java/com/facebook/hive/udf/UDFArrayConcat.java>
Following does not work - why?
```
  create table sbschema.roku_t1 (x int, s string);
  insert into sbschema.roku_t1 values
  (1, "a:1&b:2"),
  (1, "b:2&c:3"),
  (2, "c:1&d:2"),
  (2, "c:1");
 
SELECT x,
        count(*) as num_of_rows,
concat_ws('&',
 collect_set(
  split(
        concat_ws('&' , collect_set(s))
      , "&"
  )
 )
)
as group_con
FROM sbschema.roku_t1 group by x;

FAILED: SemanticException [Error 10128]: Line 6:24 Not yet supported place for UDAF 'collect_set'
```


### How to set variables in Hive script:

<https://cwiki.apache.org/confluence/display/Hive/LanguageManual+VariableSubstitution>
<https://stackoverflow.com/questions/12464636/how-to-set-variables-in-hive-scripts>


hive.support.sql11.reserved.keywords to TRUE. 
<https://cwiki.apache.org/confluence/display/Hive/HiveCounters> .  Counters
 
```

hive > show columns in table_name:

hive> set hive.cli.print.header=true;

describe extended tablenamehere 
describe formatted tablenamehere 
show partitions tablenamehere
SHOW PARTITIONS employees PARTITION(country='US');
set hive.mapred.mode=strict;  -- prohibits queries of partitioned tables without a WHERE clause that filters on partitions
```

```
hive> select 'Dudu Markovitz: 123' rlike '[^a-zA-Z\\d\\s:]';
OK
false
hive> select 'Dudu Markovitz: @123' rlike '[^a-zA-Z\\d\\s:]';
OK
true
```

Partitioning tables changes how Hive structures the data storage.
``` 
CREATE TABLE employees (
  name         STRING,
  salary       FLOAT,
  subordinates ARRAY<STRING>,
  deductions   MAP<STRING, FLOAT>,
  address      STRUCT<street:STRING, city:STRING, state:STRING, zip:INT>
)
PARTITIONED BY (country STRING, state STRING);

Following directories will be created
.../employees/country=CA/state=AB
.../employees/country=CA/state=BC
``` 
### CLI

The hive when invoked without the -i option will attempt to load $HIVE_HOME/bin/.hiverc and $HOME/.hiverc as initialization files.

set mapred.reduce.tasks=32


<https://cwiki.apache.org/confluence/display/Hive/LanguageManual+Cli>

<http://dwgeek.com/hiveserver2-beeline-command-line-shell-options-examples.html/>

   hive -f x.hql
   hive -e 'select * from test';
   
## Performance Tuning

it’s important to know which table is the largest and put it last in the
JOIN clause, or use the directive
```
/* streamtable(table_name) */ 
```
<https://dzone.com/articles/how-to-improve-hive-query-performance-with-hadoop>

###   Tez Engine
Apache Tez Engine is an extensible framework for building high-performance batch processing and interactive data processing. It is coordinated by YARN in Hadoop. Tez improved the MapReduce paradigm by increasing the processing speed and maintaining the MapReduce ability to scale to petabytes of data.
Apache Tez generalizes the MapReduce paradigm to execute a complex DAG (directed acyclic graph) of tasks. Refer to the following link for more info.

<http://hortonworks.com/blog/apache-tez-a-new-chapter-in-hadoop-data-processing/>


Tez engine can be enabled in your environment by setting hive.execution.engine to tez:
```
set hive.execution.engine=tez;
```

### Use Vectorization
<https://blog.cloudera.com/faster-swarms-of-data-accelerating-hive-queries-with-parquet-vectorization/>

Vectorization improves the performance by fetching 1,024 rows in a single operation instead of fetching single row each time. It improves the performance for operations like filter, join, aggregation, etc.

Vectorized query execution improves performance of operations like scans, aggregations, filters and joins, by performing them in batches of 1024 rows at once instead of single row each time.

<https://stackoverflow.com/questions/53409157/hive-query-optimization-settings-when-not-to-use>

<https://cwiki.apache.org/confluence/display/Hive/Vectorized+Query+Execution>

```
set hive.vectorized.execution.enabled = true;
set hive.vectorized.execution.reduce.enabled = true;
```

### Use ORCFile
Optimized Row Columnar format provides highly efficient ways of storing the hive data by reducing the data storage format by 75% of the original. The ORCFile format uses techniques like predicate push-down, compression, and more to improve the performance of the query.

Consider two tables: employee and employee_details, tables that are stored in a text file. Let's say we will use join to fetch details from both tables.
```
Select a.EmployeeID, a.EmployeeName, b.Address,b.Designation from Employee a
Join Employee_Details b
On a.EmployeeID=b.EmployeeID;
```
Above query will take a long time, as the table is stored as text. Converting this table into ORCFile format will significantly reduce the query execution time.
```
Create Table Employee_ORC (EmployeeID int, EmployeeName varchar(100),Age int)
STORED AS ORC tblproperties("compress.mode"="SNAPPY");
Select * from Employee Insert into Employee_ORC;
Create Table Employee_Details_ORC (EmployeeID int, Address varchar(100)
                                  ,Designation Varchar(100),Salary int)
STORED AS ORC tblproperties("compress.mode"="SNAPPY");
Select * from Employee_Details Insert into Employee_Details_ORC;
Select a.EmployeeID, a.EmployeeName, b.Address,b.Designation from Employee_ORC a
Join Employee_Details_ORC b
On a.EmployeeID=b.EmployeeID;
ORC supports compressed (ZLIB and Snappy), as well as uncompressed storage.
```
### Use Partitioning
With partitioning, data is stored in separate individual folders on HDFS. Instead of querying the whole dataset, it will query partitioned dataset.

Create Temporary Table and Load Data Into Temporary Table
```
Create Table Employee_Temp(EmloyeeID int, EmployeeName Varchar(100), 
                           Address Varchar(100),State Varchar(100),
                           City Varchar(100),Zipcode Varchar(100))
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
STORED AS TEXTFILE;
LOAD DATA INPATH '/home/hadoop/hive' INTO TABLE Employee_Temp;
Create Partitioned Table
Create Table Employee_Part(EmloyeeID int, EmployeeName Varchar(100), 
                           Address Varchar(100),State Varchar(100),
                           Zipcode Varchar(100))
PARTITIONED BY (City Varchar(100))
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
STORED AS TEXTFILE;
```
### Enable Dynamic Hive Partition
```
SET hive.exec.dynamic.partition = true;
SET hive.exec.dynamic.partition.mode = nonstrict;
Import Data From Temporary Table To Partitioned Table
Insert Overwrite table Employee_Part Partition(City) Select EmployeeID,
EmployeeName,Address,State,City,Zipcode from Emloyee_Temp;
```

### Use Bucketing
The Hive table is divided into a number of partitions and is called Hive Partition. 
Hive Partition is further subdivided into clusters or buckets and is called bucketing or clustering.
```
Create Table Employee_Part(EmloyeeID int, EmployeeName Varchar(100), 
                           Address Varchar(100),State Varchar(100),
                           Zipcode Varchar(100))
PARTITIONED BY (City Varchar(100))
Clustered By (EmployeeID) into 20 Buckets
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
STORED AS TEXTFILE;
```
### Cost-Based Query Optimization
Hive optimizes each query's logical and physical execution plan before submitting for final execution. However, this is not based on the cost of the query during the initial version of Hive.

During later versions of Hive, query has been optimized according to the cost of the query (like which types of join to be performed, how to order joins, the degree of parallelism, etc.).

To use cost-based optimization, set the below parameters at the start of the query.
```
set hive.cbo.enable=true;
set hive.compute.query.using.stats=true;
set hive.stats.fetch.column.stats=true;
set hive.stats.fetch.partition.stats=true;
```
<https://cwiki.apache.org/confluence/display/Hive/Configuration+Properties>

<https://stackoverflow.com/questions/56743423/hive-performance-improvement/56761966#56761966>


<https://stackoverflow.com/questions/28920328/how-to-improve-performance-of-loading-data-from-non-partition-table-into-orc-par>

<https://stackoverflow.com/questions/40750439/hive-can-one-extract-common-options-for-reuse-in-other-scripts/40783621#40783621>


Cost based optimizer
```
set hive.cbo.enable=true;
set hive.compute.query.using.stats=true;
set hive.stats.fetch.column.stats=true;
set hive.stats.fetch.partition.stats=true;
analyze table tweets compute statistics for columns;
```

set hive.execution.engine=tez


### Parallel execution
Hive queries are commonly translated into a number of stages that are executed by the default sequence. These stages are not always dependent on each other. Instead, they can run in parallel to reduce the overall job running time. We can enable this feature with the following settings and set the expected number of jobs running in parallel:

SET hive.exec.parallel=true; -- default false
SET hive.exec.parallel.thread.number=16; -- default 8




## Architecture

<http://gethue.com/>  SQL Web client

<https://github.com/dropbox/PyHive> Python client for Hive and Presto

<https://www.adaltas.com/en/2019/07/25/hive-3-features-tips-tricks/>

<https://www.adaltas.com/en/2019/06/17/druid-hive-integration/>


## Books
 
<https://www.amazon.com/Ultimate-Guide-Programming-Apache-Hive-ebook/dp/B0113L7LCO>

## HQL

<https://cwiki.apache.org/confluence/display/Hive/LanguageManual>

<https://cwiki.apache.org/confluence/display/Hive/LanguageManual+UDF#LanguageManualUDF-ConditionalFunctions>

<https://cwiki.apache.org/confluence/display/Hive/Tutorial>

<https://www.sqlservercentral.com/articles/sql-on-hadoop-hive-part-ii>

<https://analyticshut.com/big-data/hive/collect_set-and-collect_list-in-hive/> COLLECT_SET COLLECT_LIST

<https://analyticshut.com/category/big-data/hive/> Pivot, Rollup, Cube

## Install Hive on Mac

<https://formulae.brew.sh/formula/hive>

```
brew install hive

$  export HADOOP_HOME=/usr/local/Cellar/hadoop/3.2.1
$ hive
WARNING: log4j.properties is not found. HADOOP_CONF_DIR may be incomplete.
ERROR: Invalid HADOOP_COMMON_HOME
Unable to determine Hadoop version information.
'hadoop version' returned:
WARNING: log4j.properties is not found. HADOOP_CONF_DIR may be incomplete.
ERROR: Invalid HADOOP_COMMON_HOME

$ export HADOOP_COMMON_HOME=/usr/local/Cellar/hadoop/3.2.1
$ hive
Unable to determine Hadoop version information.
'hadoop version' returned:

bash -x hive
++ /usr/libexec/java_home --version 1.7+
+ JAVA_HOME=/Library/Java/JavaVirtualMachines/jdk1.8.0_231.jdk/Contents/Home
+ HIVE_HOME=/usr/local/Cellar/hive/3.1.2/libexec
+ exec /usr/local/Cellar/hive/3.1.2/libexec/bin/hive
Unable to determine Hadoop version information.
'hadoop version' returned:

```

```
$ jps
68144 NGServer
95120 Jps
68146 NGServer
67958 NGServer
68111 NGServer

```

Bettr jps output
```
$ jps
2702 DataNode
3101 ResourceManager
4879 Jps
2948 SecondaryNameNode
3306 NodeManager
```

<https://www.datageekinme.com/setup/setting-up-my-mac-hive/>

<https://superuser.com/questions/1475872/brew-install-hive-failure>

<https://gist.github.com/SureshChaganti/37413cb3c38911974472ffbbd805409e>



## CASE IF COALSECE DECODE

<http://dwgeek.com/hadoop-hive-conditional-functions-if-case-coalesce-nvl-decode.html/>

IF(boolean testCondition, T valueTrue, T valueFalseOrNull);

isnull( a )

isnotnull ( a )

 You can use OR, IN, REGEXP in the CASE expressions.
 
CASE WHEN a THEN b [WHEN c THEN d]… [ELSE e] END
```
select case 
  when dayname(now()) in ('Saturday','Sunday') then 'result undefined on weekends' 
  when x > y then 'x greater than y' 
  when x = y then 'x and y are equal' 
  when x is null or y is null then 'one of the columns is null' 
  else null 
end 
from t1;
```


CASE a WHEN b THEN c [WHEN d THEN e]… [ELSE f] END
```
select case x 
  when 1 then 'one' 
  when 2 then 'two' 
  when 0 then 'zero' 
  else 'out of range' 
end 
from t1;
```

NVL(arg1, arg2)

coalesce(value1, value 2, …) .    Returns the first non-null value for list of values provided as arguments.


decode(<expr>, <search1>,<result1>, …<search N>, <result N>, <default>)

Decode compares an expression to one or more possible values, and returns a corresponding result when a match is found.
```
SELECT event, 
 decode(  day_of_week, 
         1, "Monday", 
         2, "Tuesday", 
         3, "Wednesday", 
         4, "Thursday", 
         5, "Friday", 
         6, "Saturday", 
         7, "Sunday", 
         "Unknown day") 
  FROM calendar;
```


 

Metastore (usually MySQL) stores the table definition
/etc/hive/conf/
hive-site.xml

DROP DATABASE x
DROP TABLE a -- before DROP DATABASE x
<https://www.youtube.com/watch?v=vwac18EzGGs> . Hive Table dissected
<https://www.youtube.com/playlist?list=PLOaKckrtCtNvLuuSkDdx71hAhPyNSqf66>
<https://www.youtube.com/watch?v=dwd9m1Zl04Q> . Hive JOIN OPTIMIZATION

Shuffling is expensive
Hints
/* +STREAMTABLE */
/* +MAPJOIN */




SMB (sort merge backeted)  MAP JOIN

Hive metastore. To enable the usage of Hive metastore outside of Hive, a separate project called HCatalog was started. 
  HCatalog is a part of Hive and serves the very important purpose of allowing other tools (like Pig and MapReduce)
  to integrate with the Hive metastore.

### Partitions and bucketing
 Physically, a partition in Hive is nothing but just a sub-directory in the table directory.
CREATE TABLE table_name (column1 data_type, column2 data_type) 
PARTITIONED BY (partition1 data_type, partition2 data_type,….);
 
Partitioning is works better when the cardinality of the partitioning field is not too high .

<https://stackoverflow.com/questions/19128940/what-is-the-difference-between-partitioning-and-bucketing-a-table-in-hive>
<http://www.hadooptpoint.org/difference-between-partitioning-and-bucketing-in-hive/>

Clustering aka bucketing on the other hand, will result with a fixed number of files, 
since you do specify the number of buckets. 
What Hive will do is to take the field, calculate a hash and assign a record to that bucket.
But what happens if you use let's say 256 buckets and the field you're bucketing on has a low cardinality 
(for instance, it's a US state, so can be only 50 different values) ? 
You'll have 50 buckets with data, and 206 buckets with no data.

```
CREATE TABLE table_name PARTITIONED BY (partition1 data_type, partition2 data_type,….) 
CLUSTERED BY (column_name1, column_name2, …) 
SORTED BY (column_name [ASC|DESC], …)] 
INTO num_buckets BUCKETS;
```
Partitions can dramatically cut the amount of data you're querying.
 if you want to query only from a certain date forward, the partitioning by year/month/day is going to dramatically cut the amount of IO.
bucketing can speed up joins with other tables that have exactly the same bucketing, 
 if you're joining two tables on the same employee_id, hive can do the join bucket by bucket
 (even better if they're already sorted by employee_id since it's going to to a mergesort which works in linear time).

So, bucketing works well when the field has high cardinality and data is evenly distributed among buckets. 
Partitioning works best when the cardinality of the partitioning field is not too high.

Also, you can partition on multiple fields, with an order (year/month/day is a good example),
while you can bucket on only one field.

``SET hive.enforce.bucketing=true``

every time before writing data to the bucketed table. To leverage the bucketing in the join operation we should
```SET hive.optimize.bucketmapjoin=true```
This setting hints to Hive to do bucket level join during the map stage join. It also reduces the scan cycles to find a particular key because bucketing ensures that the key is present in a certain bucket.

## Hive 3 streaming

Hive HCatalog Streaming API
Traditionally adding new data into Hive requires gathering a large amount of data onto HDFS and then periodically adding a new partition. This is essentially a “batch insertion”. Insertion of new data into an existing partition is not permitted. Hive Streaming API allows data to be pumped continuously into Hive. The incoming data can be continuously committed in small batches of records into an existing Hive partition or table. Once data is committed it becomes immediately visible to all Hive queries initiated subsequently.
```
hive-site.xml to enable ACID support for streaming:
hive.txn.manager = org.apache.hadoop.hive.ql.lockmgr.DbTxnManager
hive.compactor.initiator.on = true (See more important details here)
hive.compactor.worker.threads > 0 
```
## Cost based optimizer Calcite 
<https://cwiki.apache.org/confluence/display/Hive/Cost-based+optimization+in+Hive>

some of optimization decisions that can benefit from a CBO:

How to order Join
What algorithm to use for a given Join
Should the intermediate result be persisted or should it be recomputed on operator failure.
The degree of parallelism at any operator (specifically number of reducers to use).
Semi Join selection




## Join algorithms in Hive
Hive only supports equi-Join currently. Hive Join algorithm can be any of the following:

### Multi way Join
If multiple joins share the same driving side join key then all of those joins can be done in a single task.

Example: (R1 PR1.x=R2.a  - R2) PR1.x=R3.b - R3) PR1.x=R4.c - R4

All of the join can be done in the same reducer, since R1 will already be sorted based on join key x.

### Common Join
Use Mappers to do the parallel sort of the tables on the join keys, which are then passed on to reducers. All of the tuples with same key is given to same reducer. A reducer may get tuples for more than one key. Key for tuple will also include table id, thus sorted output from two different tables with same key can be recognized. Reducers will merge the sorted stream to get join output.

### Map Join
SELET /* +MAPJOIN(a,b) */

Useful for star schema joins, this joining algorithm keeps all of the small tables (dimension tables) in memory in all of the mappers and big table (fact table) is streamed over it in the mapper. This avoids shuffling cost that is inherent in Common-Join. For each of the small table (dimension table) a hash table would be 

Map joins are really efficient if a table on the other side of a join is small enough to fit in the memory.
Hive supports a parameter, hive.auto.convert.join, which when it’s set to “true” suggests that Hive try to map join automatically.

## LLAP
<https://cwiki.apache.org/confluence/display/Hive/LLAP>

<<https://community.hortonworks.com/articles/149894/llap-a-one-page-architecture-overview.html>>

<https://habr.com/ru/post/486124/>

Also known as Live Long and Process, LLAP provides a hybrid execution model.  It consists of a long-lived daemon which replaces direct interactions with the HDFS DataNode, and a tightly integrated DAG-based framework.
Functionality such as caching, pre-fetching, some query processing and access control are moved into the daemon.  Small/short queries are largely processed by this daemon directly, while any heavy lifting will be performed in standard YARN containers.




## Configuration
```
hive-site.xml
hive.execution.engine = mr tez spark
hive.execution.mode = container llap
hive.exec.max.created.files
hive.exec.max.dynamic.partitions.pernode (default value being 100) is the maximum dynamic partitions that can be created by each mapper or reducer.

hive.exec.max.created.files 
hive.exec.max.dynamic.partitions
hive.merge.mapfiles=true 
hive.merge.mapredfiles=true

hive.mapred.reduce.tasks=32;
```
Ensure the bucketing flag is set
```SET hive.enforce.bucketing=true```
every time before we write data to the bucketed table.
```
SET hive.exce.parallel=true;
```
Complex Hive queries commonly are translated to a number of map reduce jobs that are executed by default sequentially. Often though some of a query’s map reduce stages are not interdependent and could be executed in parallel.

They then can take advantage of spare capacity on a cluster and improve cluster utilization while at the same time reduce the overall query executions time. The configuration in Hive to change this behaviour is a merely switching a single flag ```SET hive.exce.parallel=true```

## LEFT SEMI JOIN
In order check the existence of a key in another table, the user can use LEFT SEMI JOIN as illustrated by the following example.
```
INSERT OVERWRITE TABLE pv_users
SELECT u.*
FROM user u LEFT SEMI JOIN page_view pv ON (pv.userid = u.id)
WHERE pv.date = '2008-03-03';
```

##  Dynamic-Partition Insert

This is multi-insert:
```
FROM page_view_stg pvs
INSERT OVERWRITE TABLE page_view PARTITION(dt='2008-06-08', country='US')
       SELECT pvs.viewTime, pvs.userid, pvs.page_url, pvs.referrer_url, null, null, pvs.ip WHERE pvs.country = 'US'
INSERT OVERWRITE TABLE page_view PARTITION(dt='2008-06-08', country='CA')
       SELECT pvs.viewTime, pvs.userid, pvs.page_url, pvs.referrer_url, null, null, pvs.ip WHERE pvs.country = 'CA'
INSERT OVERWRITE TABLE page_view PARTITION(dt='2008-06-08', country='UK')
       SELECT pvs.viewTime, pvs.userid, pvs.page_url, pvs.referrer_url, null, null, pvs.ip WHERE pvs.country = 'UK';
```
Dynamic-partition insert (or multi-partition insert) :
In the dynamic partition insert, the input column values are evaluated to determine which partition this row should be inserted into. If that partition has not been created, it will create that partition automatically. Using this feature you need only one insert statement to create and populate all necessary partitions. 
```
FROM page_view_stg pvs
INSERT OVERWRITE TABLE page_view PARTITION(dt='2008-06-08', country)
       SELECT pvs.viewTime, pvs.userid, pvs.page_url, pvs.referrer_url, null, null, pvs.ip, pvs.country
```       

If the input column value is NULL or empty string, the row will be put into a special partition, whose name is controlled by the hive parameter hive.exec.default.partition.name. The default value is HIVE_DEFAULT_PARTITION{}. Basically this partition will contain all "bad" rows whose value are not valid partition names


set hive.exec.dynamic.partition.mode=nonstrict;
```
beeline> FROM page_view_stg pvs
      INSERT OVERWRITE TABLE page_view PARTITION(dt, country)
             SELECT pvs.viewTime, pvs.userid, pvs.page_url, pvs.referrer_url, null, null, pvs.ip,
                    from_unixtimestamp(pvs.viewTime, 'yyyy-MM-dd') ds, pvs.country
             DISTRIBUTE BY ds, country;
```             
This query will generate a MapReduce job rather than Map-only job. The SELECT-clause will be converted to a plan to the mappers and the output will be distributed to the reducers based on the value of (ds, country) pairs. The INSERT-clause will be converted to the plan in the reducer which writes to the dynamic partitions.


## ARRAYS , explode, inline, stack  LATERAL VIEW

<https://cwiki.apache.org/confluence/display/Hive/LanguageManual+LateralView>
Built-in Table-Generating Functions (UDTF):
* explode() takes in an array (or a map) as an input and outputs the elements of the array (map) as separate rows. \
* posexplode() is similar to explode ; it returns the element as well as its position in the original array.

* inline() explodes an array of structs to multiple rows. Returns a row-set with N columns (N = number of top level elements in the struct), one row per 

* stack() Breaks up n values V1,...,Vn into r rows. Each row will have n/r columns. r must be constant.

Lateral view is used in conjunction with user-defined table generating functions such as explode(). 
```
select inline(array(struct('A',10,date '2015-01-01'),struct('B',20,date '2016-02-02')));

SELECT pageid, adid
FROM pageAds LATERAL VIEW explode(adid_list) adTable AS adid;

CREATE TABLE array_table (int_array_column ARRAY<INT>);

select explode(array('A','B','C'));
select explode(array('A','B','C')) as col;
select tf.* from (select 0) t lateral view explode(array('A','B','C')) tf;
select tf.* from (select 0) t lateral view explode(array('A','B','C')) tf as col;
select posexplode(array('A','B','C'));

select a, b, exp, bucket  from   (select 1 as a, 2 as b, "e1:b1&e2:b2" as c) T
lateral view OUTER explode(str_to_map(c,  "&", ":")) tabeAlias AS exp, bucket

a . b . exp . bucket
1   2   e1    b1
1   2   e2    b2


select a, b, exp, bucket  from
(select 1 as a, 2 as b, "e1:b1&e2:b2" as c
 UNION 
 select 10 as a, 20 as b, NULL as c
) T
lateral view OUTER explode(str_to_map(c,  "&", ":")) tabeAlias AS exp, bucket

a . b . exp . bucket
1   2   e1    b1
1   2   e2    b2
10  20  NULL  NULL
```

## Custom Map/Reduce Scripts

 TRANSFORM clause   embeds the mapper and the reducer scripts.
```
SELECT TRANSFORM(pv_users.userid, pv_users.date) USING 'map_script' AS dt, uid CLUSTER BY dt FROM pv_users;
```

## Keywords MAP and REDUCE
MAP and REDUCE are "syntactic sugar" for the more general select transform:

```
FROM (
     FROM pv_users
     MAP pv_users.userid, pv_users.date
     USING 'map_script'
     AS dt, uid
     CLUSTER BY dt) map_output
 
 INSERT OVERWRITE TABLE pv_users_reduced
     REDUCE map_output.dt, map_output.uid
     USING 'reduce_script'
     AS date, count;
 ```    
## Distribute by Clustered by Sort by
<https://cwiki.apache.org/confluence/display/Hive/LanguageManual+SortBy>


the corresponding tables we want to join on have to be set up in the same manner with the joining columns bucketed and the bucket sizes being multiples of each other to work. The second part is the optimized query for which we have to set a flag to hint to Hive that we want to take advantage of the bucketing in the join (SET hive.optimize.bucketmapjoin=true;).
Hive uses the columns in SORT BY to sort the rows before feeding the rows to a reducer.

### Difference between Sort By and Order By
Hive supports SORT BY which sorts the data per reducer. The difference between "order by" and "sort by" is that the former guarantees total order in the output while the latter only guarantees ordering of the rows within a reducer. If there are more than one reducer, "sort by" may give partially ordered final results.

Cluster By and Distribute By are used mainly with the Transform/Map-Reduce Scripts. But, it is sometimes useful in SELECT statements if there is a need to partition and sort the output of a query for subsequent queries.

Cluster By is a short-cut for both Distribute By and Sort By.

Hive uses the columns in Distribute By to distribute the rows among reducers. All rows with the same Distribute By columns will go to the same reducer. However, Distribute By does not guarantee clustering or sorting properties on the distributed keys.

## Co-Groups

```
FROM (
     FROM (
             FROM action_video av
             SELECT av.uid AS uid, av.id AS id, av.date AS date
 
            UNION ALL
 
             FROM action_comment ac
             SELECT ac.uid AS uid, ac.id AS id, ac.date AS date
     ) union_actions
     SELECT union_actions.uid, union_actions.id, union_actions.date
     CLUSTER BY union_actions.uid) map
 
 INSERT OVERWRITE TABLE actions_reduced
     SE
```
