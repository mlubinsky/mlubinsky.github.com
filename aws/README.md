<https://codereview.stackexchange.com/questions/tagged/amazon-web-services>

Для подключения к инстансу EC2 необходим закрытый ключ. Скачайте его (расширение .pem) из панели управления Amazon EC2 и измените разрешения 

chmod 400 my-ec2-ssh-key.pem 

Храните ключ в надёжном месте или поместите его в свою папку ~/.ssh/.

 ssh -i ~/.ssh/my-ec2-key.pem ubuntu@my-ec2-public
 
 scp -i myAmazonKey.pem phpMyAdmin-3.4.5-all-languages.tar.gz ec2-user@mec2-50-17-16-67.compute-1.amazonaws.com:~/.


<https://habr.com/ru/company/otus/blog/468185/> .  AWS EC2

<https://habr.com/ru/company/otus/blog/466519/> . Детальный разбор AWS Lambda

<https://habr.com/ru/company/oleg-bunin/blog/471686/>

https://aws.amazon.com/about-aws/whats-new/2019/09/aws-transfer-for-sftp-now-supports-logical-directories-for-amazon-s3/

### EMR

Hive Version for emr-5.21.1 is: 2.3.4

<https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-hive.html>

<https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-whatsnew-history.html>

<https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-release-5x.html>

###  S3 
Amazon S3 is a simple key-based object store. When you store data, you assign a unique object key that can later be used to retrieve the data. Keys can be any string, and they can be constructed to mimic hierarchical attributes. Alternatively, you can use S3 Object Tagging to organize your data across all of your S3 buckets and/or prefixes.

<https://aws.amazon.com/s3/faqs/>
<https://news.ycombinator.com/item?id=21170652> A command line utility that allows you to stream data from multiple S3 objects directly into your terminal
<https://www.npmjs.com/package/s3st>

## Athena
<https://www.transposit.com/blog/2019.08.22-try-athena-easily-with-a-transposit-app/?c=lob>

<https://medium.com/swlh/tutorial-build-your-data-lake-using-aws-s3-athena-150c1aaa44cf>

<https://www.mungingdata.com/aws/athena-spark-best-friends>

<https://habr.com/ru/company/mailru/blog/456392/>

 ## Redshift
 
 <https://github.com/JefClaes/amazon-redshift-fundamentals> 
 
 <https://tech.iheart.com/how-we-leveraged-redshift-spectrum-for-elt-in-our-land-of-etl-cf01edb485c0>
 
 <https://blog.panoply.io/aws-redshift-tutorial>
<https://www.intermix.io/blog/short-query-acceleration/>
<https://medium.com/teads-engineering/give-meaning-to-100-billion-events-a-day-part-ii-how-we-use-and-abuse-redshift-to-serve-our-data-bc23d2ed3e07>
<https://www.intermix.io/blog/14-data-pipelines-amazon-redshift/>
<https://epiphany.pub/post?refId=a362fd3bffdc7eecde1838916fb8f4c267f5672b3774bd86dd23dce9dac72bee> hate log
<https://www.intermix.io/blog/modern-etl-tools-for-amazon-redshift/>
<https://medium.com/@thejaravi/how-we-leveraged-redshift-spectrum-for-elt-in-our-land-of-etl-cf01edb485c0>

 Redshift Spectrum is new add-on service for Redshift that Amazon introduced mid-2017. It allows you to leverage Redshift to query data directly on S3. Redshift Spectrum is a good option for those who already have/work with Redshift. For those who do not, take a look at Athena. Athena is much like Redshift Spectrum with the exception of the chosen execution engine (Athena uses Presto) whereas Spectrum uses Redshift. It should be noted that Spectrum also follows pay-per-query pricing model like Athena.
Let’s look at how Redshift and Spectrum communicate with each other, how tables are created on top of stores such as S3 and just how much interoperability is provided.
Spectrum needs an external meta store for the data catalog to maintain table definitions; we used a Hive meta store for this purpose. Our Hive/Spectrum meta store is simply a RDS instance running MariaDB. Once we setup Spectrum to talk with our Redshift cluster and use the newly created schema space in the Hive meta store, any external table created in this schema using Hive is visible and usable immediately from Redshift. You can query these tables directly from Redshift and Redshift/Spectrum will automatically move the required portion of data (based on the query) on to Redshift cluster and execute it there.
 

