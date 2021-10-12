https://livebook.manning.com/book/streaming-data/ Book (I bought it)

https://livevideo.manning.com/module/22_1_3/spark-in-motion/an-introduction-to-apache-spark/functional-programming-using-the-spark-shell?


Code for the Spark in Action Book: https://github.com/databricks/LearningSparkV2

There are 8 workers and both the workers and driver are m4.xlarge instances (16.0 GB, 4 Cores).

https://www.youtube.com/watch?v=G4D4iY_hZQ0&list=PLtfmIPhU2DkNjQjL08kR3cd4kUzWqS0vg


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

YARN app master

https://www.youtube.com/watch?v=sHqzmqppKXE&list=PLtfmIPhU2DkNjQjL08kR3cd4kUzWqS0vg&index=5  EXECUTOR Tuning


Approach 1 - one executor per core is is NOT good because
```
- it does not take advantage of running multiple tasks on same JVM
- shared/cached variables like broadcast vars and accumulators will be replicated in each core of the nodes 
- it does not leave enough memory overhead for hadoop/yarn daemon process and ApplicationManager and OS 
```

Approach 2 - one executor per node  (fat executor :
```
num-executors = one executor per noder
  total # of executors = total nodes in cluster = 10
  
executor-cores =  all cores per node (16) are assigned to one executor 
executor-memory = Total memory in cluster / total executors = 640GB/10 = 64GB

It is not good because HDFS throughput will hurt and it will result in excessive garbage result
```
Approach 3 - in beetween 1 and 2:
```
5 cores per executor
executor-cores=5  for good HDFS throughtput
Leave 1 core per node for Haddop/Yarn daemons and OS
num cores available per node = 16-1=15
Total avail;able of cores in cluster =15*10=150

Number of executors = total cores / num_cores_per_executor = 150/5 =30
Leaving 1 executor for ApplicationManager  num-executors=29

```

### Skewed RDD 

mean, median and the mode are not equel (they are equal for notmal ditribution)

The mode is the number that is repeated more often than any other, so 13 is the mode.

https://www.youtube.com/watch?v=HIlfO1pGo0w

Solutions:

1. Repartitions. spark.sql.shuffle.partitions
2. Salting (add random siffix to key)
3. Isolated sulting
4. Isolated Map join
5. Iterative broadcust Join


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
### Map MapPartition MapPartitionWithIndex

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
  step 1 - shuffle phase data in both tables are partitioned by the 
join key so they can be colocated
  step 2 - single noe hash join 
```
#### sort join

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

mapPartitions() can be used as alternative to map() and foreach() - can be called for each patition while map() and foreach() os called for each element in RDD
mapPartitionsWithIndex() 

Narrow dependency : 
RDD operations like map(), union(), filter() can operate on a single partition and map the data of that partition to the resulting single partition. These kinds of operations that map data from one to one partition are referred to as Narrow operations. 

Narrow operations don’t require distributing the data across the partitions. Each partition of the parent RDD is used by at most one partition of the child RDD.

Wide dependency : 
RDD operations like groupByKey, distinct, join may require mapping the data across the partitions in the new RDD. These kinds of operations which maps data from one to many partitions are referred to as Wide operations Each partition of the parent RDD may be depended on by multiple child partitions.


Stateless Transformations- Processing of the batch does not depend on the output of the previous batch. Examples- map (), reduceByKey (), filter ().
Stateful Transformations- Processing of the batch depends on the intermediary results of the previous batch. Examples- Transformations that depend on sliding windows

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
Some examples of actions are - aggregate, collect, count, countApprox, countByValue, first, fold, foreach, foreachPartition, max, min, reduce, saveAs* actions, saveAsTextFile, saveAsHadoopFile, take, takeOrdered, takeSample, toLocalIterator, top, treeAggregate, treeReduce

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

rdd.toDebugString
rdd.selectExpr("count(DISTINCT y ) AS uniq_x")

Stage
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

https://habr.com/ru/company/X5Group/blog/579232/. PySpark

https://mungingdata.com/apache-spark/best-books/

https://www.kdnuggets.com/2021/09/data-analysis-scala.html  Mutual Information


https://www.youtube.com/watch?v=UywbytK_6Dg  Scala Coding best practices

https://www.youtube.com/watch?v=bamfHaxA4EQ interview


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


### Installing Spark 2 on Mac

https://notadatascientist.com/running-apache-spark-and-s3-locally/

https://notadatascientist.com/install-spark-on-macos/
```
brew install scala@2.11
export SPARK_HOME=/usr/local/Cellar/apache-spark/2.4.5/libexec           
export PATH="$SPARK_HOME/bin/:$PATH"
chmod +x /usr/local/Cellar/apache-spark/2.4.5/libexec/bin/*
```


https://medium.com/swlh/pyspark-on-macos-installation-and-use-31f84ca61400

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

