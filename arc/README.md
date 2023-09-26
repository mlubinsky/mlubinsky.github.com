https://twirl.github.io/The-API-Book/index.ru.html  API book

Event - driven applications:

https://enlear.academy/aspects-of-event-driven-apps-aws-c81e80ef7fc6

https://enlear.academy/asynchronous-request-handling-with-aws-sqs-c4df33ae9717

```
In a push-based system, the event producer or pusher needs a promise from the consumer
that the consumer will be able to process whatever events are generated.

In a pull-based model, the consumers poll for events. This pull mechanism allows for buffering & batching.
 Consumer polls and process messages when it has the capacity for the same.

Also, messages can be consumed in a blocking or non-blocking way. Message brokers enable asynchronous communications between services so that the sending service need not wait for the receiving service’s reply.

This improves fault tolerance and resiliency in the systems in which they’re employed.

Amazon Simple Queue Service (SQS) is a fully managed message queueing service that allows you to decouple your applications. It helps you improve your applications’ performance and user experience by allowing you to communicate asynchronously between client and server.
```

### High Load real time architecture

https://www.epsio.io/

https://rockset.com/

https://habr.com/ru/articles/761464/ 

https://www.kdnuggets.com/how-to-digest-15-billion-logs-per-day-and-keep-big-queries-within-1-second

### API book:

https://twirl.github.io/The-API-Book/index.ru.html
https://www.amazon.com/gp/product/B09RHH44S5/

### System design
https://github.com/DovAmir/awesome-design-patterns

https://habr.com/ru/companies/kts/articles/741846/ Полное руководство по проектированию систем в виде схемы

https://habr.com/ru/companies/vk/articles/741702/  Data Formats (avro, etc)


### Streaming

Book:  <http://streamingsystems.net/>

https://eng.uber.com/streaming-real-time-analytics/

https://habr.com/ru/company/ru_mts/blog/684476/


Documenting software architecture

https://www.innoq.com/en/blog/brief-introduction-to-arc42/

Algorithms you should know before you take system design interviews

https://blog.bytebytego.com/p/algorithms-you-should-know-before

https://news.ycombinator.com/item?id=32353500


https://luminousmen.com/post/modern-big-data-architectures-lambda-kappa

https://adamvotava.medium.com/

Apache Iceberg:
https://www.youtube.com/watch?v=LiC9vZATv0o&t=8s


https://news.ycombinator.com/item?id=32429533


https://www.dremio.com/subsurface/comparison-of-data-lake-table-formats-iceberg-hudi-and-delta-lake/

### Обзор паттернов интеграции микросервисов. Часть 1 ,2
https://habr.com/ru/company/southbridge/blog/679906/

https://habr.com/ru/company/southbridge/blog/681326/


https://twirl.github.io/The-API-Book/index.ru.html

Consesnsus in distibuted systems
https://habr.com/ru/company/dododev/blog/463469/

### Memcached vs Redis

https://habr.com/ru/company/wunderfund/blog/685894/ Redis

https://architecturenotes.co/redis/ 

https://news.ycombinator.com/item?id=32426879

https://news.ycombinator.com/item?id=28830007. 

https://engineering.kablamo.com.au/posts/2021/memcached-vs-redis-whats-the-difference

### tools for writing diagrams
 


https://www.infoq.com/articles/whats-the-next-step-for-data-management/

<https://a16z.com/2020/10/15/the-emerging-architectures-for-modern-data-infrastructure/>

<https://proprogramming.org/design-dropbox-a-system-design-interview-question/>

<https://news.ycombinator.com/item?id=24814687>

<https://medium.com/better-programming/modern-day-architecture-design-patterns-for-software-professionals-9056ee1ed977>

<https://robertovitillo.com/how-to-conduct-a-system-design-interview/>

<https://habr.com/ru/company/gms/blog/516718/> Netflix  system design-интервью

https://habr.com/ru/post/516604/

<https://techblog.bozho.net/seven-legacy-integration-patterns/>

https://robertheaton.com/2020/04/06/systems-design-for-advanced-beginners/

