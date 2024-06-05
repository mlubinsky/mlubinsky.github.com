### Data observbility
https://www.montecarlodata.com/blog-introducing-the-5-pillars-of-data-observability/
```
Is the data up-to-date?
Is the data complete?
Are fields within expected ranges?
Is the null rate higher or lower than it should be?
Has the schema changed?
```

### Slowly changing dimensions

1. “SCD Type 1” — the “Old Record” is “Overwritten” with the “New Record” (MERGE/UPSERT)
2. “SCD Type 2” — a “New Record” is “Introduced” for “Each Change” of the “Attribute”.
3. “SCD Type 3” — a “New Column” is “Introduced” for “Each Change” of the “Attribute”.
```
MERGE INTO training.person TARGET
USING vw_person SOURCE
ON TARGET.PersonId = SOURCE.PersonId
WHEN MATCHED THEN
  UPDATE SET
    TARGET.FirstName = SOURCE.FirstName,
    TARGET.LastName = SOURCE.LastName,
    TARGET.Country = SOURCE.Country
WHEN NOT MATCHED THEN
  INSERT
  (
    PersonId,
    FirstName,
    LastName,
    Country
  )
  VALUES
  (
    SOURCE.PersonId,
    SOURCE.FirstName,
    SOURCE.LastName,
    SOURCE.Country
  )
```  
## Databricks
https://www.youtube.com/@Databricks

https://habr.com/ru/companies/slurm/articles/754464/ Apache Spark 3.4 для Databricks Runtime 13.0

https://habr.com/ru/companies/otus/articles/592605/

https://habr.com/ru/companies/slurm/articles/754464/

https://www.youtube.com/watch?v=BmhlAf3pk84 Databricks Certified Data Engineer Associate Exam Preparation - 45 Practice Questions & Answers
 
https://www.youtube.com/watch?v=Kn_Gu_3DCeE    REST API in Databricks 

```
The Databricks lakehouse architecture combines data stored with the Delta Lake protocol in cloud object storage with metadata registered to a metastore.
There are five primary objects in the Databricks lakehouse:

Catalog: a grouping of databases.
Database or schema: a grouping of objects in a catalog. Databases contain tables, views, and functions.
Table: a collection of rows and columns stored as data files in object storage.
View: a saved query typically against one or more tables or data sources.
Function: saved logic that returns a scalar value or set of rows.
```

#### Metastore
```
The metastore contains all of the metadata that defines data objects in the lakehouse. Azure Databricks provides the following metastore options:

Unity Catalog metastore: Unity Catalog provides centralized access control, auditing, lineage, and data discovery capabilitie
Built-in Hive metastore (legacy): Each Azure Databricks workspace includes a built-in Hive metastore as a managed service.
External Hive metastore (legacy): 
```
#### Tables
```
There are two kinds of tables in Databricks, managed and unmanaged (or external) tables.

__Managed__ tables: Databricks manages both the metadata and the data for a managed table; when you drop a table, you also delete the underlying data. Data analysts and other users that mostly work in SQL may prefer this behavior. Managed tables are the default when creating a table.

it is possible to create tables on Databricks that are not Delta tables. These tables are not backed by Delta Lake, and will not provide the ACID transactions and optimized performance of Delta tables.
Tables falling into this category include tables registered against data in external systems
and tables registered against other file formats in the data lake. 

Note

The Delta Live Tables distinction between live tables and streaming live tables is not enforced from the table perspective.


__Unmanaged__ tables will always specify a LOCATION during table creation;
 you can either register an existing directory of data files as a table or
 provide a path when a table is first defined.
Because data and metadata are managed independently, you can rename a table
or register it to a new database without needing to move any data.
Data engineers often prefer unmanaged tables and the flexibility they provide for production data.

```
#### Delta Live Tables
```
Delta Live Tables is a declarative framework for building reliable, maintainable, and testable data processing pipelines.
You define the transformations to perform on your data and
 Delta Live Tables manages task orchestration, cluster management, monitoring, data quality, and error handling.
```
https://www.youtube.com/watch?v=5E65mE_IiNQ Overview on Databricks Delta Live Tables with Multi-Hop Architecture


#### Liquid clustering
https://docs.databricks.com/en/delta/clustering.html
```
Delta Lake liquid clustering replaces table partitioning and ZORDER to simplify data layout decisions and optimize query performance.
Databricks recommends using Databricks Runtime 15.2 and above for all tables with liquid clustering enabled.
Clustering is not compatible with partitioning or ZORDER, and requires that you use Databricks to manage all layout and optimization operations for data in your table. After liquid clustering is enabled, run OPTIMIZE jobs as usual to incrementally cluster data.

CREATE TABLE table1(col0 int, col1 string) USING DELTA CLUSTER BY (col0);

ALTER TABLE <table_name> CLUSTER BY (<clustering_columns>)
```

