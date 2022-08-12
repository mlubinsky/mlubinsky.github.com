### Book

https://runawayhorse001.github.io/LearningApacheSpark/pyspark.pdf


### Skew joins
https://habr.com/ru/company/first/blog/678826/


/opt/homebrew/bin/pyspark

### Dataframe
https://spark.apache.org/docs/3.1.1/api/python/reference/api/pyspark.sql.DataFrame.html

pdf = df.toPandas()

### Pandas Dataframe to string
https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_string.html

panda_df.to_string()  -- accepts arg to print index:

print(df.select(F.count(F.when(F.isnan(c) | F.col(c).isNull(),c)).alias(c)).toPandas().to_string(index=False))  

Use limit:
df.limit(3).toPandas().to_string(index=False)


### print schema without show()
```
schema = df._jdf.schema().treeString()
print(schema)
```

### Get value from the df with single row and col:
```
df = spark.sql('select count(1) as count_check from schema.table')
value = df.collect()[0][0]
```
### head() vs first()
DataFrame.head(n=None)   (default - return 1 row)
https://spark.apache.org/docs/3.1.1/api/python/reference/api/pyspark.sql.DataFrame.head.html
```
df.head()
Row(age=2, name='Alice')
df.head(1)
[Row(age=2, name='Alice')]
```

```
df.first()
Row(age=2, name='Alice')
```
https://spark.apache.org/docs/3.1.1/api/python/reference/api/pyspark.sql.DataFrame.first.html

### JOIN

https://dzone.com/articles/pyspark-join-explained-with-examples

https://insaid.medium.com/eda-with-pyspark-1f29b7d1618

https://stackoverflow.com/questions/39067505/pyspark-display-a-spark-data-frame-in-a-table-format


### Example: F.expr, any(), head(), lit(), cast(), check for nulls

```
        for col in df.columns:
            has_nulls = f"any({col} is null)"
            if df.select(F.expr(has_nulls)).head()[0]:
                df = df.withColumn(f"{col}_uniform_scaled", F.lit(None).cast("double"))
            else:
                ...
```


### Columns with nulls

https://stackoverflow.com/questions/37262762/filter-pyspark-dataframe-column-with-none-value

https://sparkbyexamples.com/pyspark/pyspark-find-count-of-null-none-nan-values/

```
import numpy as np
from pyspark.sql import SparkSession
spark = SparkSession.builder.appName('SparkByExamples.com').getOrCreate()
data = [
    ("James","CA",np.NaN), ("Julia","",None),
    ("Ram",None,200.0), ("Ramya","NULL",np.NAN)
]
df =spark.createDataFrame(data,["name","state","number"])
df.show()


from pyspark.sql.functions import col,isnan, when, count
df.select(
         [
            count(when(isnan(c) | col(c).isNull(), c)).alias(c) for c in df.columns
         ]
   ).show()
   
   
 ### printing via toPandas()  
 print(df.select(F.count(F.when(F.isnan(c) | F.col(c).isNull(),c)).alias(c)).toPandas().to_string(index=False))  
   
```

### groupBy, sum, agg
```
df.groupBy('genre_id').agg(
 F.sum( (F.col('monetization_score').isNull()).cast('int') ).alias('monetization_null_count'),
 F.sum( (F.col('monetization_score').isNotNull()).cast('int') ).alias('monetization_NOT_null_count'),   
).orderBy('genre_id').show(40)
```

### ANY
Pandas has ANY :
https://sparkbyexamples.com/pandas/pandas-check-if-any-value-is-nan-in-a-dataframe/

 PySpark has ANY - it  can check if any value of a column meets a condition.
 
```
from pyspark.sql import functions as F

data = [[1,2,3],[None, 5, 6], [7, None, 9]]
df = spark.createDataFrame(data, schema=["col1", "col2", "col3"])

cols = [f"any({col} is null) as {col}_contains_null" for col in df.columns]

df.selectExpr(cols).show()
```

### CSV

```
from pyspark.sql.types import *

csv_schema = StructType(
   [   
       StructField('id', IntegerType(), True),
       StructField('genre_id', LongType(), True),
       StructField('downloads_weight', DoubleType(), True),
       StructField('mps_total_downloads_weight', DoubleType(), True),
       StructField('revenue_weight', DoubleType(), True),
       StructField('mps_total_revenue_weight', DoubleType(), True),
       StructField('mps_monetization_sov_weight', DoubleType(), True),
       StructField('rau_weight', DoubleType(), True),
       StructField('afu_weight', DoubleType(), True),
       StructField('adu_weight', DoubleType(), True),
       StructField('atu_weight', DoubleType(), True),
       StructField('ris_weight', DoubleType(), True),
       StructField('incremental_ratings_average_weight', DoubleType(), True),
       StructField('cumulative_ratings_average_weight', DoubleType(), True),
       StructField('cumulative_rating_count_weight', DoubleType(), True),
       StructField('incremental_rating_count_weight', DoubleType(), True)
   ]
)      
fname="file:/dbfs/FileStore/uploads/mlubinsky/20220728_mps_weights.csv"

df_csv = spark.read.option("header",True).option("delimiter",",").schema(csv_schema).csv(fname)

df_ordered=df_csv.select("genre_id","downloads_weight","mps_total_downloads_weight","revenue_weight","mps_total_revenue_weight","mps_monetization_sov_weight","rau_weight","afu_weight","adu_weight","atu_weight","ris_weight","cumulative_rating_count_weight","incremental_rating_count_weight","cumulative_ratings_average_weight","incremental_ratings_average_weight")
```

### CLEAR

aws s3 rm --recursive s3://aardvark-prod-dca-data/oss/MPS_APPIQ_TAXONOMY_WEIGHTS

### DELTA
```
### WRITE
import pyspark.sql.functions as F
path = "s3://aardvark-prod-dca-data/oss/MPS_APPIQ_TAXONOMY_WEIGHTS/"
df_ordered.withColumn("version", F.lit("1.0.0")).write.partitionBy("version").format("delta").save(path)

###   READ
from bdp.common.spark.spark_utils import load_as_spark_df
genre_params={"version":"1.0.0"}
df_genre_weights = load_as_spark_df(spark, "MPS_APPIQ_TAXONOMY_WEIGHTS_O", genre_params)


```

Problem with duplicated columns:
```
df = spark.createDataFrame(
    [
        (1, 2, 3, 4, 5 ,6 , 7 ,8 , 9),   
    ],
    ["universal_app_id", "country_code", "product_id", "platform", "device_type", "range_type", "date", "app_name", "total_downloads"]
)

df_unified_totals = spark.createDataFrame(
    [ 
        (1, 2),   
    ],
    ["universal_app_id", "country_code"]
)

dim_cats = spark.createDataFrame(
        [
        (1, 2, 3, 4, 5),  
        (10, 20, 30, 40, 50),
    ],
    ["dim_legacy_category_id", "dim_id", "dim_platform", "dim_category_id", "dim_unified_category_id"]
)  

import pyspark.sql.functions as F   
df = df.join(
            df_unified_totals, on=["universal_app_id", "country_code"]
)

df = (
            df.alias("a")
            .join(
                dim_cats.alias("b"),
                [(F.col("a.product_id") == F.col("b.dim_id"))],
                "left",
            )
            .select("a.*", "b.dim_unified_category_id")
)
print("Step 3")
for c in df.columns:
    print(c)
```
Result:
```
universal_app_id
country_code
universal_app_id
country_code
product_id
platform
device_type
range_type
date
app_name
total_downloads
dim_unified_category_id
```
