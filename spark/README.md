
1. 8 optimization techniques for DE beginners
https://lnkd.in/geskgY8Z

2. Optimization techniques every DE should know
https://lnkd.in/gfDuHT5t

3. Spark performance tuning and optimization techniques
https://lnkd.in/g9HTQxHn

4. Addressing common spark performance problems
https://lnkd.in/gECJy9cs

5. How to optimize your spark pipelines
https://lnkd.in/g6zaZRMJ

6. Performance optimization techniques in spark
https://lnkd.in/gimv4-NJ



https://www.reddit.com/r/apachespark/

https://books.japila.pl/

https://github.com/awesome-spark/awesome-spark?tab=readme-ov-file

https://github.com/OBenner/data-engineering-interview-questions?tab=readme-ov-file

https://www.reddit.com/r/databricks/

https://www.waitingforcode.com/general-data-engineering/data-ai--summit-2024-retrospective-apache-spark/read

https://habr.com/ru/companies/otus/articles/840362/ Scala Spark

https://towardsdev.com/query-plans-in-spark-internals-performance-tuning-8393b6eb0972  

https://www.newsletter.swirlai.com/p/a-guide-to-optimising-your-spark

https://www.newsletter.swirlai.com/p/a-guide-to-optimising-your-spark-841

https://blog.det.life/memory-management-in-apache-spark-f6a3499c55e2

https://www.waitingforcode.com/data-engineering/section

https://medium.com/@evyamiz/whats-the-cache-084cd174ebba caching


1. Spark Query Plans: https://lnkd.in/gspmeQ-U

2. Spark DAGs: https://lnkd.in/gT63KYSn

3. Spark Memory Management: https://lnkd.in/g_Duijqw

4. Spark Executor Tuning: https://lnkd.in/ggRS8b7u

5. Shuffle Partitions: https://lnkd.in/gb4ccdje

6. Data Partitioning: https://lnkd.in/gCQHqWac

7. Bucketing: https://lnkd.in/gKMbwrbf

8. Caching: https://lnkd.in/gJPKpPF4

9. Data Skew: https://lnkd.in/geb4cFcp

10. Salting: https://lnkd.in/gRquuyZf

11. AQE & Broadcast Joins: https://lnkd.in/gM3es6xe

12. Dynamic Partition Pruning: https://lnkd.in/gD4be_5F


### Get number of partitions in df
```
With sparkContext deprecated, was wondering is there any way to actually run
getNumPartitions as the former used to run on rdds.
 
df.rdd.getNumPartitions

df.withColumn("partitions", spark_partition_id()).select("partitions").distinct().count()

or

df.withColumn("partitions", spark_partition_id()).groupBy("partitions").count()



➤ RDD vs DataFrame:
- RDD: Low-level API, unstructured data, more control.
- DataFrame: High-level API, optimized, structured data.

➤ DataFrame vs Dataset:
- DataFrame: Untyped API, ease of use, suitable for Python.
- Dataset: Typed API, compile-time safety, best with Scala/Java.

➤ map() vs flatMap():
- map(): Transforms each element, returns a new RDD with the same number of elements.
- flatMap(): Transforms each element and flattens the result, can return a different number of elements.

➤ filter() vs where():
- filter(): Filters rows based on a condition, commonly used in RDDs.
- where(): SQL-like filtering, more intuitive in DataFrames.

➤ collect() vs take():
- collect(): Retrieves the entire dataset to the driver.
- take(): Retrieves a specified number of rows, safer for large datasets.

➤ cache() vs persist():
- cache(): Stores data in memory only.
- persist(): Stores data with a specified storage level (memory, disk, etc.).

➤ select() vs selectExpr():
- select(): Selects columns with standard column expressions.
- selectExpr(): Selects columns using SQL expressions.

➤ join() vs union():
- join(): Combines rows from different DataFrames based on keys.
- union(): Combines rows from DataFrames with the same schema.

➤ withColumn() vs withColumnRenamed():
- withColumn(): Creates or replaces a column.
- withColumnRenamed(): Renames an existing column.

➤ groupBy() vs agg():
- groupBy(): Groups rows by a column or columns.
- agg(): Performs aggregate functions on grouped data.

➤repartition() vs coalesce():
- repartition(): Increases or decreases the number of partitions, performs a full shuffle.
- coalesce(): Reduces the number of partitions without a full shuffle, more efficient for reducing partitions.

```





### Оптимизируем Shuffle в Spark
https://habr.com/ru/companies/X5Tech/articles/837348/


### Errors
```
Caused by: org.apache.spark.SparkException: Job aborted due to stage failure: Total size of serialized results of 47 tasks (1043.6 MiB) is bigger than spark.driver.maxResultSize (1024.0 MiB) at org.apache.spark.scheduler.DAGScheduler.failJobAndIndependentStages(DAGScheduler.scala:2863)

𝐌𝐞𝐚𝐧𝐢𝐧𝐠:
The error we are encountering is due to the total size of the serialized results of your Spark job exceeding the spark.driver.maxResultSize configuration parameter. This parameter sets the maximum size of results that can be fetched to the driver. When the results exceed this limit, the job is aborted to prevent the driver from running out of memory.

𝐏𝐨𝐬𝐬𝐢𝐛𝐥𝐞 𝐬𝐨𝐥𝐮𝐭𝐢𝐨𝐧𝐬:
1. Increase spark.driver.maxResultSize
spark.driver.maxResultSize: "2G"

2. 𝐑𝐞𝐝𝐮𝐜𝐞 𝐭𝐡𝐞 𝐒𝐢𝐳𝐞 𝐨𝐟 𝐭𝐡𝐞 𝐑𝐞𝐬𝐮𝐥𝐭𝐬
If increasing the spark.driver.maxResultSize is not feasible or desirable, you can try to reduce the size of the results being collected. This can be done by:
Filtering the data to include only necessary columns.


3. 𝐔𝐬𝐞 𝐟𝐨𝐫𝐞𝐚𝐜𝐡 𝐨𝐫 𝐟𝐨𝐫𝐞𝐚𝐜𝐡𝐏𝐚𝐫𝐭𝐢𝐭𝐢𝐨𝐧 𝐈𝐧𝐬𝐭𝐞𝐚𝐝 𝐨𝐟 𝐜𝐨𝐥𝐥𝐞𝐜𝐭
3.1 If you need to perform some action on each element of the RDD or DataFrame, consider using foreach or foreachPartition instead of collect. These methods perform the action on the worker nodes, avoiding the need to bring all the data to the driver.
3.2 Aggregating the data to reduce its size.
3.3 Writing the results to an external storage system (like S3, HDFS, or a database) instead of collecting them to the driver.

4. 𝐔𝐬𝐞 𝐭𝐚𝐤𝐞 𝐈𝐧𝐬𝐭𝐞𝐚𝐝 𝐨𝐟 𝐜𝐨𝐥𝐥𝐞𝐜𝐭
If you only need a sample of the data, you can use the take method instead of collect. This method retrieves only the specified number of elements.

```
### Architecture
```
Components of Spark Architecture
1. Driver Program:
-----------------
The driver program is the central piece of a Spark application. It runs the main function and is responsible for creating the Spark context, submitting jobs, and coordinating work across the cluster.
It converts user code into a directed acyclic graph (DAG) of tasks and orchestrates their execution.
2. Cluster Manager:
---------------------
The cluster manager handles the allocation of resources and scheduling of jobs across a Spark cluster.
Spark supports several cluster managers, including Apache Mesos, Hadoop YARN, and Spark’s built-in standalone cluster manager.
3. Executors:
-------------------
Executors are worker processes launched on each node of the cluster. They are responsible for executing the tasks and caching the data in memory.
Executors communicate with the driver program and report the status and results of task execution.
4. Tasks:
--------------
Tasks are the smallest unit of work in Spark. Each task represents a computation or transformation to be applied to a partition of data.
Tasks are distributed across executors by the driver program, allowing for parallel processing.


Spark Execution Workflow
******************************
When a Spark job is executed, the following steps occur:

1. Job Submission:
The driver program initiates the Spark context and submits a Spark job to the cluster manager.
2. DAG Creation:
-----------------
The Spark driver converts the user code into a directed acyclic graph (DAG) of operations. This DAG represents the sequence of transformations and actions to be applied to the data.
3. Stage Division:
-----------------
The DAG is divided into stages based on data dependencies. Each stage consists of tasks that can be executed concurrently without shuffling data.
4. Task Scheduling:
---------------------
The driver program schedules tasks for each stage and distributes them across the executors. The cluster manager allocates resources and assigns executors to the driver program.
5. Task Execution:
---------------------
Executors execute the tasks assigned to them and perform the necessary transformations and actions on the data partitions.
6. Result Collection:
----------------------
Executors return the results of the task execution to the driver program. The driver aggregates the results and performs any final operations, such as writing output to a file.
What Happens When You Execute a Script in PySpark


When you execute a script in PySpark, the following sequence of events occurs:
***********************************************************************************
1. Initialization:
The PySpark script initializes a SparkSession, which serves as the entry point to the Spark application.
Example:
from pyspark.sql import SparkSession spark = SparkSession.builder \ .appName("ExamplePySparkApp") \ .getOrCreate()
2. Data Loading and Transformation:
---------------------------------
The script loads data into DataFrames or RDDs and applies a series of transformations and actions.
Example:
df = spark.read.csv("hdfs://path/to/file.csv", header=True) df_transformed = df.filter(df['age'] > 30)
3. Job Submission:
--------------------
When an action (e.g., show(), collect(), write()) is called, the driver program creates a DAG of tasks and submits the job to the cluster manager.
Example:
df_transformed.write.parquet("hdfs://path/to/output.parquet")
4. Execution:
-----------------
The cluster manager allocates resources and assigns executors to the driver program.
The driver schedules tasks and distributes them across executors for execution.
5. Result Handling:
----------------
Executors perform the tasks and return the results to the driver.
The driver collects the results and outputs them as specified in the script.
Understanding the Job Execution Using Spark UI
The Spark UI is a web-based interface that provides detailed information about the execution of Spark jobs. It allows users to monitor and analyze the performance of their Spark applications. Here’s how you can use the Spark UI to understand what exactly is happening inside a Spark job:

Accessing the Spark UI:
The Spark UI is typically accessible at http://<driver-host>:4040. The exact URL may vary depending on your Spark cluster configuration.
```


```
for interactive queries, do not store Parquet in S3.
S3 is high-throughput but also high-latency storage. It's good for bulk reads, but not random reads, and querying Parquet involves random reads. Parquet on S3 is ok for batch jobs (like Spark jobs) but it's very slow for interactive queries (Presto, Athena, DuckDB).

The solution is to store Parquet on low-latency storage. S3 has something called S3 Express Zones (which is low-latency S3, costs slightly more). Or EBS, which is block storage that doesn't suffer from S3's high latency.
```

ASOF JOIN https://docs.snowflake.com/en/sql-reference/constructs/asof-join


Creating parquet in streaming env: https://estuary.dev/memory-efficient-streaming-parquet/

https://habr.com/ru/articles/828984/  Spark Interview questions

