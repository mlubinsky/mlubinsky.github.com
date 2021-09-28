https://mungingdata.com/category/apache-spark/

https://www.slideshare.net/databricks/fine-tuning-and-enhancing-performance-of-apache-spark-jobs

https://www.youtube.com/channel/UCoVVyUViJ3mfaEKVjAJSnVA

https://habr.com/ru/company/X5Group/blog/579232/. PySpark

https://mungingdata.com/apache-spark/best-books/

https://www.kdnuggets.com/2021/09/data-analysis-scala.html

```
exploding array column:

val df = Seq((1, "A", Seq(1,2,3)), (2, "B", Seq(3,5))).toDF("col1", "col2", "col3")
df.show()
+----+----+---------+
|col1|col2|     col3|
+----+----+---------+
|   1|   A|[1, 2, 3]|
|   2|   B|   [3, 5]|
+----+----+---------+

val df2 = df.withColumn("col3", explode($"col3"))
df2.show()
+----+----+----+
|col1|col2|col3|
+----+----+----+
|   1|   A|   1|
|   1|   A|   2|
|   1|   A|   3|
|   2|   B|   3|
|   2|   B|   5|
+----+----+----+

val df3 = df.withColumn("new_col4", explode($"col3"))
df3.show()
+----+----+---------+--------+
|col1|col2|     col3|new_col4|
+----+----+---------+--------+
|   1|   A|[1, 2, 3]|       1|
|   1|   A|[1, 2, 3]|       2|
|   1|   A|[1, 2, 3]|       3|
|   2|   B|   [3, 5]|       3|
|   2|   B|   [3, 5]|       5|
+----+----+---------+--------+

val df5 = df.withColumn("new_col4", explode($"col3")).select("col1","col2", "new_col4")
df5.show()
+----+----+--------+
|col1|col2|new_col4|
+----+----+--------+
|   1|   A|       1|
|   1|   A|       2|
|   1|   A|       3|
|   2|   B|       3|
|   2|   B|       5|
+----+----+--------+


val df7=df.select(col("col1"),col("col2"), explode(col("col3")))
 
 df7.show()
+----+----+---+
|col1|col2|col|
+----+----+---+
|   1|   A|  1|
|   1|   A|  2|
|   1|   A|  3|
|   2|   B|  3|
|   2|   B|  5|
+----+----+---+


creating alias for exploded column:
-------------------------------------
val df8=df.select(col("col1"),col("col2"), explode(col("col3")).alias("my_alias"))
 

scala> df8.show()
+----+----+--------+
|col1|col2|my_alias|
+----+----+--------+
|   1|   A|       1|
|   1|   A|       2|
|   1|   A|       3|
|   2|   B|       3|
|   2|   B|       5|
+----+----+--------+



Filter  example
------------------
val df = Seq(
  ("thor", "new york"),
  ("aquaman", "atlantis"),
  ("wolverine", "new york")
).toDF("superhero", "city")


df.show()
+---------+--------+
|superhero|    city|
+---------+--------+
|     thor|new york|
|  aquaman|atlantis|
|wolverine|new york|
+---------+--------+

df.printSchema()

// creating new column:

df.withColumn("city_starts_with_new", $"city".startsWith("new")).show()
+---------+--------+--------------------+
|superhero|    city|city_starts_with_new|
+---------+--------+--------------------+
|     thor|new york|                true|
|  aquaman|atlantis|               false|
|wolverine|new york|                true|
+---------+--------+--------------------+


println(df.schema.fieldNames.contains("city"))
println(df.schema.contains(StructField("city",StringType,true)))


https://stackoverflow.com/questions/47657072/importing-schema-from-json-with-optional-value

:paste
// Entering paste mode (ctrl-D to finish) 

import org.apache.spark.sql.expressions.scalalang._
import org.apache.spark.sql.types._
import org.apache.spark.sql.{DataFrame, Dataset, SparkSession}    
val schema = StructType(Seq(
  StructField("k1", StringType, false),
  StructField("optK", StructType(Seq(StructField("nestedK", StringType, false))), false)
))    
val df = spark.read.option("allowUnquotedFieldNames",true).schema(schema).json("s3 location of data.json")       

df: org.apache.spark.sql.DataFrame = [k1: string, optK: struct<nestedK: string>]

scala> df.show
+--------------+------+
|            k1|  optK|
+--------------+------+
|     someValue|[optV]|
|someOtherValue|  null|
+--------------+------+

```

