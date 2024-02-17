Implementing Pyspark Real Time Application || End-to-End Project 

https://www.youtube.com/watch?v=wFOojyYvLRE

https://habr.com/ru/articles/765188/  Feature eng and cluster analysis 

https://towardsdatascience.com/did-you-know-this-in-spark-sql-a7398bfcc41e

### Books

https://www.amazon.com/Advanced-Analytics-PySpark-Patterns-Learning/dp/1098103653

https://www.amazon.com/Analysis-Python-PySpark-Jonathan-Rioux/dp/1617297208/

https://www.amazon.com/Data-Algorithms-Spark-Recipes-Patterns/dp/1492082384

https://runawayhorse001.github.io/LearningApacheSpark/pyspark.pdf


https://www.amazon.com/dp/1804612987 Causal Inference and Discovery in Python: Unlock the secrets of modern causal machine learning with DoWhy, EconML, PyTorch and more


https://www.youtube.com/watch?v=jWZ9K1agm5Y  PySpark Course: Big Data Handling with Python and Apache Spark



### Compute  total counts of each of  unique words on a spark: map() and flatMap()
```
sc.textFile(“hdfs://user/bigtextfile.txt”);
def toWords(line):
      return line.split()

words = lines.flatMap(toWords)     We are going to flatMap instead of the map because our function is returning multiple values.

def toTuple(word):
     return (word, 1)

wordsTuple = words.map(toTuple)

def sum(x, y):
   return x+y

counts = wordsTuple.reduceByKey(sum)
```

### Data Lake implementation

https://sparkbyexamples.com/pyspark/pyspark-join-explained-with-examples/

https://sparkbyexamples.com/pyspark/pyspark-join-multiple-columns/

