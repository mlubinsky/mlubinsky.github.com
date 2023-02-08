#### Flinkdata  abstractions:

- DataSet    -  batch processing (Table, Jelly API  for Graph processing, FLINK ML API for Machine Learning)
- DataStream - stream processing

### Storage
- Files: local, HDFS. S3
- Databases: MongoDB, HBase
- Streams: Kafka, Flume, RabbitMQ

#### Timestamps 
- processing time (system time)
- event time - when evend occured on source (embedded within record)
- ingestion time - cannot handle out of order events
 
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
