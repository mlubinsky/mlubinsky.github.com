#### Flink data  abstractions:

- DataSet  (like Datafame in Spark)  -  batch processing (Table, Jelly API  for Graph processing, FLINK ML API for Machine Learning)
- DataStream - stream processing

#### DataSet Tranformations

- filter
- map
- flatmap
- groupby
- sum

#### Times 
 
- Processing time — time of a particular machine that will process the specific element. It could be different than the actual event time when the event is generated, and the order of events could be separate because of the network failures and delays.
- Event time — It is the time when an event is generated at the source. It’s the actual time of an event (embedded within record).
- Ingestion time — It is a time when the Flink receives an event for processing. It could be more reliable than the processing time since all the operators will see the same timestamp for the individual event;  helps to handle out of order events

#### Joins

 Following is an inner join for person (pid, personName) and location (pid,locationName) dataset.
```
DataSet<Tuple3<Integer, String, String>> joined = 
      personSet.join(locationSet, JoinOperatorBase.JoinHint.OPTIMIZER_CHOOSES)
      .where(0)
      .equalTo(0)
      .with((JoinFunction<Tuple2<Integer, String>, Tuple2<Integer, String>, 
            Tuple3<Integer, String, String>>) (personTuple, locationTuple) 
            -> new Tuple3<>(personTuple.f0, personTuple.f1, locationTuple == null? "NULL" :locationTuple.f1));
```            
Flink also let the app developers specify join hints. There are six type of join hints.

#### OPTIMIZER_CHOOSES: 
This will use the default system optimizations while doing the join operations. Hence it’s optional.

#### BROADCAST_HASH_FIRST: 
Flink is a distributed stream processing and when we are joining two different data sets or streams, both of those can be on different nodes. Joining data from different nodes can be quite expensive operation. If one of the dataset is small, we can move it to the memory of the other nodes so that whenever they are joining with each other they perform the join operation from the data in the memory and avoid the shuffling of data among different nodes. This hint will broadcast the first dataset to the different nodes before performing the join.

#### BROADCAST_HASH_SECOND: 
It is similar to the BROADCAST_HASH_FIRST except we move the second data set into the memory of the nodes for join operations to reduce shuffling.

#### REPARTITION_HASH_FIRST: 
This will create a hash table from the input dataset to optimize the lookup for the join operation. As data is large and distributed, having a hash table will help to quickly find the relevant column values when we are joining. This hint will built the hash table from the first input.

#### REPARTITION_HASH_SECOND: 
It is simlar to REPARTITION_HASH_FIRST but builds the hashtable for the second dataset. In general we use the hint for the data set that is small in size.

#### REPARTITION_SORT_MERGE: 
This hint is used to leverage the sorting to make joins faster. As we know if datasets are sorted and it’s just like serial reads on both of the datasets. This hint is passed to tell Flink that one of the dataset is already sorted and it can leverage the already sorted dataset.



#### Storage
- Files: local, HDFS. S3
- Databases: MongoDB, HBase
- Streams: Kafka, Flume, RabbitMQ


 
https://dataai.udemy.com/course/apache-flink-a-real-time-hands-on-course-on-flink/

https://www.ververica.com/blog/apache-flink-sql-past-present-and-future

Join hints (hash, broadcast, sort)

Keyed Stream (after keyBy Operation) window() Window assigner defines how entities are assigned to windows

Non-keyed stream wnidowAll()

### Window types

- Tumbling window - time based - no overlapped
- Sliding window - time based windows are overlappping (offset parameter)
- Session window - created based on activity, does not have fixed start or end time, ended then there is gap in activity
- Global window (window per key, do computation with trigger)

### Triggers

- EventTimeTrigger
- ProcessingTimeTrigger
- CountTrigger
- PurgingTrigger