https://news.ycombinator.com/item?id=23904000

<https://eng.uber.com/apache-hudi-graduation/>  Apachi Hudi

<https://landing.google.com/sre/books/> SRE book

<https://queue.acm.org/pastissues.cfm> ACM transactions

https://medium.com/wix-engineering/6-event-driven-architecture-patterns-part-1-93758b253f47

## RabbitMQ
https://news.ycombinator.com/item?id=23258301


## ML infrastructure

<https://cloud.google.com/solutions/machine-learning/mlops-continuous-delivery-and-automation-pipelines-in-machine-learning>

<https://www.youtube.com/watch?v=rMx3n0NTfZQ&feature=youtu.be&t=9957> 

<https://www.youtube.com/watch?v=G0VJTYDhCPU> 

<https://christophergs.com/machine%20learning/2020/03/14/how-to-monitor-machine-learning-models/>

<https://itnext.io/mlops-not-as-boring-as-it-sounds-eaebe73e3533> . ML Ops

<https://tecton.ai/blog/devops-ml-data/>





<https://medium.com/swlh/end-to-end-machine-learning-from-data-collection-to-deployment-ce74f51ca203>

<https://streamsql.io/blog/microservices-with-machine-learning-feature-store>

<https://towardsdatascience.com/end-to-end-deep-learning-tutorial-using-azure-f7bb524f7277>

<https://github.com/chiphuyen/machine-learning-systems-design>

<https://towardsdatascience.com/architecting-a-machine-learning-pipeline-a847f094d1c7>

<https://medium.com/hackernoon/a-guide-to-scaling-machine-learning-models-in-production-aa8831163846>



<https://github.com/heathermiller/dist-prog-book> . Distributed prog

<https://robertheaton.com/2020/04/06/systems-design-for-advanced-beginners/>

<https://news.ycombinator.com/item?id=22702293>

<https://blog.eyas.sh/2020/03/data-oriented-architecture/>

<https://news.ycombinator.com/item?id=22519974>

<https://habr.com/ru/company/ua-hosting/blog/487540/> . Metadata management

<https://news.ycombinator.com/item?id=22011743>

<https://infoq.com>

<https://www.infoq.com/news/2019/12/ebay-architecture-knowledgegraph> Knowledge Graph

<https://atlas.apache.org/#/> Data Governance and Metadata framework for Hadoop

<https://www.intermix.io/blog/14-data-pipelines-amazon-redshift/>

<https://github.com/san089/goodreads_etl_pipeline>

<http://shop.oreilly.com/product/0636920073994.do>  Book: Streaming System

<https://engineering.grab.com/plumbing-at-scale>

<https://debezium.io/blog/2020/02/10/event-sourcing-vs-cdc/>

<https://medium.com/analytics-vidhya/data-streams-and-online-machine-learning-in-python-a382e9e8d06a>

<https://tech.wayfair.com/data-science/2020/02/how-to-enable-data-scientists-to-stop-managing-etl-pipelines-and-get-back-to-doing-data-science-part-i/>


<https://imply.io/post/analytics-reference-architecture-for-iot>  Analytics refernce architecture for iot


<https://tech.wayfair.com/data-science/2020/02/how-to-enable-data-scientists-to-stop-managing-etl-pipelines-and-get-back-to-doing-data-science-part-i/>


## Hexagonal Architecture
<https://medium.com/@animeshgaitonde/hexagonal-architecture-principles-practical-example-in-java-364bb2e50075> 

<https://habr.com/ru/post/493426/>

<https://www.dataengineeringpodcast.com/datadog-timeseries-data-episode-113/> 

##  Netflix Metaflow

<https://habr.com/ru/company/ruvds/blog/482462/>

<https://docs.metaflow.org/introduction/what-is-metaflow>


<https://itnext.io/1-year-of-event-sourcing-and-cqrs-fb9033ccd1c6>.  CQRS and Event Sourcing

## Distributed systems

<https://medium.com/analytics-vidhya/data-streams-and-online-machine-learning-in-python-a382e9e8d06a>

<http://book.mixu.net/distsys/single-page.html>

