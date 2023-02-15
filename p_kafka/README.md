### Event message  contains:

- key
- value
- timestamp
- compression type
- headers for metadata (optional)
- partition and offset id (once the message is written to a topic)

Events are serialized into binary,
Topic consist of  partitions.
Default retention - 7 days.

If messages have no key, they will be evenly distributed among partitions in a round robin manner.
Messages that have the same key will always be sent to the same partition. The key is run through a hashing function which turns it into an integer (partition number).


### Topic
https://kafka.apache.org/documentation/#topicconfigs

На уровне топика можно задать такие конфигурационные параметры, как:

```
- объем хранимых данных и/или их возраст (retention.bytes, retention.ms);
- фактор избыточности данных (replication factor);
- максимальный размер одного сообщения (max.message.bytes);
- минимальное число согласованных реплик, при котором в топик можно будет записать данные (min.insync.replicas);
- возможность провести failover на не синхронную отстающую реплику с потенциальной потерей данных (unclean.leader.election.enable);
- и еще много других (https://kafka.apache.org/documentation/#topicconfigs)
```
При создании топика обязательно указывайте конкретные цифры для retention.bytes и retention.ms.
Это спасет вас от неприятной ситуации, когда топик внезапно «отъел» все дисковое пространство на брокерах.
Обычно Kafka после такого «ложится», и, чтобы завести кластер снова, одной команды `systemctl start kafka.service` не хватит.

Используйте троттлинг при балансировке партиции топика. Если вы балансируете партиции топика по брокерам без троттлинга, это может привести к сильной деградации производительности всего кластера.


### Partition

На диске данные для каждой партиции хранятся в виде файлов сегментов, по умолчанию равных одному гигабайту (контролируется через log.segment.bytes). Важная особенность — удаление данных из партиций (при срабатывании retention) происходит как раз сегментами (нельзя удалить одно событие из партиции, можно удалить только целый сегмент, причем только неактивный).




### Kafka Producer API (low level) vs Kafla Connect

более миллиона сообщений в секунду на чтение и на запись при объеме сообщений 1 килобайт

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

### Kafka streaming

https://docs.confluent.io/platform/current/streams/concepts.html#kstream

https://www.confluent.io/blog/co-partitioning-in-kafka-streams/

https://www.vultr.com/docs/how-to-use-kafka-streams-for-stateful-and-stateless-data-processing/
```
Kafka Streams has two types of APIs:

Streams DSL - A high-level API
Processor - A low-level API

The Streams DSL API offers many abstractions such as KStreams, KTable etc.
One way of breaking it down is to categorize the functionality offered by these APIs as follows:

- stateless operations: such as map and filter 

 - stateful computations: like aggregate and count, reduce
```
Grouping operations (stateless) are often used to convert the contents of a KStream to a KGroupedStream 
to perform stateful computations (covered later in this guide).
This can be achieved using groupByKey or a more generic group method.

While using groupByKey is straightforward, note that a KeyValueMapper can be used with groupBy to use a different key. 
For example, you can use it to group user transactions based on card type:
```
KStream<String, User> transactions = builder.stream("transactions");

KGroupedStream<String, String> grouped = transactions.groupBy(new KeyValueMapper<String, User, String>() {
            @Override
            public String apply(String txID, User user) {
                return user.getCardType();
            }
    });
```
#### count
````
KStream<String, User> transactions = builder.stream("transactions");
KGroupedStream<String, String> grouped = transactions.groupBy(new KeyValueMapper<String, User, String>() {
           @Override
            public String apply(String txID, User user) {
                return user.getCardType();
            }
    });
KTable<String, Long> txPerCardType = grouped.count();
````

#### reduce
reduce operation can be used to combine streams of values and implement sum, min, max etc. 

You can think of aggregate operation as a generic version of reduce.

#### Windowing with Kafka Streams
https://www.confluent.io/blog/windowing-in-kafka-streams/
```
For example, a common requirement for website analytics is to have metrics about the number of unique page views per hour, 
clicks per minute, etc. 
Windowing lets you confine the stream processing operations to execute within a time range.
```
#### Supported time windows: 
- sliding 
- tumbling - special subtype of hopping window where windowSize and advanceSize are the same
- hopping 
- session-based time windows

```
For counting unique page views per hour, you can use a tumbling time window of 60 minutes. 
Thus, page views for a product from 1 PM to 2 PM will be aggregated and a fresh time block will start after that.
Here is an example of how you might achieve this:

KStream<Product, Long> views = builder.stream("product-views");
views.groupByKey()
    .windowedBy(SessionWindows.with(Duration.ofMinutes(60)))
    .toStream()
    .to("views-per-hour");
```

Exactly once semantic (vs at least once for Spark)


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
