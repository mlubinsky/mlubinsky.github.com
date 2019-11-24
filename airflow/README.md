<https://airflow.apache.org/>

<https://airflow-tutorial.readthedocs.io/>

<https://tech.marksblogg.com/install-and-configure-apache-airflow.html>

<https://tech.marksblogg.com/airflow-postgres-redis-forex.html>

<https://github.com/godatadriven/whirl> . local development and testing of Apache Airflow workflows.

<https://blog.godatadriven.com/testing-and-debugging-apache-airflow>

<https://blog.godatadriven.com/open-source-airflow-local-development>

<https://www.manning.com/books/data-pipelines-with-apache-airflow> .  BOOK

<https://medium.com/@tomaszdudek/yet-another-scalable-apache-airflow-with-docker-example-setup-84775af5c451>

<https://cwiki.apache.org/confluence/display/AIRFLOW/Airflow+Links> Links

http://michal.karzynski.pl/blog/2017/03/19/developing-workflows-with-apache-airflow/

https://github.com/geosolutions-it/evo-odas/wiki/Airflow---about-subDAGs,-branching-and-xcom

<https://github.com/apache/airflow>

<http://pydoc.net/apache-airflow>

<http://airflow.apache.org/faq.html>

<https://www.sicara.ai/blog/2019-01-28-automate-aws-tasks-thanks-to-airflow-hooks>  AirFlow Hooks


<https://medium.com/walmartlabs/auditing-airflow-batch-jobs-73b45100045> Auditing Airflow

<https://medium.com/the-prefect-blog/why-not-airflow-4cfa423299c4> Why Not Airflow?

```
pip install apache-airflow[celery]

pip install apache-airflow[postgres,s3]

pip install -U apache-airflow

```

<https://medium.com/slido-dev-blog/automate-executing-aws-athena-queries-and-moving-the-results-around-s3-with-airflow-dd3603dc611d> Automate executing AWS Athena queries and moving the results around S3 with Airflow: 

DAGs are a high-level outline that define the dependent and exclusive tasks that can be ordered and scheduled.


### Scheduler  
This service is responsible for:
* reparsing the DAG folder every few seconds
* checking DAG schedules to determine if a DAG is ready to run
* checking all Task dependencies to determine if any Tasks are ready to be run
* setting the final DAG states in the database

### execution_date 

<https://stackoverflow.com/questions/33126159/airflow-not-scheduling-correctly-python>

is not interpreted by Airflow as the start time of the DAG, but rather the end of an interval capped by the DAG’s start time. 
Ad-hoc runs are now possible as long as they don’t share an execution_date with any other run.

### backfilling 
- running workflows back in time. This is only possible of course if external dependencies such as the availability of data can be met. What makes backfilling especially useful is the ability to rerun partial workflows. If the fetching of data is not possible back in time or is a very lengthy process you’d like to avoid, you can rerun partial workflows with backfilling.

### XCom
a utility that was introduced to allow tasks to exchange small pieces of metadata. This is a useful feature if you want task A to tell task B that a large dataframe was written to a known location in cloud storage

### Hooks

<https://airflow.apache.org/concepts.html#hooks>

<https://medium.com/geoblinktech/bring-sanity-to-your-data-pipelines-with-apache-airflow-3c9906aac77c>

### Executors

<https://www.sicara.ai/blog/2019-04-08-apache-airflow-celery-workers>

Inside airflow.cfg the executor is defined:

 Airflow proposes several executor out of the box, from the simplest to the most full-featured:
 
* SequentialExecutor: a very basic, single task at a time, executor that is also the default one. You do NOT want to use this one for anything but unit testing
* LocalExecutor: also very basic, it runs the tasks on the same host as the scheduler, and is quite simple to set-up. It’s the best candidate for small, non-distributed deployments, and development environments, but won’t scale horizontally
* CeleryExecutor: here we are beginning to scale out over a distributed cluster of Celery workers to cope with a large sized task set. Still quite easy to set-up and use, it’s the recommended setup for production
* MesosExecutor: if you’re one of the cool kids, and have an existing Mesosinfrastructure, surely your will want to leverage as a destination for your task executions
* KubernetesExecutor

## Best practices

<https://medium.com/leboncoin-engineering-blog/data-traffic-control-with-apache-airflow-ab8fd3fc8638>

Also look into attached PDF in this folder

```
airflow scheduler &
airflow webserver & .   http://localhost:8080
```

### issue

```
pip freeze | grep Flask
Flask==1.1.1
```
<https://stackoverflow.com/questions/55253263/import-airflow-importerror-cannot-import-name-version-with-python-2-7>
```
>>> from airflow.models import DAG
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/Users/mlubinsky/ide_virtual_env/lib/python2.7/site-packages/airflow/__init__.py", line 30, in <module>
    from airflow import version
ImportError: cannot import name version

```

