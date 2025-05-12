https://www.udemy.com/course/google-cloud-fundamentals-101-a-quick-guide-to-learn-gcp/

https://cloud.google.com/sql/docs Cloud SQL is a fully-managed database service that helps you set up, maintain, manage, and administer your relational databases on Google Cloud Platform.

You can use Cloud SQL with MySQL, PostgreSQL, or SQL Server.

https://medium.com/tag/gcp

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
Это самый низкий уровень, который может предложить поставщик облачных услуг, и он включает провайдера облачных вычислений, поставляющего «голую» инфраструктуру, 
включая промежуточное программное обеспечение, сетевые кабели, процессоры, графические процессоры, оперативную память, внешнее хранилище, с
ерверы и образы базовых операционных систем, например, Debian Linux, CentOS, Windows и т. д.
C GCE вы можете свободно создавать виртуальные машины, распределять ресурсы процессора и памяти, выбирать тип хранилища,
 например SSD или HDD, а также объем памяти. Это почти так же, как если бы вы создали свой собственный компьютер/рабочую станцию и занимались всеми деталями его работы.
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

SaaS представляет собой наиболее распространенные сервисы, предоставляемые поставщиками облачных услуг. Они предназначены для конечных пользователей и доступны главным образом через веб-сайты, например Gmail, Google Docs, Dropbox и т. д. Что касается Google Cloud, есть несколько предложений вне их вычислительного стека, которые являются SaaS. К ним относятся Data Studio, Big Query и т. д.


```
Dataproc is a fully managed and highly scalable service for running Apache Hadoop, Apache Spark, Apache Flink,
Presto, and 30+ open source tools and frameworks. Use Dataproc for data lake modernization, 
ETL, and secure data science, at scale, integrated with Google Cloud, at a fraction of the cost.
```
https://console.cloud.google.com/

https://habr.com/ru/hubs/googlecloud/articles/

###  Google Kubernetes Engine (GKE)

https://cloud.google.com/kubernetes-engine/

B более общем смысле GKE можно отнести к категории «Контейнер как услуга» (CaaS), иногда называемой «Kubernetes как услуга» (KaaS), который позволяет клиентам легко запускать свои Docker-контейнеры в полностью управляемой среде Kubernetes
 
### Google App Engine (GAE)

```
Как упомянуто в разделе 2.2, PaaS находится выше IaaS, и в случае GCP его также можно рассматривать как предложение над GKE. GAE — это специализированный Google PaaS,
 и как они сами лучше всего описывают себя — «несите ваш код, а мы позаботимся обо всем остальном».

Это гарантирует, что клиенты, использующие GAE, не должны иметь дело с базовым аппаратным/промежуточным программным обеспечением,
и уже могут иметь предварительно настроенную платформу, готовую к работе; все, что им нужно сделать, это предоставить код, необходимый для его запуска.

GAE автоматически обрабатывает масштабирование, чтобы удовлетворить нагрузку и спрос со стороны пользователей,
что означает, что если ваш сайт, продающий цветы, внезапно достигнет пика, потому что приближается день святого Валентина,
GAE будет обрабатывать масштабирование базовой инфраструктуры, чтобы удовлетворить спрос и гарантировать, что ваш веб-сайт не упадет из-за возросшего спроса.
Это означает, что вы платите именно за те ресурсы, которые требуются вашему приложению в данный момент.


GAE использует Kubernetes или его встроенную версию, чтобы справиться со всем этим, чтобы вам не пришлось об этом заботиться.
 GAE лучше всего подходит для компаний, которые не заинтересованы в базовой инфраструктуре и заботятся только о том, чтобы их приложение было доступно наилучшим образом.
```
Мой опыт с экзаменами GCP: Associate, Architect, Network
https://habr.com/ru/articles/543122/



### Построение ML-пайплайна для рекомендательной системы с помощью Google Cloud Platform
 https://habr.com/ru/companies/neoflex/articles/767220/

 Cloud Composer* (он же Airflow) 

https://cloud.google.com/vertex-ai/docs
  Vertex AI, облачную платформу машинного обучения от Google


https://habr.com/ru/companies/softline/articles/319704/

  
