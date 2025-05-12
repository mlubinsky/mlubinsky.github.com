https://www.udemy.com/course/kafka-streams/learn/lecture/7636248

https://habr.com/ru/articles/875330/  NATS, RabbitMQ and KAFKA

https://habr.com/ru/articles/899670/ NATS, RabbitMQ and KAFKA

https://newsletter.scalablethread.com/p/how-message-queues-work

https://habr.com/ru/companies/otus/articles/901708/ Практическое руководство по выбору брокера сообщений

https://habr.com/ru/companies/innotech/articles/699598/ Understanding the Differences Between Kafka and RabbitMQ


https://encore.dev/blog/queueing

Lot of good  Data Engimeering  links
https://rmoff.net/2025/04/22/interesting-links-april-2025/


### ktea - a Kafka TUI client
https://github.com/jonas-grgt/ktea

### Offset Explorer (formerly Kafka Tool) 

https://www.kafkatool.com/download.html

https://habr.com/ru/companies/idaproject/articles/889600/
```
приложение с графическим интерфейсом для работы с Kafka.

ОЕ позволяет быстро просматривать объекты в кластере Kafka, а также работать с сообщениями в топиках кластера.

Что позволяет делать OE:

просматривать содержимое кластеров Kafka, включая брокеров, топики и consumer’ов
просматривать и добавлять сообщения в партиции
просматривать и выставлять offset у consumer
выводить сообщения в JSON, XML и Avro формате с возможностью их локального сохранения
управлять топиками, их конфигурациями
обеспечить поддержку протоколов и механизмов аутентификации и шифрования для Apache Kafka
писать свои собственные плагины для вывода кастомных форматов данных и т.д.
```

Big Data Links:
https://rmoff.net/2025/04/22/interesting-links-april-2025/

### Kafka

https://habr.com/ru/articles/901200/ Настройка Apache Kafka для высоконагруженных систем

https://habr.com/ru/articles/880700/ Kafka на Python

https://habr.com/ru/companies/samolet/articles/880684/

https://habr.com/ru/articles/880094/ Kafka C++

https://www.youtube.com/watch?v=DU8o-OTeoCc

https://habr.com/ru/articles/865120/  Kafka visualization

https://levelup.gitconnected.com/message-queues-in-system-design-0440a1221023

https://www.linkedin.com/pulse/windowing-event-streams-bill-bejeck-jruye/

https://www.manning.com/books/kafka-streams-in-action-second-edition

https://medium.com/confluent/mastering-stream-processing-testing-flink-sql-windowed-applications-ce6e22412879

### Kafka Stream
https://habr.com/ru/articles/862976/

https://blog.devgenius.io/kafka-streams-how-to-calculate-moving-average-for-stock-price-data-stream-in-real-time-9429617d5108

https://www.freecodecamp.org/news/apache-kafka-handbook/

https://docs.google.com/presentation/d/11YgRsOTtJDzLA5FBsJ4fhx_t_PgTUwNWUvZgx7ZMpO4/edit#slide=id.g2489f38efa9_0_74

https://habr.com/ru/companies/maxilect/articles/858698/

https://habr.com/ru/companies/maxilect/articles/840972/

https://github.com/pmoskovi/kafka-learning-resources

https://blog.det.life/kafka-has-reached-a-turning-point-649bd18b967f

https://www.linkedin.com/posts/loveekumar-006_kafka-activity-7235323214782947329-D2i4

https://vutr.substack.com/p/how-did-linkedin-handle-7-trillion

### Оптимизация настроек Kafka кластера. 

https://habr.com/ru/articles/853652/

https://habr.com/ru/articles/818007/ Часть 1.

https://habr.com/ru/articles/819243/ Часть 2.

https://habr.com/ru/articles/819677/ Часть 3.


Building a Real-Time Data Streaming Pipeline for Sentiment analysis using Kafka,Postgres and Streamlit

https://kavitmht.medium.com/building-a-real-time-data-streaming-pipeline-for-sentiment-analysis-using-kafka-postgres-and-4f1c11ba51c9

### Schema Registry 

https://habr.com/ru/articles/811283/

https://habr.com/ru/articles/817121/

https://habr.com/ru/articles/738874/

https://www.youtube.com/watch?v=BVxDFL5iTx8 Kafka 3.5 KRaft instead Zookeper

https://habr.com/ru/companies/sbermarket/articles/738634/