#### Performance improvement wit OPTIMIZE and Z-ordering

https://docs.databricks.com/en/optimizations/predictive-optimization.html

OPTIMIZE table_name [WHERE predicate]
  [ZORDER BY (col_name1 [, ...] ) ]
```
One way to improve this speed is to coalesce small files into larger ones.
In Databricks Runtime 13.3 and above, Databricks recommends using clustering for Delta table layout.
 See Use liquid clustering for Delta tables.
Databricks recommends using predictive optimization to automatically run OPTIMIZE for Delta tables
```

#### Partitioning vs Z-ordering

https://medium.com/@tomhcorbin/data-storage-decisions-partitioning-vs-z-ordering-e39d5cddb178
```
Only partition tables larger than a terabyte in size.
Partitioning tables smaller than this tend not to be worth the overhead.
Try to keep your partition size around 1GB each or larger.
This helps keep the number of partitions lower.
If you regularly query a table based on a certain column,
this table might be a good candidate for partitioning.

When to Z-Order

If you expect a column to be commonly used in query predicates and if that column has high cardinality
(that is, a large number of distinct values) which might make it ineffective for PARTITIONing the table by,
then use ZORDER BY instead 

If your table is less than a terabyte in size, Z-order it instead of partitioning it.
Use Z-ordering when your queries span multiple dimensions.
But don’t don’t Z-order on too many columns.
If you regularly query based on high cardinality columns, use Z-ordering.
 

ZORDER BY Collocatse column information in the same set of files. Co-locality is used by Delta Lake data-skipping algorithms to dramatically reduce the amount of data that needs to be read. You can specify multiple columns for ZORDER BY as a comma-separated list. However, the effectiveness of the locality decreases with each additional column.

You cannot use this clause on tables that use liquid clustering.

 
SQL
   OPTIMIZE events;

  OPTIMIZE events WHERE date >= '2017-01-01';

  OPTIMIZE events
    WHERE date >= current_timestamp() - INTERVAL 1 day
    ZORDER BY (eventType);
```

https://www.youtube.com/watch?v=A1aR1A8OwOU Z-Order

### Datalake

https://docs.databricks.com/en/delta/table-properties.html Delta table properties

https://docs.databricks.com/en/delta/data-skipping.html
```
In Databricks Runtime 13.3 and above,
Databricks recommends using clustering for Delta table layout. Clustering is not compatible with Z-ordering.
See Use liquid clustering for Delta tables.
```
https://www.youtube.com/watch?v=dJvdzJQHpaQ

https://www.youtube.com/watch?v=u95h8bBWpjI


Apache Spark 3.4   вошел в релиз Databricks Runtime 13.0.

В Apache Spark 3.4 пользователи теперь могут читать и делать записи в формате Protobuf с помощью встроенных функций from_protobuf() и to_protobuf().

```
 До версии 3.4 в Dataset API Apache Spark был доступен метод PIVOT, но не его обратная операция MELT.
Теперь она включена, что дает возможность разворачивать DataFrame из широкого формата,
сгенерированного PIVOT, в исходный длинный формат, по желанию оставляя столбцы-идентификаторы.
Эта операция является обратной по отношению к groupBy(...).pivot(...).agg(...), за исключением агрегации, которая не может быть отменена.
Эта операция полезна для приведения DataFrame к формату,
в котором некоторые столбцы являются столбцами-идентификаторами, а все остальные столбцы ("значения") "разворачиваются" в строки,
оставляя только два неидентификаторных столбца, названных так, как указано.
```
#### Export CSV file locally
```
f="dbfs:/FileStore/uploads/mlubinsky/23_apps_review_count.csv"
_sqldf.write.option("header",True).csv(f)
```
Issue with code above :  it will create folder, ponentially with > 1 file

Solution - convert to pandas:
```
fname="FileStore/uploads/mlubinsky/icon_mapping_march_29.csv"
output_fname = "/dbfs/"+fname
pd = mapping_all.toPandas()
#pd.to_csv(output_fname) # this will create index
pd.to_csv(output_fname, index=False) # no index

print("mapping_all.count()=", mapping_all.count())

read_fname="dbfs:/"+fname
df_read = spark.read.option("header", "true").format("csv").load(read_fname)
print("df_read.count()=", df_read.count())
df_read.display()

Yet another way to read csv file from DBFS
def load_icon_mapping_from_dbfs(spark, params):
        path = "/FileStore/tables/IAP/Icon_mappings/IAP_Icon_map_v10.csv"
        df_csv = spark.read.option("header", "true").format("csv").load(path)
        print(icon_mapping.count())
        return df_csv

```
Check result:
```
%sh
ls /dbfs/FileStore/uploads/mlubinsky/icon_mapping_march_29.csv

```
#### How to download file from DBFS to local machine