https://habr.com/ru/companies/alfa/articles/829622/ Spark optimization guide

https://habr.com/ru/companies/oleg-bunin/articles/828836/

https://www.youtube.com/playlist?list=PLL7QpTxsA4se-mAKKoVOs3VcaP71X_LA-  Streaming systems

https://habr.com/ru/articles/806287/ PySpark + Kafka

https://www.youtube.com/watch?v=FdT5o7M35kU  Spark Out Fo Memory Explained

### Local Spark in Docker
https://medium.com/programmers-journey/deadsimple-pyspark-docker-spark-cluster-on-your-laptop-9f12e915ecf4

###  План запросов
https://www.youtube.com/watch?v=99fYi2mopbs

https://www.youtube.com/watch?v=9EIzhRKpiM8

https://habr.com/ru/articles/807421/ План запросов на примерах

https://habr.com/ru/companies/avito/articles/764996/
```
df.explain()
# есть разные опции как форматировать вывод
df.explain(mode='formatted')
```
### Spark interview questions 

https://medium.com/@siladityaghosh/complex-data-manipulation-techniques-with-apache-pyspark-407f2c3295d3

https://habr.com/ru/companies/alfa/articles/808415/

https://habr.com/ru/companies/otus/articles/808141/
```
spark = SparkSession.builder \
.appName(“MySparkApp”) \
.config(“spark.serializer”, “org.apache.spark.serializer.KryoSerializer”) \
.getOrCreate()

https://towardsdatascience.com/six-spark-exercises-to-rule-them-all-242445b24565
```

```
#   Output how many products have been actually sold at least once
print("Number of products sold at least once")
sales_table.agg(countDistinct(col("product_id"))).show()

#   Output which is the product that has been sold in more orders
print("Product present in more orders")
sales_table.groupBy(col("product_id")).agg(
    count("*").alias("cnt")).orderBy(col("cnt").desc()).limit(1).show()

# how many distinct products have been sold in each date
sales_table.groupby(col("date")).agg(countDistinct(col("product_id")).alias("distinct_products_sold")).orderBy(
    col("distinct_products_sold").desc()).show()

What is the average revenue of the orders?  (revenue = price * quantity)
print(sales_table.join(products_table, sales_table["product_id"] == products_table["product_id"], "inner").
      agg(avg(products_table["price"] * sales_table["num_pieces_sold"])).show())


Who are the second most selling and the least selling persons (sellers) for each product?
Who are those for the product with product_id = 0

# Calcuate the number of pieces sold by each seller for each product
sales_table = sales_table.groupby(col("product_id"), col("seller_id")). \
    agg(sum("num_pieces_sold").alias("num_pieces_sold"))

# Create the window functions, one will sort ascending the other one descending. Partition by the product_id
# and sort by the pieces sold
window_desc = Window.partitionBy(col("product_id")).orderBy(col("num_pieces_sold").desc())
window_asc = Window.partitionBy(col("product_id")).orderBy(col("num_pieces_sold").asc())

# Create a Dense Rank (to avoid holes)
sales_table = sales_table.withColumn("rank_asc", dense_rank().over(window_asc)). \
    withColumn("rank_desc", dense_rank().over(window_desc))

# Get products that only have one row OR the products in which multiple sellers sold the same amount
# (i.e. all the employees that ever sold the product, sold the same exact amount)
single_seller = sales_table.where(col("rank_asc") == col("rank_desc")).select(
    col("product_id").alias("single_seller_product_id"), col("seller_id").alias("single_seller_seller_id"),
    lit("Only seller or multiple sellers with the same results").alias("type")
)

# Get the second top sellers
second_seller = sales_table.where(col("rank_desc") == 2).select(
    col("product_id").alias("second_seller_product_id"), col("seller_id").alias("second_seller_seller_id"),
    lit("Second top seller").alias("type")
)

# Get the least sellers and exclude those rows that are already included in the first piece
# We also exclude the "second top sellers" that are also "least sellers"
least_seller = sales_table.where(col("rank_asc") == 1).select(
    col("product_id"), col("seller_id"),
    lit("Least Seller").alias("type")
).join(single_seller, (sales_table["seller_id"] == single_seller["single_seller_seller_id"]) & (
        sales_table["product_id"] == single_seller["single_seller_product_id"]), "left_anti"). \
    join(second_seller, (sales_table["seller_id"] == second_seller["second_seller_seller_id"]) & (
        sales_table["product_id"] == second_seller["second_seller_product_id"]), "left_anti")

# Union all the pieces
union_table = least_seller.select(
    col("product_id"),
    col("seller_id"),
    col("type")
).union(second_seller.select(
    col("second_seller_product_id").alias("product_id"),
    col("second_seller_seller_id").alias("seller_id"),
    col("type")
)).union(single_seller.select(
    col("single_seller_product_id").alias("product_id"),
    col("single_seller_seller_id").alias("seller_id"),
    col("type")
))
union_table.show()

# Which are the second top seller and least seller of product 0?

union_table.where(col("product_id") == 0).show()

```



https://habr.com/ru/companies/beeline_tech/articles/804513/ Оптимизируем параметры запуска приложения Spark. Часть первая

https://habr.com/ru/companies/sberbank/articles/805285/  Как перезапускать PySpark-приложение и зачем это может понадобиться

https://asrathore08.medium.com/spark-interview-question-xiii-e41244e41d7a

https://towardsdatascience.com/1-5-years-of-spark-knowledge-in-8-tips-f003c4743083

https://sujit-j-fulse.medium.com/optimise-an-already-optimised-heavy-spark-job-with-long-lineage-2f6cb37f8b80

https://medium.com/@stanislav.i.kulchitskiy/spark-jobs-resources-estimation-f7b6da87b64c

### Delta lake
https://medium.com/@abhinav.prakash1804/delta-lake-vs-parquet-86e1e926f446

### SPARK SQL
https://books.japila.pl/spark-sql-internals/features/

### Spark + Airflow + Docker
https://habr.com/ru/companies/lamoda/articles/810705/

https://habr.com/ru/articles/805143/ 3 способа запуска Spark в Kubernetes из Airflow

### Spark performance

https://habr.com/ru/companies/beeline_tech/articles/804513/

https://habr.com/ru/companies/oleg-bunin/articles/768284/

https://habr.com/ru/companies/avito/articles/764996/

https://habr.com/ru/companies/megafon/articles/763864/

https://holdenk.github.io/spark-flowchart/flowchart/error/

https://holdenk.github.io/spark-flowchart/flowchart/slow/

```
df = df_eu.join(df_lac, how="inner", on="value")   <--- this join is executed twice!!!

df_1 = df.filter(filter_condition_1)
df_2 = df.filter(filter_condition_2)

## Add a new col after performing some transformation
df_1 = df_1.withColumn("new_col", transform_1)
df_2 = df_2.withColumn("new_col", transform_2)

## Union the two data frames
df_1.union(df_2).count()

In the above example, we will notice that the join happened twice.
To speed up this we can call a cache to persist the joined data frame in memory.
So optimizer uses the shortcut to fetch the data instead of computing it from the source.
```

- Shuffle  https://blog.devgenius.io/shuffle-in-spark-d95b5ebe7b4e
- Skew (partitioning) https://blog.devgenius.io/spark-partitioning-da6dba06949f
- Spill  https://blog.devgenius.io/spark-spill-7e027085ca4c
- Storage
- Serialization

### Spark configuration

https://blog.devgenius.io/spark-configurations-96eab8775e7

- Application Properties
```
Spark allows us to set these application configurations in multiple ways.

1. $SPARK_HOME/conf/spark-defaults.conf file

2. $SPARK_HOME/bin/spark-submit on the command line

3. When creating the SparkSession

# Application Properties
spark.app.name 
spark.master

# Runtime properties
spark.driver|executor.extraJavaOptions
spark.driver|executor.extraClassPath

# Memory configuration
spark.driver.memory 
spark.executor.memory

# Execution environment 
spark.executor.cores

# SQL related 
spark.sql.autoBroadcastJoinThreshold
spark.sql.broadcastTimeout
spark.sql.shuffle.partitions

# Spark Streaming
spark.streaming.kafka.maxRatePerPartition
spark.streaming.backpressure.enabled

# Spark UI
spark.eventLog.dir
spark.ui.enabled
```
- Runtime environment, Execution Behaviour
- Spark SQL, Streaming
- Memory Management, Spark UI
- Networking, Security


https://jaceklaskowski.gitbooks.io/mastering-spark-sql/content/spark-sql-QueryExecution.html#execution-pipeline

https://umbertogriffo.gitbook.io/apache-spark-best-practices-and-tuning/


### Troubleshooting

https://blog.devgenius.io/debugging-a-memory-leak-in-spark-application-22140630877d

https://blog.devgenius.io/spark-questions-interview-series-c31cedf41652

### Out of memory

https://medium.com/swlh/spark-oom-error-closeup-462c7a01709d

https://blog.devgenius.io/spark-errors-uncluttered-fc0b2fb74ed0

https://medium.com/@sathamn.n/surviving-an-oom-issue-in-apache-spark-a-thrilling-interview-experience-e9f7cbd214dc
```
First, we need to find out what caused the OOM error. 
Is it execution memory, overhead, storage memory, or memory leak? Based on that we can adjust the following:

Number of cores (decreasing it)
spark.executor.memory
spark.memory.fraction
spark.memory.storageFraction
spark.executor.memoryOverhead
spark.executor.pyspark.memory
spark.memory.offHeap.size + spark.memory.offHeap.enabled
```
https://sunilrana123.medium.com/bigdata-interview-question-part-3-38f36c57bac2

https://blog.devgenius.io/solution-spark-debugging-a-slow-application-e900ebd7bec9

https://leanpub.com/beautiful-spark/

Read local file instead HDFS: https://stackoverflow.com/questions/27299923/how-to-load-local-file-in-sc-textfile-instead-of-hdfs

spark-shell
https://habr.com/ru/post/480846/

https://habr.com/ru/post/708468/
```
from pyspark.sql import SparkSession
 
spark = SparkSession.builder.getOrCreate()
spark.conf.set("spark.sql.execution.arrow.pyspark.enabled", "true")
spark

df = spark.read.csv('data/train.csv', header=True, inferSchema=True)
df.printSchema()

 Метод pandas_api преобразует существующий DataFrame в pandas-on-Spark DataFrame (это доступно только в том случае, если pandas установлен и доступен).

df.pandas_api().isna().mean()
df = df.dropna()
df.pandas_api().isna().sum()
```

### groupByKey() reduceByKey() aggregateByKey()
```
Spark provides two ways to group and process data. Grouping can be done via groupBy and groupByKey. These functions return a RelationalGroupedDataset and a KeyValueGroupedDataset[K, V], respectively.
```
https://www.gresearch.com/news/sparks-groupbykey-should-be-avoided-and-heres-why

https://stackoverflow.com/questions/43364432/spark-difference-between-reducebykey-vs-groupbykey-vs-aggregatebykey-vs-combi