```
# print the list of active DAGs
airflow list_dags

# prints the list of tasks the "tutorial" dag_id
airflow list_tasks tutorial

# prints the hierarchy of tasks in the tutorial DAG
airflow list_tasks tutorial --tree

# initialize the database
airflow initdb # This creates airflow directory in home path with airflow.cfg and logs folder.

# start the web server, default port is 8080
airflow webserver -p 8080

# start the scheduler
airflow scheduler

# visit localhost:8080 in the browser and enable the example dag in the home page
```

The first time you run Airflow, it will create a file called airflow.cfg in your $AIRFLOW_HOME directory
(~/airflow by default). This file contains Airflow’s configuration and you can edit it to change any of the settings.


cp airflow_test.py ~/airflow/dags/

<https://medium.com/@guillaume_payen/use-conditional-tasks-with-apache-airflow-98bab35f1846>

<https://medium.com/@dustinstansbury/understanding-apache-airflows-key-concepts-a96efed52b1a>


<https://eng.lyft.com/running-apache-airflow-at-lyft-6e53bb8fccff>

Airflow provides various configurables to tune the DAG performance. At Lyft, we suggest users tune the following variables:
* Parallelism: This variable controls the number of task instances that the Airflow worker can run simultaneously. Users could increase the parallelism variable in the Airflow.cfg. We normally suggest users increase this value when doing backfill.
* Concurrency: The Airflow scheduler will run no more than concurrency task instances for your DAG at any given time. Concurrency is defined in your Airflow DAG as a DAG input argument. If you do not set the concurrency on your DAG, the scheduler will use the default value from the dag_concurrency entry in your Airflow.cfg.
* max_active_runs: Airflow will run no more than max_active_runs DagRuns of your DAG at a given time. If you do not set the max_active_runs on your DAG, Airflow will use the default value from the max_active_runs_per_dag entry in your Airflow.cfg. We suggest users not to set depends_on_past to true and increase this configuration during backfill.
* Pool: Airflow pool is used to limit the execution parallelism. Users could increase the priority_weight for the task if it is a critical one.


### Tasks
Tasks are user-defined activities ran by the operators. They can be functions in Python or external scripts that you can call. Tasks are expected to be idempotent — no matter how many times you run a task, it needs to result in the same outcome for the same input parameters.

<https://medium.com/@dustinstansbury/understanding-apache-airflows-key-concepts-a96efed52b1a>
 Tasks can have two flavors: they can either execute some explicit operation, in which case they are an Operator, or they can pause the execution of dependent tasks until some criterion has been met, in which case they are a Sensor. In principle, Operators can perform any function that can be executed in Python. Similarly, Sensors can check the state of any process or data structure.

### Operators -  describes a single task
Don’t confuse operators with tasks. Tasks are defined as “what to run?” and operators are “how to run”. For example, a Python function to read from S3 and push to a database is a task. The method that calls this Python function in Airflow is the operator. Airflow has built-in operators that you can use for common tasks. You can create custom operators by extending the BaseOperator class and implementing the execute() method.

if two operators need to share information, like a filename or small amount of data, you should consider combining them into a single operator. If it absolutely can’t be avoided, Airflow does have a feature for operator cross-communication called XCom.
```
BashOperator - executes a bash command
PythonOperator - calls an arbitrary Python function
EmailOperator - sends an email
HTTPOperator - sends an HTTP request
MySqlOperator, SqliteOperator, PostgresOperator, MsSqlOperator, OracleOperator, JdbcOperator, etc. - executes a SQL command
Sensor - waits for a certain time, file, database row, S3 key, etc…
```
<https://blog.usejournal.com/testing-in-airflow-part-1-dag-validation-tests-dag-definition-tests-and-unit-tests-2aa94970570c>

There are five categories of tests in Airflow that you can write:
*  DAG Validation Tests: To test the validity of the DAG, checking typos and cyclicity.
* DAG/Pipeline Definition Tests: To test the total number of tasks in the DAG, upstream and downstream dependencies of each task etc.
* Unit Tests: To test the logic of custom Operators, custom Sensor etc.
* Integration Tests: To test the communication between tasks. For example, task1 pass some information to task 2 using Xcoms.
* End to End Pipeline Tests: To test and verify the integration between each task. You can also assert the data on successful completion of the E2E pipeline.

```
from datetime import datetime
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator
from airflow.operators import MultiplyBy5Operator

def print_hello():
 return 'Hello Wolrd'

dag = DAG('hello_world', description='Hello world example', schedule_interval='0 12 * * *', start_date=datetime(2017, 3, 20), catchup=False)

dummy_operator = DummyOperator(task_id='dummy_task', retries = 3, dag=dag)

hello_operator = PythonOperator(task_id='hello_task', python_callable=print_hello, dag=dag)

multiplyby5_operator = MultiplyBy5Operator(my_operator_param='my_operator_param',
                                task_id='multiplyby5_task', dag=dag)

dummy_operator >> hello_operator

dummy_operator >> multiplyby5_operator
```

<https://medium.com/datareply/airflow-lesser-known-tips-tricks-and-best-practises-cf4d4a90f8f>



