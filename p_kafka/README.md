Topic consist of  partitions

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
Example of WINDOW TUMBLING and EMIT FINAL:

```
CREATE TABLE T  WITH (
 kafka topic = 'my_topic',
 value_format-'AVRO'
) AS
SELECT ...
FROM
WINDOW TUMBLING(SIZE 2 HOURS, RETENTION 7 DAYS, GRACE PERIOD 10 MINUTES
WHERE x < y
...
EMIT FINAL
```
