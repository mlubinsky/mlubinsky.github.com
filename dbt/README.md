### Databriks

https://databricks.com/spark/jdbc-drivers-archive


### PySpark

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

https://datahubproject.io/

greatexpectations.io

 https://iceberg.apache.org/



### DBT

https://docs.getdbt.com/docs/introduction

https://www.youtube.com/watch?v=5rNquRnNb4E

https://www.youtube.com/watch?v=5rNquRnNb4E&list=PLy4OcwImJzBLJzLYxpxaPUmCWp8j1esvT

https://github.com/dbt-labs

### Amundsen

https://www.amundsen.io/

https://feng-tao.github.io/amundsen/databuilder/

https://github.com/amundsen-io/amundsendatabuilder

https://www.youtube.com/watch?v=GL4DxwCBn60

https://www.astronomer.io/events/recaps/data-lineage-with-openlineage-and-airflow/

https://blog.anant.us/data-engineers-lunch-36-amundsen-dse-with-airflow/