```
groupByKey() is just to group your dataset based on a key. It will result in data shuffling when RDD is not already partitioned.

The groupByKey() operation groups all values associated with a specific key into a single collection, such as a list or an iterator.
This operation does not perform any aggregation itself; it merely organizes the data by key.
 All records with the same key need to be moved to the same node in the cluster. 

reduceByKey() is something like grouping + aggregation. We can say reduceByKey() equivalent to dataset.group(...).reduce(...). It will shuffle less data unlike groupByKey().
reduceByKey() applies a reduction function (e.g., sum, count) to the values associated with each key,
merging them using the provided function.
The key difference is that reduceByKey() performs a local reduction (map-side combine) before shuffling the data across the network

aggregateByKey() is logically same as reduceByKey() but it lets you return result in different type.
In another words, it lets you have an input as type x and aggregate result as type y.
For example (1,2),(1,4) as input and (1,"six") as output.
It also takes zero-value that will be applied at the beginning of each key.

Note: One similarity is they all are wide operations.
```

### Spark SQL
https://spark.apache.org/docs/latest/api/sql/index.html

### PySpark functions
https://spark.apache.org/docs/latest/api/python/reference/pyspark.sql.html#functions

https://habr.com/ru/company/otus/blog/575740/

https://mungingdata.com/pyspark/chaining-dataframe-transformations/

 map, filter, transform, array_contains, exists ,  aggregate
 map_filter, map_zip_with, transform_keys и transform_values
 
 https://habr.com/ru/company/alfastrah/blog/481924/
 
 ```
 dfAtom = dfCon.join(dfCStat,con_stat, "inner")\
    .join(dfSubj,con_subj_own,"inner") \
    .join(dfPPers,con_ppers_own, "left") \          
    .drop("con_contract_status_id","sbj_subject_type_id",
          "pp_subject_id","con_owner_subject_id","cst_status_id")
 ```
 
### Example of agg, window, groupby: 

https://habr.com/ru/post/545870/
 
 ```
from pyspark.sql.functions import lag
from pyspark.sql import functions as F
from pyspark.sql.window import Window

# F.lag() - Equivalent of Pandas.dataframe.shift() method
*************************************************
w = Window().partitionBy().orderBy(col("proj_id"))
df_dataframe = df.withColumn('lag', F.lag("proj_end").over(w))
 
# F.when/F.otherwise - Equivalent of SQL- CASE WHEN...THEN...ELSE... END
#######################################################
df_dataframe = df_dataframe.withColumn('flag',F.when(df_dataframe["proj_start"] == df_dataframe["lag"],0).otherwise(1))
 
# Cumulative sum by column named 'flag'
#########################
w = Window().partitionBy().orderBy(col("proj_id"))
df_dataframe = df_dataframe.withColumn("proj_group", F.sum("flag").over(w))
 
# agg.min, agg.max   Equivalent of SQL - GROUP BY
#################################
from pyspark.sql.functions import  min, max
df_group = df_dataframe.groupBy("proj_group").agg(min("proj_start").alias("date_start"), \
                                                  max("proj_end").alias("date_end"))
df_group = df_group.withColumn("delta", F.datediff(df_group.date_end,df_group.date_start))
df_group.show()
 ```
 
### Median calculation
```
# Pandas
df.groupby("col1")["col2"].median()

# PySpark
from pyspark.sql import Window
import pyspark.sql.functions as F

med_func = F.expr('percentile_approx(col2, 0.5, 20)')
df.groupBy('col1').agg(med_func).show()
```

### Spark + Pandas

https://habr.com/ru/company/otus/blog/594787/ 

https://habr.com/ru/post/710338/

``` 
партиционирование немного по-разному поддерживается в Hive и в spark и может быть источником граблей. 
Просто положить данные в папочку на hdfs (с помощью distcp или файловых операций) может быть недостаточно.
Надо будет вызывать ```msck repair table```, чтобы обновить партиции в metastore. 
```
### How many partitions

https://habr.com/ru/company/otus/blog/686142/

https://habr.com/ru/company/otus/blog/704010/

У DataFrame, DataSet, созданного из файла на HDFS, будет столько партиций, сколько блоков на HDFS имеет исходный файл. 
Либо в зависимости от параметра 
```
spark.sql.files.maxPartitionBytes  // which defaults to 128MB


val fromHdfsFileDF = spark
.read
.format(“parquet”)
.load(“hdfs://user/crimes_csv/part-00000-f8e2d087-fd31-4cb5-b96e-62d36ee7074b-c000.parquet”)
fromHdfsFileDF.rdd.getNumPartitions
```

У DataFrame, DataSet, созданного в результате джойна, группировки или другой 

spark.conf.get("spark.sql.shuffle.partitions") => 200


https://habr.com/ru/company/X5Tech/blog/684024/ Parallel execution in Spark

можно зафиксировать ресурсы за вашим приложением c помощью spark.executor.instances 

initialExecutors

https://habr.com/ru/company/neoflex/blog/578654/ Very Good

https://habr.com/ru/company/onefactor/blog/695562/

https://selectfrom.dev/spark-performance-tuning-spill-7318363e18cb

https://selectfrom.dev/apache-spark-partitioning-bucketing-3fd350816911

https://habr.com/ru/company/otus/blog/653977/ . Monitoring Apache Spark

https://habr.com/ru/company/otus/blog/653033/ Spark ML example


### Spark Architecture
https://habr.com/ru/company/otus/blog/557812/
```
 процесс Spark Driver. Это управляющий (master) процесс, который содержит все процедуры и задания, 
 которые надлежит выполнить (направленные ациклические графы — DAG, определенные пользователем в коде Java, Scala или Python).
 
 Управляющий процесс передает исполнительным процессам (Executor) задачи, которые надлежит выполнить, и контролирует их успешное выполнение, 
 прежде чем будет завершен сам.

приложения Spark выполнялись в кластере больших данных Hadoop, на котором доступен модуль YARN (Yet Another Resource Negotiator)

В этой статье https://habr.com/ru/company/otus/blog/529100/
мы будем использовать AWS  r5.4xlarge,  на инстансы AWS EC2 
- 16 процессоров
- 128 ГБ
 
Когда мы запускаем наши задачи (job), нам нужно зарезервировать один процессор для операционной системы 
и системы управления кластерами (Cluster Manager). 
Поэтому мы не хотели бы задействовать под задачу сразу все 16 ЦП. 
Таким образом, когда Spark производит вычисления, на каждом узле у нас остается только 15 доступных для аллоцирования ЦП.

Самое очевидное решение, которое приходит на ум, - создать одного исполнителя (executor) с 15 ядрами. 
Проблема с большими жирными исполнителями, подобными этому, заключается в том, что исполнитель, поддерживающий такое количество ядер, 
обычно будет иметь настолько большой пул памяти (64 ГБ+), что задержки на сборку мусора будут неоправданно замедлять вашу работу. 
Поэтому мы сразу исключаем эту конфигурацию.

Следующее очевидное решение, которое приходит на ум — создать 15 исполнителей, каждый из которых имеет только одно ядро. 
Проблема здесь в том, что одноядерные исполнители неэффективны, потому что они не используют преимуществ параллелизма, 
которые обеспечивают несколько ядер внутри одного исполнителя. 
Кроме того, найти оптимальный объем служебной памяти для одноядерных исполнителей может быть достаточно сложно. 

Большинство руководств по настройке Spark сходятся во мнении, что 5 ядер (cores) на исполнителя (executor) — 
это оптимальное количество ядер с точки зрения параллельной обработки. 

--executor-cores 5

--executor-memory 34G

https://habr.com/ru/company/otus/blog/529100/
 Нам также нужно назначить драйвер для обработки всех исполнителей в узле. Если мы используем количество исполнителей, кратное 3, 
 то наш одноядерный драйвер будет размещен в своем собственном 16-ядерном узле, что означает,
что аж 14 ядер на этом последнем узле не будут использоваться в течение всего выполнения задачи. 
 
 идеальное количество исполнителей должно быть кратным 3 минус один исполнитель, чтобы освободить место для нашего драйвера.
 
 --num-executors (3x - 1)
 
```

https://habr.com/ru/post/592067/ RRD Dataframe

```
любая оптимизация должна проводиться в первую очередь с контролем:
1) плана выполнения запроса
2) занимаемых ресурсов в процессе работы
3) конфигурации spark-приложения (в частности количества памяти на экзекьютор, драйвер, уровня auto-broadcast-treshold)
4) времени выполнения
5) размеров таблиц с исходными данными.
Использование Broadcast может привести вас к плавающему OutOfMemoryException когда "маленькая" таблица вдруг окажется слоном, 
который не влезает в экзекьютор.
Не-использование Broadcast в некоторых конфигурациях данных — тоже.
```

Example of Airflow tasks which invokes Spark
https://habr.com/ru/company/neoflex/blog/700118/
```
test_tasks = []
for table in all_table_full_names:
    test_task = BashOperator(
        task_id=f"run_dq_tests_for_{table.replace('.', '_')}",
        bash_command=f"/opt/dev/spark/spark-3.2.1/bin/spark-submit \
        --driver-memory 2g \
        --executor-memory 2g \
        --executor-cores 2 \
        --conf spark.dynamicAllocation.maxExecutors=4 \
        --conf spark.dynamicAllocation.initialExecutors=2 \
        --conf spark.sql.shuffle.partitions=8 \
        --conf spark.sql.sources.partitionOverwriteMode=dynamic \
        --conf spark.pyspark.virtualenv.enabled=true \
        --conf spark.pyspark.virtualenv.type=native \
        --jars {LIBS_PATH}/postgresql-42.3.6.jar \
        --conf spark.pyspark.python={VENV_PATH}/bin/python3.9 \
        --conf spark.pyspark.virtualenv.bin.path={VENV_PATH}/bin/ \
        {SCRIPTS_PATH}/{RUN_TESTS_SCRIPT} {table}" + " {{ logical_date }}",
        dag=dag,
        trigger_rule=TriggerRule.ALL_DONE
    )
    test_tasks.append(test_task)
```


JSON createOrReplaceTempView
```
Read JSON file and register temp view

context.jsonFile("s3n://…").createOrReplaceTempView("json")

Execute SQL query

results = context.sql("""SELECT * FROM people JOIN json …""")
```
### Spark configuration  

https://blog.devgenius.io/solution-spark-debugging-a-slow-application-e900ebd7bec9

In general, the number of cores can be experimented with in the range of
3–5 for executors with memory in the range of 20–40G.

https://habr.com/ru/company/otus/blog/540396/
```
Обычными причинами, приводящими к OutOfMemory OOM (недостаточно памяти) драйвера, являются:
   rdd.collect()
   sparkContext.broadcast 
   Низкий уровень памяти драйвера, настроенный в соответствии с требованиями приложения
   Неправильная настройка Spark.sql.autoBroadcastJoinThreshold.
```
### Spark submit:

https://spark.apache.org/docs/3.2.1/submitting-applications.html
```
spark-submit 
--class <…sqlrunner> 
--name <taskname> 
--queue <yarnqueue> 
--executor-cores 1 
--executor-memory 1g 
--driver-cores 1 
--driver-memory 1g 
--num-executors 1 
--master yarn 
--deploy-mode cluster <hdfs://…sqlrunner.jar> 
sqlFile=<…sql>
```