<https://www.youtube.com/watch?v=Y6Ev8GIlbxc> distributed systems

<http://book.mixu.net/distsys/single-page.html>

<https://github.com/heathermiller/dist-prog-book/>
<https://medium.com/@yagi5/lets-study-distributed-systems-4-leader-election-78a083981321>

Latency is “the time interval between a stimulus and its response”. 'I want to get downtown. How long until I arrive? Latency is measured in time units.

Throughput is “the rate at which a system achieves its goal”. People want to get downtown. How many arrive each hour? Throughput is measured in deliveries per time.

Sometimes latency and throughput interfere with each other. Buses might deliver more people per hour than individually hailed cars (higher throughput), but it takes me personally longer to get downtown because I have to walk to a bus stop and wait for the bus (higher latency).

imagine that you have no task-switching penalties but have to perform two tasks A and B which are in theory 100 units of time each. If you perform them serially, you get the result for A at time 100 and the result for B at time 200; if you perform them in parallel switching between them, you get the benefit that at time 51 you can show both of the recipients that you are 25% complete, but you deliver A at time 199 and B at time 200. B gets the same result; A gets a strictly better result, by not multitasking. If you imagine that your reputation is proportional to the average of the inverses of your times-to-completion, your reputation is 50% better in the first case due to the 100% improvement on half of your deadlines; if you had done the same nonsense with three parallel tasks your reputation would be 83% better or so.

## circuit breaker pattern
<https://engineering.grab.com/designing-resilient-systems-part-1> circuit breaker
<https://github.com/danielfm/pybreaker>
<https://github.com/arlyon/aiobreaker>
<https://github.com/connor4312/cockatiel>

## Apache Beam

<https://habr.com/ru/company/otus/blog/454186/> Apache Beam и DataFlow для конвейеров реального времени

<https://www.youtube.com/watch?v=C6MlPaox5EI> Apache Beam

<https://towardsdatascience.com/lets-build-a-streaming-data-pipeline-e873d671fc57>

## Join Petabates

<https://medium.com/liveramp-engineering/joining-petabytes-of-data-per-day-how-liveramp-powers-its-matching-product-fe7c0f440824> Joining Petabytes of Data Per Day

<https://medium.com/liveramp-engineering/seeking-map-side-join-c2007f31fa14>  Map Site Join

##  Architecture 

<https://www.confluent.io/blog/cloud-analytics-for-on-premises-data-streams-with-kafka/>

<https://habr.com/ru/company/avito/blog/479952/>

<http://highscalability.com/blog/2019/11/25/egnyte-architecture-lessons-learned-in-building-and-scaling.html>

<https://danielsada.tech/blog/cloud-services-dos/>

<https://news.ycombinator.com/item?id=21515772>

<https://github.com/adilkhash/Data-Engineering-HowTo>

<https://habr.com/ru/company/otus/blog/479572/>  Gutenberg микросервисы Netflix Pub-Sub 

## Data Modeling

<https://github.com/linkedin/WhereHows/wiki>

<https://en.wikipedia.org/wiki/ISO_15926>

<https://dot15926.livejournal.com/27293.html>


<https://habr.com/ru/company/oleg-bunin/blog/468535/> Log analysis

## Stream vs batch

<https://github.com/zendesk/pakkr>

<https://streamz.readthedocs.io/en/latest/index.html>

<https://cgarciae.github.io/pypeln/> 

<https://habr.com/ru/company/otus/blog/477834/>

<https://github.com/voorloopnul/pipeframe>  Python  process data (stream or batch) taking advantage of python multiprocessing library.

<https://github.com/omegaml/minibatch> Instead of directly connection producers and consumers, a producer sends messages to a stream. Think of a stream as an endless buffer, or a pipeline, that takes input from many producers on one end, and outputs messages to a consumer on the other end. This transfer of messages happens asynchronously, that is the producer can send messages to the stream independent of whether the consumer is ready to receive, and the consumer can take messages from the stream independent of whether the producer is ready to send.

