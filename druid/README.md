### Druid Ingestion
Druid supports both streaming and batch ingestion. 
Druid connects to a source of raw data, typically a message bus such as Apache Kafka (for streaming data loads), or a distributed filesystem such as HDFS (for batch data loads).

Druid converts raw data stored in a source to a more read-optimized format (called a Druid “segment”) in a process calling “indexing”.

### Storage
```
Like many analytic data stores, Druid stores data in columns. Depending on the type of column (string, number, etc), different compression and encoding methods are applied. Druid also builds different types of indexes based on the column type.

Similar to search systems, Druid builds inverted indexes for string columns for fast search and filter. Similar to timeseries databases, Druid intelligently partitions data by time to enable fast time-oriented queries.

Unlike many traditional systems, Druid can optionally pre-aggregate data as it is ingested. This pre-aggregation step is known as rollup, and can lead to dramatic storage savings.
```


### Druid is likely a good choice if your use case matches a few of the following:
```
Insert rates are very high, but updates are less common.
Most of your queries are aggregation and reporting queries. For example "group by" queries. 
You may also have searching and scanning queries.
You are targeting query latencies of 100ms to a few seconds.
Your data has a time component. Druid includes optimizations and design choices specifically related to time.
You may have more than one table, but each query hits just one big distributed table. 
Queries may potentially hit more than one smaller "lookup" table.
You have high cardinality data columns, e.g. URLs, user IDs, and need fast counting and ranking over them.
You want to load data from Kafka, HDFS, flat files, or object storage like Amazon S3.
```

### Situations where you would likely not want to use Druid include:
```
You need low-latency updates of existing records using a primary key. Druid supports streaming inserts, but not streaming updates.
You can perform updates using background batch jobs.
You are building an offline reporting system where query latency is not very important.
You want to do "big" joins, meaning joining one big fact table to another big fact table, and you are okay with these queries taking a long time to complete.
```




https://druid.apache.org/docs/latest/tutorials/index.html

https://www.micahlerner.com/2022/05/15/druid-a-real-time-analytical-data-store.html

https://www.decipherzone.com/blog-detail/apache-druid-architecture

https://www.youtube.com/watch?v=6jJi11r71sY

https://www.youtube.com/watch?v=f-LLTle-Xug

https://blog.datumo.io/data-partitioning-optimization-in-apache-druid-part-i-13e71d4d3538

https://engineering.salesforce.com/delivering-high-quality-insights-interactively-using-apache-druid-at-salesforce-7a038f0fe3d1

https://medium.com/tecnolog%C3%ADa/how-we-built-a-streaming-analytics-solution-using-apache-kafka-druid-66c257adcd9a 

```
Segment — the smallest unit of storage in Apache Druid. 
Data in Druid has to be partitioned into time chunks
(the range of the time chunk is called the segment granularity), 
and these time chunks are divided into segments. 
The target segment size should be in the range of 300–700mb. Segments in Druid are immutable.

Columns=Dimensions+Metrics
Dimensions are filterable and group-able, which normally represents the scope of slice and dice in your query
Metrics are measurements of users’ interests, which usually correspond to the column where users apply aggregations at query time, 
such as max(),sum(),distinct_count(), 95thPercentile(). 
(It is worth noting that aggregations in Druid can be applied both at ingestion time and query/post-query time.)


it is worth it to put extra effort into reducing the cardinalities introduced by timestamp. 
The way Druid approaches this is called rollup; you can think of rollup in Druid as a scheme to generate a summary of data 
by truncating the timestamp and pre-aggregating. Truncating the timestamp is an effective way to reduce cardinalities that are introduced by timestamp. Druid generates mergeable aggregates after rollup in segments and records them with the same combination of dimensions (including the truncated timestamp). 
Druid can easily calculate aggregates from billions of records in sub-seconds.
```
Insights into Bitmap Index
https://levelup.gitconnected.com/insights-into-indexing-using-bitmap-index-c28a3db1ad97

Druid and Kafka

https://medium.com/outbrain-engineering/understanding-spark-streaming-with-kafka-and-druid-25b69e28dcb7

https://medium.com/pinterest-engineering/pinterests-analytics-as-a-platform-on-druid-part-1-of-3-9043776b7b76

https://medium.com/pinterest-engineering/pinterests-analytics-as-a-platform-on-druid-part-2-of-3-e63d5280a1a9

https://medium.com/pinterest-engineering/pinterests-analytics-as-a-platform-on-druid-part-3-of-3-579406ffa374


https://medium.com/@knoldus/sql-on-apache-druid-part-ii-which-sql-workload-will-be-faster-on-druid-d1a83e834c99

```
ls -ltr  /usr/local/bin/ | grep druid | cut -b 53-200

druid-broker.sh -> ../Cellar/druid/0.22.0/bin/druid-broker.sh
 druid-coordinator.sh -> ../Cellar/druid/0.22.0/bin/druid-coordinator.sh
 druid-historical.sh -> ../Cellar/druid/0.22.0/bin/druid-historical.sh
 druid-jconsole.sh -> ../Cellar/druid/0.22.0/bin/druid-jconsole.sh
 druid-middleManager.sh -> ../Cellar/druid/0.22.0/bin/druid-middleManager.sh
 druid-node.sh -> ../Cellar/druid/0.22.0/bin/druid-node.sh
 druid-overlord.sh -> ../Cellar/druid/0.22.0/bin/druid-overlord.sh
 
 
 find . -name dsql*
./libexec/bin/dsql-main
./libexec/bin/dsql



ls -ltr ./libexec/bin/ | cut -b 51-150

 verify-java
 verify-default-ports
 supervise
 start-single-server-xlarge
 start-single-server-small
 start-single-server-medium
 start-single-server-large
 start-nano-quickstart
 start-micro-quickstart
 start-cluster-query-server
 start-cluster-master-with-zk-server
 start-cluster-master-no-zk-server
 start-cluster-data-server
 service
 run-zk
 run-druid
 post-index-task-main
 post-index-task
 jconsole.sh
 java-util
 generate-example-metrics
 dsql-main
 dsql
 broker.sh
 coordinator.sh
 historical.sh
 middleManager.sh
 node.sh
 overlord.sh
```