```

yesterday_df = spark.createDataFrame([
 (1,"hulu","90046"),
 (2,"hulu+disney" ,"90026"),
 (3,"hulu+disney" ,"90026")],
 ["user_id", "product_name","zip_code"])

 today_df = spark.createDataFrame([
 (1,"hulu+disney","90046"),
 (2,"hulu+disney" ,"90036"),
 (4,"hulu+disney" ,"90026")],
 ["user_id", "product_name","zip_code"])

import pyspark.sql.functions as F

df_old = yesterday_df.withColumn('date',F.lit("10/26"))
df_new = today_df.withColumn('date',F.lit("10/27"))
df_new.show()
+-------+------------+--------+-----+
|user_id|product_name|zip_code| date|
+-------+------------+--------+-----+
|      1| hulu+disney|   90046|10/27|
|      2| hulu+disney|   90036|10/27|
|      4| hulu+disney|   90026|10/27|
+-------+------------+--------+-----+

df_new.union(df_old).show()
+-------+------------+--------+-----+
|user_id|product_name|zip_code| date|
+-------+------------+--------+-----+
|      1| hulu+disney|   90046|10/27|
|      2| hulu+disney|   90036|10/27|
|      4| hulu+disney|   90026|10/27|
|      1|        hulu|   90046|10/26|
|      2| hulu+disney|   90026|10/26|
|      3| hulu+disney|   90026|10/26|
+-------+------------+--------+-----+




# INNER JOIN with renaming columns to avoid column names duplications:

df_new.join(df_old, df_old.user_id == df_new.user_id, "inner").select(
 df_old.user_id,
 df_old.product_name.alias("old_product_name"),
 df_new.product_name.alias("new_product_name"),
 df_old.zip_code.alias("old_zip_code"),
 df_new.zip_code.alias("new_zip_code"),
 df_old.date.alias("start_date"),
 df_new.date.alias("end_date")
).show()

+-------+----------------+----------------+------------+------------+----------+--------+
|user_id|old_product_name|new_product_name|old_zip_code|new_zip_code|start_date|end_date|
+-------+----------------+----------------+------------+------------+----------+--------+
|      1|            hulu|     hulu+disney|       90046|       90046|     10/26|   10/27|
|      2|     hulu+disney|     hulu+disney|       90026|       90036|     10/26|   10/27|
+-------+----------------+----------------+------------+------------+----------+--------+

df_inner = df_new.join(df_old, df_old.user_id == df_new.user_id, "inner").select(
 df_old.user_id,
 df_old.product_name.alias("old_product_name"),
 df_new.product_name.alias("new_product_name"),
 df_old.zip_code.alias("old_zip_code"),
 df_new.zip_code.alias("new_zip_code"),
 df_old.date.alias("start_date"),
 df_new.date.alias("end_date")
)


df_new.join(df_old,
(df_old.user_id == df_new.user_id) , "inner").show()

### Find records with same id but different zip code or product_name:
df_new.join(df_old,
(df_old.user_id == df_new.user_id) &
((df_old.product_name != df_new.product_name)  | (df_old.zip_code != df_new.zip_code )) , "inner").show()

df_inner_2 = df_new.join(df_old,
(df_old.user_id == df_new.user_id) &
((df_old.product_name != df_new.product_name) | (df_old.zip_code != df_new.zip_code )), "inner").select(
 df_old.user_id,
 df_old.product_name.alias("old_product_name"),
 df_new.product_name.alias("new_product_name"),
 df_old.zip_code.alias("old_zip_code"),
 df_new.zip_code.alias("new_zip_code"),
 df_old.date.alias("start_date"),
 df_new.date.alias("end_date")
)

df_new.join(df_old, df_old.user_id == df_new.user_id , "inner").select(
df_old.user_id,
df_old.product_name,
df_old.zip_code,
df_old.date.alias("start_date"),
df_new.date.alias("end_date")
).show()


df_inner_2 = df_new.join(df_old,
(df_old.user_id == df_new.user_id) &
((df_old.product_name != df_new.product_name) | (df_old.zip_code != df_new.zip_code )), "inner").select(
 df_old.user_id,
 df_old.product_name.alias("old_product_name"),
 df_new.product_name.alias("new_product_name"),
 df_old.zip_code.alias("old_zip_code"),
 df_new.zip_code.alias("new_zip_code"),
 df_old.date.alias("start_date"),
 df_new.date.alias("end_date")
)


### Find records which exists in both  dfs and product_name and zip_code are the same:
 this syntax will eliminate duplicate column names

df_new.join(df_old,["user_id","product_name","zip_code"]).show()

df_exact_match = df_new.join(df_old,["user_id","product_name","zip_code"])

### Find records with same id but different zip code or product_name:
step 1:

df_common_user_id = df_new.join(df_old, df_old.user_id == df_new.user_id , "inner").show()

step 2: remove exact match:

df_dup = df_common_user_id.join(df_exact_match , df_common_user.user_id == df_exact_match.user_id, "leftanti")

df_dup = df_common_user_id.join(df_exact_match , ["user_id"], "leftanti")

### Leftanti returns records which exists in left only

df_old.join(df_new, df_old.user_id == df_new.user_id, "leftanti").show()
+-------+------------+--------+-----+
|user_id|product_name|zip_code| date|
+-------+------------+--------+-----+
|      3| hulu+disney|   90026|10/26|
+-------+------------+--------+-----+

df_new.join(df_old, df_old.user_id == df_new.user_id, "leftanti").show()
+-------+------------+--------+-----+
|user_id|product_name|zip_code| date|
+-------+------------+--------+-----+
|      4| hulu+disney|   90026|10/27|
+-------+------------+--------+-----+

df_new_anti = df_new.join(df_old, df_old.user_id == df_new.user_id, "leftanti")
df_old_anti = df_old.join(df_new, df_old.user_id == df_new.user_id, "leftanti")
df_new_anti.union(df_old_anti).show()
+-------+------------+--------+-----+
|user_id|product_name|zip_code| date|
+-------+------------+--------+-----+
|      4| hulu+disney|   90026|10/27|
|      3| hulu+disney|   90026|10/26|
+-------+------------+--------+-----+
```


### In a very huge text file  check if a particular keyword exists.
```
result = “Not Set”
lock = threading.Lock()
accum = sc.accumulator(0)

def map_func(line):
    #introduce delay to emulate the slowness
    sleep(1);
    if line.find(“Adventures”) > -1:
              accum.add(1);
             return 1;
    return 0;

def start_job():
    global result
    try:
        sc.setJobGroup(“job_to_cancel”, “some description”)

        lines = sc.textFile(“hdfs://hadoop1.knowbigdata.com/user/student/sgiri/wordcount/input/big.txt”);

         result = lines.map(map_func);
         result.take(1);
         except Exception as e:
                  result = “Cancelled”
lock.release()

def stop_job():
    while accum.value < 3 :
          sleep(1);
          sc.cancelJobGroup(“job_to_cancel”)
          supress = lock.acquire()
          supress = thread.start_new_thread(start_job, tuple())
          supress = thread.start_new_thread(stop_job, tuple())
          supress = lock.acquire()
```

### UDF pandas

https://towardsdatascience.com/pyspark-or-pandas-why-not-both-95523946ec7c

https://medium.com/@suffyan.asad1/an-introduction-to-pandas-udfs-in-pyspark-a0a512bd00e2


