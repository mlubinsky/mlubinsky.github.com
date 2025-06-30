https://habr.com/ru/articles/809195/ certification

https://aws.plainenglish.io/i-have-asked-this-ssh-question-in-every-aws-interview-and-heres-the-catch-ee2013a83e99

https://aws.amazon.com/es/blogs/training-and-certification/inside-look-at-the-new-ai-and-ml-aws-certifications/


https://www.reddit.com/r/databricks/

### AWS learning

https://explore.skillbuilder.aws/learn/catalog

https://explore.skillbuilder.aws/learn/mycourses Machine Learning Plan (I enrolled)

Free Amazon (AWS) Courses & Certificates.

 

Let's check out the top 8 courses for 2025:⤵️ 

1. Introduction to Artificial Intelligence

Artificial intelligence (AI), its significance, machine learning, deep learning, and Amazon's application of AI in its products are all covered in this course.

🔗https://lnkd.in/gghgJzXC


2. Introduction to Blockchain

Beginners who are curious in how blockchain may benefit businesses should take this course. 
 
It goes over the main ideas, advantages, and practical applications of blockchain technology.

🔗https://lnkd.in/gUNF35Ck


3. Data Analytics Learning Plan

This Learning Plan aids professionals in designing, building, securing, and maintaining analytics solutions, aiding in data analysis and preparing for the AWS Certified Data Analytics - Specialty exam.

🔗https://lnkd.in/gVDphkpn


4. DevOps Engineer Learning Plan

Professionals may swiftly and securely launch apps on AWS with the aid this learning plan. To help you get ready for the AWS Certified DevOps Engineer exam, it covers CI/CD, version control, and infrastructure as code.

🔗https://lnkd.in/gJT3zZts


5. Getting Started with DevOps on AWS

This course is intended for technical learners who want to understand the fundamentals of AWS DevOps. 
 
You will investigate the methods, procedures, and equipment employed in a DevOps setting.

🔗 https://lnkd.in/gJT3zZts


6. Machine Learning Terminology and Process

This course covers fundamental machine learning principles and data processing techniques, examining popular concepts approaches in machine learning projects, providing detailed explanations of each phase.

🔗 https://lnkd.in/gJ2gF_pr


7. Machine Learning Plan

It offers virtual instruction in cloud computing and machine learning services to get you ready for the AWS Certified Machine Learning - Specialty test.

🔗https://lnkd.in/gVzidHYX


8. AWS Cloud Quest: Cloud Practitioner


### Asure databricks learning

https://www.databricks.com/resources/webinar/azure-databricks-free-training-series-track

### GCP

Dataproc is a fully managed and highly scalable service for running Apache Spark, Apache Flink, Presto, and 30+ open source tools and frameworks. 

https://cloud.google.com/dataproc

https://habr.com/ru/post/117146/

https://www.everand.com/book/431727414/Google-Cloud-Platform-for-Data-Engineering-From-Beginner-to-Data-Engineer-using-Google-Cloud-Platform 

https://googlecloudcheatsheet.withgoogle.com/

https://cloud.google.com/blog/topics/developers-practitioners/introducing-google-cloud-architecture-diagramming-tool

### Azure

Learn Azure  for free from MS
https://habr.com/ru/company/microsoft/blog/503462/

https://azure.microsoft.com/en-us/free/search/?OCID=AID2000129_OLA_23943940_270839230_130845605&dclid=CImGtNrTpeoCFQMqrQYd4dYHbA


### AWS Lambda

https://medium.com/swlh/lambda-internals-exploration-ae6c21d9521e

https://towardsdatascience.com/aws-lambda-integration-with-snowflake-426debc9ec3a

### STEP function

https://juhache.substack.com/p/all-you-need-is-a-step-function?r=l9wvi

https://asrathore08.medium.com/long-running-jobs-in-step-function-with-system-manager-and-lambda-f6b2543719f3

### AWS  cheatsheets

https://www.youtube.com/watch?v=FDEpdNdFglI Intro to AWS - The Most Important Services To Learn


https://www.datadoghq.com/resources/datadog-lambda-cheatsheet/

https://www.datadoghq.com/resources/datadog-ec2-cheatsheet/

### Remove S3 bucket

aws s3 rm --recursive xxx

### S3 explained

https://www.youtube.com/watch?v=BecRFTzjXA8  (rus)

