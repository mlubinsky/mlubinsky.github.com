### How to install Apache Airflow 2.2.3 on  MacBook Pro:
```
1. Install Airflow Using pip:
Run the following command to install version 2.2.3:

 
pip install apache-airflow==2.2.3
2. Set Up Virtual Environment (Optional but Recommended):
To avoid conflicts with other Python packages, it is best to use a virtual environment:

 
python3 -m venv airflow-env
source airflow-env/bin/activate
pip install apache-airflow==2.2.3

3. Initialize Airflow:
After installation, set up your Airflow environment by initializing the database:

 
airflow db init
4. Start Airflow:
Once Airflow is set up, start the web server:

 
airflow webserver --port 8080
And then start the scheduler in another terminal window:

 
airflow scheduler
This method will give you complete control over the version of Apache Airflow you need. 

 
I am using python 3.10.9 
Is it compatible with  airflow 2.2.3 ?


Apache Airflow 2.2.3 is not compatible with Python 3.10. It supports Python versions up to 3.9.
Python 3.10 compatibility was introduced starting with Airflow version 2.3.0.

To use Airflow 2.2.3, you will need to install Python 3.9 or lower. Here’s how you can manage this:

Install Python 3.9 (if not installed already):
You can install Python 3.9 alongside your existing Python installation using pyenv or directly through Homebrew.

Using Homebrew:
 
brew install python@3.9
Using pyenv: If you prefer to use pyenv for managing multiple Python versions:
 
brew install pyenv
pyenv install 3.9.18
pyenv global 3.9.18  # Set Python 3.9 as global for the terminal
Set up Airflow with Python 3.9:
Once Python 3.9 is installed, you can create a virtual environment and install Airflow 2.2.3 in that environment:

Create a virtual environment using Python 3.9:

 
python3.9 -m venv airflow-env
source airflow-env/bin/activate
Install Apache Airflow 2.2.3:

 
pip install apache-airflow==2.2.3
This will ensure compatibility between Python and the specific Airflow version.  


You said:
I am using python 3.9.6 
Is it compatible with  airflow 2.2.3 ?
ChatGPT said:
 
Yes, Python 3.9.6 is compatible with Apache Airflow 2.2.3.
You should be able to install and run Airflow 2.2.3 without any compatibility issues using this Python version.

You can proceed with installing Airflow 2.2.3 using the steps we discussed earlier.

I run:
airflow db init
and I got errord=s:
ImportError: cannot import name 'soft_unicode' from 'markupsafe'
ChatGPT said:
 
The error you're seeing, ImportError: cannot import name 'soft_unicode' from 'markupsafe', 
occurs due to a compatibility issue between the version of markupsafe and Airflow 2.2.3.

This error is common with older versions of Airflow when a newer version of the markupsafe package (>= 2.1) is installed. The soft_unicode function was removed in Markupsafe 2.1, while Airflow 2.2.3 still depends on this function.

Solution: Downgrade markupsafe
To resolve this, downgrade markupsafe to a version that includes soft_unicode, such as 2.0.1.

You can downgrade markupsafe using the following command:

 
pip install markupsafe==2.0.1
After downgrading, retry the Airflow database initialization:

 
airflow db init
Let me know if you encounter further issues!


You said:
should I uninstall Markupsafe 3.0.1 before installing version 2.0.1 ?
ChatGPT said:
 
You do not need to manually uninstall markupsafe 3.0.1 before downgrading. When you run the pip install markupsafe==2.0.1 command, pip will automatically replace the existing version (3.0.1) with the one you specify (2.0.1).

Here’s the command to directly install the compatible version:

 
pip install markupsafe==2.0.1
This will ensure that the incompatible version is replaced with the correct one. After the installation, you can check if the downgrade was successful by running:

 
pip show markupsafe
This should display version 2.0.1. You can then retry running

airflow db init.

 
I open Chrome browser on localhost:8080
I need to provide username and password. I do not know them.
 
By default, Apache Airflow uses the authentication mechanism called "RBAC"
(Role-Based Access Control), which requires a username and password to access the web interface.

To create an admin user (username and password), you can use the following command:
Run this in your terminal where Airflow is set up:

 
airflow users create \
  --username admin \
  --firstname Admin \
  --lastname User \
  --role Admin \
  --email admin@example.com \
  --password admin
This will create a user with the username admin and password admin (you can change these values as needed).

Login:

After running the command, go back to the Airflow web UI at localhost:8080 and log in using the credentials you just set:
Username: admin
Password: admin (or whatever password you set)
```

### Create and run the simplest Airflow DAG (Directed Acyclic Graph), follow these steps:
```
Step 1: Create a New DAG File
Navigate to your Airflow DAGs folder (typically ~/airflow/dags on your system).

Create a new Python file for your DAG. For example, simple_dag.py.

 
cd ~/airflow/dags
nano simple_dag.py
Add the following simple DAG code in simple_dag.py:

 
from datetime import datetime
from airflow import DAG
from airflow.operators.dummy import DummyOperator

# Define the default arguments for the DAG
default_args = {
    'start_date': datetime(2023, 10, 1),  # Set the start date for the DAG
}

# Create the DAG object
dag = DAG(
    'simple_dag',  # Name of the DAG
    default_args=default_args,
    schedule_interval='@daily',  # Runs daily
    catchup=False  # Prevent backfilling
)

# Define a dummy task
start = DummyOperator(
    task_id='start_task',
    dag=dag,
)

# Task order (in this case, it's just one task)
start
This DAG contains:

One task (start_task) using a DummyOperator (a placeholder task that does nothing).
The DAG runs daily (schedule_interval='@daily'), starting from October 1, 2023.
catchup=False prevents backfilling (Airflow won't try to run the DAG for dates in the past).
Step 2: Activate the DAG in Airflow
Make sure Airflow is running:

Start the scheduler and web server if they aren't already running:

 
airflow scheduler
In another terminal, run:

 
airflow webserver --port 8080
Open the Airflow web UI by navigating to http://localhost:8080.

In the DAGs list, look for simple_dag. It should appear after a short time. If it doesn’t show up immediately, you can trigger a refresh by restarting the scheduler:

 
airflow dags trigger simple_dag

Step 3: Trigger the DAG
On the web interface, find simple_dag and turn on the toggle switch to make the DAG active.
To manually run the DAG, click the Play button (Trigger DAG) next to simple_dag in the web UI.
After triggering, the DAG will start executing. You can view task progress and logs by clicking on the Graph View or Task Instance.
Step 4: Monitor the DAG
You can monitor the DAG execution in the web interface:

Tree View: Shows a tree of task instances over time.
Graph View: Shows the dependencies of tasks in the DAG.
Task Instance Logs: You can view the logs of each task execution by clicking on the task in the Graph View.
This is the simplest setup to create, run, and monitor a DAG in Apache Airflow.
```

