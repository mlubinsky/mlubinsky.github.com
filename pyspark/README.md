### Book

https://runawayhorse001.github.io/LearningApacheSpark/pyspark.pdf


### StructType 
 
StructType() constructor takes list of StructField, 
StructField takes a fieldname and type of the value.

### MapType
https://sparkbyexamples.com/pyspark/pyspark-maptype-dict-examples/


```
from pyspark.sql.types import StructField, StructType, StringType, MapType
schema = StructType([
    StructField('name', StringType(), True),
    StructField('properties', MapType(StringType(),StringType()),True)
])


from pyspark.sql import SparkSession
spark = SparkSession.builder.appName('SparkByExamples.com').getOrCreate()
dataDictionary = [
        ('James',{'hair':'black','eye':'brown'}),
        ('Michael',{'hair':'brown','eye':None}),
        ('Robert',{'hair':'red','eye':'black'}),
        ('Washington',{'hair':'grey','eye':'grey'}),
        ('Jefferson',{'hair':'brown','eye':''})
        ]
df = spark.createDataFrame(data=dataDictionary, schema = schema)
print(df.schema)
df.printSchema()
 |-- name: string (nullable = true)
 |-- properties: map (nullable = true)
 |    |-- key: string
 |    |-- value: string (valueContainsNull = true)

df.show(truncate=False)

## let read the same data without specifying schema:
df2 = spark.createDataFrame(data=dataDictionary)
print(df2.schema)
StructType([StructField('_1', StringType(), True), StructField('_2', MapType(StringType(), StringType(), True), True)])

df2.printSchema()
 |-- _1: string (nullable = true)
 |-- _2: map (nullable = true)
 |    |-- key: string
 |    |-- value: string (valueContainsNull = true)
 

```
Explode properties column: will generate 2 columns: key and value
```
from pyspark.sql.functions import explode
df.select(df.name,explode(df.properties)).show()

#  Get only keys:
from pyspark.sql.functions import map_keys
df.select(df.name,map_keys(df.properties)).show()

# Get only values:
from pyspark.sql.functions import map_values
df.select(df.name,map_values(df.properties)).show()
```

### JSON schema

```
new_json="""{
 "contentID": { "S": "s-para"}
 }
"""
print(new_json)

# Read without schema:
df = spark.read.json(sc.parallelize([new_json]))
df.show()
df.printSchema()

print(df.schema)
The printed schema can be used "as is" to define the schema:

# Read with schema:
contentID_schema=StructType([
        StructField("S", StringType(), True)
])

beehive_schema = StructType([
   StructField("contentID", contentID_schema ,True)
])

df2 = spark.read.schema(beehive_schema).json(sc.parallelize([new_json]))
df2.printSchema()
root
 |-- contentID: struct (nullable = true)
 |    |-- S: string (nullable = true)

df2.show(truncate=False)

```

#### check_uniq in dataframe

```
+    def _check_uniq(df, msg):
+        cols = [ 'date', 'product_id', 'unified_product_id', 'country_code', 'device_code',
+                'market_code', 'genre_id']
+        logger.info(msg + " check_uniq total records=" + str(df.count()))
+        for c in cols:
+            if c not in df.columns:
+                logger.info("ERROR " + c + " not in " + str(df.columns))
+
+        df_gr = df.groupBy(*cols).count().filter(F.col('count') > 1)
+        cnt = df_gr.count()
+        if cnt > 0:
+            logger.info(msg + " check_uniq failed number of non-uniq keys= " + str(cnt))
+            logger.info(df_gr.limit(10).toPandas().to_string(index=False))
+        else:
+            logger.info(msg + " check_uniq OK")
+
```


### Partitions

https://habr.com/ru/company/otus/blog/686142/

### Skew joins
https://habr.com/ru/company/first/blog/678826/


/opt/homebrew/bin/pyspark


### Show verically (useful for wide table)
```
fname="/FileStore/uploads/reviews_20220822_hour_23/20600000009072.gz"
df = spark.read.options(header='False', inferSchema='True', delimiter='\t').schema(schema).csv(fname) 
df.show(n=3, truncate=250, vertical=True)
```

### For left join  find which join column doesn not have match
```
    df = df.join(df_genre_weights, on=["genre_id"], how="left")
    df_missing_genres = df.select('genre_id').filter(F.col("downloads_weight").isNull()).distinct().collect()
    missing_genres = [v['genre_id'] for v in df_missing_genres]

    print("missing genres =" + str(missing_genres))
```    
    
### Dataframe
https://spark.apache.org/docs/3.1.1/api/python/reference/api/pyspark.sql.DataFrame.html

pdf = df.toPandas()

### Pandas Dataframe to string
https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_string.html

panda_df.to_string()  -- accepts arg to print index:

print(df.select(F.count(F.when(F.isnan(c) | F.col(c).isNull(),c)).alias(c)).toPandas().to_string(index=False))  

Use limit:
df.limit(3).toPandas().to_string(index=False)


### Reading parquet and delta files
```
path="s3://aardvark-prod-dca-data/fact/APP_TOTAL_REVENUE/range_type=WEEK/date=2012-01-14/" 
df=spark.read.parquet(path)

df = spark.read.format(“delta”).load(path)

df.display()
```

### createOrReplaceTempView
https://spark.apache.org/docs/3.1.3/api/python/reference/api/pyspark.sql.DataFrame.createOrReplaceTempView.html
```
df=spark.read.format("delta").load("s3://aardvark-prod-dca-data/fact/APP_TOTAL_REVENUE/range_type=WEEK/")
df.createOrReplaceTempView("weekly_table")
spark.sql(SQL).show(55)
```
### print schema without show()
```
schema = df._jdf.schema().treeString()
print(schema)
```

### GROUP BY HAVING COUNT() > 1

```
df.groupBy(*cols).count().show()

df.groupBy(*cols).count().filter(F.col('count')>1).show()
```

How to convert this to PySpark:

```
sqlContext.sql("select Category,count(*) as 
count from hadoopexam where HadoopExamFee<3200  
group by Category having count>10")
```
Answer:
```
from pyspark.sql.functions import *

df.filter(df.HadoopExamFee<3200)
  .groupBy('Category')
  .agg(count('Category').alias('count'))
  .filter(col('count')>10)
```

GEneric answer:
```
df.groupBy(someExpr).agg(somAgg).where(somePredicate) 
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


### Group by

df.filter(df.colname == 50.0).groupBy('another_colname').count().show()


### Infinity:
```
def _replace_infs(c, v):
        is_infinite = c.isin(
            [
                F.lit("+Infinity").cast("float")
                , F.lit("-Infinity").cast("float")
            ]
        )
return F.when(c.isNotNull() & is_infinite, v).otherwise(c)
        
        
df = df.withColumn(
                s, self._replace_infs(F.col(s), F.lit(None))
)         
```
### Expression
https://www.nbshare.io/notebook/374005461/Pyspark-Expr-Example/
```
from pyspark.sql.functions import (col, expr)
# here we update the column "Classify" using the CASE expression. 
# The conditions are based on the values in the Salary column
modified_df = df.withColumn("Classify", 
    expr("CASE WHEN Salary < 5000 THEN 1 "+
               "WHEN Salary < 10000 THEN 2 " +
                "ELSE 3 " + 
           END")
    )
    
modified_df = df.withColumn("New_Salary", expr("Salary + 500"))    

```

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
