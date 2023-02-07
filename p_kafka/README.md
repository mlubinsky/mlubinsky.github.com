### Event message - are serialized into binary,

- key
- value
- timestamp
- compression type
- headers for metadata (optional)
- partition and offset id (once the message is written to a topic)


Topic consist of  partitions.
Default retention - 7 days.

If messages have no key, they will be evenly distributed among partitions in a round robin manner.
Messages that have the same key will always be sent to the same partition. The key is run through a hashing function which turns it into an integer (partition number).


Kafka Producer API (low level) vs Kafla Connect

### Kafka Producer/Consumer API:
 - for almost any language
 - good if you own producer code
``` 
 subscribe()
 poll()
 send()
 flush()
 beginTransaction()
 ...
```
### Kafka Connect API:
 - Low to no code option
 - Hunderds of data sources (an sincs)
 - Manu fully managed through Confluent Clound
 - Create for integrating with data at rest

### Kafka Streams
```
KStream
KTable
filter()
map()
flatmap()
join()
aggregate()
```

### ksqlDB:
 - SQL syntax: CREATE STREAM, CREATE TABLE, SELECT, JOIN, GROUP BY, SUM
 - Kafka Streams under the hood

```
CREATE TABLE T (
 id STRING PRINARY TABLE
) WITH (
 kafka topic = 'my_topic',
 value_format-'AVRO'
)

CREATE STREAM s (
 id STRING PRINARY TABLE
) WITH (
 kafka topic = 'my_topic',
 value_format-'AVRO'
)
```
Create stream with JOIN using EMIT CHANGES
```
CREATE STREAM J  WITH (
 kafka topic = 'my_topic',
 value_format-'AVRO'
)
FROM a
INNER JOIN b
ON a.id = b.id
EMIT CHANGES
```
Example of WINDOW TUMBLING and EMIT FINAL (will wait till window is closed + grace period) :

```
CREATE TABLE T  WITH (
 kafka topic = 'my_topic',
 value_format-'AVRO'
) AS
SELECT ...
FROM
WINDOW TUMBLING(SIZE 2 HOURS, RETENTION 7 DAYS, GRACE PERIOD 10 MINUTES)
WHERE x < y
...
EMIT FINAL
```
