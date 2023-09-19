### Amazon Redshift does not enforce primary key and foreign key constraints
Specify the primary key and foreign keys for all your tables.

Amazon Redshift does not enforce primary key and foreign key constraints, 
but the query optimizer uses them when it generates query plans. 
 

### DISTRIBUTION KEY
https://docs.aws.amazon.com/redshift/latest/dg/c_best-practices-best-dist-key.html
```
When you run a query, the query optimizer redistributes the rows to the compute nodes as needed to perform any joins and aggregations. 
The goal in selecting a table distribution style is to minimize the impact of the redistribution step by locating the data
 where it needs to be before the query is run.
```
When you create a table, you can designate one of four distribution styles; AUTO, EVEN, KEY, or ALL.
https://docs.aws.amazon.com/redshift/latest/dg/c_choosing_dist_sort.html
```
With AUTO distribution, Amazon Redshift assigns an optimal distribution style based on the size of the table data. 
For example, if AUTO distribution style is specified, Amazon Redshift initially assigns the ALL distribution style to a small table.
When the table grows larger, Amazon Redshift might change the distribution style to KEY, 
choosing the primary key (or a column of the composite primary key) as the distribution key. 
If the table grows larger and none of the columns are suitable to be the distribution key, Amazon Redshift changes the distribution style to EVEN. 
The change in distribution style occurs in the background with minimal impact to user queries.
```
### SORT KEY
https://docs.aws.amazon.com/redshift/latest/dg/c_best-practices-sort-key.html


### CONSTRAINTS
```
Define primary key and foreign key constraints between tables wherever appropriate.
Even though they are informational only, the query optimizer uses those constraints to generate more efficient query plans.

Do not define primary key and foreign key constraints unless your application enforces the constraints.
Amazon Redshift does not enforce unique, primary-key, and foreign-key constraints.
```


<https://stackoverflow.com/questions/62418138/redshift-copy-from-the-empty-s3-partition>

<https://www.intermix.io/blog/14-data-pipelines-amazon-redshift/>

<https://sonra.io/2018/01/01/using-apache-airflow-to-build-a-data-pipeline-on-aws/>


https://docs.aws.amazon.com/redshift/latest/dg/r_COUNT.html  APPROXIMATE COUNT DISTINCT

<https://www.youtube.com/user/AmazonWebServices>

<https://fivetran.com/blog/warehouse-benchmark>

<https://fivetran.com/blog/obt-star-schema>

```
When you run a query, WLM assigns the query to a queue according to the user's user group or by matching a query group that is listed in the queue configuration with a query group label that the user sets at runtime.

Currently, the default for clusters using the default parameter group is to use automatic WLM. Automatic WLM manages query concurrency and memory allocation. For more information, see Implementing automatic WLM.

With manual WLM, Amazon Redshift configures one queue with a concurrency level of five, which enables up to five queries to run concurrently, plus one predefined Superuser queue, with a concurrency level of one. You can define up to eight queues. Each queue can be configured with a maximum concurrency level of 50. The maximum total concurrency level for all user-defined queues (not including the Superuser queue) is 50.

The easiest way to modify the WLM configuration is by using the Amazon Redshift Management Console. You can also use the Amazon Redshift command line interface (CLI) or the Amazon Redshift API.
```


### Locks in Redshift

https://docs.aws.amazon.com/redshift/latest/dg/r_STV_LOCKS.html

```
select distinct(id) table_id
,trim(datname)   db_name
,trim(nspname)   schema_name
,trim(relname)   table_name
from stv_locks
join stv_tbl_perm on stv_locks.table_id = stv_tbl_perm.id
join pg_class on pg_class.oid = stv_tbl_perm.id
join pg_namespace on pg_namespace.oid = relnamespace
join pg_database on pg_database.oid = stv_tbl_perm.db_id;


select table_id, last_update, lock_owner, lock_owner_pid from stv_locks;


select pg_terminate_backend(26023);
```



