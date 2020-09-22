
https://habr.com/ru/company/lamoda/blog/518620/

<https://diogoalexandrefranco.github.io/about-airflow-date-macros-ds-and-execution-date/>


<https://airflow.apache.org/docs/stable/scheduler.html#scheduling-triggers>

```  
Note that if you run a DAG on a schedule_interval of one day, the run stamped 2016-01-01 will be trigger soon after 2016-01-01T23:59. 
In other words, the job instance is started once the period it covers has ended.
Let's Repeat That The scheduler runs your job one schedule_interval AFTER the start date, at the END of the period.
```
<https://stackoverflow.com/questions/58414350/airflow-skip-current-task> SkipTask

<https://habr.com/ru/post/512386/> Airflow in russian

http://blog.manugarri.com/how-to-trigger-a-dag-with-custom-parameters-on-airflow-ui/

### How to get result of SQL?

https://airflow.apache.org/docs/stable/_modules/airflow/operators/sql.html

https://stackoverflow.com/questions/60601713/how-to-store-the-sql-query-result-using-airflow-and-use-the-result-in-if-else-co

https://towardsdatascience.com/airflow-sharing-data-between-tasks-7bbaa27eeb1

```
def do_work():
    hiveserver = HiveServer2Hook()
    hql = "SELECT COUNT(*) FROM foo.bar"
    row_count = hiveserver.get_records(hql, schema='foo')
    print row_count[0][0]
```    
    
All available Hive Hooks methods can be found here: 

https://github.com/apache/incubator-airflow/blob/master/airflow/hooks/hive_hooks.py


### XCOM
https://pythonhosted.org/airflow/concepts.html#xcoms  

https://github.com/airbnb/airflow/blob/master/airflow/example_dags/example_xcom.py


<https://stackoverflow.com/questions/62403142/airflow-branchpythonoperator-chaining>
```
 think you suggest to use the chain func like this:
chain ([t1,t2,t3, fork_task, join_task] )
? (edited) 

Michael Lu  2 hours ago
I am not clear

Nick Benthem  2 hours ago
I'd just use it as chain(t1,t2,t3,fork_task,[branch_1,branch_2],join_task)

Michael Lu  2 hours ago
I see your point. I will try it shortly
The chain() returns nothing.
How my return statement should look like?

Nick Benthem  1 hour ago
I wouldn't even use a new function - I'd just call
chain(t1,t2,t3,fork_task,[branch_1,branch_2],join_task) for your downstream dependencies

Michael Lu  1 hour ago
I am trying to say what  I do not understand clearly how to use it -   f()  has the return statement; what I shout pass to return?

Michael Lu  43 minutes ago
The def f() : is not created by me, I have to obey the contract.
How to convert the current return:
return ( t1 >> t2 >> t3)
to my requirement?

Nick Benthem  40 minutes ago
That seems like a weird contract - and I would re-examine what you're trying to do. You might be able to wrap the function in a lambda of some sort - but t1 >> t2 is just a moniker for __rshift__. It's a function call you're trying to do - but that's getting awfully wonky.
Check out the code here for what that >> logic is doing: https://github.com/apache/airflow/blob/5355909b5f4ef0366e38f21141db5c95baf443ad/airflow/models.py#L2569
airflow/models.py:2569
    def __rshift__(self, other):
    
<https://github.com/apache/airflow|apache/airflow>apache/airflow | Added by GitHub
```

<https://www.youtube.com/watch?v=XJf-f56JbFM>

<http://michal.karzynski.pl>

<https://bhavaniravi.com/blog/apache-airflow-introduction>

<https://github.com/quantumblacklabs/kedro> . Kedro: best-practice for data and ML pipelines.

<https://pyvideo.org/pycon-hk-2018/industrial-machine-learning-pipelines-with-python-airflow.html> 


DynamoDB
<https://medium.com/searce/serverless-approval-mechanism-for-ml-pipeline-using-airflow-on-aws-ecosystem-5f91a8121749>


<https://www.astronomer.io/guides/templating/> template and macro

<https://gtoonstra.github.io/etl-with-airflow/index.html>

## Udemy
<https://www.udemy.com/course/the-ultimate-hands-on-course-to-master-apache-airflow/> . Udemy /pereuc...

 
## Setup

<https://medium.com/@achilleus/robust-apache-airflow-deployment-dd02a6c75c78>

<https://medium.com/@achilleus/easy-way-to-manage-your-airflow-setup-b7c030dd1cb8>


## Bash operator

<https://marclamberti.com/blog/airflow-bashoperator/>

## Transfer

<https://airflow.apache.org/docs/stable/_modules/airflow/operators/s3_file_transform_operator.html> S3 file transform

