### Airflowctl
https://airflowsummit.org/sessions/2023/introducing-airflowctl/
pip install airflow ctl
https://github.com/kaxil/airflowctl

 Airflow: как повысить стабильность загрузки данных в 5 раз
https://habr.com/ru/articles/792872/


### Mage, prefect, Dagster, AWS Step function, AWS Glue
https://www.mage.ai/

https://gitlab.kitware.com/computer-vision/cmd_queue


Airflow Book:
https://www.astronomer.io/ebooks/data-pipelines-with-apache-airflow.pdf

https://medium.com/numberly-tech-blog/orchestrating-python-workflows-in-apache-airflow-fd8be71ad504

https://medium.com/nerd-for-tech/airflow-mwaa-automating-etl-for-a-data-warehouse-f5e50d14713c

https://medium.com/nerd-for-tech/airflow-catchup-backfill-demystified-355def1b6f92

pip install apache-airflow
```
Airflow is basically coding DAGs, that are composed of Tasks, that are run by Operators

Airflow “Hooks” are a high level interface that leverages Airflow Connections to get access to such resources.
They often use external libraries or tedious network operations “under the hood”.

Operators
Airflow has a very extensive set of operators available, here are some examples:

BashOperator - executes a bash command
PythonOperator - calls an arbitrary Python function
EmailOperator - sends an email
```

https://medium.com/nerd-for-tech/airflow-features-callback-trigger-clsuter-policy-cc7f8022e7d3

https://medium.com/numberly-tech-blog/orchestrating-python-workflows-in-apache-airflow-fd8be71ad504

Deferreble operators

https://blog.devgenius.io/airflow-deferrable-operators-5a7c90aaa14f

https://www.youtube.com/watch?v=uB7zweaF8EA What is new in Airflow 2.7 ?

https://blog.devgenius.io/airflow-task-parallelism-6360e60ab942

Airflow in Docker:

https://stackabuse.com/running-airflow-locally-with-docker-a-technical-guide/


https://www.youtube.com/watch?v=JJ_nnGkZjBc&list=PL2Uw4_HvXqvY2zhJ9AMUa_Z6dtMGF3gtb&index=126

https://stackoverflow.com/questions/50708226/airflow-macros-in-python-operator

https://www.astronomer.io/events/webinars/improve-your-dags-with-hidden-airflow-features/

https://www.datafold.com/blog/3-most-underused-features-of-apache-airflow

Task failure handling:
https://stackabuse.com/handling-task-failures-in-airflow-a-practical-guide/

https://habr.com/ru/articles/737046/

https://airflow.apache.org/docs/apache-airflow/stable/dag-run.html

https://habr.com/ru/companies/neoflex/articles/736292/

```
dag = DAG(
    "example_parameterized_dag",
    schedule=None,
    start_date=pendulum.datetime(2021, 1, 1, tz="UTC"),
    catchup=False,
)
```


How to start DAG from command line:
```
airflow.sh schedule -d airflow_stats_dag &
```

How to disable DAG:

1) if you set the start date of the dag to some date way in the future, 
you'll halt it until that time period. Dag stays in tact, but doesn't run.

2) set an end_date in the past

3)
```
default_args: {
      schedule_interval = '@once'
     } 
```


https://habr.com/ru/company/otus/blog/679104/

https://habr.com/ru/post/682460/

https://habr.com/ru/post/682384/

https://habr.com/ru/post/682714/


https://habr.com/ru/post/684296/


https://shopify.engineering/lessons-learned-apache-airflow-scale

https://news.ycombinator.com/item?id=31480320

docker-compose up --build

MWAA is abbreviation of:
https://aws.amazon.com/managed-workflows-for-apache-airflow/


### Airflow 2
https://airflow.apache.org/blog/airflow-two-point-oh-is-here/

https://towardsdatascience.com/is-apache-airflow-2-0-good-enough-for-current-data-engineering-needs-6e152455775c

