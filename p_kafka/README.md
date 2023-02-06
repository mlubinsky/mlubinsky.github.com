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