Both Snowflake and Redshift Spectrum allow queries on ORC files as external files located in Amazon S3. However, Snowflake edged out Redshift Spectrum for its ability to also load and transform ORC data files directly into Snowflake.


####   \d stl_load_errors

```
     Column      |            Type             | Modifiers
-----------------+-----------------------------+-----------
 userid          | integer                     |
 slice           | integer                     |
 tbl             | integer                     |
 starttime       | timestamp without time zone |
 session         | integer                     |
 query           | integer                     |
 filename        | character(256)              |
 line_number     | bigint                      |
 colname         | character(127)              |
 type            | character(10)               |
 col_length      | character(10)               |
 position        | integer                     |
 raw_line        | character(1024)             |
 raw_field_value | character(1024)             |
 err_code        | integer                     |
 err_reason      | character(100)              |
 is_partial      | integer                     |
 start_offset    | bigint                      |
 
 ```

## Dremio

<https://www.dremio.com/>

<https://xcalar.com>

## ClickHouse

<https://habr.com/ru/company/ua-hosting/blog/483112/>

<https://news.ycombinator.com/item?id=19019943>

<https://www.altinity.com/blog/migrating-from-redshift-to-clickhouse>

<https://weekly-geekly.github.io/articles/433346/index.html>

## Looker

<https://training.looker.com/looker-for-data-consumers> training 
<https://discourse.looker.com>

Redshift Optimization by AWS
<https://looker.com/platform/blocks/source/redshift-optimization-by-aws>

### Fabio Beltramini: Deep Dive_Redshift Optimization
<https://www.slideshare.net/looker/join-2017deep-diveredshift-optimization>

<https://help.looker.com/hc/en-us/articles/360023627014--Analytic-Block-Redshift-Performance-Optimization>

<https://github.com/llooker/blocks_redshift_admin>

<https://www.youtube.com/watch?v=wCxwYb5voJc> . Fabio Beltramini JOIN 2017 Deep Dive - Redshift Optimization


<https://docs.looker.com/data-modeling/learning-lookml/how-looker-generates-sql>

<https://www.intermix.io/blog/fix-slow-looker-dashboards-redshift/>


<http://rkulla.blogspot.com/2017/10/using-amazon-redshift-with-looker.html>

<https://help.looker.com/hc/en-us/articles/360023513514-How-to-Optimize-SQL-with-EXPLAIN>

<https://help.looker.com/hc/en-us/articles/360001847227>

<https://help.looker.com/hc/en-us/articles/360001288108-Dynamically-Select-Fields-Using-Parameters>

## N-Tile

https://docs.aws.amazon.com/redshift/latest/dg/r_WF_NTILE.html
```
WITH A as (
select 1 as x
union all
select 2 as x
union all
select 3 as x
union all
select 4 as x
union all
select 5 as x
union all
select 6 as x
union all
select 7 as x
)
select ntile, avg(x) FROM 
( 
    SELECT x, ntile(3)   OVER (order by x ASC) FROM A
) B group by ntile;
```
 


## GRANT Permission
https://aodba.com/how-to-create-a-schema-and-grant-access-to-it-in-aws-redshift/
```
GRANT USAGE ON SCHEMA my_schema_name TO my_user_name;
GRANT SELECT ON ALL TABLES IN SCHEMA my_schema_name TO my_user_name;
ALTER DEFAULT PRIVILEGES IN SCHEMA my_schema_name GRANT SELECT ON TABLES TO my_user_name;
```

### UDF
<https://docs.aws.amazon.com/redshift/latest/dg/udf-creating-a-scalar-sql-udf.html>
```
create function f_sql_greater (float, float)
  returns float
stable
as $$
  select case when $1 > $2 then $1
    else $2
  end
$$ language sql; 
```




### stored procedures
<https://docs.aws.amazon.com/redshift/latest/dg/stored-procedure-overview.html>