### Update Dataframe
```
import pyspark.sql.functions as F
from pyspark.sql.functions import col, when 
path= "s3://b2c-prod-dca-model-evaluate/oss/MPS_APPIQ_TAXONOMY_WEIGHTS_DS/version=0.3/"
aio_weights = spark.read.parquet(path)
updated_weights = aio_weights.withColumn("revenue_weight",
                 when(col("genre_id") == 2012, 0)
                .when(col("genre_id") == 2009004, 1)
                .otherwise(col("revenue_weight"))
              )  
aio_weights.printSchema()
updated_weights.printSchema()


version="1.1.0"
updated_weights = updated_weights.withColumn("version",F.lit(version))
new_path = "s3://aardvark-prod-dca-data/oss/MPS_APPIQ_TAXONOMY_WEIGHTS"

updated_weights.write.format("delta").partitionBy("version").save(new_path)
```

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

### Explode
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

### Window function to calculate sum and cumulative

```
from pyspark.sql import Window
from pyspark.sql.functions import sum
l = [
  (1, 10, '2020-11-01'), 
  (1, 30, '2020-11-02'), 
  (1, 50, '2020-11-03')
]
df = spark.createDataFrame(l,['user_id', 'price', 'purchase_date'])
w1 = Window().partitionBy('user_id')
w2 = Window().partitionBy('user_id').orderBy('purchase_date')
(
  df
  .withColumn('total_expenses', sum('price').over(w1))
  .withColumn('cumulative_expenses', sum('price').over(w2))
).show()
+-------+-----+-------------+--------------+-------------------+
|user_id|price|purchase_date|total_expenses|cumulative_expenses|
+-------+-----+-------------+--------------+-------------------+
|      1|   10|   2020-11-01|            90|                 10|
|      1|   30|   2020-11-02|            90|                 40|
|      1|   50|   2020-11-03|            90|                 90|
+-------+-----+-------------+--------------+-------------------+

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

### Group by
```
df.filter(df.colname == 50.0).groupBy('another_colname').count().show()
from pyspark.sql.functions import avg

df.groupBy("category").agg(avg("sales")).show()
```


#### groupBy, sum, agg
```
df.groupBy('genre_id').agg(
 F.sum( (F.col('monetization_score').isNull()).cast('int') ).alias('monetization_null_count'),
 F.sum( (F.col('monetization_score').isNotNull()).cast('int') ).alias('monetization_NOT_null_count'),   
).orderBy('genre_id').show(40)
```

#### GROUP BY HAVING COUNT() > 1


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

Generic answer:
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

### https://towardsdatascience.com/2-silent-pyspark-mistakes-you-should-be-aware-of-de52c3a188c4
```
Let’s say we have a dataset with millions of rows.
We make a mistake in calculating the sales quantities.
Then, we create aggregate features based on the sales quantities such as weekly total,
 the moving average of the last 14 days, and so on.
 These features are used in a machine learning model that predicts the demand in the next week.

We evaluate the predictions and find out the accuracy is not good enough.
Then, we spend lots of time trying different things to improve the accuracy such as feature engineering or hyperparameter tuning.
 These strategies don’t have a big impact on the accuracy because the problem is in the data.

This is a scenario that we may encounter when working with large datasets.
In this article, we’ll go over two specific PySpark mistakes that might cause unexpected results.
For those who haven’t used PySpark yet, it is the Python API for Spark,
which is an analytics engine used for large-scale data processing.

We’ll create a small dataset for a few rows and columns.
It’s enough to demonstrate and explain the two cases we’ll cover. Both are applicable to much larger datasets as well.

from pyspark.sql import SparkSession
from pyspark.sql import Window, functions as F

# initialize spark session
spark = SparkSession.builder.getOrCreate()

# create a spark dataframe using a list of dictionaries
data = [
    {"group_1": 'A', "group_2": 104, "id": 1211},
    {"group_1": 'B', "group_2": None, "id": 3001},
    {"group_1": 'B', "group_2": 105, "id": 1099},
    {"group_1": 'A', "group_2": 124, "id": 3380}
]

df = spark.createDataFrame(data)

# display the dataframe
df.show()

# output
+-------+-------+----+
|group_1|group_2|  id|
+-------+-------+----+
|      A|    104|1211|
|      B|   NULL|3001|
|      B|    105|1099|
|      A|    124|3380|
+-------+-------+----+
The DataFrame contains 4 rows and 3 columns and there is a missing value (i.e. NULL) in the second row of the second column.

1. concat and concat_ws
The concat and concat_ws functions are used for concatenating (i.e. combining) string columns. There is a small difference between them in the case of having Null values. We need to take it into consideration. Otherwise, the result of the concatenation operation might be misleading.

Let’s first use the concat function to combine the group_1 and group_2 columns to create a new column called group .

