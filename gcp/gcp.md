https://www.udemy.com/course/google-cloud-fundamentals-101-a-quick-guide-to-learn-gcp/

https://www.citadelcloudmanagement.com/wp-content/uploads/2023/05/2a1631cf2dcc736f8330e7d54571ba13Google-Cloud-Platform-in-Action-PDFDrive-.pdf

https://cloud.google.com/docs

https://cloud.google.com/products

https://www.reddit.com/r/googlecloud/

https://cloud.google.com/architecture/migrate-aws-lambda-to-cloudrun

https://cloud.google.com/run/docs/ Cloud Run is a fully managed application platform that lets you run containers that are invocable via requests or events. Cloud Run is serverless: it abstracts away all infrastructure management, so you can focus on what matters most—building great applications

### DataFlow
 https://cloud.google.com/dataflow/  
https://habr.com/ru/companies/google/articles/323908/  
http://research.google.com/pubs/pub43864.html  


```
Dataflow is a fully managed service that uses open source Apache Beam SDK to enable advanced streaming use cases at enterprise scale.
It offers rich capabilities for state and time, transformations, and I/O connectors.
 Dataflow scales to 4K workers per job and routinely processes petabytes of data.
It features autoscaling for optimal resource utilization in both batch and streaming pipelines.
```


### Cloud SQL
https://cloud.google.com/sql/docs Cloud SQL is a fully-managed database service that helps you set up, maintain, manage, and administer your relational databases on Google Cloud Platform.

You can use Cloud SQL with MySQL, PostgreSQL, or SQL Server.



https://cloud.google.com/pubsub/docs/overview
```
Comparing Pub/Sub to other messaging technologies
Pub/Sub combines the horizontal scalability of Apache Kafka and Pulsar with features found in messaging middleware
such as Apache ActiveMQ and RabbitMQ. Examples of such features are dead-letter queues and filtering.

Note: Google Cloud Managed Service for Apache Kafka is available. If you're considering a migration from Kafka to Pub/Sub,
 consult this migration guide.
Another feature that Pub/Sub adopts from messaging middleware is per-message parallelism, rather than partition-based messaging.
Pub/Sub "leases" individual messages to subscriber clients, then tracks whether a given message is successfully processed.

By contrast, other horizontally scalable messaging systems use partitions for horizontal scaling.
This forces subscribers to process messages in each partition in order and limits the number of concurrent clients to the number of partitions.
Per-message processing maximizes the parallelism of subscriber applications, and helps ensure publisher and subscriber independence.
```

https://medium.com/tag/gcp

### Dataproc
```
Dataproc is a fully managed and highly scalable service for running Apache Hadoop, Apache Spark, Apache Flink,
Presto, and 30+ open source tools and frameworks. Use Dataproc for data lake modernization, 
ETL, and secure data science, at scale, integrated with Google Cloud, at a fraction of the cost.
```
https://cloud.google.com/dataproc

https://cloud.google.com/dataproc#documentation

https://medium.com/@study7vikas/google-cloud-architect-learning-day-42-642a4658221d

### Terraform
 https://developer.hashicorp.com/terraform/intro 

```
HashiCorp Terraform is an infrastructure as code tool that lets you define both cloud and on-prem resources in human-readable configuration files
that you can version, reuse, and share.
You can then use a consistent workflow to provision and manage all of your infrastructure throughout its lifecycle.
 Terraform can manage low-level components like compute, storage, and networking resources, as well as high-level components
 like DNS entries and SaaS features.
```
https://habr.com/ru/companies/timeweb/articles/769010/


### Инфраструктура как услуга (IaaS)
 Google Compute Engine (GCE) — IaaS  
```
Это самый низкий уровень, который может предложить поставщик облачных услуг, и он включает провайдера облачных вычислений, п
оставляющего «голую» инфраструктуру, 
включая промежуточное программное обеспечение, сетевые кабели, процессоры, графические процессоры, оперативную память, внешнее хранилище, с
ерверы и образы базовых операционных систем, например, Debian Linux, CentOS, Windows и т. д.
C GCE вы можете свободно создавать виртуальные машины, распределять ресурсы процессора и памяти, выбирать тип хранилища,
 например SSD или HDD, а также объем памяти.
Это почти так же, как если бы вы создали свой собственный компьютер/рабочую станцию и занимались всеми деталями его работы.
```
https://cloud.google.com/compute/docs/machine-types