### splitting string

<https://docs.aws.amazon.com/redshift/latest/dg/r_POSITION.html>

<https://docs.aws.amazon.com/redshift/latest/dg/r_STRPOS.html> . (one-based, not zero-based). 0 if not found

POSITION(), STRPOS()

Find the beginning of bucket:
``` 
    bucket_start_pos= SELECT STRPOS(active_exp_map, exp_name || ':') 
    if bucket_start_pos = 0:
       return ''
    else:      
       bucket_start_pos = bucket_start_pos + LEN(exp_name || ':')
```
Find the next & (or the end of string) after pos:
SUBSTRING(string, start_position, number_characters )
```
  bucket_end_pos = select STRPOS(SUBSTRING(active_exp_map, pos, LEN(active_exp_map), '&') -- may be 0
  if bucket_end_pos = 0:
     experiment= SUBSTRING(active_exp_map, bucket_start_pos, LEN(exp_name)  )
  else:
      experiment= SUBSTRING(SUBSTRING(active_exp_map, pos, LEN(active_exp_map)), 1, bucket_end_pos)
```
scalar UDF



Assuming what : is added to arg2 during the call

```
create function f_bucket (varchar, varchar)
  returns varchar
stable
as $$

SELECT 
    CASE 
        WHEN 0 =  STRPOS($1, $2 ) THEN ''
        ELSE 
	    CASE 
               WHEN 0 = STRPOS(SUBSTRING($1, STRPOS($1, $2) + LEN($2), LEN($1)), '&')  
	           THEN SUBSTRING($1, STRPOS($1, $2)+ LEN($2), LEN($1) )
	       ELSE
	               -- there is an issue in next line
	                SUBSTRING($1, STRPOS($1, $2) + LEN($2) ,  STRPOS($1, '&') - STRPOS($1, $2) - LEN($2)   )
           END 
    END 	   
$$ language sql;  

select f_bucket('abcxx:de','abcxx:');  -- OK
select f_bucket('abcxx:de&f:gkk','f:');  -- OK
select f_bucket('abcxx:de&f:gkk','abcxx:');  -- ok
select f_bucket('a:b&c:d','a:');   -- ok

select   STRPOS('a:b&c:d', 'a:') + LEN('a:')  -- 3
select   SUBSTRING('a:b&c:d', STRPOS('a:b&c:d', 'a:') + LEN('a:'), LEN('a:b&c:d'))  -- b&c:d
select STRPOS(SUBSTRING('a:b&c:d', STRPOS('a:b&c:d', 'a:') + LEN('a:'), LEN('a:b&c:d')), '&')   -- 2 (position of &)
select SUBSTRING('a:b&c:d', STRPOS('a:b&c:d', 'a:') + LEN('a:') , STRPOS('a:b&c:d', '&') - STRPOS('a:b&c:d', 'a:') - LEN('a:')  ) -- b 
```



Use regexp_count to determine how many instances of our delimiter (", ") are found 

 We will assume that a table of numbers already exists in the database, though this can be created using this pattern:
 <https://discourse.looker.com/t/generating-a-numbers-table-in-mysql-and-redshift/482>
 
 The split_part function, which takes a string, splits it on some delimiter, and returns the first, second, ... , nth value specified from the split string.

<https://help.looker.com/hc/en-us/articles/360024266693-Splitting-Strings-into-Rows-in-the-Absence-of-Table-Generating-Functions>
```
SELECT row_number() OVER(order by 1) AS product_tag_id
  , products.id as product_id
  , split_part(products.tags, ', ', numbers.num) AS tag_name
FROM products
JOIN numbers
ON numbers.num <= regexp_count(products.tags, ',\\s') + 1
```



### One more