df = df.withColumn("group", F.concat("group_1", "group_2"))

df.show()

# output
+-------+-------+----+-----+
|group_1|group_2|  id|group|
+-------+-------+----+-----+
|      A|    104|1211| A104|
|      B|   NULL|3001| NULL|
|      B|    105|1099| B105|
|      A|    124|3380| A124|
+-------+-------+----+-----+
Everything seems ok except for the second row. The group_2 value is null, which causes the group value to be null as well.

The output of the concat function is null if any of the concatenated values is null.

This is not the ideal behavior. If we only have the first group info,
then we’d except the group value to be equal to that value (i.e. “B”).
Just because we don’t have the subgroup info, we don’t want to lose information about the first level grouping.

In such cases, it’s better to use the concat_ws function. Let’s try it.

df = df.withColumn("group", F.concat_ws("group_1", "group_2"))

df.show()

# output
+-------+-------+----+-----+
|group_1|group_2|  id|group|
+-------+-------+----+-----+
|      A|    104|1211|  104|
|      B|   NULL|3001|     |
|      B|    105|1099|  105|
|      A|    124|3380|  124|
+-------+-------+----+-----+
This is not the output we expect. The second row of the group column is empty,
which is not very different from having a null value. Also, the other group values are also wrong. This is worse than what the concat function did.

To solve this problem, we just need to specify a separator.
If we don’t need a character between groups, we can just provide an empty string as a separator.

df = df.withColumn("group", F.concat_ws("", "group_1", "group_2"))

df.show()

# output
+-------+-------+----+-----+
|group_1|group_2|  id|group|
+-------+-------+----+-----+
|      A|    104|1211| A104|
|      B|   NULL|3001|    B|
|      B|    105|1099| B105|
|      A|    124|3380| A124|
+-------+-------+----+-----+
Now, the output is just as we expect.

2. Conditional column creation
Consider we want to create a new column based on the values in other columns. In PySpark, we can use the when function for this task. In the case of multiple conditions, we can chain the when functions and conclude with the otherwise function.

The order of conditions matter in some cases. It’s best explained with an example so let’s get to it.

We have the following DataFrame:

+-------+-------+----+-----+
|group_1|group_2|  id|group|
+-------+-------+----+-----+
|      A|    104|1211| A104|
|      B|   NULL|3001|    B|
|      B|    105|1099| B105|
|      A|    124|3380| A124|
+-------+-------+----+-----+
We want to create a dummy column according to the following conditions:

If group 1 is A, it is 100
If group 1 is A and group 2 is 124, it is 200
Otherwise it is 300
Using the when and otherwise functions, we can create this dummy column as follows:

df = df.withColumn(
    "dummy",
    F.when(F.col("group_1")=="A", 100)\
    .when(((F.col("group_1")=="A") & (F.col("group_2")=="124")), 200)\
    .otherwise(300)
)

df.show()

# output
+-------+-------+----+-----+-----+
|group_1|group_2|  id|group|dummy|
+-------+-------+----+-----+-----+
|      A|    104|1211| A104|  100|
|      B|   NULL|3001|    B|  300|
|      B|    105|1099| B105|  300|
|      A|    124|3380| A124|  100|
+-------+-------+----+-----+-----+
The output is not exactly correct. The last row fits the second condition (group 1 is A and group 2 is 124) so the value in the dummy column should be 200.

The reason for this problem is the order of conditions. Since we write the condition group_1=="A" before a more specific (or sub) condition group_1=="A" & group_2=="124" , the latter is kind of ignored.

If we switch these two conditions, the output will actually be correct.

df = df.withColumn(
    "dummy",
    F.when(((F.col("group_1")=="A") & (F.col("group_2")=="124")), 200)\
    .when(F.col("group_1")=="A", 100)\
    .otherwise(300)
)

df.show()

# output
+-------+-------+----+-----+-----+
|group_1|group_2|  id|group|dummy|
+-------+-------+----+-----+-----+
|      A|    104|1211| A104|  100|
|      B|   NULL|3001|    B|  300|
|      B|    105|1099| B105|  300|
|      A|    124|3380| A124|  200|
+-------+-------+----+-----+-----+
Now the last value of the dummy column is 200, which is correct.

This is hard to notice when working with larger datasets. But, it might have a big impact on the downstream tasks. The output might be completely wrong. Thus, we should always pay attention to the order of conditions in such cases.

Final words
Data cleaning and processing are very important steps in a workflow as they affect downstream processes. A small mistake we make in these steps might lead to erroneous results.

Be aware of silent mistakes that do not raise an error but have the potential to fail your model or product.
```