Airflow 2.3.0 dropped support for Python 3.6. It’s tested with Python 3.7, 3.8, 3.9 and 3.10.

```
from airflow.decorators import dag, task
from airflow.utils.dates import days_ago

@dag(default_args={'owner': 'airflow'}, schedule_interval=None, start_date=days_ago(2))

def tutorial_taskflow_api_etl():
   @task
   def extract():
       return {"1001": 301.27, "1002": 433.21, "1003": 502.22}

   @task
   def transform(order_data_dict: dict) -> dict:
       total_order_value = 0
       for value in order_data_dict.values():
           total_order_value += value
       return {"total_order_value": total_order_value}

   @task()
   def load(total_order_value: float):
       print("Total order value is: %.2f" % total_order_value)

   order_data = extract()
   order_summary = transform(order_data)
   load(order_summary["total_order_value"])

tutorial_etl_dag = tutorial_taskflow_api_etl()
```

### BranchPythonOperator
```
    def _choose_platform(**kwargs):
        platform = kwargs.get("templates_dict").get("platform")
        print("INSIDE _choose_platform(): platform=", platform)
        if platform == "all":
            return ["etl_reviews_ios", "etl_reviews_android"]
        elif platform == "ios":
            return [
                "etl_reviews_ios",
            ]
        elif platform == "android":
            return [
                "etl_reviews_android",
            ]
        else:
            return None

    choose_platform = BranchPythonOperator(
        task_id="choose_platform",
        python_callable=_choose_platform,
        templates_dict={"platform": "{{ dag_run.conf.get('platform', 'all') }}"},
    )

start >> choose_platform >> [etl_reviews_ios, etl_reviews_android]
```

#### BranchPythonOperator
https://airflow.apache.org/docs/apache-airflow/stable/_api/airflow/operators/python/index.html
```
classairflow.operators.python.BranchPythonOperator(*, 
    python_callable, 
    op_args=None, 
    op_kwargs=None, 
    templates_dict=None, 
    templates_exts=None, 
    show_return_value_in_logs=True, **kwargs)
    
Bases: PythonOperator, airflow.models.skipmixin.SkipMixin
```
You can pass params to python_callable vi op_args or op_kwarrgs

```
PythonOperator have a named parameter op_kwargs and accepts dict object.

have

t5_send_notification = PythonOperator(
    task_id='t5_send_notification',
    provide_context=True,
    python_callable=SendEmail,
    op_kwargs={"my_param":'value1'},
    dag=dag,
)

def SendEmail(my_param,**kwargs):
    print(my_param) #'value_1'
    msg = MIMEText("The pipeline for client1 is completed, please check.")
    msg['Subject'] = "xxxx"
    msg['From'] = "xxxx"
```

Allows a workflow to “branch” or follow a path following the execution of this task.

It derives the PythonOperator and expects a Python function that returns a single task_id or list of task_ids to follow. The task_id(s) returned should point to a task directly downstream from {self}. 

 


### Writing DAG with XCOM
From https://databand.ai/blog/airflow-2-0-and-why-we-are-excited-at-databand/
```
def prepare_email(**kwargs):
    ti = kwargs['ti']
    raw_json = ti.xcom_pull(task_ids='get_ip')
    external_ip = json.loads(raw_json)['origin']
    ti.xcom_push(key="subject", value=f'Server connected from {external_ip}')
    ti.xcom_push(key="body", value=f'Seems like today your server executing Airflow is connected from the external IP {external_ip}')

with DAG('send_server_ip', default_args=default_args, schedule_interval=None) as dag:
    get_ip = SimpleHttpOperator(task_id='get_ip', endpoint='get', method='GET', xcom_push=True)
    email_info = PythonOperator(task_id="prepare_email", python_callable=prepare_email, xcom_push=True, provide_context=True)
    send_email = EmailOperator(
        task_id='send_email',
        to='example@example.com',
        subject="{{ ti.xcom_pull(key='subject', task_ids='prepare_email') }}",
        html_content="{{ ti.xcom_pull(key='body', task_ids='prepare_email') }}"
    )

get_ip >> email_info >> send_email
```
### Writing DAGs with decorators
From https://databand.ai/blog/airflow-2-0-and-why-we-are-excited-at-databand/
https://databand.ai/blog/streamline-your-pipeline-code-with-functional-dags-in-airflow-2-0/

