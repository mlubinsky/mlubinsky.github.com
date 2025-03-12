### Install Python on Mac
https://lobste.rs/s/rchiux/how_install_python_on_mac

### UV
https://bluesock.org/~willkg/blog/dev/switch_pyenv_to_uv.html

https://news.ycombinator.com/item?id=43307563

- uv python install <version> if you want a particular version of python to be installed

- uv init --vcs none in each directory to initialize the python project

- uv add [--dev] to add libraries to your venv

- uv run <cmd> when you want to run a command in the venv

### PyInstaller
https://lobste.rs/s/szslrx/how_convert_python_applications

### How to run multiple Python versions on Windows:

https://stackoverflow.com/questions/4583367/how-to-run-multiple-python-versions-on-windows

```
py -0
 -V:3.8 *         Python 3.8 (64-bit)
 -V:2.7           Python 2.7
 -V:2.7-32        Python 2.7-32

```
instead of running python command run pylauncher command (py) specyfing which version of Python you want;
```
py -2.6 – version 2.6
py -2 – latest installed version 2.x
py -3.4 – version 3.4
py -3 – latest installed version 3.x
```

https://devblogs.microsoft.com/python/python-linting-video/

https://www.b-list.org/weblog/2022/may/13/boring-python-dependencies/

https://www.b-list.org/weblog/2023/dec/07/pip-install-safely/

https://www.stuartellis.name/articles/python-modern-practices/

https://habr.com/ru/companies/productstar/articles/826732/ pip commands explained

```
python -m pip install -r requirements/app.txt


python -m pip install \
    --require-hashes \
    --no-deps \
    --only-binary :all: \
    -r requirements/app.txt

```

https://www.b-list.org/weblog/2023/dec/05/understanding-python-venv/

virtualenv -p c:\python2.5\python.exe c:\venvs\2.5

virtualenv -p c:\python2.6\python.exe c:\venvs\2.6

then you can activate the first and work with Python 2.5 like this

c:\venvs\2.5\activate

and when you want to switch to Python 2.6 you do

deactivate  
 
The py script.py launches the Python version stated in #! or Python 2 if #! is missing. The py -3 script.py launches the Python 3.

### My Mac
```
pwd
/Users/mlubinsky/Library/Python/3.9/bin

-rwxr-xr-x@ 1 mlubinsky  staff       256 Apr 18 12:50 pip
-rwxr-xr-x@ 1 mlubinsky  staff       256 Apr 18 12:50 pip3
-rwxr-xr-x@ 1 mlubinsky  staff       256 Apr 18 12:50 pip3.10
-rwxr-xr-x@ 1 mlubinsky  staff       256 Apr 18 12:50 pip3.9
-rwxr-xr-x@ 1 mlubinsky  staff  23797762 Apr 18 12:49 ruff


pip3 list
Package    Version
---------- -------
altgraph   0.17.2
future     0.18.2
macholib   1.15.2
pip        23.1
ruff       0.0.261
setuptools 58.0.4
six        1.15.0
wheel      0.37.0
[~]$ ruff
-bash: ruff: command not found
 
[~]$ python3 -m pip  install ruff
Defaulting to user installation because normal site-packages is not writeable
Requirement already satisfied: ruff in ./Library/Python/3.9/lib/python/site-packages (0.0.261)
 
[~]$ pip3 -V
pip 23.1 from /Users/mlubinsky/Library/Python/3.9/lib/python/site-packages/pip (python 3.9)
```
https://snarky.ca/how-virtual-environments-work/ 

https://news.ycombinator.com/item?id=35131357

### PIPX 

https://github.com/pypa/pipx

https://pypa.github.io/pipx/

Installing self-contained programs written in Python not packaged for your distro:

    PIPX_HOME=/usr/local/pipx PIPX_BIN_DIR=/usr/local/bin pipx install app==1.2.3
    
It sets up an isolated install for each app with only its deps and makes it transparent.

 
 



https://pip-tools.readthedocs.io/en/latest/

https://pdm.fming.dev/ PDM

https://mathspp.com/blog/how-to-create-a-python-package-in-2022

https://realpython.com/python-virtual-environments-a-primer/ 

https://hackercodex.com/guide/python-development-environment-on-mac-osx/


https://kaderovski.com/posts/ultimate-python-development-environment-configuration/

https://bas.codes/posts/python-virtualenv-venv-pip-pyenv-poetry

<https://modelpredict.com/python-dependency-management-tools> 

https://python.plainenglish.io/10-tools-to-help-claw-your-way-back-to-sanity-while-coding-python-df0af160c33e

https://www.andreagrandi.it/2022/01/29/install-python-with-pyenv-and-pyenvvirtualenv-create-virtual-environment-with-specific-python-version-macos/

https://blog.pronus.io/en/posts/python/how-to-set-up-a-perfect-python-project/


pyenv + poetry
https://briansunter.com/blog/python-setup-pyenv-poetry/


### Flake Black ruff

https://devblogs.microsoft.com/python/python-linting-video/