https://habr.com/ru/companies/southbridge/articles/730380/

https://stackabuse.com/how-to-list-all-kafka-topics/

Structure of Kafka message (binary):

Messages are usually small (less than 1 MB) and sent in a standard data format, such as JSON, Avro, or Protobuf. Even so, they can be compressed to save on data. 

The compression type can be set to gzip, lz4, snappy, zstd, or none.

Once a message is sent into a Kafka topic, it also receives a partition number and offset id (more about these later).

```
key - usually string or int
value
headers for metadata (optional)
compt=ression type (e.g. gzip)
topic
partition integer
offset long
timestamp
timestampType
```

https://www.youtube.com/watch?v=W-wr4Fxmjsc   (ru)

https://habr.com/ru/company/southbridge/blog/683168/

#### Stream 

https://habr.com/ru/articles/850832/

https://towardsdatascience.com/master-the-kafka-shell-in-5-minutes-topics-producers-and-consumers-explained-442a15f1dac1

https://www.vultr.com/docs/how-to-use-kafka-streams-for-stateful-and-stateless-data-processing/

https://towardsdatascience.com/apache-kafka-in-python-how-to-stream-data-with-producers-and-consumers-307e84ca8bdb

https://towardsdatascience.com/make-a-mock-real-time-stream-of-data-with-python-and-kafka-7e5e23123582


<https://www.jesse-anderson.com/2019/10/why-i-recommend-my-clients-not-use-ksql-and-kafka-streams/> Do not use Kafka Stream and KSQL

<https://www.confluent.io/blog/build-streaming-etl-solutions-with-kafka-and-rail-data> 

<https://medium.com/@sathishjayaram/points-to-remember-while-processing-streaming-timeseries-data-in-order-using-kafka-and-spark-38cdf787a304>

<https://dzone.com/articles/life-beyond-kafka-with-apache-pulsar>   Apache Pulsar

<https://dzone.com/articles/5-courses-to-learn-apache-kafka-in-2019> 5 Kafka classes /courses

<https://dev.to/victorgil/using-apache-kafka-to-implement-event-driven-microservices-af2>

<https://ordepdev.me/posts/tales-from-running-kafka-streams-in-production>

### Kafka and Python

https://www.toptal.com/microservices/event-driven-microservices-kafka-python

https://habr.com/ru/company/neoflex/blog/686242/ PySpark and Kafka

https://habr.com/ru/companies/southbridge/articles/735262/

https://habr.com/ru/post/587592/

https://habr.com/ru/post/578916/ Python микросервисы с Kafka 

https://towardsdatascience.com/real-time-anomaly-detection-with-apache-kafka-and-python-3a40281c01c9


http://www.technocratsid.com/install-kafka-on-macos/

Issue: https://stackoverflow.com/questions/35788697/leader-not-available-kafka-in-console-producer

vi config/server.properties

add below line:

listeners=PLAINTEXT://localhost:9092

bin/kafka-server-stop.sh

bin/kafka-server-start.sh -daemon config/server.properties


```
brew install kafka
==> Caveats
==> zookeeper
To have launchd start zookeeper now and restart at login:
  brew services start zookeeper
Or, if you don't want/need a background service you can just run:
  zkServer start
==> kafka
To have launchd start kafka now and restart at login:
  brew services start kafka
Or, if you don't want/need a background service you can just run:
  zookeeper-server-start /usr/local/etc/kafka/zookeeper.properties & kafka-server-start /usr/local/etc/kafka/server.properties
  
  
$ cat /usr/local/etc/kafka/zookeeper.properties

dataDir=/usr/local/var/lib/zookeeper
# the port at which the clients will connect
clientPort=2181

$ cat   /usr/local/etc/kafka/server.properties
...
zookeeper.connect=localhost:2181
log.dirs=/usr/local/var/lib/kafka-logs
...
  
$  find /usr -type f | grep kafka-console | xargs ls -l
 
-r-xr-xr-x  144  /usr/local/Cellar/kafka/2.3.1/bin/kafka-console-consumer
-r-xr-xr-x  144 /usr/local/Cellar/kafka/2.3.1/bin/kafka-console-producer
-rwxr-xr-x  945 /usr/local/Cellar/kafka/2.3.1/libexec/bin/kafka-console-consumer.sh
-rwxr-xr-x  944 /usr/local/Cellar/kafka/2.3.1/libexec/bin/kafka-console-producer.sh

zkServer start
kafka-topics --create --zookeeper localhost:2181 --replication-factor 1 --partitions 1 --topic testTopic

kafka-console-producer --broker-list localhost:9092 --topic testTopic

$ kafka-topics --describe --zookeeper localhost:2181
Topic: testTopic	PartitionCount: 1	ReplicationFactor: 1	Configs:
	Topic: testTopic	Partition: 0	Leader: 0	Replicas: 0	Isr: 0

kafka-console-consumer --bootstrap-server localhost:9092 --topic testTopic --from-beginning

WARN [Consumer clientId=consumer-console-consumer-46359-1, groupId=console-consumer-46359] Error while fetching metadata with correlation id 73 : {testTopic=LEADER_NOT_AVAILABLE} (org.apache.kafka.clients.NetworkClient)


$ cat /usr/local/Cellar/kafka/2.3.1/bin/kafka-console-consumer

#!/bin/bash
JAVA_HOME="$(/usr/libexec/java_home --version 1.8)" exec "/usr/local/Cellar/kafka/2.3.1/libexec/bin/kafka-console-consumer.sh" "$@"

```