### Spark-sql

```
nohup spark-sql 
--master yarn  
--conf spark.dynamicAllocation.enabled=true 
--conf spark.executor.memoryOverhead=6GB 
--conf spark.dynamicAllocation.maxExecutors=100 
--conf spark.shuffle.service.enabled=true 
--conf spark.sql.shuffle.partitions=6000 
--conf spark.driver.maxResultSize=8g 
--conf spark.serializer=org.apache.spark.serializer.KryoSerializer 
--conf mapreduce.input.fileinputformat.input.dir.recursive=true 
--conf spark.hive.mapred.supports.subdirectories=true 
--executor-memory 30g 
--driver-memory 10g 
--executor-cores 5 
-f /home/hadoop/vambati/test.hql > test.log &
```

### COMPUTE STATISTICS and SQL HINTs

 Spark существуют различные алгоритмы реализации join-ов: SortMergeJoin, BroadcastHashJoin, CartesianProduct 
 https://habr.com/ru/company/sberbank/blog/496310/

Для этого посредством spark-submit вызываем команду вида:

ANALYZE TABLE scheme_name.table_name COMPUTE STATISTICS;


https://medium.com/credera-engineering/how-to-write-unit-tests-for-spark-f8ea22cf6448 Unit test

Проверить, что статистика собрана, можно в среде hive командой вида:
```
show create table scheme_name.table_name;
```
Нужно посмотреть, появились ли в конце описания в блоке TBLPROPERTIES свойства
'spark.sql.statistics.numRows' и 'spark.sql.statistics.totalSize':
```
CREATE EXTERNAL TABLE `scheme_name.table_name`(
TBLPROPERTIES (
…
  'spark.sql.statistics.numRows'='363852167', 
  'spark.sql.statistics.totalSize'='82589603650', 
…


insert overwrite table target_scheme.target_table
select /*+ BROADCAST(t) */ big.field1,
       big.field2,
       t.field3
  from source_scheme.big_table as big
  left join source_scheme.small_table as t
    on big.field1 = t.field1;
```

 Spark SQL есть и другие хинты, в т.ч. с версии 2.4 появляются хинты
 
 ```
 /*+ COALESCE(n) */, где n – количество партиций, на которые будет разбит результат, 
 /* + REPARTITION (n) */, где n – количество партиций при repartition.
```
По умолчанию задача соединения двух таблиц, выполненная посредством spark-submit, будет разбита на 200 партиций. 
Изменить эту настройку по умолчанию можно, задав другое значение конфигурации spark.sql.shuffle.partitions, например:
```
--conf spark.sql.shuffle.partitions=1000
```
### PySpark
https://insaid.medium.com/eda-with-pyspark-1f29b7d1618

https://habr.com/ru/company/otus/blog/594787/ . pandaspark pyspark in spark 3.2

 https://stackoverflow.com/questions/39067505/pyspark-display-a-spark-data-frame-in-a-table-format


https://habr.com/ru/company/X5Group/blog/579232/. PySpark
https://www.youtube.com/watch?v=_C8kWso4ne4
https://parisrohan.medium.com/an-attempt-to-spark-your-interest-in-pyspark-fddccdc3081f
https://medium.com/swlh/pyspark-on-macos-installation-and-use-31f84ca61400


end o pySpark



https://towardsdatascience.com/six-spark-exercises-to-rule-them-all-242445b24565

https://habr.com/ru/company/otus/blog/592605/

https://www.youtube.com/channel/UCl8BC-R6fqITW9UrSXj5Uxg

https://www.youtube.com/channel/UClM7fatYZhgbMqpqyqHmKAw/videos

https://livebook.manning.com/book/streaming-data/ Book (I bought it)

https://livevideo.manning.com/module/22_1_3/spark-in-motion/an-introduction-to-apache-spark/functional-programming-using-the-spark-shell?

#### Bucketing

https://selectfrom.dev/apache-spark-partitioning-bucketing-3fd350816911

https://towardsdatascience.com/best-practices-for-bucketing-in-spark-sql-ea9f23f7dd53

https://medium.com/analytics-vidhya/spark-bucketing-is-not-as-simple-as-it-looks-c74f105f4af0
```
Spark also gives us the option of bucketing while writing data to tables.
In bucketing data is divided into smaller portions called “buckets”.

df.write.bucketBy(12, "key").saveAsTable("table_name")
Number of files in bucketing = df.partition * number of bucket

 To use bucket join for tables having buckets multiple of each other we need to set the following:

spark.sql.bucketing.coalesceBucketsInJoin.enabled
```
### Skew 
https://medium.com/@suffyan.asad1/handling-data-skew-in-apache-spark-techniques-tips-and-tricks-to-improve-performance-e2934b00b021

https://towardsdatascience.com/deep-dive-into-handling-apache-spark-data-skew-57ce0d94ee38

https://habr.com/ru/company/first/blog/678826/

```
оптимизации перекошенного соединения в AQE: Adaptive Query Execution 

spark.sql.adaptive.skewJoin.enabled:
Этот логический параметр определяет, включена или выключена оптимизация перекошенного соединения. 
Значение по умолчанию — true.

spark.sql.adaptive.skewJoin.skewedPartitionFactor:
Этот целочисленный параметр управляет интерпретацией перекошенного раздела.
Значение по умолчанию равно 5.

spark.sql.adaptive.skewJoin.skewedPartitionThresholdInBytes:
Этот параметр в мегабайтах также управляет интерпретацией перекошенного раздела.
Значение по умолчанию равно 256 MB.

Раздел считается перекошенным, если оба параметра
(partition size (размер раздела) > skewedPartitionFactor * median partition size (медианный размер раздела)) и
(partition size > skewedPartitionThresholdInBytes) соответствуют действительности.
```

https://medium.com/curious-data-catalog/sparks-skew-problem-does-it-impact-performance-257cdef53680

https://medium.com/curious-data-catalog/spill-often-ignored-sparks-performance-problem-9b4c1ea962f

### Salting

https://towardsdatascience.com/skewed-data-in-spark-add-salt-to-compensate-16d44404088b

https://medium.com/curious-data-catalog/sparks-salting-a-step-towards-mitigating-skew-problem-5b2e66791620


https://habr.com/ru/company/newprolab/blog/530568/ What is new in Spark 3.0

### Partitioning

https://blog.devgenius.io/spark-partitioning-da6dba06949f


In Spark, the number of partitions comes into the picture at three stages of the pipeline.
```
Input / Reading
Shuffle / Transformation
Output / Writing
```

Reading:
```
For reading files from Parquet, JSON, and ORC we can set the bytes for each partition.

spark.default.parallelism — how many partitions are read in when doing spark.read
spark.sql.files.maxPartitionBytes — The maximum number of bytes to put into a single partition when reading files.
spark.sql.files.minPartitionNum — minimum number of split file partition
spark.files.openCostInBytes — estimated cost to open a file

While reading from databases we can ser (partitionColumn, lowerBound, upperBound, numPartitions ).
 These values will divide the data(between lower & upper bound) into partitions (a number equal to numPartitions). S
o let us say we have an Id column and we set lowerBound to 1 and upperBound to 40000 with numPartitions to 4.
Then in the case of equal distribution spark will have 4 partitions with 10000 records each.

Note: For while reading from folders containing large number of files,
enumeration of datasets is a challenge as it happens on driver.
This processing of file listing follows a serial code path and can be slow.
There are third party solutions, like RapidFile, to speed up file listing.

```
Shuffle
```
When we perform a wide transformation (group by, join, window function, sort) there is a shuffle(redistribution) of data.
During this shuffle, new partitions get created or removed.
E.g If we use row_number() function it will reduce the number of partition to 1.

The smaller size of partitions (more partitions) will increase the parallel running jobs, which can improve performance, but too small of a partition will cause overhead and increase the GC time. Larger partitions (fewer number of partitions) will decrease the number of jobs running in parallel.

df.rdd.getNumPartitions()

spark.sql.shuffle.partitions— Default number of partitions returned by transformations like
 join, reduceByKey, and parallelize when not set by user. Default is 200.

We can manually tweak the number of partitions by coalescing or repartitioning.

repartition(numPartitions) — Uses RoundRobinPartitioning
repartition(partitionExprs) — Uses HashPartitioner
repartitionByRange(partitionExprs) — Uses range partitioning.
coalesce(numPartitions) — Use only to reduce the number of partitions.

Note: In most cases, Coalesce should be preferred over repartition while reducing the number of partitions.

But Repartition guarantees that the data distribution in the partition is roughly the same size.
So in some cases,it may be preferred.

In case where are performing aggregate on unique columns we should control the shuffle by using repartition.

Good partitioning of data leads to better speed and fewer OOMs errors.

The repartition leads to a full shuffle of data between the executors making the job slower.
The coalesce operation doesn’t trigger a full shuffle when it reduces the number of partitions.
It only transfers the data from partitions being removed to existing partitions.
```
###  Get partitions and there record count for each one:
```
from pyspark.sql.functions import spark_partition_id, asc, desc

df.withColumn("partitionId", spark_partition_id())\
    .groupBy("partitionId")\
    .count()\
    .orderBy(asc("count"))\
    .show()
```
Output
```
The number of files that get written out is controlled by the parallelization of your DataFrame or RDD.
So if your data is split across 10 Spark partitions you cannot write fewer than 10 files without reducing partitioning (e.g. coalesce or repartition).
```
### PartitionBy
https://spark-school.ru/blog/partitionby/
```
Apache spark поддерживает два вида партиций: в оперативной памяти в виде фрейма данных (DataFrame) и на диске в виде файла:

Партиция в памяти выполняется с помощью вызовов repartition или coalesce.
Партиция на диске выполняется с помощью вызова partitionBy (это аналогично партициям в Hive).
```

https://medium.com/@tomhcorbin/mastering-pyspark-partitioning-repartition-vs-partitionby-cfde90aa3622
```
When you call df.write.partitionBy('column'), each of the original partitions in df is written independently. That is, each of your original partitions is sub-partitioned separately based on the 'column', and a separate file is written for each sub-partition. This means that the number of output files depends on the distribution of data in the original partitions.

You would expect partitionBy() to create a global partitioning based on the specified column, resulting in a number of output files equal to the number of unique values in the column. However, partitionBy() operates on the level of individual partitions, leading to a potentially larger number of output files.

One strategy to control the number of output files is to use repartition() before partitionBy(). This allows you to control the number of partitions in memory before writing out the data. Here's how you can do it:

df.repartition(7, "DayOfWeek").write.partitionBy("DayOfWeek").parquet("path")

In this example, the DataFrame is first repartitioned into 7 partitions based on ‘DayOfWeek’. repartition() uses a hash-based partitioner, which ensures that the unique ‘DayOfWeek’ values make their way into each partition. Then, when writing out the data with partitionBy(), each of these 7 partitions is written independently, resulting in a maximum of 7 output files for each unique value in 'DayOfWeek'.



partitionBy() — Partitions the output by the given columns on the file system.
maxRecordsPerFile — number of records in a single file in each partition. This helps in fixing large file problem.

When we write data, using the maxRecordsPerFile option, we can limit the number of records that get written per file in each partition.

To get one file per partition, use repartition() with the same columns you want the output to be partitioned by.

The partitionBy method does not trigger any shuffle but it may generate a too many files.
Imagine we have 200 partitions, and we want to partition data by date.
Each spark task will produce 365 files in which leads to 365×200=73k files.

partition_cols = [] 
df.repartition(*partition_cols)\
  .write.partitionBy(*partition_cols)\
  .mode(SaveMode.Append).parquet(path)
```
### Bucketing: bucketBy
```
Spark also gives us the option of bucketing while writing data to tables.
In bucketing data is divided into smaller portions called “buckets”.

df.write.bucketBy(12, "key").saveAsTable("table_name")
Number of files in bucketing = df.partition * number of bucket

Also, To use bucket join for tables having buckets multiple of each other we need to set the following:

spark.sql.bucketing.coalesceBucketsInJoin.enabled
```