## S3 -> Redshift
<https://airflow.apache.org/docs/stable/_modules/airflow/operators/s3_to_redshift_operator.html> S3 -> Redshift

<https://sonra.io/2018/01/01/using-apache-airflow-to-build-a-data-pipeline-on-aws/> .  S3 to Redshift
```
copy product_tgt1
from 's3://productdata/product_tgt/product_details.csv
iam_role 'arn:aws:iam::<aws-account-id>:role/<role-name>'
region 'us-east-2';

 copy AAA.T_FACT
from 's3://AAA-data-warehouse/facts_orc/AAA_device/date_key=2019-10-20/000000_0'
 credentials 'aws_iam_role=arn:aws:iam::182333787270:role/RedShiftDevDataProcessingDevPrivileges'
format as ORC
```


The scheduler runs a DAG soon after (start_date + schedule_interval) is passed
```
airflow list_dags
airflow initdb
airflow webserver
airflow scheduler
airflow connections
airflow connections -h
airflow list_tasks <DAG_id>
airflow list_dag_runs <DAG_id>
airflow trigger_dag <DAG_id>
airflow test <DAG_id> <task_id> arguments # runs task without checking dependencies
airflow next_execution   <DAG_id> .  # next execution time
airflow delete_dag <DAG_id>
```

in airflow.cfg there are 2 parameters related to concurrency:

parallelism
dag_concurrency

```
with DAG (...) as dag:
    t1= SomeOperator()  # no need to pass dag to operator !!!
    t2= Another Operator
    
    t1 >> t2 >> [t3, t4] >> t8
```    

<https://habr.com/ru/company/mailru/blog/344398/>

<https://towardsdatascience.com/how-to-use-airflow-without-headaches-4e6e37e6c2bc>

<https://t.me/ruairflow>

<https://habr.com/ru/company/mailru/blog/479900/>

<https://janakiev.com/blog/apache-airflow-systemd/>

Roku
<https://blog.usejournal.com/roku-is-locking-down-tvs-until-you-give-personal-data-397ceadfd458>

<https://www.reddit.com/r/bigdata/comments/dwae40/tutorial_on_how_to_use_airflow_without_pain/>

Airflow doesn’t treat data as a first class citizen. You should query data, then pass it via XCOM. 

Airflow’s usage pattern is to extract data, save it somewhere like S3, then pass the s3 bucket and key location to the next task via XCOM. There are many many downsides to using heavy (really big) XCOMs, and your metadata database has to store that data to pass between tasks, and IIRC it doesn’t ever delete the data. 


<https://airflow.apache.org/>

<https://airflow-tutorial.readthedocs.io/>

<https://towardsdatascience.com/apache-airflow-tips-and-best-practices-ff64ce92ef8>

<https://towardsdatascience.com/how-to-use-airflow-without-headaches-4e6e37e6c2bc>

<https://tech.marksblogg.com/install-and-configure-apache-airflow.html>

<https://tech.marksblogg.com/airflow-postgres-redis-forex.html>

<https://zulily-tech.com/2019/11/19/evolution-of-zulilys-airflow-infrastructure/>

<https://airflow.apache.org/docs/stable/faq.html>
 By design, an Airflow DAG will execute at the completion of its schedule_interval.

The Airflow scheduler triggers the task soon after the start_date + schedule_interval is passed.

The default schedule_interval is one day (datetime.timedelta(1)). 
You must specify a different schedule_interval directly to the DAG object you instantiate

The task instances directly upstream from the task need to be in a success state. Also, if you have set 
``depends_on_past=True``, 
the previous task instance needs to have succeeded (except if it is the first run for that task). Also, if ``wait_for_downstream=True``, make sure you understand what it means. You can view how these properties are set from the Task Instance Details page for your task.

That means one schedule_interval AFTER the start date. An hourly DAG, for example, will execute its 2pm run when the clock strikes 3pm. The reasoning here is that Airflow can't ensure that all data corresponding to the 2pm interval is present until the end of that hourly interval.
 

For a DAG to be executed, the ``start_date`` must be a time in the past, otherwise Airflow will assume that it's not yet ready to execute. When Airflow evaluates your DAG file, it interprets ``datetime.now()`` as the current timestamp (i.e. NOT a time in the past) and decides that it's not ready to run. Since this will happen every time Airflow heartbeats (evaluates your DAG) every 5-10 seconds, *it'll never run*.