### Client
<https://github.com/twmb/kcl> Kafka client

<https://github.com/obsidiandynamics/kafdrop> UI for Kafka

https://habr.com/ru/company/parimatch_tech/blog/544304/. Kafka clients with GUI

### Books
https://medium.com/@1900jwatson/the-best-books-to-learn-apache-kafka-b808f9be43d9

https://habr.com/ru/company/southbridge/blog/550934/

https://habr.com/ru/company/otus/blog/532954/  KAFKA API

https://habr.com/ru/company/southbridge/blog/530498/  

<https://lobste.rs/s/xylmdn/i_m_not_feeling_async_pressure>

<https://news.ycombinator.com/item?id=23206566>


### Docker
<https://alexandrugris.github.io/distributed/systems/2017/06/11/kafka-patterns.html> Kafka in Docker

<https://florimond.dev/blog/articles/2018/09/building-a-streaming-fraud-detection-system-with-kafka-and-python/> - in Docker

There is pdf version of this file:
<https://medium.com/@stephane.maarek/how-to-use-apache-kafka-to-transform-a-batch-pipeline-into-a-real-time-one-831b48a6ad85>

<https://medium.com/high-alpha/data-stream-processing-for-newbies-with-kafka-ksql-and-postgres-c30309cfaaf8>

<https://habr.com/ru/company/tinkoff/blog/481784/> 

<https://habr.com/ru/post/466385/>  Изучение механики обмена сообщениями посредством ActiveMQ и Kafka. Глава 1


## RQ Celery etc

<https://testdriven.io/blog/asynchronous-tasks-with-flask-and-redis-queue/>

<https://news.ycombinator.com/item?id=21940598>

## RabbitMQ
<https://itnext.io/connecting-competing-microservices-using-rabbitmq-28e5269861b6>

<https://blog.theodo.com/2019/08/event-driven-architectures-rabbitmq/>

<https://www.erlang-solutions.com/blog/rabbit-s-anatomy-understanding-topic-exchanges.html>

<https://medium.com/@shivama205/rabbitmq-best-practices-67a27ef72a57>

## RabbitMQ vs Kafka

https://habr.com/ru/company/innotech/blog/698838/

https://habr.com/ru/company/southbridge/blog/666326/

https://habr.com/ru/company/southbridge/blog/536164/

<https://www.infoq.com/presentations/rabbitmq-kafka/> 

<https://habr.com/ru/company/itsumma/blog/471858/> 

<https://jack-vanlightly.com/blog/2018/9/2/rabbitmq-vs-kafka-part-6-fault-tolerance-and-high-availability-with-kafka>

<https://habr.com/ru/company/itsumma/blog/437446/>
<https://habr.com/ru/company/itsumma/blog/416629/>

In addition to scalability and low latency, Kafka popularity comes from allowing more flexible and agile consumer patterns. Essentially, the consumer is in control. You don’t need to have subscribed to the queue (and be up and running) when the message is produced. You can subscribe to it later (days, weeks, months later) and still get old messages.

Rabbit MQ and similar “old style” messaging services are more about the producer. They have things like “guaranteed delivery” and “guaranteed single execution”. They are still good for job execution, where the producer has a job to do, for example, to reset a password or change a customer account across multiple business systems. In other words, they are good for typical Enterprise Service Bus (ESB) type applications, something that has the “guaranteed (right now) single delivery” requirements.