https://app-annie-p-dom-aio.cloud.databricks.com/files/uploads/mlubinsky/icon_mapping_march_29.csv?o=3836794479208844

https://app-annie-p-mkt-derivatives.cloud.databricks.com/files/uploads/anna/paid_search.csv?o=651224624067749

https://app-annie-p-dom-aio.cloud.databricks.com/files/tables/IAP/Icon_mappings/IAP_Icon_map_v10.csv?o=3836794479208844

 


just change the part after o=


### Generate sequence
```
SELECT explode( sequence(DATE'2018-02-01', DATE'2018-02-09', INTERVAL 1 DAY) ) as generated_date
```

###  consider PIVOT, UNPIVOT

```
WITH G as
(  
SELECT explode( sequence(DATE'2022-08-01', DATE'2022-11-30', INTERVAL 1 DAY) ) as generated_date
)
,
daily_reviews as ( 
SELECT
  app_id, process_date, count(*) as daily_reviews_cnt
from parquet.`s3://b2c-prod-advanced-review/fact/REVIEW_UNIFORM/version=1.0.5/`
where process_date > '2022-08-01' and process_date <=  '2022-11-30'
-- and ( app_id = 20600000009072 or   app_id =  20600000000465 )
group by app_id, process_date
),

popular_apps as
(
 select app_id, 
 max(daily_reviews_cnt) as max_daily_reviews_cnt,
 sum(daily_reviews_cnt) as sum_daily_reviews_cnt
 from daily_reviews
 group by app_id
 having max(daily_reviews_cnt) > 100
)
,
g_cross_app as
(
SELECT G.generated_date, popular_apps.app_id, 
popular_apps.max_daily_reviews_cnt,
popular_apps.sum_daily_reviews_cnt
FROM G 
CROSS join popular_apps
)
,
gaps as (
SELECT 
G.generated_date,  
G.app_id, 
G.max_daily_reviews_cnt,
G.sum_daily_reviews_cnt,
r.process_date,
r.daily_reviews_cnt
FROM  g_cross_app as G LEFT JOIN 
daily_reviews as r ON G.generated_date = r.process_date AND G.app_id = r.app_id
where  r.process_date IS NULL
order by G.generated_date
),
result as
( 
SELECT 
M.app_id, 
M.app_name,
gaps.sum_daily_reviews_cnt,
array_join(sort_array(collect_list(generated_date)), ', ') as dates_without_reviews

FROM gaps
JOIN  APP_NAMES_view AS M ON   gaps.app_id = M.app_id
group by M.app_id, M.app_name,
gaps.sum_daily_reviews_cnt
 
)
SELECT * FROM result
order by sum_daily_reviews_cnt DESC
```

### Delta format

https://mungingdata.com/delta-lake/updating-partitions-with-replacewhere/

```
from bdp.common.spark.spark_utils import load_as_spark_df
import pyspark.sql.functions as F

path= "s3://b2c-prod-dca-model-evaluate/oss/MPS_APPIQ_TAXONOMY_WEIGHTS_DS/version=0.3/"
aio_weights = spark.read.parquet(path)
aio_weights = aio_weights.withColumn("version",F.lit("1.1.0"))

params={"version": "1.0.0"}
df_WEIGHTS_100 = load_as_spark_df(spark, "MPS_APPIQ_TAXONOMY_WEIGHTS_O", params)

new_path = "s3://aardvark-prod-dca-data/oss/tmp_MPS_APPIQ_TAXONOMY_WEIGHTS"

#### replaceWhere https://mungingdata.com/delta-lake/updating-partitions-with-replacewhere/
aio_weights.write.partitionBy("version").format("delta").save(new_path)
df_WEIGHTS_100.write.format("delta").option("replaceWhere", "version" == "1.0.0").mode("overwrite").save(new_path)
```

### Message:
Determining location of DBIO file fragments. This operation can take some time.

https://docs.databricks.com/optimizations/disk-cache.html

c5d, r5d, and z1d series workers are configured for disk caching, but not enabled by default. To enable for caching, see Enable or disable the disk cache.

spark.databricks.io.cache.enabled true
spark.databricks.io.cache.maxDiskUsage "{DISK SPACE PER NODE RESERVED FOR CACHED DATA}"
spark.databricks.io.cache.maxMetaDataCache "{DISK SPACE PER NODE RESERVED FOR CACHED METADATA}"

https://www.databricks.com/blog/2018/07/31/processing-petabytes-of-data-in-seconds-with-databricks-delta.html

Solution:
%sql Optimize [table name]


How to interact with files on Databricks

https://docs.databricks.com/files/index.html 

%sh <command> /dbfs/<path>/

```
%sh: Allows you to run shell code in your notebook. To fail the cell if the shell command has a non-zero exit status, add the -e option. This command runs only on the Apache Spark driver, and not the workers. 
To run a shell command on all nodes, use an init script.

