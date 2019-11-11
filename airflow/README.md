https://airflow.apache.org/

<https://github.com/apache/airflow>

<http://pydoc.net/apache-airflow>

```
>>> from airflow.models import DAG
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/Users/mlubinsky/ide_virtual_env/lib/python2.7/site-packages/airflow/__init__.py", line 30, in <module>
    from airflow import version
ImportError: cannot import name version
```
# print the list of active DAGs
airflow list_dags

# prints the list of tasks the "tutorial" dag_id
airflow list_tasks tutorial

# prints the hierarchy of tasks in the tutorial DAG
airflow list_tasks tutorial --tree

# initialize the database
airflow initdb

# start the web server, default port is 8080
airflow webserver -p 8080

# start the scheduler
airflow scheduler

# visit localhost:8080 in the browser and enable the example dag in the home page
```

The first time you run Airflow, it will create a file called airflow.cfg in your $AIRFLOW_HOME directory
(~/airflow by default). This file contains Airflow’s configuration and you can edit it to change any of the settings.

https://cwiki.apache.org/confluence/display/AIRFLOW/Airflow+Home

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
‘We’re All Using Airflow Wrong and How to Fix It’ by Jessica Laughlin. Bluecore Engineering. Aug, 2018.

```