Unlike usual asynchronous messaging, however, we want the consumer to receive messages in small batches to optimize throughput. That is, we want the pipeline to emit messages only subject to some criteria of grouping messages, where each group is called a mini-batch. 

<https://petl.readthedocs.io/> . petl transformation pipelines make minimal use of system memory and can scale to millions of rows if speed is not a priority. However if you are working with very large datasets and/or performance-critical applications then other packages may be more suitable, e.g., see pandas, pytables, bcolz and blaze. 

https://github.com/olirice/flupy . Fluent data pipelines for python and your shell

<https://github.com/robinhood/faust> . Python Stream Processing

<https://github.com/gazette/core> Gazette is infrastructure for building streaming platforms: platforms composed of loosely coupled services, built and operated by distinct teams, managing and serving large amounts of state, but all communicating continuously through a common catalog of streamed data. It features a lightweight container & cloud-native architecture, high availability, and integrates elegantly with existing batch workflows.

<https://netflix.github.io/mantis/>

<https://www.learnstorybook.com/design-systems-for-developers/react/en/introduction/>

<https://www.lightbend.com/blog>

## Real time

<https://habr.com/ru/post/503084/> 
<https://www.lightbend.com/blog/use-kafka-streams-dynamically-controlled-streams>

<https://medium.com/the-telegraph-engineering/pulse-the-telegraph-journey-towards-real-time-analytics-cd08c1078fa6> 

<https://github.com/rikace/Presentations/blob/master/ReactiveStreams/slides/StreamProcessing.pdf>

<https://research.fb.com/publications/realtime-data-processing-at-facebook/> Realtime Data Processing at Facebook


<https://medium.com/@D11Engg/building-scalable-real-time-analytics-alerting-and-anomaly-detection-architecture-at-dream11-e20edec91d33> 

<https://www.infoq.com/presentations/stream-analysis-fp/> . Real-Time Stream Analysis in Functional Reactive Programming

<https://towardsdatascience.com/tracking-nyc-citi-bike-real-time-utilization-using-kafka-streams-1c0ea9e24e79>

<https://www.memsql.com/blog/real-time-analytics-at-uber-scale/>

<https://www.youtube.com/watch?v=kdmAiQeYGgE> Building a real-time analytics pipeline with BigQuery and Cloud Dataflow

## systems


<https://dzone.com/articles/how-to-build-a-google-search-autocomplete> How to Build a Google Search Autocomplete

<https://research.fb.com/publications/scuba-diving-into-data-at-facebook/> Scuba: Diving into Data at Facebook

<https://engineering.fb.com/data-infrastructure/scribe/> Scribe: Transporting petabytes per hour

<https://habr.com/ru/company/oleg-bunin/blog/466295/>

<https://www.vertabelo.com/blog/business-logic-in-the-database-yes-or-no-it-depends/>

<https://news.ycombinator.com/item?id=21032805>

<https://hackernoon.com/best-practices-for-event-driven-microservice-architecture-e034p21lk>

<https://8thlight.com/blog/ignacio-piantanida/2019/09/17/software-architecture.html>

<https://blog.pragmaticengineer.com/operating-a-high-scale-distributed-system/>

<https://herbertograca.com/2019/08/12/documenting-software-architecture/>

<http://blog.cleancoder.com/uncle-bob/2019/08/22/WhyClojure.html>

<https://martinfowler.com/architecture/>

<https://news.ycombinator.com/item?id=20562733>

<https://habr.com/ru/company/piter/blog/461283/> System Design

<https://www.youtube.com/watch?v=ZgdS0EUmn70>


<https://github.com/dagster-io/dagster> Duster

<https://habr.com/ru/post/454668/>


<https://news.ycombinator.com/item?id=22034101> Tools  for “Data Munging / Data Merging”

<https://dagster.readthedocs.io/> Dagster is a system for building modern data applications. 

<https://www.getdbt.com/>

<http://visidata.org/>

<https://github.com/simonw/csvs-to-sqlite> CSV to SQLite