```
repartition(numPartitions) — Uses RoundRobinPartitioning
repartition(partitionExprs) — Uses HashPartitioner
repartitionByRange(partitionExprs) — Uses range partitioning.
coalesce(numPartitions) — Use only to reduce the number of partitions.
```
https://www.amazon.com/Guide-Spark-Partitioning-Explained-Depth/dp/B08L25WHJ4  Guide to Spark Partitioning

https://medium.com/@vladimir.prus/spark-partitioning-the-fine-print-5ee02e7cb40b

https://towardsdatascience.com/the-art-of-joining-in-spark-dcbd33d693c

https://medium.com/nerd-for-tech/apache-spark-optimization-techniques-b982e71153ff

https://ajithshetty28.medium.com/lesser-known-facts-short-cuts-in-spark-part2-4dc801a83dfb

https://databricks.com/p/webinar/databricks-on-aws-3-part-training-series Free training

https://habr.com/ru/post/568276/ Databricks

https://habr.com/ru/company/neoflex/blog/578654/ оптимизация производительности на реальных примерах

http://cloudsqale.com/

Code for the Spark in Action Book: https://github.com/databricks/LearningSparkV2

There are 8 workers and both the workers and driver are 

https://aws.amazon.com/ec2/pricing/on-demand/
https://habr.com/ru/company/otus/blog/529100/
```
m4.xlarge  instance:  16.0 GB, 4 Cores
r5.4xlarge instance:  128GB 16 cores
```

```
--executor-cores 5
--executor-memory 34G
--num-executors (3x - 1)
--driver-memory 34G
--driver-cores 5
```

https://www.youtube.com/watch?v=G4D4iY_hZQ0&list=PLtfmIPhU2DkNjQjL08kR3cd4kUzWqS0vg

https://towardsdatascience.com/overcoming-apache-sparks-biggest-pain-points-b374cebcf6a4

https://github.com/ankurchavda/SparkLearning#spark-learning-guide

https://pub.towardsai.net/4-tips-to-write-scalable-apache-spark-code-1c736e4d698e


https://github.com/ankurchavda/SparkLearning/blob/master/advanced/optimizations.md


The general recommendation for Spark is to have 4x of partitions to the number of cores in cluster available for application, 
and for upper bound — the task should take 100ms+ time to execute

spark-submit params

Leave aside 1 core per node fo cluster management deamons:
NamedNode, SecondaryNamed Node,DataNode,JobTracker,TaskManager

5 tasks per executor. Executor= 1 JVM.
Task is 1 thread which process 1 partition


https://medium.com/expedia-group-tech/part-3-efficient-executor-configuration-for-apache-spark-b4602929262

https://medium.com/expedia-group-tech/part-6-summary-of-apache-spark-cost-tuning-strategy-8d06148c5da6

### Spark config for performance

https://medium.com/expedia-group-tech/part-3-efficient-executor-configuration-for-apache-spark-b4602929262

https://habr.com/ru/company/otus/blog/540396/

https://habr.com/ru/company/otus/blog/541426/

https://www.unraveldata.com/resources/troubleshooting-apache-spark/


https://medium.com/swlh/insights-into-parquet-storage-ac7e46b94ffe

```
spark.sql.shuffle.partitions might be one of the most critical configurations in Spark. 
It configures the number of partitions to use when shuffling data for joins or aggregations. 
Configuring this value won’t always mean dealing with the skew issue, but it could be general optimization on the Spark job. 
The default value is 200, which is suitable for many big data projects back in the day and still relevant for small/medium size data projects.

2. Broadcast join
Broadcast join might be the fastest join type that you can use to avoid skewness. 
By giving when the BROADCAST hint, we explicitly provide information to Spark on which dataframe we’d need to send to each executor.

The broadcast join usually works with smaller size dataframe like dimension tables or the data has metadata. 
It is not appropriate for transaction tables with millions of rows.

df_skew.join(broadcast(df_evenly.select(“value”)),”value”, “inner”).count()


spark.executor.memory или spark.driver.memory
spark.yarn.executor.memoryOverhead

"spark.memory.fraction". По умолчанию — 60%. 
Из них по умолчанию 50% (настраивается параметром "spark.memory.storageFraction"

Для файлов HDFS каждая задача Spark будет считывать блок данных размером 128 МБ. 
Таким образом, если выполняется 10 параллельных задач, 
то потребность в памяти составляет не менее 128*10 только для хранения разбитых на разделы данных. 

Если это этап reduce-stage (стадия Shuffle), то для определения количества задач Spark будет использовать либо настройку "spark.default.parallelism" для RDD (Resilient Distributed Dataset),
либо "spark.sql.shuffle.partitions" для DataSet (набор данных). 
Сколько задач будет выполняться параллельно каждой управляющей программе, 
будет зависеть от свойства "spark.executor.cores". 
Если это значение установить больше без учета памяти, т
о программы могут отказать  и привести к ситуации OOM (недостаточно памяти)

OutOfMemory may be beause of driver settings:

rdd.collect()

sparkContext.broadcast 

Низкий уровень памяти драйвера, настроенный в соответствии с требованиями приложения

Неправильная настройка Spark.sql.autoBroadcastJoinThreshold - try to reduce it

Код, написанный с помощью Spark SQL⁵, выполняется не так, как код, написанный с использованием RDD. 
Когда запускается действие, Spark генерирует код, который сворачивает несколько трансформаций данных в одну функцию. 
Этот процесс называется формированием кода всего этапа (Whole-Stage Code Generation)⁶. 
Spark пытается воспроизвести процесс написания специального кода для конкретной задачи,
в котором не используются вызовы виртуальных функций. 

```

### toDebug and explain()

https://medium.com/@chitrarth236/spark-dataframe-api-part-1-fundamentals-41dd51e46714

By default, explain with no argument will display the physical plan

explain(mode=”simple”) displays the physical plan
explain(mode=”extended”) displays physical and various logical plans
explain(mode=”cost”) displays the optimized logical plan and related statistics
explain(mode=”formatted”) displays a split output composed of a physical plan outline and a section with each node’s details
explain(mode=”codegen”) displays the java code to be executed

  How to  determine whether a function causes a shuffle or not without the help of documentation?
For any function, just create an RDD and call toDebugString, for example:

```
 val a = sc.parallelize(Array(1,2,3)).distinct
 a.toDebugString
 
MappedRDD[5] at distinct at <console>:12 (1 partitions)
 MapPartitionsRDD[4] at distinct at <console>:12 (1 partitions)
**ShuffledRDD[3] at distinct at <console>:12 (1 partitions)**
  MapPartitionsRDD[2] at distinct at <console>:12 (1 partitions)
    MappedRDD[1] at distinct at <console>:12 (1 partitions)
       MappedRDD[1] at distinct at <console>:12 (1 partitions)
``` 
As you can see distinct creates a shuffle. I
t is also particularly important to find out this way rather than docs because 
there are situations where a shuffle will be required or not required for a certain function. 

For example, join usually requires a shuffle 
but if you join two RDDs that branch from the same RDD spark can sometimes elide the shuffle.



### Spark Web UI
https://spark.apache.org/docs/latest/web-ui.html

https://habr.com/ru/company/otus/blog/526892/

https://medium.com/swlh/spark-ui-to-debug-queries-3ba43279efee

https://habr.com/ru/company/otus/blog/526892/

http://spark.apache.org/docs/latest/web-ui.html

https://sparkbyexamples.com/spark/spark-web-ui-understanding/

### Adaptive query execution (AQE)  Spark >= 3.0

```
AQE increases and decreases partitions by dynamically coalescing or splitting the partitions.

spark.sql.adaptive.enabled true
spark.sql.adaptive.skewJoin.enabled true
spark.sql.adaptive.coalescePartitions.enabled true
spark.sql.adaptive.advisoryPartitionSizeInBytes 134217728
spark.sql.adaptive.skewJoin.skewedPartitionFactor
spark.sql.adaptive.skewJoin.skewedPartitionThresholdInBytes
spark.sql.adaptive.advisoryPartitionSizeInBytes
Note: Caching the DataFrame just before writing disables AQE for the transformations that occur in our DataFrame before calling cache().
```
https://habr.com/ru/company/cloudera/blog/560246/

Spark определяет подходящее количество партиций для первого этапа, но для второго этапа использует по умолчанию "магическое число" - 200.

И это плохо по трем причинам:

1. 200 вряд ли будет идеальным количеством партиций, а именно их количество является одним из критических факторов, влияющих на производительность;

2. Если вы запишете результат этого второго этапа на диск, у вас может получиться 200 маленьких файлов;

spark.conf.set(“spark.sql.shuffle.partitions”,”2″)

https://sparkbyexamples.com/spark/spark-adaptive-query-execution/



Когда оба: 
```
 spark.sql.adaptive.enabled и
 spark.sql.adaptive.coalescePartitions.enabled 
```
установлены на true, Spark объединит смежные перемешанные разделы в соответствии с целевым размером, указанным в spark.sql.adaptive.advisoryPartitionSizeInBytes.
Это делается, чтобы избежать слишком большого количества мелких задач.

вам необходимо предоставить AQE свое определение перекоса.

Это включает в себя два параметра:

1.   spark.sql.adaptive.skewJoin.skewedPartitionFactor является относительным: партиция считается с пересом, если ее размер больше, чем этот коэффициент, умноженный на средний размер партиции, а также, если он больше, чем

2.   spark.sql.adaptive.skewedPartitionThresholdInBytes, который является абсолютным: это порог, ниже которого перекос будет игнорироваться.
    
### Structured Streaming

https://habr.com/ru/company/neoflex/blog/674944/ PySpark Structured Streaming и Kafka

https://habr.com/ru/company/neoflex/blog/686242/ PySpark + Kafka

https://databricks.com/blog/2017/01/19/real-time-streaming-etl-structured-streaming-apache-spark-2-1.html

https://habr.com/ru/company/otus/blog/670266/

https://habr.com/ru/company/ozontech/blog/656883/

https://habr.com/ru/company/otus/blog/557812/
Когда данные передаются в тему Kafka, они автоматически распределяются между разделами согласно ключу, который вы определили в сообщении Kafka. 