To properly trigger your DAG to run, make sure to insert a fixed time in the past (e.g. datetime(2019,1,1)) and set ``catchup=False`` (unless you're looking to run a backfill).

Note: You can manually trigger a DAG run via Airflow's UI directly on your dashboard (it looks like a "Play" button). A manual trigger executes immediately and will not interrupt regular scheduling, though it will be limited by any concurrency configurations you have at the DAG, deployment level or task level. When you look at corresponding logs, the run_id will show manual__ instead of scheduled__.

<https://www.astronomer.io/blog/7-common-errors-to-check-when-debugging-airflow-dag/>

## Metadata tables
```
psql -U airflow
\dt
alembic_version
chart
connection
dag
dag_pickle
dag_run
import_error
job
..
log
..
task_instance
..
users
variable
xcom
```

## Docker

<https://github.com/benattali/airflow-with-docker>

### Whirl - local development and testing of Apache Airflow using Docker
<https://github.com/godatadriven/whirl> . 
<https://blog.godatadriven.com/open-source-airflow-local-development>
<https://blog.godatadriven.com/testing-and-debugging-apache-airflow> Testing and debugging Apache Airflow

How We Solved Our Airflow I/O Problem By Using A Custom Docker Operator
<https://medium.com/enigma-engineering/how-we-solved-our-airflow-i-o-problem-by-using-a-custom-docker-operator-dcc7c8111be5>

Containerizing Data Workflows
<https://medium.com/enigma-engineering/containerizing-data-workflows-95df1d338048>


<https://medium.com/@tomaszdudek/yet-another-scalable-apache-airflow-with-docker-example-setup-84775af5c451>

<https://github.com/puckel/docker-airflow> used by Udemy class

```
docker exec -it <container_id> bash
docker exec -it <container_id> sh -c "/entrypoint.sh" /bin/bash"

```

## Book
<https://www.manning.com/books/data-pipelines-with-apache-airflow> .  BOOK


<https://cwiki.apache.org/confluence/display/AIRFLOW/Airflow+Links> Links

http://michal.karzynski.pl/blog/2017/03/19/developing-workflows-with-apache-airflow/

https://github.com/geosolutions-it/evo-odas/wiki/Airflow---about-subDAGs,-branching-and-xcom

<https://github.com/apache/airflow>

<http://pydoc.net/apache-airflow>

<http://airflow.apache.org/faq.html>

### Trigger Rules

* one_success (at least) 
* all_success
* all_done
* all_failed
* one_failed
* none_failed (sucseeded or skipped)
* none_skipped

### Hooks

<https://airflow.apache.org/concepts.html#hooks>

<https://www.sicara.ai/blog/2019-01-28-automate-aws-tasks-thanks-to-airflow-hooks>  AirFlow Hooks
 

Hooks uses aifflow.model.connection.Connection to get hostnames and auth info



<https://medium.com/geoblinktech/bring-sanity-to-your-data-pipelines-with-apache-airflow-3c9906aac77c>


<https://medium.com/walmartlabs/auditing-airflow-batch-jobs-73b45100045> Auditing Airflow


<https://eng.lyft.com/running-apache-airflow-at-lyft-6e53bb8fccff> Lyft uses Airflow

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



### Executors

<https://www.sicara.ai/blog/2019-04-08-apache-airflow-celery-workers>

The executor is defined in airflow.cfg

 Airflow proposes several executor out of the box, from the simplest to the most full-featured:
 
* SequentialExecutor: a very basic, single task at a time, executor that is also the default one. You do NOT want to use this one for anything but unit testing, it uss SQLite -> will not require you to install any external db

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

Airflow provides various configurables to tune the DAG performance.  we suggest users tune the following variables:
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

### PythonOperator
 
 if you provide  ``provide_context=True``, you need to have ``**kwargs`` in your function
 if you're passing everything through templates_dict  
 your param will be available in ``kwargs['templates_dict']['file_in']``
  
```
DummyOperator
BashOperator - executes a bash command
PythonOperator - calls an arbitrary Python function
BranchPythonOperator (python_callable) returns task_id or list of task to which control to be given
HiveOperator
EmailOperator - sends an email
HTTPOperator - sends an HTTP request
MySqlOperator, SqliteOperator, PostgresOperator, MsSqlOperator, OracleOperator, JdbcOperator, etc. - executes a SQL command
Sensor - waits for a certain time (poke_interval, timeout, soft_fail), file, database row, S3 key, event etc… FileSensor, TimeDeltaSensor, S3KeySensor
TranferOperator - moves data from one system to another: e.g. S3ToRedshiftTranfer, etc

```
### DummyOperator

* can be used for mock testing insterad the read operator
* shell be used in this case:
    (t1,t2,t3) may be executed in any order; (t4,t5,t6) may be started only after all (t1,t2,t3) are finished



### Testing DAGs

<https://blog.usejournal.com/testing-in-airflow-part-1-dag-validation-tests-dag-definition-tests-and-unit-tests-2aa94970570c>

<https://medium.com/@chandukavar/testing-in-airflow-part-2-integration-tests-and-end-to-end-pipeline-tests-af0555cd1a82>

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
Here is  multiplyby5_operator:
```
import logging

from airflow.models import BaseOperator
from airflow.plugins_manager import AirflowPlugin
from airflow.utils.decorators import apply_defaults

log = logging.getLogger(__name__)


class MultiplyBy5Operator(BaseOperator):
    @apply_defaults
    def __init__(self, my_operator_param, *args, **kwargs):
        self.operator_param = my_operator_param
        super(MultiplyBy5Operator, self).__init__(*args, **kwargs)

    def execute(self, context):
        log.info('operator_param: %s', self.operator_param)
        return (self.operator_param * 5)


class MultiplyBy5Plugin(AirflowPlugin):
    name = "multiplyby5_plugin"
```    


Validation Test
```
import unittest
from airflow.models import DagBag

class TestDagIntegrity(unittest.TestCase):

    LOAD_SECOND_THRESHOLD = 2

    def setUp(self):
        self.dagbag = DagBag()

    def test_import_dags(self):
        self.assertFalse(
            len(self.dagbag.import_errors),
            'DAG import failures. Errors: {}'.format(
                self.dagbag.import_errors
            )
        )

    def test_alert_email_present(self):

        for dag_id, dag in self.dagbag.dags.iteritems():
            emails = dag.default_args.get('email', [])
            msg = 'Alert email not set for DAG {id}'.format(id=dag_id)
            self.assertIn('alert.email@gmail.com', emails, msg)


suite = unittest.TestLoader().loadTestsFromTestCase(TestDagIntegrity)
unittest.TextTestRunner(verbosity=2).run(suite)
```

Pipeline /definition test:
```

import unittest
from airflow.models import DagBag

class TestHelloWorldDAG(unittest.TestCase):
    """Check HelloWorldDAG expectation"""

    def setUp(self):
        self.dagbag = DagBag()

    def test_task_count(self):
        """Check task count of hello_world dag"""
        dag_id='hello_world'
        dag = self.dagbag.get_dag(dag_id)
        self.assertEqual(len(dag.tasks), 3)

    def test_contain_tasks(self):
        """Check task contains in hello_world dag"""
        dag_id='hello_world'
        dag = self.dagbag.get_dag(dag_id)
        tasks = dag.tasks
        task_ids = list(map(lambda task: task.task_id, tasks))
        self.assertListEqual(task_ids, ['dummy_task', 'multiplyby5_task','hello_task'])

    def test_dependencies_of_dummy_task(self):
        """Check the task dependencies of dummy_task in hello_world dag"""
        dag_id='hello_world'
        dag = self.dagbag.get_dag(dag_id)
        dummy_task = dag.get_task('dummy_task')

        upstream_task_ids = list(map(lambda task: task.task_id, dummy_task.upstream_list))
        self.assertListEqual(upstream_task_ids, [])
        downstream_task_ids = list(map(lambda task: task.task_id, dummy_task.downstream_list))
        self.assertListEqual(downstream_task_ids, ['hello_task', 'multiplyby5_task'])

    def test_dependencies_of_hello_task(self):
        """Check the task dependencies of hello_task in hello_world dag"""
        dag_id='hello_world'
        dag = self.dagbag.get_dag(dag_id)
        hello_task = dag.get_task('hello_task')

        upstream_task_ids = list(map(lambda task: task.task_id, hello_task.upstream_list))
        self.assertListEqual(upstream_task_ids, ['dummy_task'])
        downstream_task_ids = list(map(lambda task: task.task_id, hello_task.downstream_list))
        self.assertListEqual(downstream_task_ids, [])

suite = unittest.TestLoader().loadTestsFromTestCase(TestHelloWorldDAG)
unittest.TextTestRunner(verbosity=2).run(suite)

```
TestMultiplyBy5Operator:
```
import unittest
from datetime import datetime
from airflow import DAG
from airflow.models import TaskInstance
from airflow.operators import MultiplyBy5Operator


class TestMultiplyBy5Operator(unittest.TestCase):

    def test_execute(self):
        dag = DAG(dag_id='anydag', start_date=datetime.now())
        task = MultiplyBy5Operator(my_operator_param=10, dag=dag, task_id='anytask')
        ti = TaskInstance(task=task, execution_date=datetime.now())
        result = task.execute(ti.get_template_context())
        self.assertEqual(result, 50)


suite = unittest.TestLoader().loadTestsFromTestCase(TestMultiplyBy5Operator)
unittest.TextTestRunner(verbosity=2).run(suite)
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

 