## REST API
<https://habr.com/post/435180/> Бессерверный REST API 

## Lambda

<https://habr.com/ru/post/457100/>

<http://veekaybee.github.io/2018/09/24/the-case-of-the-broken-lambda/>

<https://stackabuse.com/automating-aws-ec2-management-with-python-and-boto3/>

Lambda example
```
  import os,sys
  import boto3
  from my_submodule.models MyModels
  
  def handler(event, context):
    ..
```

<https://www.expeditedssl.com/aws-in-plain-english>

<https://habr.com/post/421991/> free AWS

<https://news.ycombinator.com/item?id=18042382>  DB on AWS


## Flask on AWS

<https://towardsdatascience.com/deploying-a-python-web-app-on-aws-57ed772b2319>

<https://blog.apcelent.com/deploy-flask-aws-lambda.html>

<https://www.codementor.io/dushyantbgs/deploying-a-flask-application-to-aws-gnva38cf0> 

<https://imrankhan17.github.io/pages/flask.html> 

<https://medium.com/@rodkey/deploying-a-flask-application-on-aws-a72daba6bb80>

<https://www.datasciencebytes.com/bytes/2015/02/24/running-a-flask-app-on-aws-ec2/>

<https://linuxacademy.com/blog/amazon-web-services-2/deploying-a-containerized-flask-application-with-aws-ecs-and-docker/>




<https://habr.com/company/jugru/blog/417943/> . Serverless и React 

<https://www.infoq.com/presentations/serverless-architecture-patterns>

<https://docs.aws.amazon.com/lambda/latest/dg/invoking-lambda-function.html>


<https://blog.sqreen.io/streaming-data-amazon-kinesis/>

<https://read.iopipe.com/lessons-from-building-a-serverless-data-pipeline-with-aws-kinesis-and-lambda-4d8cf0ebcbc9>

<https://www.confluent.io/blog/decoupling-systems-with-apache-kafka-schema-registry-and-avro/>

<https://towardsdatascience.com/from-big-data-to-micro-services-how-to-serve-spark-trained-models-through-aws-lambdas-ebe129f4849c>


<https://aws.amazon.com/blogs/opensource/data-processing-pipeline-kinesis-kubeless/>

## ML on AWS
<https://aws.amazon.com/iot-analytics/>

<https://aws.amazon.com/blogs/machine-learning/forecasting-time-series-with-dynamic-deep-learning-on-aws/>

<https://github.com/aws-samples/serverless-sagemaker-orchestration>

<https://towardsdatascience.com/brewing-up-custom-ml-models-on-aws-sagemaker-e09b64627722>

<https://www.studio.ml/zero-overhead-scalable-machine-learning-part-2/>

<https://medium.com/akeneo-labs/machine-learning-workflow-with-sagemaker-b83b293337ff>

<https://www.pluralsight.com/courses/tensorflow-aws-azure-gcp-deploying-models>

<https://www.udemy.com/aws-machine-learning-a-complete-guide-with-python/>

<https://github.com/awslabs/amazon-sagemaker-examples>

<https://github.com/Kenza-AI/sagify>

<https://mc.ai/training-and-deploying-ml-dl-models-on-aws-sagemaker-made-simple/>

<http://sujitpal.blogspot.com/2018/04/aws-ml-week-and-adventures-with.html>

<https://medium.com/@julsimon>
<https://towardsdatascience.com/how-to-deploy-a-machine-learning-model-on-aws-lambda-24c36dcaed20>

<https://aws.amazon.com/blogs/machine-learning/train-and-host-scikit-learn-models-in-amazon-sagemaker-by-building-a-scikit-docker-container/>

<https://pypi.org/project/sagemaker/>

<https://github.com/rtlee9/serveit/>

<https://github.com/awslabs/amazon-sagemaker-examples/tree/master/advanced_functionality/scikit_bring_your_own/container>

<https://medium.com/@julsimon/mastering-the-mystical-art-of-model-deployment-c0cafe011175>

