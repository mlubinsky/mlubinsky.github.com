### Data observbility
https://www.montecarlodata.com/blog-introducing-the-5-pillars-of-data-observability/
```
Is the data up-to-date?
Is the data complete?
Are fields within expected ranges?
Is the null rate higher or lower than it should be?
Has the schema changed?
```
## Databricks

#### Export CSV file locally
```
f="dbfs:/FileStore/uploads/mlubinsky/23_apps_review_count.csv"
_sqldf.write.option("header",True).csv(f)
```
Issue with code above :  it will create folder, ponentially with > 1 file

Solution - convert to pandas:
```
output_fname = "/dbfs/FileStore/uploads/mlubinsky/23_apps_review_count.csv"
pd = df_23.toPandas()
pd.to_csv(output_fname) # this will create index
pd.to_csv('your.csv', index=False) # no index

%sh
ls /dbfs/FileStore/uploads/mlubinsky/23_apps_review_count.csv


df_23 = spark.read.option("header", "true").format("csv").load(f)
display(df_23)


https://app-annie-p-mkt-derivatives.cloud.databricks.com/files/uploads/anna/paid_search.csv?o=651224624067749
just change the part after o=
```

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
