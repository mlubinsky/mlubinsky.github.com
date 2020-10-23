
<https://habr.com/ru/company/mailru/blog/504952/> Avro, Parquet, ...


Problem: if we have no records in Hive partition the copy in redshift will fail
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

### CASCADE keyword

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


### Lateral
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