```
create or replace function f_bucket (varchar, varchar)
 returns varchar
stable
as $$
SELECT 
  CASE 
    WHEN 0 = STRPOS($1, $2 ) THEN ''
    ELSE 
	  CASE 
        WHEN 0 = STRPOS(SUBSTRING($1, STRPOS($1, $2) + LEN($2), LEN($1)), '&')  
	      THEN SUBSTRING($1, STRPOS($1, $2) + LEN($2), LEN($1) )
	    ELSE
             SUBSTRING($1, STRPOS($1, $2) + LEN($2) , STRPOS($1, '&') - STRPOS($1, $2) - LEN($2)  )
      END 
  END 	  
$$ language sql;
```



<https://www.holistics.io/blog/splitting-array-string-into-rows-in-amazon-redshift-or-mysql/>

```
create table books (tags varchar(1000));

insert into books values
	('A, B, C, D'),
	('D, E'),
	('F'),
	('G, G, H')
;

with NS AS (  
  select 1 as n union all
  select 2 union all
  select 3 union all
  select 4 union all
  select 5 union all
  select 6 union all
  select 7 union all
  select 8 union all
  select 9 union all
  select 10
)
select  
  TRIM(SPLIT_PART(B.tags, ',', NS.n)) AS tag
from NS  
inner join books B ON NS.n <= REGEXP_COUNT(B.tags, ',') + 1
```

### dim_experiment  - extract the buckets for given experiment

```
select id, SUBSTRING(single_bucket, 1, STRPOS(single_bucket, ':')-1 ) FROM (
 with NS AS (
  select 1 as n union all
  select 2 union all
  select 3 union all
  select 4 union all
  select 5 union all
  select 6 union all
  select 7 union all
  select 8 union all
  select 9 union all
  select 10
)
select  A.id, TRIM(SPLIT_PART(A.buckets, ',', NS.n))  as single_bucket from NS
inner join roku.dim_experiment A  ON NS.n <= REGEXP_COUNT(A.buckets, ',') + 1
where id = 'phmXsT1GH'
) C;
```




```
CREATE TABLE dev.test_active_exp_map(id integer, active_exp_map VARCHAR(1000)); 
 
 insert into dev.test_active_exp_map (id, active_exp_map)
 values(1, 'e1:b1&e2:b2')

 insert into dev.test_active_exp_map (id, active_exp_map)
 values(2, 'e3:b3')
 
 select id, split_part(active_exp_map,'&',1)  from dev.test_active_exp_map . -- 1st element
 
  select id, split_part(active_exp_map,'&',2) from dev.test_active_exp_map .  -- 2nd element
 
 --- next query put the chuncks between & as separate rows
 with NS AS (
  select 1 as n union all
  select 2 union all
  select 3 union all
  select 4 union all
  select 5 union all
  select 6 union all
  select 7 union all
  select 8 union all
  select 9 union all
  select 10
)
select TRIM(SPLIT_PART(A.active_exp_map, '&', NS.n))   from NS
inner join dev.test_active_exp_map A  ON NS.n <= REGEXP_COUNT(A.active_exp_map, '&') + 1

--- next query put chuncks between & as rows and between : in separate columns
 
  with NS AS (
  select 1 as n union all
  select 2 union all
  select 3 union all
  select 4 union all
  select 5 union all
  select 6 union all
  select 7 union all
  select 8 union all
  select 9 union all
  select 10
)
select
  split_part(TRIM(SPLIT_PART(A.active_exp_map, '&', NS.n)), ':',1) as test,  split_part(TRIM(SPLIT_PART(A.active_exp_map, '&', NS.n)), ':',2) as bucket
from NS
inner join dev.test_active_exp_map A  ON NS.n <= REGEXP_COUNT(A.active_exp_map, '&') + 1
 
```

###  JSON
<https://docs.aws.amazon.com/redshift/latest/dg/json-functions.html>

<https://popsql.com/learn-sql/redshift/how-to-query-a-json-column-in-redshift/>

<https://blog.getdbt.com/how-to-unnest-arrays-in-redshift/>