Kafka, however, shifts the control to the consumer(s), who can decide when and how (and if) it wants to consume the messages. Rather than a job to execute, Kafka is more about status messages, along the lines of: “Hey everyone, this thing just happened. Do with it what you wish.”

Because it persists the messages, essentially forever, it allows for better separation between the producer and consumer. The producer puts a message on the queue and then forgets about it. The consumers are free to process and reprocess the messages as much as they want.

It’s especially good for two situations: 1) Unreliable consumers who come and go, and 2) Multiple consumers - including future new consumers you may not have anticipated when you first created the system.

Because it persists the messages for a long time, you can create new consumers at any time and replay old messages to “catch up”. Further, a consumer can go down for several days (or weeks, depending on how long you keep the persisted messages) and then it can get all caught up once it finally comes back up.

Also it’s great way to mix production & development environments. Dev consumers can safely consume a production data stream. Since Kafka allows for any number of consumer groups, this is a great pattern to test your Development code. It also allows for easy Blue/Green deployments, where both systems (Blue and Green) can consume from the same producer feed and you can swap the environments at any time. Another good use-case is A/B Testing. Both your A & B systems can consume from the same production queue and stay up-to-date with the latest data, and then you can randomly distribute your customers between A & B at any time. Because Kafka can have any number of consumers and you can create new consumers at any time, you and launch new A/B tests at any time.

This is in contrast to Rabbit-MQ implementations (and similar messaging contracts) which typically remove the message from the queue once it has been delivered and processed, i.e. once the delivery guarantee has been met. If there’s a problem, they move the message to a “dead letter” queue, which requires special processing and handling (read: more work, more complexity). Allowing multiple consumers to attach to a Rabbit-MQ-style queuing system is probably not recommended. ESB systems that I’ve been involved with require very heavy deployment cycles with lots of testing for new consumers.

https://www.reddit.com/r/programming/comments/8muszb/apache_kafka_vs_rabbitmq/
 https://itnext.io/connecting-competing-microservices-using-rabbitmq-28e5269861b6  
 https://www.quora.com/Why-does-Kafka-scale-better-than-other-messaging-systems-like-RabbitMQ
https://habr.com/company/itsumma/blog/416629/  
https://habr.com/company/itsumma/blog/418389/
                                                     
 
##  Kafka

<https://medium.com/@andy.bryant/processing-guarantees-in-kafka-12dd2e30be0e>



<https://habr.com/ru/post/466585/> book article

<https://youtu.be/JalUUBKdcA0>

<https://yokota.blog/>