https://habr.com/ru/company/cloud4y/blog/681376/

https://habr.com/ru/companies/selectel/articles/822855/ S3 + python

https://blog.plerion.com/things-you-wish-you-didnt-need-to-know-about-s3/

https://calpaterson.com/s3.html

https://lobste.rs/s/t9d5z4/s3_is_files_not_filesystem

https://news.ycombinator.com/item?id=39656657

###  Scalable analytics with AWS

https://aws.amazon.com/ec2/instance-types/

https://www.youtube.com/watch?v=uQdzcIf_KII .  AWS Full Course In 11 Hours 

https://medium.com/@tomas.duhourq/building-scalable-analytics-with-aws-part-i-6de6a90e3513

https://iamondemand.com/blog/how-to-setup-lambda-using-only-the-aws-cli/ 

https://github.com/hseera/aws-python-utilities.  AWS Python utils


https://blog.serverlessq.com/aws-sns-vs-sqs-what-are-the-main-differences

### aws config
```
[DYNAMO]$ cat  ~/.aws/config
[default]
region = us-west-2
output = json
[DYNAMO]$ cat  ~/.aws/credentials
[default]
aws_access_key_id = YourKeyId
aws_secret_access_key = YourSecretAccessKey
```

https://github.com/hseera/aws-python-utilities

### DynamoDB
https://www.dynamodbbook.com/ book
https://www.dynamodbguide.com/key-concepts   
https://www.alexdebrie.com/posts/dynamodb-paper
https://www.alexdebrie.com/posts/dynamodb-partitions/
https://www.alexdebrie.com/posts/dynamodb-one-to-many/#denormalization-by-using-a-complex-attribute
```
A single DynamoDB item cannot exceed 400KB of data
The second type of primary key is a composite primary key. 
A composite primary key consists of two elements: a partition key and a sort key. 

89 million requests per second is a big database by any standards (and that's just Amazon's use of DynamoDB)!

Under the hood, DynamoDB is splitting your data into partitions, which are independent storage segments of roughly 10GB in size. 
DynamoDB uses the partition key to assign your items to a given partition,
An individual partition is actually a set of three partition instances in different availability zones which form a replication group. 
One of the instances is the leader for a given partition and is responsible for handling all writes. 
When a write comes in, the leader writes it locally and ensures it is commited to at least one additional replica before returning to the client. 
This increases durability in the event of failure, as the loss of one node will not result in loss of data.

Коллекция элементов в DynamoDB относится ко всем элементам в таблице или индексе, которые имеют общий ключ раздела (partition key).

На примере ниже у нас есть таблица DynamoDB, которая содержит актеров и фильмы, в которых они играли.
Основной ключ является составным, где ключ раздела - имя актера, а ключ сортировки - название фильма.
```
https://habr.com/ru/articles/732578/

https://www.dynamodbbook.com/

https://news.ycombinator.com/item?id=32094046

https://github.com/dineshsonachalam/Lucid-Dynamodb

https://www.usenix.org/system/files/atc22-vig.pdf

https://medium.com/duda/dynamodb-everything-you-need-to-know-about-single-table-design-3535a3d4f024

```
aws dynamodb list-tables --endpoint-url http://localhost:8000
aws dynamodb describe-table --table-name Music  --endpoint-url http://localhost:8000
```
Global and local secondary indexes:
https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/bp-indexes-general.html

https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/getting-started-step-6.html

Time Series:
https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/bp-time-series.html

https://www.youtube.com/watch?v=HaEPXoXVf2k

https://amazon-dynamodb-labs.com 

https://amazon-dynamodb-labs.com/design-patterns/ex8streams.html

https://medium.com/nerd-for-tech/asynchronous-api-with-dynamodb-streams-4117776f2fa4. Streams

https://www.freecodecamp.org/news/ultimate-dynamodb-2020-cheatsheet/

https://intellipaat.com/blog/amazon-aws-dynamodb-tutorial/

#### PartiQL
https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/ql-reference.html

https://aws.amazon.com/about-aws/whats-new/2021/02/you-now-can-use-partiql-with-dynamodb-local-to-query-insert-update-and-delete-table-data-in-amazon-dynamodb/

### DynamoDB Local

https://aws.amazon.com/about-aws/whats-new/2021/02/you-now-can-use-partiql-with-dynamodb-local-to-query-insert-update-and-delete-table-data-in-amazon-dynamodb/