```
create table dbt_jthandy.flatten_test (
    order_id int, 
    json_text varchar(1000)
    )
;

insert into dbt_jthandy.flatten_test
  (order_id, json_text) 
values
  (1, '{  
     "items":[  
        {  
           "id":"fa4b6cd3-4719-4b97-848b-7f2025f5e693",
           "quantity":1,
           "sku":"M900353-SWB-RYL-2",
           "list_price":60.0
        },
        {  
           "id":"c39f9474-a278-4162-9cfa-aa068f4e1665",
           "quantity":1,
           "sku":"F033199-SWB-FWL-1",
           "list_price":20.0
        }
     ]}')
;
```

<https://sonra.io/2019/04/24/working-with-json-in-redshift-options-limitations-and-alternatives/>
```

create table books (tags varchar(1000));

insert into books values
	('["A", "B", "C", "D"]'),
	('["D", "E"]'),
	('["F"]'),
	('["G", "G", "H"]')
;


with NS AS (
	select 1 as n union all
    select 2 union all
    select 3 union all
    select 4 union all
    select 5 union all
    select 6 union all
    select 7 union all
    select 8 union all
    select 9 union all
    select 10
)
select
  TRIM(JSON_EXTRACT_ARRAY_ELEMENT_TEXT(B.tags, NS.n - 1)) AS val
from NS
inner join books B ON NS.n <= JSON_ARRAY_LENGTH(B.tags)

```

## Redshift functions
Functions - <https://docs.aws.amazon.com/redshift/latest/dg/c_SQL_functions.html>
<https://docs.aws.amazon.com/redshift/latest/dg/r_Window_function_examples.html>

https://docs.aws.amazon.com/redshift/latest/dg/r_STRTOL.html
select strtol('0xf',16) answer: 15

<https://docs.aws.amazon.com/redshift/latest/dg/r_Examples_of_avg_WF.html>


<https://aws.amazon.com/blogs/big-data/simplify-management-of-amazon-redshift-clusters-with-the-redshift-console/>

<https://www.youtube.com/user/AWSwebinars/search?query=redshift> AWS Redshift Tech Talk

<https://docs.aws.amazon.com/redshift/latest/dg/c_high_level_system_architecture.html>

 #### Dense Compute (DC2) nodes 
 <https://aws.amazon.com/about-aws/whats-new/2017/10/amazon-redshift-announces-dense-compute-dc2-nodes-with-twice-the-performance-as-dc1-at-the-same-price/> 
 to provide low latency and high throughput for demanding data warehousing workloads. DC2 nodes feature powerful Intel E5-2686 v4 (Broadwell) CPUs, fast DDR4 memory, and NVMe-based solid state disks (SSDs). We’ve tuned Amazon Redshift to take advantage of the better CPU, network, and disk on DC2 nodes, providing up to twice the performance of DC1 at the same price. 
 <https://aws.amazon.com/redshift/pricing/>

<https://aws.amazon.com/redshift/>

<https://aws.amazon.com/blogs/aws/amazon-redshift-update-next-generation-compute-instances-and-managed-analytics-optimized-storage/>

<https://docs.aws.amazon.com/redshift/latest/mgmt/configuring-connections.html>

<https://aws.amazon.com/blogs/big-data/simplify-management-of-amazon-redshift-clusters-with-the-redshift-console/>

<https://aws.amazon.com/blogs/big-data/query-your-amazon-redshift-cluster-with-the-new-query-editor/>

<https://aws.amazon.com/blogs/aws/using-spatial-data-with-amazon-redshift/> spatial data


### Redshift Performance

<https://aws.amazon.com/about-aws/whats-new/2018/07/amazon-redshift-now-provides-customized-best-practice-recommendations-with-advisor/>

<https://aws.amazon.com/blogs/big-data/top-10-performance-tuning-techniques-for-amazon-redshift/>

