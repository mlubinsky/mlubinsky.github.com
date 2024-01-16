I bought this:
https://www.udemy.com/cart/success/1027511410/

### Storage
```
As data is loaded, Snowflake organizes data into 16MB variable length chunks called micro-partitions.
 It automatically captures metadata statistics about every entry, including every column's minimum and maximum value.

Snowflake Micro-partitions are immutable, and, once written cannot be modified

This means an update against one or more rows creates a new version of the entire micro-partition with the updated rows

The prior micro-partition is kept for time travel or immediately removed as required. 
```

### Performance

https://www.analytics.today/blog/top-3-snowflake-performance-tuning-tactics

```
select query_type
,      warehouse_size
,      warehouse_name
,      partitions_scanned
,      partitions_total
,      partitions_scanned / nullifzero(partitions_total) * 100 as pct_scanned
from sb_query_history
where warehouse_size is not null
and   partitions_scanned > 1000
and   pct_scanned > 0.8
order by partitions_scanned desc,
         pct_scanned desc;
```

### Clustering

https://docs.snowflake.com/en/user-guide/tables-clustering-keys

https://www.analytics.today/blog/snowflake-clustering-best-practice

alter table sales   cluster by (status, store_no);

### WDH
```
Virtual Warehouse consists of several servers, and each server is a computer with (currently) eight virtual CPUs, memory and SSD storage.  When a query is executed, data is read from Remote Storage into Local Storage (SSD), acting as a data cache.  

When created, a Virtual Warehouse comprises a cluster of servers that work together as a single machine and are sized as simple T-Shirt sizes.
SIZE     NODES       VCPUs
XSMALL  1            8
SMALL   2            16
MEDIUM  4            32
LARGE   8            64 
XLARGE  16           128
X2LARGE 32           256
...
X6LARGE


create warehouse PROD_REPORTING with
        warehouse_size     = SMALL
       auto_suspend        = 600
       auto_resume         = true
       initially_suspended = true
       comment = 'PROD Reporting Warehouse';

use warehouse PROD_REPORTING;

alter warehouse PROD_REPORTING set
   warehouse_size    = MEDIUM;


alter warehouse PROD_REPORTING set
    warehouse_size    = MEDIUM
    min_cluster_count = 1
    max_cluster_count = 5
    scaling_policy = ‘STANDARD’;

```
### Stream

### Task

CREATE OR REPLACE TASK x 
WAREHAUSE = COMPUTE_WH
SCHEDULE="USING CRON  * * 7 UTC'  # SCHEDULE='1 MINUTE'
AS 'SQL STAREMENT'

Tree of tasks

### Transient, Permanent and External tables

### Dynamic table 

https://docs.snowflake.com/en/user-guide/dynamic-tables-about

### UDF / store proc

https://docs.snowflake.com/en/developer-guide/snowflake-scripting/index

```
CREATE OR REPLACE PROCEDURE x()
RETURNS FLOAT
LANGUAGE SQL
AS
$$
   SQL STATEMENTS
$$
```

https://www.youtube.com/watch?v=GUn9zN-wtf4

https://www.decube.io/post/snowflake-vs-databricks-side-by-side-comparison

https://habr.com/ru/post/663922/

https://docs.snowflake.com/en/

https://www.youtube.com/watch?v=kqZRXoFcKo0  What Is Information Schema In Snowflake | Chapter-22

https://www.youtube.com/watch?v=Jg5KQ7UpaqI. Interview questions

https://github.com/Snowflake-Labs/awesome-snowflake

snowflake concepts like Streams, tasks, warehouse optimizations, SQL tuning/pruning

https://christianlauer90.medium.com/how-snowflake-enforces-its-data-cloud-snowflake-summit-2022-a34caab204ad

https://www.snowflake.com/blog/snowpark-python-innovation-available-all-snowflake-customers/

###

https://www.linkedin.com/learning/learning-snowflakedb/learn-the-snowflake-data-life-cycle?autoplay=true&u=2102905

https://github.com/lynnlangit/learn-snowflakedb

https://medium.com/snowflake

https://www.youtube.com/playlist?list=PLba2xJ7yxHB73xHFsyu0YViu3Hi6Ckxzj

https://toppertips.com/

https://toppertips.com/snowflake-etl-example-ch19-part01


### Overview

https://apisero.com/airflow-integration-with-snowflake/ Airflow + Snowflake

spark + snowflake:
https://medium.com/@pious.tiwari/use-spark-with-snowflake-as-datasource-c390447a0762

<https://www.infoq.com/presentations/snowflake-architecture/>

<https://www.analytics.today/blog/tuning-snowflake>

<https://www.analytics.today/blog/database-administration-snowflake>

<https://www.analytics.today/blog/high-performance-real-time-processing-with-snowflake>