QuestDB is a fast NewSQL database for Hybrid Transactional, Analytical and Time Series processing workloads. Users can interact via HTTP endpoints, our web console, wire protocols (PostgreSQL and Influx) and programmatic APIs. The entire database fits in a dependency-free 3.5mb package and is Open Source under Apache 2.0.
<https://www.questdb.io/>


```
важно разделить бизнес-требования и функциональные требования
Бизнес требования звучат следующим образом:


"Внедрить веб-систему и систему отслеживания сотрудников на базе мобильных устройств, которая фиксирует курьеров на их маршрутах и повышает эффективность за счет мониторинга активности курьеров, их отсутствия на работе и производительности труда."


Тут можно выделить ряд характерных признаков, которые будут указывать, что это требования от бизнеса:


-бизнес-требования всегда написаны с точки зрения клиента;
-это широкие требования высокого уровня, но все же ориентированные на детали;
-они не являются целями компании, но помогают компании достичь целей;
-отвечают на вопросы «почему» и «что». Что хочет компания получить? И почему ей это нужно.

Функциональные требования — это Действия, которые система должна выполнить, для реализации бизнес-требований. 
Таким образом, функциональные требования связаны с разрабатываемым решением или программным обеспечением. 
Сформулируем функциональные требования для вышеуказанного примера:


-система должна отображать долготу и широту сотрудника через GPS/ГЛОНАСС;
-система должна отображать позиции сотрудников на карте;
-система должна позволять менеджерам отправлять уведомления своим подчиненным на местах.

Выделим следующие особенности:

-функциональные требования всегда пишутся с точки зрения системы;
-они более конкретные и подробные;
-именно благодаря выполнению функциональных требований, разрабатывается, эффективное решение, отвечающее потребностям бизнеса и целям клиента;
-отвечают на вопрос «как». Как система решает бизнес требования.

Следует сказать пару слов о нефункциональных требованиях 
(также известных как «требования к качеству»), которые накладывают ограничения на дизайн или реализацию 
(например, требования к производительности, безопасности, доступности, надежности). Такие требования отвечают на вопрос «какой» должна быть система.


Разработка — это перевод бизнес требований в функциональные. 
Прикладное программирование — это реализация функциональных требований, а системное — нефункциональных.
```


<https://boyter.org/2018/03/collection-favorite-optimization-posts-articles/>

System thinking
<https://neilkakkar.com/understanding-systems.html>

<https://news.ycombinator.com/item?id=19832048>

<https://thesystemsthinker.com/>


<https://github.com/mlubinsky/mlubinsky.github.com/blob/master/arc/Designing_Distributed_Systems.pdf> . BOOK

<https://github.com/aphyr/distsys-class>

<https://news.ycombinator.com/item?id=19290069>

<https://rjzaworski.com/2019/03/7-commandments-for-event-driven-architecture>

<https://news.ycombinator.com/item?id=19705461>

<https://habr.com/ru/post/443058/> Clear Architecture

<http://www.tugberkugurlu.com/archive/software-architecture-and-system-design---getting-your-grip-and-some-related-resources>

<https://engineering.videoblocks.com/web-architecture-101-a3224e126947>

<https://www.youtube.com/channel/UCn1XnDWhsLS5URXTi5wtFTA>  system design

<https://www.reddit.com/r/Python/comments/ap5vo7/the_clean_architecture_in_python_an_excellent/>

<https://news.ycombinator.com/item?id=19133097>

<https://habr.com/ru/company/odnoklassniki/blog/437858/>  Проектирование высоконагруженных систем

<https://youtu.be/dE699lHDW7I>

<https://www.youtube.com/watch?v=DSGsa0pu8-k>

<https://queue.acm.org/pastissues.cfm> .  Magazine

<https://www.youtube.com/watch?v=_Hc0WkBUmcQ> Высокопроизводительная и отказоустойчивая архитектура

<https://textbooks.opensuny.org/introduction-to-the-modeling-and-analysis-of-complex-systems/>

<https://news.ycombinator.com/item?id=18908843>

<https://eng.uber.com/aresdb/>

<https://blog.keen.io/architecture-of-giants-data-stacks-at-facebook-netflix-airbnb-and-pinterest-9b7cd881af54>