https://aws.amazon.com/about-aws/whats-new/2021/05/amazon-dynamodb-local-now-supports-the-aws-sdk-for-java-2-x/

#### DynamoDB  official doc
https://docs.amazonaws.cn/en_us/amazondynamodb/latest/developerguide/bp-time-series.html

https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb.html

https://boto.cloudhackers.com/en/2.6.0/dynamodb_tut.html

https://www.youtube.com/watch?v=HaEPXoXVf2k&t=3456s

### AWS

https://habr.com/ru/post/529242/

<https://gumroad.com/l/aws-good-parts/reddit-20200402?rdt_cid=3012255594103770994>

<https://medium.com/aws-tutor>

<https://github.com/cdk-patterns/serverless>

<https://medium.com/aws-tutor/a-complete-guide-to-the-machine-learning-tools-on-aws-8a012cb4de76>

### AWS book $35

<https://gumroad.com/l/aws-good-parts>

<https://dashbird.io/blog/complete-aws-lambda-handbook-beginners-part-1/>

<https://pybit.es/aws-lambda-external-libraries.html>

### aws cli via brew
```
brew install awscli
==> Pouring awscli-1.16.300.mojave.bottle.tar.gz
==> Caveats
The "examples" directory has been installed to:
  /usr/local/share/awscli/examples

Bash completion has been installed to:
  /usr/local/etc/bash_completion.d

zsh completions and functions have been installed to:
  /usr/local/share/zsh/site-functions
==> Summary
 /usr/local/Cellar/awscli/1.16.300: 8,079 files, 58.8MB
 
 which aws
/usr/local/bin/aws

aws --version
aws-cli/1.16.300 Python/3.7.5 Darwin/18.7.0 botocore/1.13.36
```
### aws cli via pip install

Running a Python script on an EC2 instance
https://medium.com/@hello_prism/running-a-python-script-on-an-ec2-instance-8691589b3080

https://realpython.com/courses/python-boto3-aws-s3/

```
cd my_virt_envs/
virtualenv aws
pip install awscli --upgrade

/Users/mlubinsky/my_virt_envs/aws/bin/aws
 
/Users/mlubinsky/my_virt_envs/aws/bin/aws --version
aws-cli/1.16.304 Python/2.7.10 Darwin/18.7.0 botocore/1.13.40

```

<https://bash-my-aws.org/> .  set of CLI commands for managing resources on Amazon Web Services

<https://news.ycombinator.com/item?id=21921293>

<https://expeditedsecurity.com/aws-in-plain-english/>

<https://medium.com/@tomas.duhourq/building-scalable-analytics-with-aws-part-i-6de6a90e3513>  

<https://towardsdatascience.com/how-to-deploy-a-streamlit-app-using-an-amazon-free-ec2-instance-416a41f69dc3> . 

<https://dzone.com/articles/how-to-set-up-a-data-lake-architecture-with-aws>

<https://dzone.com/articles/aws-lake-formation-for-data-lakes>

<https://codereview.stackexchange.com/questions/tagged/amazon-web-services>

<https://medium.com/@tomas.duhourq/building-scalable-analytics-with-aws-part-i-6de6a90e3513>

<https://aws.amazon.com/getting-started/projects/build-log-analytics-solution/> 

<https://fuzzyblog.io/blog/category.html#aws>


<https://fuzzyblog.io/blog/aws/2016/09/20/aws-tutorial-08-using-ssh-s-config-file-with-your-aws-boxes.html>

Для подключения к инстансу EC2 необходим закрытый ключ. Скачайте его (расширение .pem) из панели управления Amazon EC2 и измените разрешения 

chmod 400 my-ec2-ssh-key.pem 

Храните ключ в надёжном месте или поместите его в свою папку ~/.ssh/.

 ssh -i ~/.ssh/my-ec2-key.pem ubuntu@my-ec2-public
 
 scp -i myAmazonKey.pem phpMyAdmin-3.4.5-all-languages.tar.gz ec2-user@mec2-50-17-16-67.compute-1.amazonaws.com:~/.


wget http://<bucket-name>.s3.amazonaws.com/file.jpg
 
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
<https://expeditedsecurity.com/aws-in-plain-english/s3/>

<https://aws.amazon.com/efs/when-to-choose-efs/> EFS vs S3