<https://snowflakecommunity.force.com/s/question/0D50Z00009F8nPTSAZ/how-to-choose-the-right-virtual-warehouse-size-in-snowflake-for-your-workload>

```
1. How does snowflake determine that sufficient resources are not available for a particular query? To put it in a different way, how does snowflake determine the amount resources required by a query?

Snowflake has real time data on CPU, memory and SSD usage on the cluster, and estimates of the cost of executing queries to determine if there are resources available. For example, a query estimated to scan terabytes of data may need to run on every node on the cluster in parallel, would need sufficient free resources to be executed, and may be suspended until resources are available. The objective is to provide a consistent query elapsed time for a given warehouse size.

This means, once a query has started, it will be given resources to complete, and the machine will not be over-loaded with additional queries. (Unlike nearly every other on-premise data warehouse I've used).

2. Can we create multi-cluster warehouse with different sizes for each cluster?


No. The multi-cluster feature aims to simply provide the same as existing query performance for additional users. You'll see why in the next question. 

3. "Multi-cluster warehouses are best utilized for scaling resources to improve concurrency for users/queries. They are not as beneficial for improving the performance of slow-running queries or data loading. For these types of operations, resizing the warehouse provides more benefits."
Is it better to use a warehouse of size Large or use a multi-cluster warehouse with two clusters of size Medium each?
The statement implies that a huge resource hungry might run better on single big warehouse rather than on multi-cluster warehouse with small clusters. Why?

The way I explain this to customers is (a) Scale up for data volumes (b) Scale out for additional users.

Effectively, if you have query workloads processing gigabytes of data, the elapsed time will half each time you scale up the resources. This is because each increase includes more hardware. eg. A medium VWH has 4 nodes available but a large has 8 nodes. When a query is executed on a cluster, it will use (if available) as many as the nodes in parallel to execute the query. Hence a LARGE VWH will complete the same task twice as fast.

Note: A very small query might only use one thread on a single node, and for this reason, increasing the warehouse size for very short running queries may not be the most efficient use of resources.

However, if you configure your VWH to scale out (for example MEDIUM with a maximum of two clusters), it will ONLY scale out if the number of concurrent processes (or users) overload the machine. Any single query will only ever execute on a single MEDIUM sized cluster. The other queries will be free to use the second cluster.


That's why if you have a single LARGE cluster it will always complete a large workload twice as fast as a MEDIUM - even if multi-cluster (scale out) is switched on.

Note: My tests (to be written up in an article) demonstrate performance does indeed double at each step in warehouse size - PROVIDED YOU'RE PROCESSING AT LEAST A GIGABYTE OF DATA. For very small queries (under 1Gb scanned), the performance gets no benefit over about an XLARGE.
<https://www.reddit.com/r/BusinessIntelligence/comments/d1x42g/is_anyone_here_using_snowflake_i_especially_want/> . Criticizm

 Snowflake is case-sensitive. So you have to wrap any string queries in a lower() statement to get things to lower case. This requirement has resulted in some bad data from a few analysts (or longer query turnaround times) until we all got used to it.
```

Cool staff in snowflake 10 articles:
<https://sqlkover.com/?s=Cool+Stuff+in+Snowflake&submit=Search>

 

<https://www.dataengineeringpodcast.com/snowflakedb-cloud-data-warehouse-episode-110/>

<https://juliandontcheff.wordpress.com/2019/01/14/few-interesting-facts-about-oracle-adb-redshift-and-snowflake/>

<https://www.periscopedata.com/blog/interactive-analytics-redshift-bigquery-snowflake>

<http://dwgeek.com/snowflake-architecture-cloud-data-warehouse.html/>

<https://docs.snowflake.net/manuals/other-resources.html>

<https://nl.devoteam.com/wp-content/uploads/sites/15/2018/04/a-detailed-view-inside-snowflake.pdf>

<https://s3.amazonaws.com/snowflake-workshop-lab/Snowflake_free_trial_LabGuide.pdf>

<https://blog.getdbt.com/how-we-configure-snowflake/>

<https://hevodata.com/blog/snowflake-data-warehouse-features/>

<https://getaround.tech/snowflake-migration/>

<https://www.stitchdata.com/blog/migration-from-redshift-to-snowflake/>

<https://discourse.getdbt.com/t/structure-snowflake-database-schema/211/9>

<https://visualbi.com/blogs/snowflake/snowflake-best-practices-performance-optimization/>

<https://www.infoq.com/presentations/snowflake-automatic-clustering/>

 By default, Snowflake cluster is based on the order in which we receive the records. Just imagine a stream of records coming into the system and we just chop when we are able to create the file size. The only partitioning logic that we use is, "Are we able to create the file size that we want?" We keep collecting, let's say, we have 10 records when we can create the file size that we want, we chop at every 10 records and create this file and flush to S3. As you can see, it's the values are grouped only by one dimension and that is the dimension in which data is being loaded into the system. It's not grouped by any other logical dimension within the data. We don't look into the data itself and try to group it based on a specific column by default.