Annotating a function with the @task decorator converts the function to a “PythonFunctionalOperator” that’s created behind the scenes when Airflow prepares your DAG for execution. 

The multiple_outputs attribute marks that this function will return more than a single value.
```
@task(multiple_outputs=True)
def prepare_email(raw_json: str) -> Dict[str, str]:
    external_ip = json.loads(raw_json)['origin']
    return {
        'subject':f'Server connected from {external_ip}',
        'body': f'Seems like today your server executing Airflow is connected from the external IP {external_ip}'
    }

with DAG('send_server_ip', default_args=default_args, schedule_interval=None) as dag:
    get_ip = SimpleHttpOperator(task_id='get_ip', endpoint='get', method='GET', xcom_push=True)
    email_info = prepare_email(get_ip.output)
    send_email = EmailOperator(
        task_id='send_email',
        to='example@example.com',
        subject=email_info['subject'],
        html_content=email_info['body']
    )

```

Четыре хитрости в работе с пайплайнами данных, о которых знают не все
https://habr.com/ru/company/vk/blog/659389/

e-mail notification
```
from airflow.utils.email import send_email

email_to = 'receivers@email.com'
email_subject = '(FAILED) ' + jobname + date
email_content = 'Your job has failed.'
send_email(email_to, email_subject, email_content)
```
Slack nitification https://slack.dev/python-slack-sdk/web/index.html
```
from slack import WebClient
client = WebClient(token = 'your token here')
response = client.chat_postMessage(
                channel = slack_cannel,
                text = message
                )
 ```   
 Logging
``` 
Import PostgresHook

#Extraction Job
def ExtractFromSource(query):
    query_to_run = query
    logging.info("Query : %" query_to_run)
    
    cursor = PostgresHook(connection).get_conn().cursor()
    logging.info("Connecting to Postgres Connection %" connection)
cursor.execute(query_to_run)
    result = cursor.fetchall()
```

## Airflow sensors

https://marclamberti.com/blog/airflow-sensors/

### Airflow wait for s3 file
https://www.mikulskibartosz.name/postpone-airflow-dag-until-s3-upload/

https://hevodata.com/learn/s3keysensor/

https://airflow.apache.org/docs/apache-airflow/1.10.5/_api/airflow/sensors/s3_key_sensor/index.html


https://blog.fal.ai/the-unbundling-of-airflow-2/ 

https://airflow.apache.org/docs/

https://levelup.gitconnected.com/airflow-command-line-interface-cli-cheat-sheet-6e5d90bd3552

airflow dags list
airflow tasks list

https://airflow.readthedocs.io/en/1.10.10/concepts.html

### Dynamic DAGs

https://www.astronomer.io/guides/dynamically-generating-dags

https://towardsdatascience.com/data-engineers-shouldnt-write-airflow-dags-b885d57737ce

https://towardsdatascience.com/data-engineers-shouldnt-write-airflow-dags-part-2-8dee642493fb


To to make Several DAGs folders?
https://xnuinside.medium.com/how-to-load-use-several-dag-folders-airflow-dagbags-b93e4ef4663c

we need to put in your standard dag_folder special tiny python script.
Call this file something like ‘add_dag_bags.py’ with very simple code inside. 
To show, how it works, we will create two separate folders: ‘~/new_dag_bag1’ and ‘~/work/new_dag_bag2’. 
It does not matter how much long path and there it is placed. Airflow just must have rights to access those folders.
Code in add_dag_bags.py will be:

```
""" add additional DAGs folders """
import os
from airflow.models import DagBag
dags_dirs = ['~/new_dag_bag1', '~/work/new_dag_bag2']

for dir in dags_dirs:
   dag_bag = DagBag(os.path.expanduser(dir))

   if dag_bag:
      for dag_id, dag in dag_bag.dags.items():
         globals()[dag_id] = dag
```

### Book

https://www.manning.com/books/data-pipelines-with-apache-airflow

https://www.manning.com/downloads/2060 . source code

https://marclamberti.com/blog/airflow-branchpythonoperator/ . BranchPythonOperator

Dynamic DAG
https://galea.medium.com/airflow-dynamic-dags-python-globals-4f40905d314a


Decorator Airflow
https://levelup.gitconnected.com/airflow-decorators-for-a-clean-data-pipeline-48ebdf12e9b0


```
import os
import sys
import sysconfig
import logging
from airflow.operators.python_operator import PythonOperator

def py_info():
  print("-- Python version --")
  print(sys.version_info)
  #logging.info(sys.version_info)

  print("site-packages=")
  print(sysconfig.get_path('purelib'))
  #logging.info(sysconfig.get_path('purelib'))


  print("\n--- ENVIRONMENT VARIABLES ---\n")
  for k,v in sorted(os.environ.items()):
     print(k,":",v)
     #logging.info(k + "=" + v)


  print("\n---- PATH ----\n")
  for item in os.environ["PATH"].split(':') :
     print(item)
     #logging.info(item)
     
info = PythonOperator(
  task_id = 'info',
  python_callable = py_info,
  dag = dag
)
```     

### Medium articles

https://towardsdatascience.com/tagged/apache-airflow

### Cross-DAG dependencies

https://blog.devgenius.io/airflow-cross-dag-dependency-b127dd3b69d8

https://medium.com/quintoandar-tech-blog/effective-cross-dags-dependency-in-apache-airflow-1885dc7ece9f

Airflow provides us with 3 native ways to create cross-dag dependency.
```
Push-based — TriggerDagRunOperator
Pull-based — ExternalTaskSensor
Across Environments — Airflow API (SimpleHttpOperator)
```





### Airflow 2

https://towardsdatascience.com/is-apache-airflow-2-0-good-enough-for-current-data-engineering-needs-6e152455775c



### Dynamically generated DAGs
https://www.astronomer.io/guides/dynamically-generating-dags

### Udemy

https://www.udemy.com/course/the-ultimate-hands-on-course-to-master-apache-airflow/learn/lecture/15819418#overview

(code in introduction )

https://github.com/marclamberti/airflow-materials-vm

https://marclamberti.com/


https://www.udemy.com/course/apache-airflow/learn/lecture/17368650

### Articles

https://habr.com/ru/post/549458/

https://khashtamov.com/en/introduction-to-apache-airflow/



### Kubernetes issue: Only works with the Celery or Kubernetes executors, sorry

https://github.com/apache/airflow/issues/12341