<https://aws.amazon.com/blogs/big-data/top-8-best-practices-for-high-performance-etl-processing-using-amazon-redshift/>

<https://aws.amazon.com/blogs/big-data/amazon-redshift-engineerings-advanced-table-design-playbook-distribution-styles-and-distribution-keys/>

<https://www.youtube.com/watch?v=wCxwYb5voJc> . Fabio Beltramini JOIN 2017 Deep Dive - Redshift Optimization

<https://www.youtube.com/watch?v=6UEWFAtvmsY>

<https://www.youtube.com/watch?v=iuQgZDs-W7A>

<https://discourse.looker.com/t/troubleshooting-redshift-performance-extensive-guide/326>

#### analyze predicate
<https://aws.amazon.com/blogs/big-data/collect-data-statistics-up-to-5x-faster-by-analyzing-only-predicate-columns-with-amazon-redshift/>

#### short query acceleration
<https://aws.amazon.com/about-aws/whats-new/2017/11/amazon-redshift-uses-machine-learning-to-accelerate-dashboards-and-interactive-analysis/>

#### caching
<https://aws.amazon.com/about-aws/whats-new/2017/11/amazon-redshift-introduces-result-caching-for-sub-second-response-for-repeat-queries/>

#### late materiazation
<https://aws.amazon.com/about-aws/whats-new/2017/12/amazon-redshift-introduces-late-materialization-for-faster-query-processing/>

#### query monitoring rules
<https://docs.aws.amazon.com/redshift/latest/dg/cm-c-wlm-query-monitoring-rules.html>

 specifying sort keys, distribution keys, and column encodings can significantly improve storage, I/O, and query performance.

#### system tables
<https://aws.amazon.com/premiumsupport/knowledge-center/logs-redshift-database-cluster/>

Executed queries are logged in STL_QUERY. DDL statements are logged in STL_DDLTEXT. 
The text of non-SELECT SQL commands are logged in STL_UTILITYTEXT.

SVL_STATEMENTTEXT: Provides a complete record of SQL commands that have been run on the system. 
Combines all of the rows in the STL_DDLTEXT, STL_QUERYTEXT, and STL_UTILITYTEXT tables.

STL_CONNECTION_LOG: Logs authentication attempts, connections, or disconnections.

<https://docs.aws.amazon.com/redshift/latest/dg/c_intro_STL_tables.html>

<https://docs.aws.amazon.com/redshift/latest/dg/r_EXPLAIN.html>

<https://docs.aws.amazon.com/redshift/latest/dg/r_PG_TABLE_DEF.html>

<https://docs.aws.amazon.com/redshift/latest/dg/r_SVV_TABLE_INFO.html>

<https://docs.aws.amazon.com/redshift/latest/dg/r_STL_QUERY_METRICS.html>

```
  SELECT tablename, "column" , "type", encoding, sortkey  
  FROM  PG_TABLE_DEF 
  WHERE schemaname='roku' and distkey = true ;

  SELECT tablename, "column" , "type", encoding, sortkey,  distkey  
  FROM  PG_TABLE_DEF 
  WHERE schemaname='roku' and sortkey <> 0 ;
```

```
SELECT * FROM information_schema.tables
WHERE table_schema = 'myschema'; 

SELECT * FROM information_schema.columns
WHERE table_schema = 'myschema' AND table_name = 'mytable'; 
```

<https://docs.aws.amazon.com/redshift/latest/dg/c-query-processing.html>

<https://docs.aws.amazon.com/redshift/latest/dg/c-query-tuning.html>

<https://docs.aws.amazon.com/redshift/latest/dg/c-query-performance.html>

<https://www.intermix.io/blog/top-14-performance-tuning-techniques-for-amazon-redshift/>

<https://medium.com/udemy-engineering/improving-amazon-redshift-performance-our-data-warehouse-story-5ec1282c13d8>

### code

<https://github.com/awslabs/amazon-redshift-utils/blob/master/src/AdminScripts/top_queries.sql>

