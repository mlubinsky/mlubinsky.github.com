```
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

creating new column:

df.withColumn("city_starts_with_new", $"city".startsWith("new")).show()
+---------+--------+--------------------+
|superhero|    city|city_starts_with_new|
+---------+--------+--------------------+
|     thor|new york|                true|
|  aquaman|atlantis|               false|
|wolverine|new york|                true|
+---------+--------+--------------------+
```

A Column object corresponding with the city column can be created using the following three syntaxes:
```
$"city"
df("city")
col("city") (must run import org.apache.spark.sql.functions.col first)
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