### backfill
```
 sudo /opt/airflow/airflow backfill --help
 
[2020-12-08 03:07:05,373] {__init__.py:51} INFO - Using executor CeleryExecutor
usage: airflow backfill [-h] [-t TASK_REGEX] [-s START_DATE] [-e END_DATE]
                        [-m] [-l] [-x] [-i] [-I] [-sd SUBDIR] [--pool POOL]
                        [--delay_on_limit DELAY_ON_LIMIT] [-dr] [-v] [-c CONF]
                        [--reset_dagruns] [--rerun_failed_tasks]
                        dag_id

positional arguments:
  dag_id                The id of the dag

optional arguments:
  -h, --help            show this help message and exit
  -t TASK_REGEX, --task_regex TASK_REGEX
                        The regex to filter specific task_ids to backfill
                        (optional)
  -s START_DATE, --start_date START_DATE
                        Override start_date YYYY-MM-DD
  -e END_DATE, --end_date END_DATE
                        Override end_date YYYY-MM-DD
  -m, --mark_success    Mark jobs as succeeded without running them
  -l, --local           Run the task using the LocalExecutor
  -x, --donot_pickle    Do not attempt to pickle the DAG object to send over
                        to the workers, just tell the workers to run their
                        version of the code.
  -i, --ignore_dependencies
                        Skip upstream tasks, run only the tasks matching the
                        regexp. Only works in conjunction with task_regex
  -I, --ignore_first_depends_on_past
                        Ignores depends_on_past dependencies for the first set
                        of tasks only (subsequent executions in the backfill
                        DO respect depends_on_past).
  -sd SUBDIR, --subdir SUBDIR
                        File location or directory from which to look for the
                        dag
  --pool POOL           Resource pool to use
  --delay_on_limit DELAY_ON_LIMIT
                        Amount of time in seconds to wait when the limit on
                        maximum active dag runs (max_active_runs) has been
                        reached before trying to execute a dag run again.
  -dr, --dry_run        Perform a dry run
  -v, --verbose         Make logging output more verbose
  -c CONF, --conf CONF  JSON string that gets pickled into the DagRun's conf
                        attribute
  --reset_dagruns       if set, the backfill will delete existing backfill-
                        related DAG runs and start anew with fresh, running
                        DAG runs
  --rerun_failed_tasks  if set, the backfill will auto-rerun all the failed
                        tasks for the backfill date range instead of throwing
                        exceptions

```



### How to get data from Postgres: use PostgresHook

 https://marclamberti.com/blog/the-postgresoperator-all-you-need-to-know/

 https://airflow.apache.org/docs/stable/_api/airflow/hooks/postgres_hook/index.html
 
 https://youtu.be/ATUARuFh3JQ

## Macro
https://stackoverflow.com/questions/64796614/airflow-how-to-pass-template-macro-to-hive-script

Book:
<https://livebook.manning.com/book/data-pipelines-with-apache-airflow/chapter-5/v-5/78>


## Dependencies between tasks - ExternalTaskSensor

https://www.mikulskibartosz.name/using-sensors-in-airflow/


## template and macros

<https://www.astronomer.io/guides/templating/> 

ds and macros variables can only be accessed through template as they only exists during execution and not during python code parsing
  
https://stackoverflow.com/questions/43149276/accessing-the-ds-variable-in-airflow

https://stackoverflow.com/questions/36730714/execution-date-in-airflow-need-to-access-as-a-variable/45725005#45725005

```
EXEC_DATE = '{{ ds }}'
EXEC_DATE = '{{ macros.ds_add(ds, 1) }}'
```

https://towardsdatascience.com/best-practices-for-airflow-developers-990c8a04f7c6
```
not all operator parameters are templated, so you need to make sure Jinja templating is enabled for the operators that you plan to pass macros to. 
To check which parameters in an operator take macros as arguments, look for the template_fields attribute in the operator source code.
For example, as of today, the most recent version of PythonOperator has three templated parameters:
‘templates_dict’, ‘op_args’, and ‘op_kwargs’:
template_fields = ('templates_dict', 'op_args', 'op_kwargs')

In order to enable templating for more parameters, simply overwrite thextemplate_fields attribute.
Since this attribute is an immutable tuple, make sure to include the original list of templated parameters when you overwrite it.
```
 http://airflow.apache.org/docs/stable/_modules/airflow/operators/hive_operator.html#HiveOperator.template_fields

https://habr.com/ru/company/lamoda/blog/518620/

<https://diogoalexandrefranco.github.io/about-airflow-date-macros-ds-and-execution-date/>
```
{{ ds }} The execution date of the running DAG as YYYY-MM-DD
{{ macros.ds_add(ds, 5) }} add 5 days
```
<https://airflow.apache.org/docs/stable/scheduler.html#scheduling-triggers>