<https://towardsdatascience.com/how-to-deploy-a-machine-learning-model-on-aws-lambda-24c36dcaed20>

<https://www.slideshare.net/AmazonWebServices/realtime-analytics-using-data-from-iot-devices-aws-online-tech-talks>

<https://aws.amazon.com/quickstart/architecture/aws-industrial-time-series-data-connector/>

<https://aws.amazon.com/blogs/iot/using-aws-iot-for-predictive-maintenance/>

<https://cloudacademy.com/learning-paths/cloud-academy-introduction-to-machine-learning-on-aws-126/>

<https://cloudacademy.com/learning-paths/cloud-academy-applying-machine-learning-and-ai-services-on-aws-181/>

<https://aws.amazon.com/blogs/machine-learning/forecasting-time-series-with-dynamic-deep-learning-on-aws/>



## Postgres on AWS

<https://www.percona.com/blog/2018/07/17/when-should-i-use-amazon-aurora-and-when-should-i-use-rds-mysql/>

<https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_PostgreSQL.html>

<https://gist.github.com/juliandunn/15ac4d5e1c96645ee133> 

<https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/rds-metricscollected.html>

<https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.PostgreSQL.CommonDBATasks.html>

<https://blog.dbi-services.com/postgresql-on-amazon-rds-configuring-the-beast/> Parameter Groups

## MySQL benchmarking

<https://dev.to/frosnerd/deploying-and-benchmarking-an-aws-rds-mysql-instance-2faf>  

## AWS

<https://www.imaginarycloud.com/blog/aws-gold-infrastructure/>

<https://habr.com/company/jugru/blog/417943/>

<https://tech.trivago.com/2018/07/13/aws-kinesis-with-lambdas-lessons-learned/>

<https://hackernoon.com/a-crash-course-on-serverless-apis-with-express-and-mongodb-77774f7730fe>

<https://news.ycombinator.com/item?id=17523480>

<https://www.youtube.com/watch?v=mUzsYt3Bj08> AWS Docker

<https://read.acloud.guru/> Cloud guru 

<https://www.slideshare.net/AmazonWebServices/getting-started-on-aws-awsome-day-dallas-2018>

<https://epsagon.com/blog/lambda-internals-part-2-going-deeper>

<https://epsagon.com/blog/how-to-make-lambda-faster-memory-performance-benchmark>

<https://medium.freecodecamp.org/the-best-ways-to-test-your-serverless-applications-40b88d6ee31e>

### SQS simple queue service (poll). SNS - pub/sub (push)

<https://epsagon.com/blog/how-to-setup-aws-lambda-with-sqs>

<https://dev.to/frosnerd/event-handling-in-aws-using-sns-sqs-and-lambda-2ng>    SNS SQS

<https://dev.to/adnanrahic/how-to-deploy-a-nodejs-application-to-aws-lambda-using-serverless-2nc7>

 <https://habr.com/company/abdoc/blog/352856/>
 
 
 ## TerraForm
 <https://habr.com/ru/post/450410/>
 
 ## TerraForm vs CloudFormation
 
 <https://habr.com/company/jugru/blog/420661/> 
 
 <https://medium.com/@bradford_hamilton/deploying-containers-on-amazons-ecs-using-fargate-and-terraform-part-2-2e6f6a3a957f>
 
 До недавнего времени разработка бессерверных приложений сильно осложнялась тем, что не было средств полноценного локального тестирования lambda-функций и API. 
При создании приложений нужно было или работать все время онлайн, редактируя код в браузере, 
или постоянно архивировать и загружать в облако исходный код lambda-функций. 

Летом 2017 произошел прорыв. AWS создал новый упрощенный стандарт шаблонов CloudFormation, который они назвали Serverless Application Model (SAM) и одновременно 
запустили проект sam-local. Обо всем по порядку.

Amazon CloudFormation — это такой сервис, который позволят описывать всю нужную для вашего приложения инфраструктуру AWS с помощью файла шаблона в формате JSON или YAML. 
Это очень-очень удобная штука. Потому что без нее вам нужно вручную через веб-консоль или командный интерфейс 
создавать множество нужных вам ресурсов: ламбда-функции, база данных, API, роли и политики… 