Каждое сообщение добавляется в тему Kafka с определенным смещением или с идентификатором, указывающим его позицию в разделе. 

Если в качестве ключа задать null, то сообщение будет автоматически равномерно распределяться между разделами.


```
 kafka-topics 
 --zookeeper <host>:2181 
 --create 
 --topic <topic-name> 
 --partitions <number-of-partitions> 
 --replication-factor <number-of-replicas>
```
https://livebook.manning.com/book/streaming-data/ Book (I bought it)

```
val sparkConf = new SparkConf().setAppName("DirectKafkaWordCount")
val ssc = new StreamingContext(sparkConf, Seconds(2))

// Create direct kafka stream with brokers and topics
val topicsSet = topics.split(",").toSet
val kafkaParams = Map[String, Object](
  ConsumerConfig.BOOTSTRAP_SERVERS_CONFIG -> brokers,
  ConsumerConfig.GROUP_ID_CONFIG -> groupId,
  ConsumerConfig.KEY_DESERIALIZER_CLASS_CONFIG -> classOf[StringDeserializer],
  ConsumerConfig.VALUE_DESERIALIZER_CLASS_CONFIG -> classOf[StringDeserializer])
val messages = KafkaUtils.createDirectStream[String, String](
  ssc,
  LocationStrategies.PreferConsistent,
  ConsumerStrategies.Subscribe[String, String]
  (topicsSet, kafkaParams))

// Get the lines, split them into words, count the words and print
val lines = messages.map(_.value)
val words = lines.flatMap(_.split(" "))
val wordCounts = words.map(x => (x, 1L)).reduceByKey(_ + _)
wordCounts.print()

// Start the computation
ssc.start()
ssc.awaitTermination()
```

https://spark.apache.org/docs/latest/structured-streaming-programming-guide.html

https://habr.com/ru/company/rambler_and_co/blog/569932/



### Spark Streaming

will be delays between event time and processing time due to how data is ingested and whether the overall application experiences issues like downtime.

#### Stateless transformation 
```
Each batch doing its own processing independently of anything that occurred prior to this batch. 
Example: HTTP protocol, REST API

There are stateless operations, such as filter(), map(), and flatMap(), which do not keep data around (do not maintain state) while moving from processing from one stream element to the next. 

And there are stateful operations, such as distinct(), limit(), sorted(), reduce(), and collect(), which may pass the state from previously processed elements to the processing of the next element.
```
#### Stateful transformations
 the processing of each micro-batch of data depends on the previous batches of data either fully or partially.
 Stateful stream processing means a “State” is shared between events(stream entities).
 And therefore past events can influence the way the current events are processe
 
In Kafka, there are two kinds of operations, stateless and stateful. When a stateless operation is made on a Kafka message, it can be done totally independently from any other message processing. This makes the operations quick and light-weight. 
 
https://habr.com/ru/company/ru_mts/blog/685492/

https://habr.com/ru/post/451160/
```
В потоковом пайплайне важно понимать разделение операций на stateless и stateful.

инструменты Spark Structured Streaming для stateful-операций. Рассмотрим здесь три из них:

1. Event time - время, в которое событие произошло. 
2. Watermark;
3. окно в join condition
```
### Watermark
```
– это то время, после которого все события потока должны храниться в стейте и которое обновляется в конце обработки каждого микробатча. Watermark позволяет ограничить количество хранимых событий.

watermark  allow Spark to understand when to close the aggregate window and produce the correct aggregate result.


sensorStreamDF = spark \
  .readStream \
  .format("kafka") \
  .option("kafka.bootstrap.servers", "host1:port1,host2:port2") \
  .option("subscribe", "tempAndPressureReadings") \
  .load()

sensorStreamDF = sensorStreamDF \
.withWatermark("eventTimestamp", "10 minutes") \
.groupBy(window(sensorStreamDF.eventTimestamp, "10 minutes")) \
.avg(sensorStreamDF.temperature,
     sensorStreamDF.pressure)

sensorStreamDF.writeStream
  .format("delta")
  .outputMode("append")
  .option("checkpointLocation", "/delta/events/_checkpoints/temp_pressure_job/")
  .start("/delta/temperatureAndPressureAverages")
  
Вычисляется Watermark так:
a) берём максимальное (минимальное или среднее, есть вариации) время события в стейте (Event time);
b) вычитаем watermarkDelay – некоторое значение типа timedelta, которое мы задали в коде.
Теперь стейт не будет разрастаться, потому что старые события будут удаляться автоматически.

Kafka timestamp очень ненадёжный: в половине случаев приходил нулевой Event time

мы хотим установить правило: все интересующие нас события на клиенте происходят в течение N минут после ответа сервиса. 
Чтобы поиск шёл не по всему стейту, а только по определённому временному окну вокруг события, 
достаточно указать ограничения на Event time обоих потоков относительно друг друга в условии джойна.

Так будет выглядеть условие для простого джойна:

s1 = input_stream1.alias("s1")
s2 = input_stream2.alias("s2")

s1.join(
s2, on="""
s1.word=s2.word
and s1.event_time <= s2.event_time + interval '5 seconds'
and s1.event_time >= s2.event_time - interval '30 seconds'
""")

 Классический вариант решения проблемы skew (скоса) – добавить в NULL-ключи соль для более равномерного распределения – оказался не лучшим вариантом. 
 Мы нашли более эффективный способ: выделили все события с NULL-ключами в отдельный поток и стали писать его в базу без джойна.

```


### Stage , Job , Task

https://www.youtube.com/watch?v=1BaGOCPA7OA

https://www.youtube.com/watch?v=P1knn8i1Ijs

Action creates Job  (1:1) (collection of stages) ;  stage is collection of tasks; task is running on 1 partition / core

```
В Spark обработка блоков от одной перетасовки (Shuffle) до другой называется этапом (Stage). 
 
A job will then be decomposed into single or multiple stages; 
stages are further divided into individual tasks;
and tasks are units of execution that the Spark driver's scheduler ships to Spark Executors on the Spark worker nodes to execute in your cluster.

A Spark stage is a smaller sets of tasks that depend on each other.
Stages are created for each job based on shuffle boundaries, i.e. what operations can be performed serially or in parallel
```
  - physical unit of execution
  - step in physical execution plan
  - collection of task - one task per partition
  - job is collection of stages
  
  There are 2 types of stages:
  
    - ShuffleMapstage (map)
    - ResultStage. (reduce)


https://habr.com/ru/company/neoflex/blog/578654/
```
viDF = spark.read.parquet("/tst/vi/")
viDF.createOrReplaceTempView("ViewingInterval")
spark.sql("""select t.*, 
                    explode(get_list_of_seconds(duatation)) as secondNumber 
               from ViewingInterval""")
  
Let do repartition (shuffle) to use many core

viDF = spark.read.parquet("/tst/vi/")
viDF.repartition(60).createOrReplaceTempView("ViewingInterval")
spark.sql("""select t.*, 
                    explode(get_list_of_seconds(duatation)) as secondNumber 
               from ViewingInterval""")  
```

YARN app master

##  EXECUTOR Tuning

https://www.youtube.com/watch?v=sHqzmqppKXE&list=PLtfmIPhU2DkNjQjL08kR3cd4kUzWqS0vg&index=5 


#### Approach 1 - one executor per CORE is NOT good because
```
- it does not take advantage of running multiple tasks on same JVM
- shared/cached variables like broadcast vars and accumulators will be replicated in each core of the nodes 
- it does not leave enough memory overhead for hadoop/yarn daemon process and ApplicationManager and OS 
```

#### Approach 2 - one executor per NODE  (fat executor) :
```
num-executors = one executor per noder
  total # of executors = total nodes in cluster = 10
  
executor-cores =  all cores per node (16) are assigned to one executor 
executor-memory = Total memory in cluster / total executors = 640GB/10 = 64GB

It is not good because HDFS throughput will hurt and it will result in excessive garbage result
```
#### Approach 3 - in beetween 1 and 2:
```
5 cores per executor
executor-cores=5  for good HDFS throughtput
Leave 1 core per node for Haddop/Yarn daemons and OS
num cores available per node = 16-1=15
Total available of cores in cluster =15*10=150

Number of executors = total cores / num_cores_per_executor = 150/5 =30
Leaving 1 executor for ApplicationManager  num-executors=29

```

### Skewed RDD 

mean, median and the mode are not equel (they are equal for notmal ditribution)

The mode is the number that is repeated more often than any other, so 13 is the mode.

https://www.youtube.com/watch?v=HIlfO1pGo0w

```
Solutions:

1. Repartitions. spark.sql.shuffle.partitions
2. Salting (add random siffix to key)
3. Isolated sulting
4. Isolated Map join
5. Iterative broadcust Join
```

add salt to join key

https://habr.com/ru/company/otus/blog/541426/

https://towardsdatascience.com/skewed-data-in-spark-add-salt-to-compensate-16d44404088b

```
val salted_fact_df = spark.sql
( 
"select " + 
"concan(key,'_', FLOOR(RAND(123456)*19))" 
+ as SALTED_KEY, val FROM original_fact_table"
)
salted_fact_df.createOrReplaceGlobalTempView(fat_table_salted)


we could salt on the key to distributing data evenly, but that changed my join 
key. How do you join back to the original key after salting?


df_left = df_skew.withColumn(“salt”, (rand() * spark.conf.get(“spark.sql.shuffle.partitions”)).cast(“int”))

```

### Off heap 
```
 Spark могут хранить информацию вне кучи (off-heap). Вы можете включить off-heap накопитель, используя команды

-conf spark.memory.offHeap.enabled = true

-conf spark.memory.offHeap.size = Xgb.
Будьте осторожны при использовании хранилища вне кучи (off-heap), т.к. это не повлияет на размер памяти самой кучи (on-heap),
т.е. не уменьшает ее объем. Поэтому, чтобы определить общий лимит памяти, задайте меньший размер кучи.
```



### Pair RDD
allow to access each key in parallel

countByKey()
collectAsMap()
lookup(key)

reduceByKey()
join()


### Bucketing
```
create table a(id int, info STRING)
clustered by(id)
sorted by (id)
INTO 8 buckets



spark.range(10e4.toLong)
.write
.bucketBy(4,"id")
.sortBy("id")
.mode(SaveMode.Overwrite)
saveAsTable("bucketed_4_10e4")


spark.range(10e6.toLong)
.write
.bucketBy(4,"id")
.sortBy("id")
.mode(SaveMode.Overwrite)
saveAsTable("bucketed_4_10e6")

val b1= spark.table("bucketed_4_10e4")
val b2= spark.table("bucketed_4_10e6")

display(b1.join(b2, "id"))
no shuffling durning the join (SortMergeJoin)

```


### Dataframe vs Dataset vs RDD

RDD has map(), filter() , reduce()

convert from a DataFrame to an RDD via its rdd method: df.rdd is RDD[Row] 
convert from an RDD to a DataFrame (if the RDD is in a tabular format) 
via the toDF() method

val sampleRDD = sqlContext.jsonFile("hdfs://localhost:9000/jsondata.json")

val sample_DF = sampleRDD.toDF()