```  
Note that if you run a DAG on a schedule_interval of one day, the run stamped 2016-01-01 will be trigger soon after 2016-01-01T23:59. 
In other words, the job instance is started once the period it covers has ended.
Let's Repeat That The scheduler runs your job one schedule_interval AFTER the start date, at the END of the period.
```
<https://stackoverflow.com/questions/58414350/airflow-skip-current-task> SkipTask

<https://habr.com/ru/post/512386/> Airflow in russian

http://blog.manugarri.com/how-to-trigger-a-dag-with-custom-parameters-on-airflow-ui/

## How to combine tasks

  Task C will run after both Task A and B complete
[task_a, task_b] >> task_c

```
from airflow.utils.helpers import chain
#  Both Task B and C depend on Task A
# Task D depends on both Task B and C
chain(task_a, [task_b, task_c], task_d)

# The statement above is equivalent to:
task_a >> [task_b, task_c] >> task_d

Use cross_downstream() to set dependencies between two groups of tasks:
from airflow.utils.helpers import cross_downstream
# Task C and D will run after both Task A and B complete
cross_downstream([task_a, task_b], [task_c, task_d])
# The statement above is equivalent to:
[task_a, task_b] >> task_c
[task_a, task_b] >> task_d
```
https://stackoverflow.com/questions/62895219/getting-error-in-airflow-dag-unsupported-operand-types-for-list-and-lis
```
File "/tmp/mlubinsky/roku-dag-bag.pex/agg/agg_daily_non_bucketed/agg_daily_non_bucketed.py", line 476, in get_agg_daily_dag
    >> [hive_agg_amoeba_allocation_daily_task_1, redshift_agg_amoeba_allocation_events_load_task_1]
TypeError: unsupported operand type(s) for >>: 'HiveOperator' and 'list'
```
Following does not work:
```
task_1 >> [task_2 , task_3] >> [ task_4 , task_5 ] >> task_6 
```
You can fix it:
```
task_1 >> [task_2 , task_3]
task_2 >> [task_4, task_5] >> task_6
task_3 >> [task_4, task_5]
```
or
```
task_1 >> [task_2 , task_3]
task_2 >> task_4
task_3 >> task_5
[task_4, task_5] >> task_6
```
Airflow task dependencies can't handle [list]>>[list]. Easiest way around this is to specify your dependencies over multiple lines:
```
task_1 >> [task_2 , task_3]
task_2 >> [task_4, task_5]
task_3 >> [task_4, task_5]
[task_4 , task_5 ] >> task_6
```



Another example:
```
first_event_chain = 
(
   hv_agg_channel_ux_day_prep & 
   hv_agg_channel_ux_day_stg & 
   hv_agg_channel_ux_day & 
   (
     agg_channel_ux_day |
           (
               hv_agg_channel_ux_week & agg_channel_ux_week
            ) 
            |
             (hv_agg_channel_ux_month & agg_channel_ux_month)
    )
    & 
    channel_events_done_dummy_task
 )


-----------------------------------------------

 channel_provider_ux_agg_task_chain = 
 (
   channel_provider_ux_check_done & 
     (hv_channel_provider_ux_details_stg & 
        (hv_channel_provider_ux_monthly  &
          (
            (
              check_agg_channel_ux_provider_metrics_monthly &
              channel_provider_ux_month &
              hv_channel_provider_ux_weekly &
              channel_provider_ux_weekly
            )
           | 
           channel_provider_task_chain
          ) &
          channel_provider_ux_dm_task
        ) | channel_provider_ux_done_dummy_task
       ) &   channel_provider_ux_join_task
 )
 
 
 
IF3 - Looking to check for path s3://roku-dea-dev/sand-box/roku-data-warehouse/donemarkers/tables/roku/agg_channel_ux_provider_metrics_time_grain/2020-10-23.done 
```                                        




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

## The Airflow scheduler triggers the task soon after the start_date + schedule_interval is passed.

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

 
https://levelup.gitconnected.com/running-airflow-in-docker-759068fb43b2

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

 