<https://www.missioncloud.com/blog/resource-amazon-ebs-vs-efs-vs-s3-picking-the-best-aws-storage-option-for-your-business/>

<https://www.upsolver.com/blog/7-guidelines-ingesting-big-data-lakes>

<https://docs.aws.amazon.com/AmazonS3/latest/dev/optimizing-performance.html>


## Boto3

  https://realpython.com/courses/python-boto3-aws-s3/
  
https://www.learnaws.org/2021/05/12/aws-iam-boto3-guide/
  
  https://dashbird.io/blog/boto3-aws-python/

<https://stackoverflow.com/questions/36205481/read-file-content-from-s3-bucket-with-boto3>

<https://boto3.amazonaws.com/v1/documentation/api/latest/index.html> Boto is  AWS  SDK for Python. It enables Python developers to create, configure, and manage AWS services, such as EC2 and S3.

https://boto3.amazonaws.com/v1/documentation/api/latest/guide/s3-uploading-files.html

<https://realpython.com/python-boto3-aws-s3/>
<https://realpython.com/courses/python-boto3-aws-s3/> Boto

<https://stackabuse.com/automating-aws-ec2-management-with-python-and-boto3/>

Lambda example
```
  import os,sys
  import boto3
  from my_submodule.models MyModels
  
  def handler(event, context):
    ..
```

Amazon S3 is a simple key-based object store. When you store data, you assign a unique object key that can later be used to retrieve the data. Keys can be any string, and they can be constructed to mimic hierarchical attributes. Alternatively, you can use S3 Object Tagging to organize your data across all of your S3 buckets and/or prefixes.

You should use a lexicographic date format (yyyy/mm/dd) when storing your data on S3. Since files are listed by S3 in lexicographic order, failing to store them in the correct format will cause problems down the line when retrieving the data.

 

Note that while Amazon previously recommended to randomizing prefix naming with hashed characters, this is no longer the case according to their most up-to-date documentation.

<https://docs.aws.amazon.com/AmazonS3/latest/dev/optimizing-performance.html>

<https://www.upsolver.com/blog/small-file-problem-hdfs-s3>


### Count the files in an S3 bucket - three ways.

#### Method 1: aws s3 ls
 ```
 aws s3 ls s3://adl-ohi/ --recursive --summarize | grep "Total Objects:"
 ```
Total Objects: 444803

### Method 2: aws s3api
  S3  filesystem  has an API that you can call. Yep – a json api:
```
aws s3api list-objects --bucket adl-ohi --output json --query "[length(Contents[])]"
[
    448444
]
```

### Method 3: A Python Example: boto3
 
```
#!/usr/local/bin/python

import sys
import boto3

s3 = boto3.resource('s3')
s3bucket = s3.Bucket(sys.argv[1])
size = 0
totalCount = 0

for key in s3bucket.objects.all():
    totalCount += 1
    size += key.size

print('total size:')
print("%.3f GB" % (size*1.0/1024/1024/1024))
print('total count:')
print(totalCount)
```
which gives output like this:
```
python3 scratch/count_s3.py adl-ohi
total size:
0.298 GB
total count:
486468
```

<https://aws.amazon.com/s3/faqs/>
<https://news.ycombinator.com/item?id=21170652> A command line utility that allows you to stream data from multiple S3 objects directly into your terminal
<https://www.npmjs.com/package/s3st>

## Athena

<https://www.bryteflow.com/how-to-get-your-amazon-athena-queries-to-run-5x-faster/>

<https://www.reddit.com/r/aws/comments/e3iuix/any_success_stories_using_amazon_athena/>

<https://www.transposit.com/blog/2019.08.22-try-athena-easily-with-a-transposit-app/?c=lob>

<https://towardsdatascience.com/query-data-from-s3-files-using-aws-athena-686a5b28e943>

<https://medium.com/swlh/tutorial-build-your-data-lake-using-aws-s3-athena-150c1aaa44cf>

<https://www.mungingdata.com/aws/athena-spark-best-friends>

<https://medium.com/traackr-devs/athena-vs-q-battle-of-the-data-parsers-7c5a7b522b3f>

<https://habr.com/ru/company/mailru/blog/456392/>


## REST API
<https://habr.com/post/435180/> Бессерверный REST API 

## Lambda

<https://habr.com/ru/post/457100/>

<http://veekaybee.github.io/2018/09/24/the-case-of-the-broken-lambda/>



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
 
 
