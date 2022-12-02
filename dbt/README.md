## Databricks

#### Export CSV file locally
```
f="dbfs:/FileStore/uploads/mlubinsky/23_apps_review_count.csv"
_sqldf.write.option("header",True).csv(f)
-- issue :  command above will create folder, ponettiall > 1 file

-- solution - convert to pandas
output_fname = "/dbfs/FileStore/uploads/mlubinsky/23_apps_review_count.csv"
pd = df_23.toPandas()
pd.to_csv(output_fname)

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