A Column object corresponding with the city column can be created using the following three syntaxes:
```
$"city"
df("city")
col("city") (must run import org.apache.spark.sql.functions.col first)


This is tha same:

val s1 = df.select("city")
val s2 = df.select($"city")

```



https://medium.com/analytics-vidhya/4-performance-improving-techniques-to-make-spark-joins-10x-faster-2ec8859138b4

https://medium.com/walmartglobaltech/decoding-memory-in-spark-parameters-that-are-often-confused-c11be7488a24

https://sivaprasad-mandapati.medium.com/

https://medium.com/swlh/building-partitions-for-processing-data-files-in-apache-spark-2ca40209c9b7

https://medium.com/@jhwang1992m/3-a-case-study-of-spark-performance-optimization-on-large-dataframes-8fa06fa6e0ff 

https://towardsdatascience.com/analytical-hashing-techniques-5a0393f3fc1c




https://levelup.gitconnected.com/4-advanced-apache-spark-tips-for-faster-performance-dd0a1cc829aa

data file compaction

https://medium.com/@himanigadve/dynamic-data-file-compaction-in-apache-spark-5d347cf3deb0


https://mungingdata.com/apache-spark/using-the-console/

https://mallikarjuna_g.gitbooks.io/spark/content/

Working with JSON

https://analyticshut.com/reading-json-data-in-spark/
https://stackoverflow.com/questions/34069282/how-to-query-json-data-column-using-spark-dataframes
https://sparkbyexamples.com/spark/spark-read-and-write-json-file/
https://medium.com/expedia-group-tech/working-with-json-in-apache-spark-1ecf553c2a8c
https://habr.com/ru/company/leroy_merlin/blog/563066/
http://javachain.com/how-to-process-json-data-using-apache-spark/
https://bigdataprogrammers.com/how-to-read-json-file-in-spark/
https://kontext.tech/column/spark/532/scala-parse-json-string-as-spark-dataframe


### Installing Spark 2 locally
```
brew search apache-spark@
 
apache-spark                                  
eddies/spark-tap/apache-spark@2.2.0           
eddies/spark-tap/apache-spark@2.3.2           
eddies/spark-tap/apache-spark@2.4.6 ✔
eddies/spark-tap/apache-spark@1.6.2           
eddies/spark-tap/apache-spark@2.2.2          
eddies/spark-tap/apache-spark@2.3.4           
apache-spark@1.6.2
```


```
brew tap eddies/spark-tap
brew install apache-spark@2.4.6
```
now you can use:
```
spark-shell
pyspark
```

Spark 3
```
brew info apache-spark
apache-spark: stable 3.1.2 (bottled), HEAD
Engine for large-scale data processing
https://spark.apache.org/
Not installed
From: https://github.com/Homebrew/homebrew-core/blob/HEAD/Formula/apache-spark.rb
License: Apache-2.0
==> Dependencies
Required: openjdk@11 ✘
```

#### in docker

 https://habr.com/ru/post/577762/
 
```
git clone https://github.com/big-data-europe/docker-hadoop.git
git clone https://github.com/big-data-europe/docker-spark
git clone https://github.com/big-data-europe/docker-hive

cd docker-hadoop
sudo docker-compose up -d

cd ../docker-spark
sudo docker-compose up -d

cd ../docker-hive
 sudo docker-compose up -d

cd ..
docker ps
## In browser: http://localhost:9870/
```

