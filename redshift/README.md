<https://www.youtube.com/user/AmazonWebServices>


<https://fivetran.com/blog/warehouse-benchmark>

<https://fivetran.com/blog/obt-star-schema>

Both Snowflake and Redshift Spectrum allow queries on ORC files as external files located in Amazon S3. However, Snowflake edged out Redshift Spectrum for its ability to also load and transform ORC data files directly into Snowflake.

## Dremio

<https://www.dremio.com/>

<https://xcalar.com>

## ClickHouse

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