DataFrame: named columns, uses a catalyst optimizer , weakly typed

df.filter("age > 21");

Because the code above is referring to data attributes by name, it is not possible for the compiler to catch any errors. If attribute names are incorrect then the error will only detected at runtime, when the query plan is created.


In following code: people("deptId"), 
you're not getting back an Int, or a Long, you're getting back a Column object 
```
val people = sqlContext.read.parquet("...")
val department = sqlContext.read.parquet("...")

people.filter("age > 30")
  .join(department, people("deptId") === department("id"))
  .groupBy(department("name"), "gender")
  .agg(avg(people("salary")), max(people("age")))
```

On the contrary, DataSet[T] is typed

val people: People = val people = sqlContext.read.parquet("...").as[People]


```
spark.createDataFrame(
    [
        (1, 'Lakshay'),  
        (2, 'Aniruddha'),
        (100, 'Siddhart')
    ],
    ['id', 'Name'] #   columns labels here
)
```
#### Datasets is an extension of Dataframes API with the benefits of both RDDs and the Datasets. 

dataset.filter(_.age < 21);


It is fast as well as provides a type-safe interface - synax and semantic aeero during compilation
#### encoders

Dataset API has the concept of encoders which translate between JVM representations (objects) and Spark’s internal binary format. Spark has built-in encoders which are very advanced in that they generate byte code to interact with off-heap data and provide on-demand access to individual attributes without having to de-serialize an entire object


Aggregation is faster in DataFrames.

https://www.youtube.com/watch?v=xuXOiD3drps

https://www.youtube.com/watch?v=Ofk7G3GD9jk

 
### To use RDD in SparkSQL create view from RDD

myRDD.createOrReplaceTempView(viewName = "my_view_name")
spark.sqlContext.sql("SELECT ...")
.write
.option("header",true)
.csv(path="./../a.txt")

### Avoid groupBy

```
Example: word count with reduceBy:
-----------------
val words= Array("aa", "bb", "cc", "cc", "cc")
val wordsPairsRDD=sc.parallelize(words).map(word => (word,1))
val  result    =  wordsPairsRDD
   .reduceByKey(_+_)
   .collect()

println(result)
Answer:  Array (("aa",1), ("bb",1), ("cc",3))

Let do the same as above using groupBy:
----------------------------------------

val  result    =  wordsPairsRDD
   .groupByKey()
   .map(t => (t._1, t._2.sum))
   .collect()
```


### HashPartitioner  and RangePartitioner

RDD keys should be hashable  

RDD partition number is key.hashCode % number of partitions

DataSet use MurMurHash3

PySpark use portable_hash

Multiple keys can be assigned to the same partition

number of elements per partition
```
import org.apache.spark.rdd.RDD

val rdd=sc.paralelize(
     for {
         x <- 1 to 3
         y <- 1 to 2
     } yield (x,None), 8)
     
rdd.collect.foreach(println))
(1,None)
(1,None)
(2,None)
(2,None)
(3,None)
(3,None)

def countByPartition(rdd: RDD[(Int, None.Type)]) = {
  rdd.mapPartitions(iter => Iterator(iter.length))
}

countByPartition(rdd).collect()
 result number of elements per partition: 
 Array[Int] = Array (0,1,1,1,0,1,1,1)


 Let repartition dataset based using HashPartitioner
 
 import org.apache.spark.HashPartitioner
 val rddOne=rdd.partitionBy(new HashPrtitioner(1))

```
### Map MapPartition MapPartitionWithIndex transformations

https://www.youtube.com/watch?v=UMEnrYf8LPQ

https://www.youtube.com/watch?v=TtfUUvFoKYw

#### map() 
```
works on a single Row at a time
returns after each input row
does not hold the output result in memory
```
#### mapPartitions() 
```
works on a partition at a time
returns after processing all rows in partition
output is retained in memory

can be used as alternative to map() and foreach() - can be called for each patition while map() and foreach() os called for each element in RDD
```
#### mapPartitionsWithIndex() 
```
works on a partition at a time along with retaining the index of partitions
returns after processing all rows in partition
output is retained in memory

val dfList = (1 to 100) toList
val df = dfList.toDF().map(x => x.getInt(0))
val.df1.repartition(4).rdd.mapPartitionsWithIndex( (index,itr) => Iterator (index, itr.length))).toDF("index", "psize").show()
```


### Performance: partition pruning , predicate pushdown 

https://medium.com/swlh/troubleshooting-stragglers-in-your-spark-application-47f2568663ec

https://www.youtube.com/watch?v=PJvpseiPACQ

https://www.youtube.com/watch?v=_Ne27JcLnEc

### Logical vs Physical Plan
```
park Internals have 4 kinds of Query Plans. Lets discuss about them in detail below:

Parsed Logical Plan (Unresolved): This plan parses the query to check the correctness of the query syntax. It will throw a ParseException if there are any syntax errors.
Why is this plan unresolved?
Parsed logical plan only checks for the correctness of syntax and cannot identify if the entities like table name / column name used in the query exists or not. Therefore, it is unresolved.
Analyzed Logical plan (Resolved): This plan analyses if all the entities like table names, column names, views, etc. used in the query exists or not. It will throw an AnalysisException if for instance a table with the name mentioned in the query doesn’t exist. After checking for the syntax correctness in the Parsed Logical Plan, the system then checks for any analysis exception by cross-checking with the Catalog leading to a Resolved Logical Plan. Hence this is a resolved plan.
Optimized Logical Plan (Catalyst Optimizer): In this plan certain sets of predefined rules by the help of catalyst optimizer are used to optimize the query execution plan at the early stages.
Example:
a) Predicate Pushdown : In this case the filters are pushed down or applied at the very early stages. This ensures that operations are performed on only relevant data.
b) Combining multiple projections (select columns) into a single projection.
c) Combining multiple filters into a single operation.
Physical Plan: This plan is used to identify / decide what kind of joins or aggregations strategies can be chosen for optimal query performance.
Example :
a) Whether to use Hash Aggregate or Sort Aggregate
b) Which type of Join to be used — Broadcast Hash Join | Sort-Merge Join | Shuffle-Hash Join.

```
### Cost and rule based optimizer

https://habr.com/ru/company/neoflex/blog/417103/
```
 два вида оптимизаторов запросов:


Оптимизаторы, основанные на фиксированных правилах (Rule-based optimizator, RBO).
Оптимизаторы, основанные на оценке стоимости выполнения запроса (Cost-based optimizator, CBO).

Первые заточены на применении набора фиксированных правил, например, применение условий фильтраций из where на более ранних этапах, если это возможно, предвычисление констант и т.д.

CBO оптимизатор для оценки качества полученного плана используют стоимостную функцию, которая обычно зависит от объема обрабатываемых данных, количества строк, попадающих под фильтры, стоимости выполнения тех или иных операций.

Ознакомиться детально с дизайн-спецификацией на CBO для Apache Spark можно по ссылкам: спецификация и основная JIRA задача для реализации.

Отправной точкой для изучения полного набора существующих оптимизаций может послужить код Optimizer.scala.

Вот небольшая выдержка из длинного списка доступных оптимизаций:

def batches: Seq[Batch] = {
  val operatorOptimizationRuleSet =
    Seq(
      // Operator push down
      PushProjectionThroughUnion,
      ReorderJoin,
      EliminateOuterJoin,
      PushPredicateThroughJoin,
      PushDownPredicate,
      LimitPushDown,
      ColumnPruning,
      InferFiltersFromConstraints,
      // Operator combine
      CollapseRepartition,
      CollapseProject,
      CollapseWindow,
      CombineFilters,
      CombineLimits,
      CombineUnions,
      // Constant folding and strength reduction
      NullPropagation,
      ConstantPropagation,
........

Следует отметить, что список данных оптимизаций включает в себя как оптимизации, основанные на правилах, так и оптимизации, основанные на оценки стоимости запроса, о которых будет сказано ниже.

Особенностью CBO является то, что для корректной работы ему необходимо знать и хранить информацию по статистике данных, используемых в запросе — количество записей, размер записи, гистограммы распределения данных в столбцах таблиц.

Для сбора статистики используется набор SQL команд ANALYZE TABLE… COMPUTE STATISTICS, кроме того, необходим набор таблиц для хранения информации, API предоставляется через ExternalCatalog, точнее через HiveExternalCatalog.

Так как в настоящий момент CBO по умолчанию отключен, то основной упор будет сделан на исследовании доступных оптимизация и нюансов RBO.
```
https://www.youtube.com/watch?v=E26fK8kgXaU

### Join types: 

https://towardsdatascience.com/demystifying-joins-in-apache-spark-38589701a88e

https://habr.com/ru/company/otus/blog/556722/
```
1. Перемешанный хеш (Shuffle Hash Join)
2. Широковещательный хеш (Broadcast Hash Join)
3. Сортировка через слияние (Sort Merge Join)
4. Dекартов джойн (Cartesian Join)
5. Широковещательный джойн вложенного цикла (Broadcast Nested Loop Join)
```



### Join without shuffle


if 2 RDDs are co-located (in the same partition) then no need for shiffle

if 2 rdds have the same partitioner 
where shuffled as part of the same action

smallDF
LargeDF
10MB - default size for broadcust

https://www.youtube.com/watch?v=isOuTH_49pY

#### shuffle hash join 
```
 useful where any partition of the build side could be fit into memory
 ome  table is mutch smaller then  the other one, then cost to build a hash table on a smaller table is less than sorting the larger table

 only when spark.sql.join.preferSortMergeJoin=false
 and the cost to build the hash table is less then sorting the data
 
 but keep in mind - sort merge join is preferred over Shuffle Hash Join 

  step 1 - shuffle phase: data in both tables are re-partitioned by the  join key so they can be colocated
  step 2 - single node hash join 
```
#### sort join is the default strategy

```
step 1 - shuffle  phase: data in both tables are re-partitioned by the  join key so they can be colocated
step 2 - sort phase data sorted within each partition parallely
step 3 - merge phase: join 2 sorted and partitioned data

если  размер достаточно большой, то будет выбран SortMergeJoin. 
Чтобы выполнить этот вид соединения, Spark должен сделать так, чтобы одинаковые ключи из основного набора данных и из дельты расположились совместно (в партициях RDD с одинаковыми индексами) и были отсортированы в пределах партиций. 
Записи можно только перераспределить и отсортировать заново, затратив на это время и ресурсы. 

Производится Shuffle: записи каждого набора перемешиваются по значению хешей. 
Перемешивание устраняет любую сортировку, которая сохранилась при чтении, теперь порядок записей никак не зависит от первоначального.

SortMergeJoin делает своё дело, полученный набор данных сохраняет тот же порядок записей, что был после Shuffle и локальной сортировки.

```


#### broadcast join (spark.sql.autoBroadcastJoinThreshold=10485760  = 10MB by default)

spark.sql.autoBroadcastJoinThreshold = -1 to disable broadcast
join just lookup on local node
hash join on each executor
no shufffling envolved

https://www.youtube.com/watch?v=_q-MOcfS0Ls  join dataframes

--driver-memory(1G)