```
python3 -m pip  install ruff
Defaulting to user installation because normal site-packages is not writeable
Requirement already satisfied: ruff in ./Library/Python/3.9/lib/python/site-packages (0.0.261)
```
https://habr.com/ru/company/skillfactory/blog/659493/

python3 -m pip install flake8

flake8 myscript.py

python3 -m pip install black

black --check myscript.py

black --diff myscript.py

black myscript.py

### pip

https://realpython.com/what-is-pip/

<https://snarky.ca/why-you-should-use-python-m-pip/>.  python -m pip

```pip search ZZZ``` does not work
Solution:

```
   pip install pip_search
   pip_search ZZZ
```

 https://pythonspeed.com/articles/conda-vs-pip/    Pip vs conda

Python 2.7 pip.  
curl https://bootstrap.pypa.io/2.7/get-pip.py --output get-pip.py

https://www.codementor.io/@adammertz/quick-tip-how-i-use-pip-tools-to-wrangle-dependencies-1fzreskhok . pip-tools


<https://cjolowicz.github.io/posts/hypermodern-python-01-setup/>

<https://pip.pypa.io/en/stable/user_guide/>

### venv vs  virtualenv

 venv: This is a built-in module in Python >= 3.3 
 
Two most popular virtual environment libraries for Python are venv and virtualenv. The difference between these two are negligible. However, there is one big difference and that is venv is a standard library that does not need to be installed while virtualenv needs to be installed with pip.

### pipenv vs virtualenv

pipenv is similar to virtualenv , it has one extra feature, which is Pipfile , Pipfile is similat to what we see as packages. json in npm . Pipfile contains all the installed packages in the current environment, and automatically updates itself if you install a new package inside the same environment.


### pyenv pipenv
```
To install Python 3.10, I recommend using pyenv. 
Pyenv allows you to have multiple versions of Python on your workstation.
Here’s what I did to install 3.10.4 on my laptop after installing Pyenv. (3.10.4 was the latest version of 3.10 
when I wrote this, you might choose to install any version above 3.10.0).

pyenv install 3.10.4

Then, I used pyenv-virtualenv to make a virtual environment to work with the new 3.10 install.

pyenv virtualenv 3.10.4 python-matching
pyenv activate python-matching
```

https://www.jackhoy.com/web-applications/2017/02/12/setting-up-a-python-dev-environment.html

<https://github.com/pyenv/pyenv>

https://chriswarrick.com/blog/2018/07/17/pipenv-promises-a-lot-delivers-very-little/

<https://dev.to/writingcode/the-python-virtual-environment-with-pyenv-pipenv-3mlo>

<https://khashtamov.com/ru/pyenv-python/>

<https://virtualenv.pypa.io/en/latest/> 
pyenv, poetry, black, flake8, isort, pre-commit, pytest, coverage, tox, Azure Pipelines, sphinx, and readthedocs:

<https://medium.com/georgian-impact-blog/python-tooling-makes-a-project-tick-181d567eea44>


### Virtualenv

```
/Users/mlubinsky/my_virt_envs
which pip
python -m pip install virtualenv
virtualenv -p /Users/mlubinsky/opt/anaconda3/bin/python pywedge
source pywedge/bin/activate
```

```
import sys
print(sys.prefix) # '/System/Library/Frameworks/Python.framework/Versions/3.5'
import site
data = site.getsitepackages()
print(data)

pip install virtualenv
mkdir python-virtual-environments 
cd python-virtual-environments

# Python 2:
$ virtualenv env
```

### venv + pip (Python 3)
```
python3 -m venv venv_name
echo $PATH
source path_to_venv_name/bin/activate (or . venv_name/bin/activate)
echo $PATH

pip install ...
...
deactivate

Airflow

https://medium.com/accredian/setting-up-apache-airflow-in-macos-57ab9e8edb8a

python3 -m venv airflow_env
source airflow_env/bin/activate
pip3 install apache-airflow[gcp,sentry,statsd]
pip3 install pyspark
airflow db init
mkdir dags
airflow users create --username admin --password your_password --firstname your_first_name --lastname your_last_name --role Admin --email your_email@some.com
airflow users list
airflow scheduler
airflow webserver
Once the scheduler and webserver get initialized, open any browser and go to http://localhost:8080/.
airflow.cfg file 
```


You can call it directly by referencing the venv python exe eg 

venv_folder/bin/python /path/to/your/script.py


### Anaconda setup

Install Anaconda https://towardsdatascience.com/how-to-easily-set-up-python-on-any-m1-mac-5ea885b73fab


###   Python  on   Mac  :
https://asdf-vm.com/

https://justinmayer.com/posts/homebrew-python-is-not-for-you/

https://hackercodex.com/guide/python-development-environment-on-mac-osx/

https://gist.github.com/chris-zen/9e61db6924bd37fbe414f648614ca4c5

https://www.youtube.com/watch?v=qJ-0N34Sa_E How to set up Python 3.8 for software development (In 2021)

#### pytest
https://coderslegacy.com/pytest-tutorial-unit-testing-in-python/
