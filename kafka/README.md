

## RabbitMQ
<https://itnext.io/connecting-competing-microservices-using-rabbitmq-28e5269861b6>



## RabbitMQ vs Kafka

https://www.reddit.com/r/programming/comments/8muszb/apache_kafka_vs_rabbitmq/
 https://itnext.io/connecting-competing-microservices-using-rabbitmq-28e5269861b6  
 https://www.quora.com/Why-does-Kafka-scale-better-than-other-messaging-systems-like-RabbitMQ
https://habr.com/company/itsumma/blog/416629/  
https://habr.com/company/itsumma/blog/418389/
                                                     
 
##  Kafka
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
   <https://medium.com/@stephane.maarek/the-kafka-api-battle-producer-vs-consumer-vs-kafka-connect-vs-kafka-streams-vs-ksql-ef584274c1e>
   <https://www.e4developer.com/2018/05/20/how-to-easily-run-kafka-with-docker-for-development/>
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
 
<https://multithreaded.stitchfix.com/blog/2018/09/05/datahighway/>

<https://medium.com/@itseranga>


https://medium.com/@stephane.maarek/how-to-use-apache-kafka-to-transform-a-batch-pipeline-into-a-real-time-one-831b48a6ad85  
     
https://www.confluent.io/blog/putting-power-apache-kafka-hands-data-scientists/
https://www.infoq.com/articles/traffic-data-monitoring-iot-kafka-and-spark-streaming
       https://jobs.zalando.com/tech/blog/many-to-many-using-kafka/index.html
       
<https://www.confluent.io/blog/building-streaming-application-ksql/> . KSQL

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