<https://github.com/awslabs/amazon-redshift-utils/tree/master/src>

<https://github.com/search?q=org%3Aawslabs+redshift>

<https://github.com/search?q=org%3Aawslabs+redshift&type=Code>

### Compression

### Data distribution across nodes
 get the most out of this feature, your data needs to be properly distributed. If your data is skewed, some nodes will have to work more than others - and your query is only as fast as the slowest node.  
<https://docs.aws.amazon.com/redshift/latest/dg/c_best-practices-best-dist-key.html>

## Amazon Redshift Advisor 
https://aws.amazon.com/about-aws/whats-new/2019/08/amazon-redshift-now-recommends-distribution-keys-for-improved-query-performance/
Amazon Redshift now recommends distribution keys for improved query performance
Posted On: Aug 20, 2019

Amazon Redshift Advisor now recommends the most appropriate distribution key for frequently queried tables to improve query performance. The Advisor generates tailored recommendations by analyzing the cluster's performance and query patterns. You can then use the ALTER TABLE ALTER DISTKEY command to add or modify the distribution key of a table, without impacting concurrent read or write queries. 

When you specify the appropriate distribution key for a table, Amazon Redshift places a similar number of rows on each node when loading data into that table. A query that joins multiple tables will run much faster, if those tables can be joined on their distribution key columns.

With this Advisor update, Amazon Redshift can now determine the appropriate distribution key, by constructing a graph representation of the SQL join history, and optimizing for data transferred across nodes when joins occur. For more information, see Choosing a Data Distribution Style.

Advisor is accessible in the left-hand navigation menu on the Amazon Redshift console. Note that Advisor will only show distribution key recommendations if they would have a significant, positive impact on your workload. For more information, see Working with Recommendations from Amazon Redshift Advisor.


<https://docs.aws.amazon.com/redshift/latest/dg/tutorial-tuning-tables-distribution.html>

<https://docs.aws.amazon.com/redshift/latest/dg/t_Distributing_data.html> Choosing data distribution style

<https://docs.aws.amazon.com/redshift/latest/dg/tutorial-tuning-tables-distribution.html>

* Distribute the fact table and one dimension table on their common columns.
* Choose the largest dimension based on the size of the filtered dataset.
* Choose a column with high cardinality in the filtered result set.
* Change some dimension tables to use ALL distribution.


### Sort keys 
Redshift stores your data on disk in sorted order according to the sort key.
<https://docs.aws.amazon.com/redshift/latest/dg/t_Sorting_data.html>


define how the data is organized within each node. If your query only needs a subset of data that is defined by a column that is in sorted order, Amazon Redshift can hone in on just that block of data for your query instead of scanning the entire table .


## Tables design

<https://aws.amazon.com/blogs/big-data/amazon-redshift-engineerings-advanced-table-design-playbook-distribution-styles-and-distribution-keys/> 

<https://docs.aws.amazon.com/redshift/latest/dg/r_CREATE_TABLE_examples.html>

<https://docs.aws.amazon.com/redshift/latest/dg/t_Defining_constraints.html>

<https://docs.aws.amazon.com/redshift/latest/dg/tutorial-tuning-tables.html>

<https://docs.aws.amazon.com/redshift/latest/dg/c_analyzing-table-design.html>

<https://docs.aws.amazon.com/redshift/latest/dg/diagnostic-queries-for-query-tuning.html#identify-queries-that-are-top-candidates-for-tuning>



<https://aws.amazon.com/blogs/aws/new-concurrency-scaling-for-amazon-redshift-peak-performance-at-all-times/> concurrency scaling

<https://www.intermix.io/blog/amazon-redshift-concurrency-scaling/>


Without using Workload Management (WLM), each query gets equal priority. The result is that some workloads may end up using excessive cluster resources and block business-critical processes.

<https://www.intermix.io/blog/automatic-wlm/>

