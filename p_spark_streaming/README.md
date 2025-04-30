https://www.arroyo.dev/blog/stateful-stream-processing

https://www.onehouse.ai/blog/apache-spark-structured-streaming-vs-apache-flink-vs-apache-kafka-streams-comparing-stream-processing-engines  Apache Flink™ vs Apache Kafka™ Streams vs Apache Spark™ Structured Streaming

https://medium.com/@byanalytixlabs/flink-vs-kafka-a-quick-guide-to-stream-processing-engines-b09dd0e6b8af Flink vs. Kafka

https://aws.amazon.com/blogs/big-data/a-side-by-side-comparison-of-apache-spark-and-apache-flink-for-common-streaming-use-cases/ A side-by-side comparison of Apache Spark and Apache Flink

https://romanglushach.medium.com/flink-spark-storm-kafka-a-comparative-analysis-of-big-data-stream-processing-frameworks-for-dab3dd42fc16 Flink, Spark, Storm, Kafka: A Comparative Analysis

https://www.linkedin.com/pulse/spark-kafka-stream-flink-unraveling-processing-trinity-ujjwal-gupta/ Spark, Kafka Stream, Flink: Unraveling the Stream Processing Trinity

Book:
https://www.amazon.com/Scaling-Machine-Learning-Spark-Distributed/dp/1098106822

https://habr.com/ru/companies/otus/articles/764136/

Kafka + PySpark Streaming
https://medium.com/plumbersofdatascience/kafka-with-spark-streaming-different-approaches-to-read-data-f38616c023b8

https://github.com/manuzhang/awesome-streaming Awesome streaming

####  Youtube

https://www.youtube.com/watch?v=Wqko7MunKZs Flink vs Kafka Streams/ksqlDB: Comparing Stream Processing Tools

https://www.youtube.com/watch?v=_8fHV5woDtQ  Flink Deep Dive - Concepts and Real Examples

https://www.youtube.com/watch?v=laNOk_6lPB8. Find the Right Data Streaming Architecture for Your Data Needs - AWS Online Tech Talks

https://www.youtube.com/watch?v=BXOD6pncb7s  Data Pipelines: Introduction to Streaming Data Pipelines

https://www.youtube.com/watch?v=4OHUTJDlnag  Flink + Pulsar: The Path To Unified Batch and Streaming

https://www.youtube.com/watch?v=QxZDdumDEO0  Как лечить гипертонию с помощью упражнений? Профилактика повышенного артериального давления


https://www.youtube.com/results?search_query=Apache+Flink+ru


#### Spark Structured Streaming

Micro batching, not real time
Uses DAG as execution engine ( Flink uses controlled cyclic dependency graph as execution engine) 


```
You can define the watermark of a query by specifying the event time column and the threshold on
how late the data is expected to be in terms of event time.
For a specific window ending at time T, the engine will maintain state and
allow late data to update the state until (max event time seen by the engine - late threshold > T).
In other words, late data within the threshold will be aggregated, but data later
than the threshold will start getting dropped.

windowedCounts = words \
    .withWatermark("timestamp", "10 minutes") \
    .groupBy(
        window(words.timestamp, "10 minutes", "5 minutes"),
        words.word) \
    .count()

Spark supports three types of time windows:

- tumbling - (fixed-sized), non-overlapping
- sliding -  (fixed-sized), overlapping
- session -  Session window has a dynamic size of the window length, depending on the inputs.
A session window starts with an input, and expands itself if following input has been received within gap duration.
For static gap duration, a session window closes when there’s no input received within gap duration after receiving the latest input.

Session window uses session_window function. The usage of the function is similar to the window function.

sessionizedCounts = events \
    .withWatermark("timestamp", "10 minutes") \
    .groupBy(
        session_window(events.timestamp, "5 minutes"),
        events.userId) \
    .count()
```

#### Checkpoints
Streaming applications are always running and most of them are maintaining some kind of state. 
Preserving the state across failures/restarts becomes a vital part of State management. 
The checkpoint is the solution to the State recovery and implemented using WAL (write-ahead logs).

The checkpoint is achieved by writing the state of the streaming query into the HDFS folder. Once the query restarts, It reads the HDFS folder to recover the state of the query before accepting new data from the data source stream.

Checkpoint directory (/hadoop/checkpoint/)

/offsets: 

Indicates to what point data has been consumed for processing from the data source stream. Example: In the case of Kafka source, It contains the {PartitionId: Offset} details for the Kafka topic. 
For each micro-batch (created for each trigger), the new offset file is created. 
 
/commits: 

Indicates to what point the processing engine has processed the data. 
Corresponding to each “offset” file there will be a “commit” file once the data is processed. The below figure describes 3 commit files corresponding to the offsets file. 

/source: 
It contains information about the data source; Example: Location of the file, Kafka topic name, etc.


/state: 
As the name indicates, this folder contains the state of each computed partition in the encoded format (LZ4). 
If Spark has 200 partitions, there would be 200 directories under the state folder.

#### Watermarks

Watermarks are the solution to forever state management of the windows to accommodate late events.
It provides a mechanism to control the state in a bounded way. It controls the state to grow indefinitely.

Watermarks are highly recommended with stateful aggregations otherwise resource usage will shoot upwards and may lead to breaking the system.

** Watermarks are supported only with Update Output mode.

Output modes:

complete
update
append
window_agg_df = trade_df \
  .withWatrmark("CreatedTime", " 30 minute") \
  .groupBy(window(col("CreatedTime"), " 15 minute")) \
   .agg(sum("Buy").alias("TotalBuy"),
        sum("Sell.alias("TotalSell"))
        
 output_df = window_agg_df.select("window.start",  "window.end", "TotalBuy", "TotalSell")
 
 window_query = output_df.writeStream \
  .format("console") \
  .outputMode("complete") \
  .option("checkpointLocation", "chk-point-dit") \
  .trigger(processingTime="1 minute") \
  .start()
  
  window.query.awaitTermination()
tumbling window - not overlapped

watermark - what is the maximum possible delay?

when late records are not relevant?

### Links 
https://dataai.udemy.com/course/spark-streaming-using-python/learn/lecture/22355480#overview

https://github.com/LearningJournal/Spark-Streaming-In-Python

https://medium.com/@shivagarg91/state-management-stateful-stateless-aggregations-on-unbounded-data-in-structured-streaming-1-3-6cf95cc32724

https://spark.apache.org/docs/latest/structured-streaming-programming-guide.html

https://www.udemy.com/course/apache-spark-streaming-in-scala/

https://dataai.udemy.com/course/spark-streaming-using-python/l

https://www.packtpub.com/product/real-time-stream-processing-using-apache-spark-3-for-scala-developers-video/9781803242040

https://jaceklaskowski.gitbooks.io/spark-structured-streaming/content/spark-sql-streaming-stateful-stream-processing.html