<https://www.braze.com/perspectives/article/building-braze-job-queues-resiliency>

<https://leanpub.com/clean-architectures-in-python>



<https://habr.com/ru/company/cloud4y/blog/330462/> consensus in distributed systems (Paxos, etc

<https://medium.com/netflix-techblog/implementing-the-netflix-media-database-53b5a840b42a>

<https://medium.com/@tomas.duhourq/building-scalable-analytics-with-aws-part-i-6de6a90e3513> AWS

<https://www.ebayinc.com/stories/blogs/tech/an-approach-for-metadata-store-on-large-volume-data-sets/>

<https://www.tellius.com/building-a-seamless-search-driven-analytics-experience-across-multiple-data-sources-with-apache-spark/>

<https://allegro.tech/2018/10/turnilo-lets-change-the-way-people-explore-big-data.html>

<https://azure.microsoft.com/en-us/blog/microsoft-open-sources-trill-to-deliver-insights-on-a-trillion-events-a-day/>

<https://eng.uber.com/uber-big-data-platform/>

<https://www.youtube.com/watch?v=UzLMhqg3_Wc&list=PLrmLmBdmIlps7GJJWW9I7N0P0rB0C3eY2>

<https://habr.com/company/rostelecom/blog/432166/> NiFi

<https://habr.com/company/yandex/blog/431650/>

### Spotify
<https://labs.spotify.com/2017/10/16/big-data-processing-at-spotify-the-road-to-scio-part-1/>
<https://labs.spotify.com/2017/10/23/big-data-processing-at-spotify-the-road-to-scio-part-2/>
<https://labs.spotify.com/2017/11/20/autoscaling-pub-sub-consumers/>
<https://labs.spotify.com/2013/03/15/backend-infrastructure-at-spotify/>

### Netflix
<https://medium.com/netflix-techblog/evolution-of-the-netflix-data-pipeline-da246ca36905>


## System Design Tools

<https://c4model.com/>

drive.io

<https://news.ycombinator.com/item?id=20096865> System Design Tools

<https://terrastruct.com/>

<https://news.ycombinator.com/item?id=21958986>

## Big Data Architecture

<https://github.com/common-workflow-language/common-workflow-language/wiki/Existing-Workflow-systems>

<https://streamsets.com/blog/>

<https://news.ycombinator.com/item?id=18508284>

<https://blog.gruntwork.io/5-lessons-learned-from-writing-over-300-000-lines-of-infrastructure-code-36ba7fadeac1>

<http://www.smashcompany.com/technology/one-write-point-one-read-point-one-log>

<https://dataissexy.wordpress.com/>

<https://habr.com/company/wrike/blog/430374/>

<https://github.com/rtb7syl/face-kafka> Kafka + Face recognition

<https://www.confluent.io/wp-content/uploads/2016/08/Making_Sense_of_Stream_Processing_Confluent_1.pdf> .  Stream processing  

<https://blog.yugabyte.com/how-yugabytedb-scales-to-more-than-1-million-inserts-per-sec/> 1 mln inserts per sec

## Concurrency

<https://github.com/heathermiller/dist-prog-book/blob/master/chapter/2/futures.md>

<http://nikgrozev.com/2015/07/14/overview-of-modern-concurrency-and-parallelism-concepts/>

<https://slikts.github.io/concurrency-glossary/>

<https://habr.com/post/430672/> concurrency
 
<https://github.com/heathermiller/dist-prog-book/blob/master/chapter/2/futures.md>

<http://nikgrozev.com/2015/07/14/overview-of-modern-concurrency-and-parallelism-concepts/>


<https://medium.com/@NetflixTechBlog/performance-under-load-3e6fa9a60581> . Performance-concurrency

## Pipelines

<https://www.red-gate.com/simple-talk/cloud/cloud-data/current-state-newsqlnosql-cloud-arena/>

<https://turbolent.com/data-processing-pipeline.html>


## Elastic Search
https://datadome.co/store-50-million-event-per-second-in-elasticsearch/

<https://www.elastic.co/blog/the-birthday-paradox-and-concurrently-indexing-in-elasticsearch>