### Migration from Redshift

<https://redpillanalytics.com/so-you-want-to-migrate-to-snowflake-part-2/>

<http://erqt.mikeprange.de/redshift-to-snowflake-migration.html>

<https://community.snowflake.com/s/article/Migrating-from-Redshift-to-Snowflake>

<https://support.snowflake.net/s/article/How-To-Migrate-Data-from-Amazon-Redshift-into-Snowflake>

https://community.snowflake.com/s/article/Migrating-from-Redshift-to-Snowflake-in-Python

<https://snowflakesolutions.net/snowflake-vs-redshift/>

<https://discourse.getdbt.com/t/the-difference-between-users-groups-and-roles-on-postgres-redshift-and-snowflake/429>

<https://medium.com/@jthandy/how-compatible-are-redshift-and-snowflakes-sql-syntaxes-c2103a43ae84>

```
Warehouses” and “databases” are not the same thing within Snowflake. A database in Snowflake really 
just represents a storage partition, while warehouses are compute resources.

You can have multiple warehouses processing data in the same “database” concurrently. 
For example, you can have a “segment” warehouse writing to the “raw” database 
at the same time a “stitch” warehouse is writing to the “raw” database. 
I am not aware of any scaling considerations with “databases” within Snowflake. 
My understanding is that a database is just an organizational partition on top of the storage to help
with stuff like permissions. Your scaling would be handled with warehouses.
```


<https://docs.snowflake.net/manuals/sql-reference-commands.html>

<https://www.sigmacomputing.com/blog> . SIGMACOMPUTING

<https://yellowbrick.com/> .   YELLOWBRICK


https://towardsdatascience.com/machine-learning-in-snowflake-fdcff3bdc1a7

<https://docs.snowflake.net/manuals/user-guide/tables-micro-partitions.html>

<http://cloudsqale.com/2019/12/02/snowflake-micro-partitions-and-clustering-depth/>

<https://medium.com/hashmapinc/snowflakes-cloud-data-warehouse-what-i-learned-and-why-i-m-rethinking-the-data-warehouse-75a5daad271c>

<https://tech.instacart.com/migration-from-redshift-to-snowflake-the-path-for-success-4caaac5e3728>

<https://medium.com/@richiebachala/snowflake-redshift-bigquery-b84d2cb60168>


<https://www.alooma.com/answers/why-did-you-choose-snowflake-over-amazon-redshift-for-your-cloud-data-warehouse>

<https://www.alooma.com/blog/a-guide-to-selecting-the-right-cloud-data-warehouse>

<https://www.periscopedata.com/blog/interactive-analytics-redshift-bigquery-snowflake>

<https://hevodata.com/blog/snowflake-vs-redshift/>

<https://medium.com/@ubethke/comparing-snowflake-cloud-data-warehouse-to-aws-athena-query-service-4f0ea32ef6db>


<https://0x0fff.com/snowflake-the-good-the-bad-and-the-ugly/>

<https://www.snaplogic.com/blog/observations-from-the-snowflake-summit-19>

<https://www.reddit.com/r/aws/comments/6mm6p4/what_is_your_experience_using_snowflake/>

<https://www.reddit.com/r/bigdata/comments/e1g7jf/are_there_any_competitors_to_snowflake/>

## Data Load

<https://www.linkedin.com/pulse/building-etlelt-solutions-leverage-power-snowflake-2-van-schalkwyk/>

<https://www.linkedin.com/pulse/building-etlelt-solutions-leverage-power-snowflake-1-van-schalkwyk/> 
https://www.blendo.co/blog/etl-snowflake-data-warehouse/

 For example, you might want to exclude some PII related fields from loading into the data warehouse for privacy reasons.

Snowflake, allows you to perform some tasks like:

Filtering fields/columns out during COPY
Perform CASTING on your fields if you want to change your data types
Reorder your columns
Truncate data
Your COPY command for a bulk or Snowpipe loading process can contain a “SELECT” part which transforms the data based on your requirements.

Thatis is possible because of the great separation between storage and processing in Snowflake.

We saw that it is possible to perform some core transformation tasks during the loading of your data into Snowflake. Although this is a powerful mechanism, you might still need to transform further your data to make it ready for consumption for your analysts. For example, you might want to create fact and dimension tables as part of a star schema.



https://docs.snowflake.net/manuals/user-guide/data-load-snowpipe-intro.html

### Looker
<https://blog.redpillanalytics.com/managing-snowflake-data-warehouse-compute-in-looker-e445543987b2>

<https://github.com/llooker/snowflake-usage-block>

<https://medium.com/sevensenders-techblog/speaking-data-with-snowflake-and-looker-e4b219ed37aa>

<https://looker.com/blog/using-snowflake-mvs-in-looker>