%fs: Allows you to use dbutils filesystem commands.
For example, to run the dbutils.fs.ls command to list files, 
you can specify %fs ls instead. For more information, see How to interact with files on Databricks.

%md: Allows you to include various types of documentation, including text, images, and mathematical formulas and equations. See the next section.

```

https://www.youtube.com/c/databricks

https://community.cloud.databricks.com/login.html. - playground

https://docs.databricks.com/data/databricks-datasets.html

https://databricks.com/session_na20/patterns-and-operational-insights-from-the-first-users-of-delta-lake

### DB workflow

Workflows > click Create

#### jobs
https://docs.databricks.com/data-engineering/jobs/jobs.html
A job is a way to run non-interactive code in a Databricks cluster. 
For example, you can run an extract, transform, and load (ETL) 

https://docs.databricks.com/data-engineering/jobs/index.html

You create jobs through the Jobs UI, the Jobs API, or the Databricks CLI. 
The Jobs UI allows you to monitor, test, and troubleshoot your running and completed jobs.

https://databricks.com/blog/2022/05/10/introducing-databricks-workflows.html

https://docs.databricks.com/data-engineering/jobs/jobs-quickstart.html


https://www.youtube.com/watch?v=H2FS4ijpFZA


### JDBC

https://databricks.com/spark/jdbc-drivers-archive

### PySpark

https://runawayhorse001.github.io/LearningApacheSpark/pyspark.pdf

What is the difference:
#### createOrReplaceTempView
https://spark.apache.org/docs/3.1.3/api/python/reference/api/pyspark.sql.DataFrame.createOrReplaceTempView.html
```
df=spark.read.format("delta").load("s3://aardvark-prod-dca-data/fact/APP_TOTAL_REVENUE/range_type=WEEK/")
df.createOrReplaceTempView("weekly_table")
spark.sql(SQL).show(55)
```
#### registerTempTable (deprecated)

https://spark.apache.org/docs/3.1.3/api/python/reference/api/pyspark.sql.DataFrame.registerTempTable.html?highlight=registertemptable
```
path="s3://aardvark-prod-dca-data/fact/APP_TOTAL_REVENUE/range_type=WEEK/date=2012-01-14/"
df=spark.read.format("delta").load(path)
df.show(3)

df.registerTempTable("like_table_name")
df_result = spark.sql("select * from like_table_name ")
df_result.show(3)
```



https://dbmstutorials.com/pyspark/spark-overview-and-setup.html

https://sparkbyexamples.com/pyspark-tutorial/

https://sqlandhadoop.com/pyspark-tutorial-distinct-filter-sort-on-dataframe/

https://sqlandhadoop.com/pyspark-filter-25-examples-to-teach-you-everything/

https://www.youtube.com/watch?v=SBTvJU2vEoc&list=PL7_h0bRfL52qWoCcS18nXcT1s-5rSa1yp


```
from pyspark.sql.types import StructType, StructField, IntegerType

schema = StructType([
    StructField("member_srl", IntegerType(), True),
    StructField("click_day", IntegerType(), True),
    StructField("productid", IntegerType(), True)])

df = spark.read.csv("user_click_seq.csv",header=False,schema=schema)
```


Rename columns:
```
column_list=['catid','catgroup','catname','catdesc']
df_category=df_category.toDF(*column_list)
df_category.show(truncate=False)

df_category.columns 
df_category.dtypes  # column names and types
df_category.printSchema()
```

### New staff

https://databricks.com/product/photon

https://datahubproject.io/ - instead Amundsen

greatexpectations.io

 https://iceberg.apache.org/



### DBT
  
  https://www.adventofdata.com/modern-data-modeling-start-with-the-end/

  https://medium.com/datamindedbe/use-dbt-and-duckdb-instead-of-spark-in-data-pipelines-9063a31ea2b5

https://docs.getdbt.com/docs/introduction

https://www.youtube.com/watch?v=5rNquRnNb4E

https://www.youtube.com/watch?v=5rNquRnNb4E&list=PLy4OcwImJzBLJzLYxpxaPUmCWp8j1esvT

https://github.com/dbt-labs

### Amundsen or (https://datahubproject.io/ - instead Amundsen)

https://www.amundsen.io/

https://feng-tao.github.io/amundsen/databuilder/

https://github.com/amundsen-io/amundsendatabuilder

https://www.youtube.com/watch?v=GL4DxwCBn60

https://www.astronomer.io/events/recaps/data-lineage-with-openlineage-and-airflow/

https://blog.anant.us/data-engineers-lunch-36-amundsen-dse-with-airflow/