<http://www.sqlhaven.com/>

 Redshift has a built-in S3 importer, which is the recommended way to load data. Therefore, once every 10 minutes, a script is launched that connects to Redshift and asks it to load data using the
 ```s3://events-bucket/main/year=2018/month=10/day=14/10_3*``` prefix 
 

 
You can create primary key constraint while creating tables in Redshift database but 
*it will not be enforced while loading Redshift tables*. 
Redshift query planner uses these constraints to create better query execution plan. |
If Primary key is set at the column level, it must be on a single column




<https://docs.aws.amazon.com/redshift/latest/dg/c_redshift_system_overview.html>

<https://github.com/JefClaes/amazon-redshift-fundamentals>

<https://blog.panoply.io/aws-redshift-tutorial>

<https://www.intermix.io/blog/short-query-acceleration/>

## Use cases
<https://medium.com/teads-engineering/give-meaning-to-100-billion-events-a-day-part-ii-how-we-use-and-abuse-redshift-to-serve-our-data-bc23d2ed3e07>

https://medium.com/teads-engineering/give-meaning-to-100-billion-events-a-day-part-ii-how-we-use-and-abuse-redshift-to-serve-our-data-bc23d2ed3e07

<https://www.intermix.io/blog/14-data-pipelines-amazon-redshift/>

<https://epiphany.pub/post?refId=a362fd3bffdc7eecde1838916fb8f4c267f5672b3774bd86dd23dce9dac72bee> hate log

<https://www.intermix.io/blog/modern-etl-tools-for-amazon-redshift/> 

### Stored procedures

<https://docs.aws.amazon.com/redshift/latest/dg/stored-procedure-overview.html>

<https://aws.amazon.com/blogs/big-data/bringing-your-stored-procedures-to-amazon-redshift/>

### Litvinchik
<https://tech.marksblogg.com/billion-nyc-taxi-rides-redshift-large-cluster.html>

<https://tech.marksblogg.com/all-billion-nyc-taxi-rides-redshift.html>

<https://tech.marksblogg.com/importing-data-from-s3-into-redshift.html>

<https://tech.marksblogg.com/billion-nyc-taxi-rides-redshift.html>

### Spectrum 

Amazon Redshift Spectrum to query data directly from files on Amazon S3.
<https://docs.aws.amazon.com/redshift/latest/dg/c-getting-started-using-spectrum.html>

<https://www.intermix.io/blog/amazon-redshift-spectrum-diving-data-lake/>

<https://tech.iheart.com/how-we-leveraged-redshift-spectrum-for-elt-in-our-land-of-etl-cf01edb485c0>

<https://medium.com/@thejaravi/how-we-leveraged-redshift-spectrum-for-elt-in-our-land-of-etl-cf01edb485c0>

Redshift Spectrum is new add-on service for Redshift that Amazon introduced mid-2017. 
It allows you to leverage Redshift to query data directly on S3. 
Redshift Spectrum is a good option for those who already have/work with Redshift. 
For those who do not, take a look at Athena. 

Athena is much like Redshift Spectrum with the exception of the chosen execution engine (Athena uses Presto) 
whereas Spectrum uses Redshift. It should be noted that Spectrum also follows pay-per-query pricing model like Athena.
Let’s look at how Redshift and Spectrum communicate with each other, 
how tables are created on top of stores such as S3 and just how much interoperability is provided.
Spectrum needs an external meta store for the data catalog to maintain table definitions; 
we used a Hive meta store for this purpose. Our Hive/Spectrum meta store is simply a RDS instance running MariaDB.
Once we setup Spectrum to talk with our Redshift cluster and use the newly created schema space in the Hive meta store,
any external table created in this schema using Hive is visible and usable immediately from Redshift.
You can query these tables directly from Redshift and Redshift/Spectrum will automatically move the required
portion of data (based on the query) on to Redshift cluster and execute it there.