<https://mux.com/blog/stateful-stream-processing-with-kafka-and-go/>

 * Producer:
   - Async (no garantee)
   - Commited to leader
   - Commited to leader & Quorum
 
 * Consumer: can fetch offset for given partition and get record
   - At least once
   - At most once
   - Effectively once
   - Exactly once
  
  Features:
 - Log compactions preserving disk space
 - Disk Not heap
 - Pagecache to Socket
 - Balanced Partitions & Leaders
 - Produce and Consumer Quotas (# of event per sec)
 - Heroku Kafla
```   
 $ grep dataDir config/zookeeper.properties
dataDir=/tmp/zookeeper
 $ grep clientPort config/zookeeper.properties
clientPort=2181
 $ grep log.dirs config/server.properties
log.dirs=/tmp/kafka-logs  


bin/zookeeper-server-start.sh config/zookeeper.properties

kafka-server-start.sh config/server.properties
```   

<https://assets.ctfassets.net/oxjq45e8ilak/5C3BJ4jXm0xaI5Cz8ZN2ra/e3cceba5659722f6d94859f0e96356dc/Grigoriy_Koshelev_Kogda_vs_poshlo_po_Kafke.pdf>
<https://youtu.be/A_yUaPARv8U>



<https://medium.com/@madhur25/considerations-for-high-throughput-kafka-producer-ed97c2c332c>

   <https://medium.com/@stephane.maarek/the-kafka-api-battle-producer-vs-consumer-vs-kafka-connect-vs-kafka-streams-vs-ksql-ef584274c1e>
   <https://www.e4developer.com/2018/05/20/how-to-easily-run-kafka-with-docker-for-development/>
   <http://www.kai-waehner.de/blog/>
   
   https://www.youtube.com/results?search_query=%D0%B3%D0%B0%D0%BC%D0%BE%D0%B2+kafka     гамов
   
   <https://www.youtube.com/watch?v=pPmsCztSFeE> Kafka льёт, а Spark разгребает
   
   <http://www.kai-waehner.de/blog/>
   
docker run --network=kafka -d --name=zookeeper -e ZOOKEEPER_CLIENT_PORT=2181 confluentinc/cp-zookeeper

docker run --network=kafka -d -p 9092:9092 --name=kafka -e KAFKA_ZOOKEEPER_CONNECT=zookeeper:2181 -e KAFKA_ADVERTISED_LISTENERS=PLAINTEXT://kafka:9092 -e KAFKA_OFFSETS_TOPIC_REPLICATION_FACTOR=1 confluentinc/cp-kafka
   
cat /etc/hosts
127.0.0.1	kafka
  
#docker ps
CONTAINER ID        IMAGE                       COMMAND                  CREATED             STATUS              PORTS                          NAMES
8f922cdf9ef9        confluentinc/cp-kafka       "/etc/confluent/dock…"   6 minutes ago       Up 6 minutes        0.0.0.0:9092->9092/tcp         kafka
a60205abccba        confluentinc/cp-zookeeper   "/etc/confluent/dock…"   13 minutes ago      Up 13 minutes       2181/tcp, 2888/tcp, 3888/tcp   zookeeper

 
docker exec -it 8f922cdf9ef9 bin/bash

ls /etc/confluent/docker/
configure	  kafka.properties.template  mesos-setup.sh
docker-utils.jar  launch		     run
ensure		  log4j.properties.template  tools-log4j.properties.template
 
<https://habr.com/ru/company/avito/blog/465315/> 
 
<https://multithreaded.stitchfix.com/blog/2018/09/05/datahighway/>

<https://medium.com/@itseranga>

<https://youtu.be/PgkRhlUwYyE> . Виктор Гамов

<https://youtu.be/ZH3AlesuSpw> . Kafka Streams и Firehose API . (ru)

https://medium.com/@stephane.maarek/how-to-use-apache-kafka-to-transform-a-batch-pipeline-into-a-real-time-one-831b48a6ad85  
     
https://www.confluent.io/blog/putting-power-apache-kafka-hands-data-scientists/

https://www.infoq.com/articles/traffic-data-monitoring-iot-kafka-and-spark-streaming

https://jobs.zalando.com/tech/blog/many-to-many-using-kafka/index.html
       
<https://www.confluent.io/blog/building-streaming-application-ksql/> . KSQL

<https://talks.rmoff.net/9ih1WQ/building-stream-processing-applications-for-apache-kafka-using-ksql> KSQL

http://highscalability.com/blog/2018/4/9/give-meaning-to-100-billion-events-a-day-the-analytics-pipel.html

https://jeeconf.com/program/the-journey-from-queues-to-data-pipeline-streams/

https://jeeconf.com/program/building-event-sourced-systems-with-kafka-streams/

https://jeeconf.com/program/reactive-stream-processing-with-akka-streams/

https://hackernoon.com/thorough-introduction-to-apache-kafka-6fbf2989bbc1

https://itnext.io/from-monoliths-to-microservices-b6b851ab43e3

https://www.datanami.com/2018/04/30/how-netflix-optimized-flink-for-massive-scale-on-aws/ Flink
                                                     
https://habr.com/company/sberbank/blog/353608/ 

https://habr.com/company/piter/blog/352978/  

https://habr.com/post/354486/   

https://habr.com/company/skbkontur/blog/353204/ 

https://www.youtube.com/watch?v=eublKlalobg&feature=youtu.be

https://speakerdeck.com/vikgamov/devnexus-2018-apache-kafka-a-streaming-data-platform

https://www.confluent.io/blog/ksql-in-action-enriching-csv-events-with-data-from-rdbms-into-AWS/  
 
https://medium.com/tecnolog%C3%ADa/how-we-built-a-streaming-analytics-solution-using-apache-kafka-druid-66c257adcd9a 
 https://assets.ctfassets.net/oxjq45e8ilak/1y637HHnSQQMewS0m4usYS/95ffde03d09c3f49dcc7fe85fc976553/Gamov_Kafka_EOS.pdf
 
https://habr.com/company/jugru/blog/354238/
 
http://tech.marksblogg.com/presto-connectors-kafka-mongodb-mysql-postgresql-redis.html Presto