### Платформа как услуга (PaaS)
```
PaaS включает в себя только поставщика облачных услуг, предлагающего определенную платформу, на которой пользователи могут создавать приложения. 
Это абстракция над IaaS, означающая, что поставщик облака берет на себя все детали типов ЦП, памяти, ОЗУ, хранилища, сетей и т. д. 
Как показано на рисунке 2, вы, как клиент, имеете небольшой контроль над реальной платформой, поскольку облачный провайдер занимается всеми деталями инфраструктуры за вас. 
Вы запрашиваете выбранную платформу и собираете на ней проект. 
Примерам PaaS являютс Heroku, Google App Engine
```
https://cloud.google.com/sdk/docs/install
 Google Cloud CLI includes the gcloud, gsutil and bq command-line tools
https://medium.com/@asmitha23052002/uploading-files-to-google-cloud-storage-gcs-using-the-gsutil-command-line-tool-71bca0a2b731

Gsutil is deprecated - you need to move to using gcloud storage instead
https://cloud.google.com/storage/docs/discover-object-storage-gcloud

```python
from google.cloud import storage

# Initialize a client
client = storage.Client()

# List all buckets
buckets = client.list_buckets()
for bucket in buckets:
    print("Bucket name:", bucket)
```

### Программное обеспечение как услуга (SaaS)
```
SaaS представляет собой наиболее распространенные сервисы, предоставляемые поставщиками облачных услуг.
Они предназначены для конечных пользователей и доступны главным образом через веб-сайты, например Gmail, Google Docs, Dropbox и т. д.
 Что касается Google Cloud, есть несколько предложений вне их вычислительного стека, которые являются SaaS. К ним относятся Data Studio, Big Query и т. д.
```

https://console.cloud.google.com/

https://habr.com/ru/hubs/googlecloud/articles/

###  Google Kubernetes Engine (GKE)

https://cloud.google.com/kubernetes-engine/

B более общем смысле GKE можно отнести к категории «Контейнер как услуга» (CaaS), иногда называемой «Kubernetes как услуга» (KaaS), который позволяет клиентам легко запускать свои Docker-контейнеры в полностью управляемой среде Kubernetes
 
### Google App Engine (GAE)

```
PaaS находится выше IaaS, и в случае GCP его также можно рассматривать как предложение над GKE.
GAE — это специализированный Google PaaS,
 и как они сами лучше всего описывают себя — «несите ваш код, а мы позаботимся обо всем остальном».

Это гарантирует, что клиенты, использующие GAE, не должны иметь дело с базовым аппаратным/промежуточным программным обеспечением,
и уже могут иметь предварительно настроенную платформу, готовую к работе;
все, что им нужно сделать, это предоставить код, необходимый для его запуска.

GAE автоматически обрабатывает масштабирование, чтобы удовлетворить нагрузку и спрос со стороны пользователей,
что означает, что если ваш сайт, продающий цветы, внезапно достигнет пика, потому что приближается день святого Валентина,
GAE будет обрабатывать масштабирование базовой инфраструктуры, чтобы удовлетворить спрос и гарантировать,
что ваш веб-сайт не упадет из-за возросшего спроса.
Это означает, что вы платите именно за те ресурсы, которые требуются вашему приложению в данный момент.


GAE использует Kubernetes или его встроенную версию, чтобы справиться со всем этим, чтобы вам не пришлось об этом заботиться.
 GAE лучше всего подходит для компаний, которые не заинтересованы в базовой инфраструктуре и заботятся только о том,
чтобы их приложение было доступно наилучшим образом.
```
Мой опыт с экзаменами GCP: Associate, Architect, Network
https://habr.com/ru/articles/543122/



### Построение ML-пайплайна для рекомендательной системы с помощью Google Cloud Platform
 https://habr.com/ru/companies/neoflex/articles/767220/

 Cloud Composer* (он же Airflow) 

https://cloud.google.com/vertex-ai/docs
  Vertex AI, облачную платформу машинного обучения от Google


https://habr.com/ru/companies/softline/articles/319704/

  