С помощью CloudFormation инфраструктуру можно нарисовать или в специальном дизайнере, или написать ее руками в шаблоне. 
 В любом случае в итоге получается файл шаблона, 
с помощью которого дальше можно в пару-тройку кликов или одной командой поднять все, что нужно для приложения. 
А дальше при необходимости вносить изменения в этот шаблон и применять их опять же одной командой. 
Это делает поддержку инфраструктуры приложения гораздо легче. Получается, инфраструктура, как код.

CloudFormation прекрасен, его шаблоны позволяют описать практически 100% ресурсов AWS. Но из-за его универсальности это достаточно «многословный» формат — 
шаблоны могут быстро вырастать до приличных размеров. Осознавая это и преследуя цель сделать создание бессерверных приложений проще, AWS создали новый формат SAM. 

Можно условно считать, что обычные шаблоны CloudFormation пишутся на языке низкого уровня. 
А шаблоны SAM — на языке высокого уровня, таким образом, позволяя 
описывать инфраструктуру бессерверных приложений при помощи упрощенного синтаксиса. 
 Шаблоны SAM трансформируются CloudFront в обычные шаблоны при деплое.

Что же такое sam-local? Это инструмент командной строки, позволяющий работать локально с бессерверными приложениями, описанными шаблонами SAM. 
Sam-local позволяет тестировать lambda-функции, генерировать события от различных сервисов AWS, запускать API Gateway, проверять шаблоны SAM — и всё это локально!

Sam-local использует docker-контейнер для эмуляции API Gateway и Lambda. Принцип работы следующий. При запуске sam-local ищет файл шаблона SAM папке проекта. 
 Он анализирует файл шаблона и запускает в docker-контейнере выделенные в шаблоне ресурсы: открывает API и подключает к ним ламбда-функции. 
 Причем поддержка очень близкая к работе реальных lambda-функций 
 (лимиты, показывается объем использованной памяти и длительность выполнения). 
          
 <https://github.com/open-guides/og-aws>
 
 <https://epsagon.com/blog/how-to-handle-aws-lambda-errors-like-a-pro>
 
 <https://news.ycombinator.com/item?id=17064676>
 
 <https://www.serverlessops.io/blog/serverless-ops-aws-lambda-serverless-development-workflow>
 
 <https://medium.com/epsagon/the-right-way-to-distribute-messages-effectively-in-serverless-applications-f427e4229e67>
 
 <https://medium.com/epsagon/aws-lambda-internals-part-2-going-deeper-1e12b9d2515f>
 
 <https://blog.sourcerer.io/full-guide-to-developing-rest-apis-with-aws-api-gateway-and-aws-lambda-d254729d6992>
 
 <https://servers.lol>
 
 <https://serverless.com/>
 
 <https://habr.com/company/funcorp/blog/354394/> AWS
 
 <https://read.acloud.guru/six-months-of-serverless-lessons-learned-f6da86a73526> 
 
 <https://www.jefclaes.be/2017/12/passing-aws-certified-solutions.html>  AWS exam
 

 
 <https://www.rainerhahnekamp.com/en/single-instance-ecs-setup/>
 
 <https://itnext.io/creating-a-blueprint-for-microservices-and-event-sourcing-on-aws-291d4d5a5817>
 
 <https://www.nodexplained.com/blog-detail/2018/04/27/explore-the-amazon-web-services-management-console>
 
 <https://medium.com/epsagon/lambda-internals-exploring-aws-lambda-462f05f74076>   AWS
 
 <https://itnext.io/creating-a-blueprint-for-microservices-and-event-sourcing-on-aws-291d4d5a5817>
 
 <https://blog.sicara.com/deploy-serverless-lambda-s3-api-aws-2cf99b8f34ae>
 
 <https://itnext.io/create-ftp-on-aws-ec2-f6e57d4d7f25>  FTP on AWS
 
 <https://loige.co/aws-command-line-s3-content-from-stdin-or-to-stdout/>
 
 <https://read.acloud.guru/how-we-built-a-big-data-analytics-platform-on-aws-for-100-large-users-for-under-2-a-month-b37425b6cc4>
 
 <https://www.javacodegeeks.com/tag/amazon-aws>
 
 
