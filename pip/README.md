https://snarky.ca/how-virtual-environments-work/ 

https://news.ycombinator.com/item?id=35131357

https://pypa.github.io/pipx/

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


### Flake Black
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


### pyenv pipenv

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

$ python3 -m venv venv_name
echo $PATH
source path_to_venv_name/bin/activate (or . venv_name/bin/activate)
echo $PATH

pip install ...
...
deactivate
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