<https://cwiki.apache.org/confluence/display/AIRFLOW/Airflow+Home>

<https://towardsdatascience.com/a-definitive-compilation-of-apache-airflow-resources-82bc4980c154>

https://twitter.com/ApacheAirflow

<https://github.com/jghoman/awesome-apache-airflow>

<https://www.reddit.com/r/dataengineering/>

<https://www.sicara.ai/blog/2019-01-28-automate-aws-tasks-thanks-to-airflow-hooks>

 <https://medium.com/airbnb-engineering/airflow-a-workflow-management-platform-46318b977fd8>
‘Airflow: a workflow management platform’ by Maxime Beauchemin (Creator of Apache Airflow). Airbnb Engineering and Data Science. June, 2015.

https://medium.com/@r39132/apache-airflow-grows-up-c820ee8a8324
‘Apache Airflow Grows Up!’ by Sid Anand (Chief Data Engineer, Paypal. Committer & PMC Member Apache Airflow). Medium. Jan, 2019.

```
‘Understanding Apache Airflow’s Key Concepts’ by Dustin Stansbury (Data Scientist, Quizlet). Medium (~ 1.8k +1's). May, 2017.
‘Airflow 101: How to start automating your data pipelines with Airflow’ by Sriram Baskaran (Program Director, Data Engineering Insight Data Science). Medium(~ 1.2k +1's). Oct, 2018.
[Video] ‘Best practices with Airflow- an open source platform for workflows & schedules’ by Maxime Beauchemin (Creator of Apache Airflow).
[Video] ‘Modern ETL-ing with Python and Airflow (and Spark)’ by Tamara Mendt (Data Engineer, HelloFresh). PyConDE 2017.
[Video] ‘A Practical Introduction to Airflow’ by Matt Davis (Data Platform Engineering at Clover). PyData SF 2016.
[Video] ‘Developing elegant workflows in Python code with Apache Airflow’ by Michael Karzynski (Tech Lead at Intel). EuroPython Conference. July 2017.
[Video] ‘How I learned to time travel, or, data pipelining and scheduling with Airflow’ by Laura Lorenz (Data & SWE at Industry Dive). PyData DC 2016.
Airflow in the Industry
‘Managing Uber’s Data Workflows at Scale’ by Alex Kira. Uber Data Engineering. Feb, 2019.
‘Productionizing ML with workflows at Twitter’ by Samuel Ngahane and Devin Goodsell. Twitter Engineering. June, 2018.
‘Apache Airflow at Pandora’ by Ace Haidrey. Pandora Engineering. Mar, 2018.
‘Running Apache Airflow at Lyft’ by Tao Feng, Andrew Stahlman, and Junda Yang. Lyft Engineering. Dec, 2018.
‘Why Robinhood uses Airflow’ by Vineet Goel. Robinhood Engineering. May, 2017.
‘Collaboration between data engineers, data analysts and data scientists’ by Germain Tangus (Senior Data Engineer, Dailymotion). Dailymotion Engineering. May, 2019.
‘How Sift Trains Thousands of Models using Apache Airflow’ by Duy Tran. Sift Engineering. Mar, 2018.
‘Airflow, Meta Data Engineering, and a Data Platform for the World’s Largest Democracy’ by Vinayak Mehta. Socialcops Engineering. Aug, 2018.
‘Data Traffic Control with Apache Airflow’ by Nicolas Goll Perrier (Data Engineer, leboncoin). leboncoin Engineering Blog. Jan, 2019.
‘Airflow Part 2: Lessons Learned (at SnapTravel)’ by Nehil Jain. SnapTravel Engineering. Jun, 2018.
‘Using Apache Airflow to Create Data Infrastructure in the Public Sector’ by Varun Adibhatla and Laurel Brunk. Astronomer.io. Oct, 2017.
‘Airflow at WePay’ by Chris Riccomini. WePay. Jul, 2016.
Airflow Distributed Deployment
‘How Apache Airflow Distributes Jobs on Celery workers’ by Hugo Lime (Data Scientist, Sicara AI and Big Data). Sicara Engineering. Apr, 2019.
‘A Guide On How To Build An Airflow Server/Cluster’ by Tianlon Song (Sr. Software Engineer, Machine Learning & Big Data at Zillow). Oct, 2016.
Testing
‘Data’s Inferno: 7 Circles of Data Testing Hell with Airflow’ by WB Advanced Analytics. Jan, 2018.
‘Testing in Airflow Part 1 — DAG Validation Tests, DAG Definition Tests and Unit Tests’ by Chandu Kavar on Medium ( ~1k +1's). Aug 2018.
Additional Reading
```
<https://medium.com/bluecore-engineering/were-all-using-airflow-wrong-and-how-to-fix-it-a56f14cb0753>
‘We’re All Using Airflow Wrong and How to Fix It’ by Jessica Laughlin. Bluecore Engineering. Aug, 2018.

 
