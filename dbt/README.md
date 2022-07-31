### Databriks

https://www.youtube.com/c/databricks

https://community.cloud.databricks.com/login.html. - playground

https://docs.databricks.com/data/databricks-datasets.html

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