<http://app-from-scratch.darkleaf.ru/> . Clojure

https://habr.com/company/yandex/blog/428700/ .  Model deployment

<https://habr.com/post/429472/> .  Consule SpringBoot Docker Compose

<https://medium.com/stream-processing/what-is-stream-processing-1eadfca11b97>

<https://jeeconf.com/program/50-shades-of-data-how-when-and-why-big-relational-nosql-elastic-graph-event/>

<https://github.com/kaiwaehner/kafka-connect-iot-mqtt-connector-example>

<https://github.com/kaiwaehner/ksql-udf-deep-learning-mqtt-iot>

<https://medium.com/@simon.aubury/machine-learning-kafka-ksql-stream-processing-bug-me-when-ive-left-the-heater-on-bd47540cd1e8>

<https://habr.com/post/427739/>

<https://habr.com/post/428431/>

<https://herbertograca.com/2017/07/03/the-software-architecture-chronicles/>

<https://medium.com/@adhorn/patterns-for-resilient-architecture-part-2-9b51a7e2f10f>

<https://www.youtube.com/watch?v=3UfZN59Nsk8> Dataflow: A Unified Model for Batch and Streaming Data Processing

<https://eng.uber.com/uber-big-data-platform/>



<https://www.cockroachlabs.com/blog/brief-history-high-availability/>



<https://www.youtube.com/watch?v=owTuuVt6Oro> Apache Beam

<https://news.ycombinator.com/item?id=18055002> 

<https://www.youtube.com/watch?v=z1xLDzx7hgw>

<https://www.amazon.com/Release-Design-Deploy-Production-Ready-Software/dp/1680502395> Release it (nigard)

<https://www.amazon.com/Building-Microservices-Designing-Fine-Grained-Systems/dp/1491950358>
sam newman's microservices (o reilly)

<https://www.amazon.com/Just-Enough-Software-Architecture-Risk-Driven/dp/0984618104>
Just enough software architecture (g. fairbanks)

<https://itnext.io/module-oriented-architecture-4b54c8976415>

<https://dataintensive.net/>

<https://medium.com/tag/streaming-analytics/archive>

<https://habr.com/company/jugru/blog/421787/>

<http://highscalability.com/blog/2018/4/9/give-meaning-to-100-billion-events-a-day-the-analytics-pipel.html>

<https://www.confluent.io/blog/putting-power-apache-kafka-hands-data-scientists/>



<https://habr.com/post/353734/> Distributed Architecture

<https://www.youtube.com/user/profyclub/videos>    HiLoad russian conf  


<https://thingsboard.io/docs/reference/architecture/> .   IoT


<https://www.jowanza.com/blog/2018/9/8/real-time-station-tracking-ford-gobike-and-mapd>

<https://multithreaded.stitchfix.com/blog/2018/09/05/datahighway/>

https://medium.com/hydrosphere-io/machine-learning-models-monitoring-architectures-part-0-ec58e338d87f

<http://www.georgefairbanks.com/e-book/>

<https://github.com/donnemartin/system-design-primer>

https://www.youtube.com/watch?v=x30DcBfCJRI

https://www.youtube.com/watch?v=t2Ti-pZGy8I

<https://quickbooks-engineering.intuit.com/re-think-your-data-pipelines-in-the-decoupled-era-5b032bc8b779>

https://www.youtube.com/watch?v=tpspO9K28PM&t=155s

https://github.com/gaia-pipeline/gaia

https://github.com/Jeffail/benthos

<http://www.acodersjourney.com/2018/07/system-design-interview-load-balancing/>

https://engineering.videoblocks.com/web-architecture-101-a3224e126947

https://news.ycombinator.com/item?id=17522362

https://the-cloud-book.com/

https://www.goodreads.com/book/show/25686275-the-art-of-scalability

https://www.goodreads.com/book/show/18043011-clean-architecture

## Jenkins
https://www.automationqc.com/jenkins-pipeline-for-beginners/

https://godaddy.github.io/2018/06/05/cicd-best-practices/