--executor-memory (1G)

Spark standalone and YARN only:
  --executor-cores NUM        Number of cores per executor. (Default: 1 in YARN mode,
                              or all available cores on the worker in standalone mode)


YARN:
--num-executors(2)

Spark standalone and Mesos only:
  --total-executor-cores NUM  Total cores for all executors.


 Cluster deploy mode only:
  --driver-cores NUM          Number of cores used by the driver, only in cluster mode
                              (Default: 1).


How to get # of partitions:
myRDD.partitions.size
myRDD.getPartitions()

### map vs flatMap

map is 1:1 transform
flatMap may return 0,1, or many elements

val data = spark.read.textFile("a.txt").rdd
val res=data.flatMap(line=>line.split(" "))

### Coalesce vs repartition

coalesce only can decrease # of partitions and it reuse the existing partitions to mimimize shuffling
but it will lead to unequal sized partitions

repartition - full shuffle to evenly distribute data

### Transformation are functions implemented on RDD reulting in another RDD
Basic Transformations are - map and filter. After the transformation, the resultant RDD is always different from its parent RDD.
It can be smaller (e.g. filter, count, distinct, sample), bigger (e.g. flatMap(), union(), Cartesian()) or the same size (e.g. map).

### Wide vs narrow tranformations

https://blog.devgenius.io/unleashing-the-power-of-apache-spark-narrow-and-wide-transformations-in-action-4c2483480c4a 

#### Narrow dependency : 
RDD operations like map(), union(), filter() can operate on a single partition and map the data of that partition to the resulting single partition. These kinds of operations that map data from one to one partition are referred to as Narrow operations. 

Narrow operations don’t require distributing the data across the partitions. Each partition of the parent RDD is used by at most one partition of the child RDD.

#### Wide dependency : 
RDD operations like groupByKey, distinct, join may require mapping the data across the partitions in the new RDD. These kinds of operations which maps data from one to many partitions are referred to as Wide operations Each partition of the parent RDD may be depended on by multiple child partitions.


#### Stateless Transformations
Processing of the batch does not depend on the output of the previous batch.

Examples- map (), reduceByKey (), filter ().

#### Stateful Transformations
 Processing of the batch depends on the intermediary results of the previous batch.

Examples- Transformations that depend on sliding windows


### Shuffling

Triggered by wide transformations like

- Repartition
- ByKey operations (except counting)
- Joins, the worse being cross joins
- Sorting
- Distinct
- GroupBy


### Action
Actions are RDD operations that produce non-RDD values. They materialize a value in a Spark program. 

In other words, an RDD operation that returns a value of any type but RDD[T] is an action. They trigger the execution of RDD transformations to return values. Simply put, an action evaluates the RDD lineage graph.
Actions are one of two ways to send data from executors to the driver (the other being accumulators).
Some examples of actions are
- aggregate,
- collect,
- count,
- countApprox,
- countByValue,
- first,
- fold,
- foreach,
- foreachPartition,
- max,
- min,
- reduce,
- saveAs* : saveAsTextFile, saveAsHadoopFile,
- show
- take, takeOrdered, takeSample,
- toLocalIterator,
- top,
- treeAggregate,
- treeReduce

### Driver
The driver process runs your main() function, sits on a node in the cluster, and is responsible for three things: maintaining information about the Spark Application; responding to a user’s program or input; and analyzing, distributing, and scheduling work across the executors (defined momentarily).

### Task
A task is a unit of work that can be run on a partition of a distributed dataset and gets executed on a single executor. The unit of parallel execution is at the task level. All the tasks within a single stage can be executed in parallel.

### Stage
A stage is a collection of tasks that can run in parallel. A new stage is created when there is data shuffling.

### Persistance
difference between persist() and cache()?
persist() allows the user to specify the storage level whereas cache() uses the default storage level.

cache() = persist(StorageLeVel.MEMORY_ONLY)

Apache Spark automatically persists the intermediary data from various shuffle operations, however, it is often suggested that users call persist () method on the RDD in case they plan to reuse it. Spark has various persistence levels to store the RDDs on disk or in memory or as a combination of both with different replication levels.
The various storage/persistence levels in Spark are:

MEMORY_ONLY - stores RDD as DEserialized Java object

MEMORY_ONLY_SER as SERIALIZED (smaller memory size)

MEMORY_AND_DISK  stores RDD as deserialized Java object and dist

MEMORY_AND_DISK_SER. as SERIALIZED (smaller memory size)

DISK_ONLY

OFF_HEAP


```
import scala.util._
import org.apache.spark.sql.functions._

val df1=Seq.fill(50, Random.nextInt).toDF("C1")
val df2=df1.withColumn(("C2", rand()).join(df1,"C1").persist(StorageLevel.DISK_ONLY)
val df3=df1.withColumn(("C3", rand()).join(df2,"C2").cache()
val df4=df1.withColumn(("C4", rand()).join(df2,"C3").cache()
val df5=df1.withColumn(("C5", rand()).join(df2,"C4").cache()
val df6=df1.withColumn(("C6", rand()).join(df2,"C5").cache()

display(df6)
```

#### checkpointing
Lineage graphs are always useful to recover RDDs from failure but this is generally time-consuming if the RDDs have long lineage chains. Spark has an API for checkpointing i.e. a REPLICATE flag to persist. However, the decision on which data to the checkpoint - is decided by the user. Checkpoints are useful when the lineage graphs are long and have wide dependencies.

### Executors
https://stackoverflow.com/questions/32621990/what-are-workers-executors-cores-in-spark-standalone-cluster

An executor is a single JVM process that is launched for an application on a worker node. 
Executor runs tasks and keeps data in memory or disk storage across them. Each application has its own executors. 
A single node can run multiple executors and executors for an application can span multiple worker nodes. 
An executor stays up for the duration of the Spark Application and runs the tasks in multiple threads. 
The number of executors for a spark application can be specified inside the SparkConf or via the flag –num-executors from the command line.
Executor performs all the data processing.
Reads from and writes data to external sources.
Executor stores the computed data in-memory, cache or on hard disk drives.
Interacts with the storage systems.

One Executor per node is considered to be more stable than two or three executors per node as is used in systems like YARN.
Try to group-wide transformations together for best automatic optimization


### Minimizing data transfers and avoiding shuffling
  The various ways in which data transfers can be minimized when working with Apache Spark are:
- Using Broadcast Variable- Broadcast variable (readonly, in cache on every machine) no need to copy to every task; enhances the efficiency of joins between small and large RDDs.
- Using Accumulators – Accumulators help update the values of variables in parallel while executing.
- The most common way is to avoid operations ByKey, repartition or any other operations which trigger shuffles.


### Performance tuning
  data serialization
  memory tuning
  tuning data structure
  serriaized rdd storage
  garbage collection tuning
  level of parallelism
  broadcast large variable
  data locality

https://pub.towardsai.net/how-you-should-save-the-output-of-your-spark-etl-jobs-if-you-are-not-writing-to-a-database-c95a113eef1 

https://pub.towardsai.net/a-practical-tip-when-working-with-random-samples-on-spark-23f6dbbe722b 

```
rdd.toDebugString
rdd.selectExpr("count(DISTINCT y ) AS uniq_x")


spark.range(1000).filter("id > 100").selectExpr("sum(id)").explain()

== Physical Plan ==
*Aggregate(functions=[sum(id#201L)])
+- Exchange SinglePartition, None
   +- *Aggregate(functions=[sum(id#201L)])
      +- *Filter (id#201L > 100)
         +- *Range 0, 1, 3, 1000, [id#201L]

```

### Stage
https://towardsdatascience.com/unraveling-the-staged-execution-in-apache-spark-eff98c4cdac9

 https://medium.com/data-arena/merging-different-schemas-in-apache-spark-2a9caca2c5ce
 
```
spark-submit \
    --master k8s://https://$(minikube ip):8443 \
    --deploy-mode cluster \
    --name spark-pi \
    --class org.apache.spark.examples.SparkPi \
    --conf spark.executor.instances=2 \
    --conf spark.kubernetes.authenticate.driver.serviceAccountName=spark-sa \
    --conf spark.kubernetes.container.image=localhost:5000/spark-local \
    local:///opt/spark/examples/jars/spark-examples_2.12-3.1.1.jar
 ```  
 

https://medium.com/technexthere/how-does-spark-joining-strategy-working-c826954e2611

https://medium.com/@adrianchang/apache-spark-checkpointing-ebd2ec065371

### Spark Transformations Explained with use cases | Apache Spark FAQs

Part-1: https://youtu.be/0eUWFN0vciA
Part-2: https://youtu.be/N4rdGx4jsO4
Part-3: https://youtu.be/ECIXh1fOpks

https://www.youtube.com/watch?v=iLpjNItogwc. Apache Spark Memory Management 

#### Apache Spark Series A-Z

https://www.youtube.com/watch?v=FKWarVIffvU&list=PLHoQFin5tpu_JfE_k-tvVjeja9RXvBIdm Apache Spark Series A-Z

https://www.youtube.com/watch?v=s6hxAj9MCL4 Closure and Accumulators in Apache spark

https://www.youtube.com/watch?v=ebbx83jPbmQ Shuffle in Spark | Session-10 | Apache Spark Series from A-Z

https://www.youtube.com/watch?v=n9ejUp7yDhY Interoperating RDDs, Dataframe, Datasets | Session-13

https://www.youtube.com/watch?v=4dWHu-3nosE  Spark Streaming Log files in a Directory | Session-15

https://www.youtube.com/watch?v=lyn0MyZdrc4  Aggregations on Streaming Data in Spark | Session-16

https://www.youtube.com/watch?v=eb3QJVATebI Spark Structured Streaming & Output Sinks | Session-17

https://mungingdata.com/category/apache-spark/

https://medium.com/technexthere/how-to-size-spark-application-ff2a9d487926

https://medium.com/@adrianchang/apache-spark-partitioning-e9faab369d14

https://www.slideshare.net/databricks/fine-tuning-and-enhancing-performance-of-apache-spark-jobs

https://www.youtube.com/channel/UCoVVyUViJ3mfaEKVjAJSnVA



https://mungingdata.com/apache-spark/best-books/

https://www.kdnuggets.com/2021/09/data-analysis-scala.html  Mutual Information


https://www.youtube.com/watch?v=UywbytK_6Dg  Scala Coding best practices

https://www.youtube.com/watch?v=bamfHaxA4EQ interview

 



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


### Installing Spark 2 on Mac

https://medium.com/@le.oasis/setting-up-apache-spark-on-macos-a-comprehensive-guide-78af7642deb1

https://notadatascientist.com/running-apache-spark-and-s3-locally/

https://notadatascientist.com/install-spark-on-macos/
```
brew install scala@2.11
export SPARK_HOME=/usr/local/Cellar/apache-spark/2.4.5/libexec           
export PATH="$SPARK_HOME/bin/:$PATH"
chmod +x /usr/local/Cellar/apache-spark/2.4.5/libexec/bin/*
```



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

### Spark 3
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

https://sbakiu.medium.com/docker-best-practices-in-apache-spark-application-deployments-c013ad5aab9e

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

