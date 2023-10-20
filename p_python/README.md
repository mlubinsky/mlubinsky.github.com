### Python notes

https://github.com/gto76/python-cheatsheet

https://wiki.python.org/moin/TimeComplexity

https://github.com/luminousmen/data-toolset   Avro and Parquet 

https://habr.com/ru/companies/kaspersky/articles/762788/

### random notes
```
from math import factorial
factorial(3)
6

list('abc')
['a', 'b', 'c']
w = [c for c in 'abc']
w
['a', 'b', 'c']
``` 
### Float type
https://www.techbeamers.com/floating-point-numbers-in-python/
```
Machine epsilon (eps) is the smallest positive number that, when added to 1.0, results in a value greater than 1.0.
It measures the precision of the floating-point system.
In Python, you can access the machine epsilon using sys.float_info.epsilon.
```
Example:  Machine epsilon in Python
```
import sys
epsilon = sys.float_info.epsilon
print(epsilon)  # Output: 2.220446049250313e-16
```

 Special values in floating-point: inf -inf
```
infinity_pos = float('inf')
infinity_neg = float('-inf')
nan = float('nan')

print(infinity_pos)  # Output: inf
print(infinity_neg)  # Output: -inf
print(nan)           # Output: nan
```
  Overflowing a float to infinity
```
large_number = 1.7e308     # A very large positive floating-point number
result = large_number * 2  # Doubling the already large number
print(result)              # Output: inf
```

#### Task runners

https://just.systems/man/en/chapter_1.html

https://taskfile.dev/

https://pydoit.org/

https://github.com/TekWizely/run


####
https://www.bitecode.dev/p/you-are-comfy-with-python-basics

https://lobste.rs/s/sns4mr/comfy_with_python_basic_tooling_now_what

```
An object’s identity is a unique identifier that distinguishes it from other objects. 
ou can use the built-in id() function to get the identity of any Python object.

In Python, you can create aliases of variables using the assignment operator (=). 
Assignments don’t create copies of objects in Python. 
Instead, they create bindings between the variable and the object involved in the assignment. 
Therefore, when you have several aliases of a given list, changes in an alias will affect the rest of the aliases.
```

### shallow copy/ deepcopy
```
copy() - the elements themselves are not deep-copied, so if the original object contains nested structures (like lists or dictionaries), 
the references to these nested objects are copied, not the objects themselves. 
This means that changes made to the nested objects in the original object will also be reflected in the shallow copy and vice versa:`

A shallow copy of an existing list is a new list containing references to the objects stored in the original list. 
In other words, when you create a shallow copy of a list, Python constructs a new list with a new identity.
Then, it inserts references to the objects in the original list into the new list.
There are at least three different ways to create shallow copies of an existing list. You can use:

 - The slicing operator, [:]
 - The .copy() method
 - The copy() function from the copy module
```
Code:
```
countries = ["United States", "Canada", "Poland", "Germany", "Austria"]
nations = countries[:]   # sane as  nations = countries.copy()
id(countries) == id(nations) # Result: False
id(nations[0]) == id(countries[0]) # Result: True
# let update countries  -> it will not impact nations:
#  if you change an element in one of the lists, then the change won’t reflect in the copy.
countries[0] = "USA"
id(countries[0]) == id(nations[0]) # Result: False
```

When you create a deep copy of a list, Python constructs a new list object and then inserts copies of the objects from the original list recursively.
```
from copy import deepcopy
>>> matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
>>> matrix_copy = deepcopy(matrix)
```
### List  
https://realpython.com/python-list/
https://realpython.com/how-to-split-a-python-list-into-chunks/
https://realpython.com/python-flatten-list/
```
 append() adds single item to list
 extend()  adds iterable to list
 insert(index,value) into specified position
 remove(item) removes 1st occurance
 pop([index]) argument is optional - removes last item in the list
 clear() removes all
 index("value") - raises ValueError exception if not found, if value occures many times it returns 1st entry
 count("value") - returns 0 if not found 
```

### List comprehention  [expression for item in list if conditional]

list comprehension is the process of creating a new list from an existing list. Or, you can say that it is Python's unique way of appending a for loop to a list
```
list_b = [i**2 for i in range(1, 20)]
```
### List as stack or queue
https://realpython.com/how-to-implement-python-stack/
https://realpython.com/queue-in-python/

```
stack = []
stack.append("Copy")
stack.append("Paste")
stack.append("Remove")
stack # ['Copy', 'Paste', 'Remove']

stack.pop() #'Remove'
stack.pop() #'Paste'
stack.pop() #'Copy'
stack       # []
```

queue:
```
queue = []
queue.append("John")
queue.append("Jane")
queue.append("Linda")
queue  # ['John', 'Jane', 'Linda']
queue.pop(0) # 'John'
queue.pop(0) # 'Jane'
queue.pop(0) #'Linda'
```

However, in performance-critical situations or when your lists are large, you may want to use more efficient data types, such as collections.deque, for example.

### Set  -  mutable
```
my_list = [1, 2, 2, 3, 4, 4, 4]
the_set = set(my_list) 

my_set.remove('x') # If the element is not found in the set, the remove() method will raise a KeyError

 discard()  removes the specified element if it's present, but if it's not, the method does nothing and doesn't raise an error
 clear()
 combined = a.union(b)
 combined = a | b
 common_elements = a.intersection(b)
 common_elements = a & b
 diff_elements = a.difference(b)
 diff_elements = a - b
 x.issubset(y)
 (y.issuperset(x)
 {expression for item in iterable if condition}
 numbers = [1, 2, 3, 4, 5, 6]
 even_numbers = {x for x in numbers if x % 2 != 0}

 frozen_numbers = frozenset(numbers)
```
### Import

https://coderslegacy.com/how-to-import-python-files-from-subdirectories/

https://coderslegacy.com/python-lazy-loading-with-importlib/

How to import arbitrary code: https://stackoverflow.com/questions/19009932/import-arbitrary-python-source-file-python-3-3
```
#!/usr/bin/env python3

import os
import importlib

def import_path(path):
    module_name = os.path.basename(path).replace('-', '_')
    spec = importlib.util.spec_from_loader(
        module_name,
        importlib.machinery.SourceFileLoader(module_name, path)
    )
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    sys.modules[module_name] = module
    return module

notmain = import_path('not-main')
print(notmain)
print(notmain.x)
```

### functools module

https://florian-dahlitz.de/articles/introduction-to-pythons-functools-module
```
cached_property()
cmp_to_key()
lru_cache()
partial()
partialmethod()
reduce()
singledispatch()
singledispatchmethod()
total_ordering()
update_wrapper()
wraps()
```

@functools.cache
def do_something(a, b):

#### functools reduce()
```
from functools import reduce
city = ['L', 'o', 'n', 'd', 'o', 'n', 2, 0, 2, 0]
city_to_str = reduce(lambda x, y: str(x) + str(y), city)
print(city_to_str)
# London2020
```

### Collection module: 
https://www.pynerds.com/python-collections-module/

https://erikvandeven.medium.com/python-uncovering-the-overlooked-core-functionalities-54590420c225

https://github.com/dabeaz-course/python-mastery/tree/main

https://news.ycombinator.com/item?id=36853495

https://dev.to/scofieldidehen/advanced-python-tips-for-development-olo

Code quality tools:

https://habr.com/ru/companies/otus/articles/750214/

### Conference talks

https://www.youtube.com/c/pyconus

https://www.youtube.com/playlist?list=PLt4L3V8wVnF4GJb8dekLGTNx44FNIFwdv

#### pip

https://stackabuse.com/installing-python-packages-from-a-git-repo-with-pip/

https://www.b-list.org/weblog/2022/may/13/boring-python-dependencies/

https://www.bitecode.dev/p/relieving-your-python-packaging-pain

```
import sys
sys.executable
## Result: '/Users/mlubinsky/anaconda3/bin/python'
```

### Using -m flag

python -m pip install -U pip

https://stackoverflow.com/questions/50821312/meaning-of-python-m-flag

https://til.simonwillison.net/python/stdlib-cli-tools

https://news.ycombinator.com/item?id=36515531

python -m http.server 8001
```
modules with a if __name__ == "__main__": block that are available on Python's standard  path
can be executed from the terminal using python -m name_of_module
```
python -m site

```
try:
    from StringIO  StringIO ## for Python 2
except Error:
    from io  StringIO ## for Python 3
```

### Dictionary

####  Merge dictionaries
```
d1 = {'a': 1, 'b': 2}
d2 = {'b': 3, 'c': 4}
{**d1, **d2}
{'a': 1, 'b': 3, 'c': 4}
```
It returns a new dictionary object, 
however, if d1 and d2 have the same key, then d1 will overwrite d2. 

If you use the dictionary update method, the original object will be modified, for example:
```
d1 = {'a':1, 'b':2}
d1 = {'c':1, 'd':2}
d2.update(d1)
d2
{'c': 1, 'd': 2, 'a': 1, 'b': 2}
```
#### Iterate dictionary
```
d = {'c': 3, 'd': 4, 'a': 1, 'b': 2}
 
for key, value in d.items():
    print(key, value)
 

for key in d:
    print(key, d[key])

```
#### Dictionary derivation
You can use dict comprehension to build a dictionary:
```
fruits = ['apple', 'mango', 'banana','cherry']
{f:len(f) for f in fruits}
```
Result:

{'apple': 5, 'mango': 5, 'banana': 6, 'cherry': 6}

####  Sort dictionary
A dictionary is essentially an unordered container object (in fact, 
Python 3.6 started to support order, but this order refers to the order in which keys are added). 
You can sort a dictionary by key or value using lambda function as sort key:
```
d = {"c": 3, "a": 1, "f":6, "b": 0}

##### Sort by key
 
sorted(d.items(), key=lambda x:x[0])
# [('a', 1), ('b', 0), ('c', 3), ('f', 6)]

#### Sort by value
sorted(d.items(), key=lambda x:x[1])
# [('b', 0), ('a', 1), ('c', 3), ('f', 6)]
```
####  Dictionary count
Count the number of occurrences of each letter in the list:
```
chars = ['a', 'b','c','a','d','c']
d = {}
for c in chars:
    d[c] = d.get(c, 0) + 1

# {'a': 2, 'b': 1, 'c': 2, 'd': 1}
Or you can use the collections.defaultdict method:

 collections
chars = ['a', 'b','c','a','d','c']

dd = collections.defaultdict(int)
for c in chars:
    dd[c] += 1
```

####  Delete item from dictionary
 
```
d = {'ob1':'computer', 'ob2':'mouse', 'ob3':'printer'}
del d['ob1']
# {'ob3': 'printer', 'ob2': 'mouse'}

Delete all items:

d = {'ob1':'computer', 'ob2':'mouse', 'ob3':'printer'}
d.clear()
# {}
```
#### Convert two lists to a dictionary
To create a dictionary from two sequences, use the dict() and zip() method.
```
stocks = ['reliance', 'infosys', 'tcs'] 
prices = [2175, 1127, 2750] 
d = dict(zip(stocks, prices))
print(d)# {'reliance': 2175, 'infosys': 1127, 'tcs': 2750}
```

#### fromkeys() to build a dictionary
```
The dictionary fromkeys() method is used to create a new dictionary, 
and the elements in the iterable object are used as the keys in the dictionary, 
and all keys correspond to the same value, and the default is None.

{}.fromkeys(["name", "age"])
{'name': None, 'age': None}

  or if you don't wnat to use None
{}.fromkeys(["Jack", "Chow","Fook"], 0)
{'Jack': 0, 'Chow': 0, 'Fook': 0}
10. setdefault() to return the value of a key
The syntax of the method setdefault() is dict.setdefault(key, default=None).

Parameters:

key — the key value to look up.
default — the default key value to set when the key does not exist.
Return value:
If the key is in the dictionary, return the corresponding value. If not in the dictionary, insert the key and set the default value default, and return default, the default value is None.
```
For example:
```
dict1 = {'name': 'tony', 'likes': 'soccer', 123: 456}

dict1.setdefault('name', 'jack')
dict1.setdefault('likes', None)
dict1.setdefault('weight', None)

# Output
{'name': 'tony', 'likes': 'soccer', 123: 456, 'weight': None}

```
### Ruff - linter, it also can replaces Black and isort
https://marketplace.visualstudio.com/items?itemName=charliermarsh.ruff

https://stackoverflow.com/questions/75639719/decrease-mistake-severity-for-ruff-python-linter-in-vscode-extension

```
pip install ruff
ruff check .
ruff check file.py --ignore E501    # to ignore E501 Line too long
```
https://www.blog.pythonlibrary.org/2023/06/28/an-intro-to-ruff-an-extremely-fast-python-linter/

### Links
https://medium.com/techtofreedom/10-python-interview-questions-for-senior-developers-4fefe773719a

https://www.jjinux.com/2022/08/python-my-favorite-python-tricks-for.html

https://realpython.com/python-string-contains-substring/

https://www.stationx.net/python-data-structures-cheat-sheet/

https://github.com/amaargiru/pycore

https://github.com/prabhupant/python-ds

https://itnext.io/dependency-injection-in-python-a1e56ab8bdd0

https://medium.com/@fareedkhandev/best-data-analysis-library-in-python-ad2572288017 PyGWalker


### Profiling

https://docs.python.org/3/library/profile.html

https://github.com/plasma-umass/scalene

https://pypi.org/project/scalene 

https://habr.com/ru/companies/ruvds/articles/757336/ cProfile  / profile

https://realpython.com/python-profiling/

### Fast python

https://pythonbooks.org/python-high-performance-second-edition/

https://www.amazon.com/High-Performance-Python-Performant-Programming/dp/1492055026/

https://www.amazon.com/Python-Science-Tiago-Rodrigues-Antao/dp/1617297933

https://pythonspeed.com/

https://coderslegacy.com/cython-vs-cpython-comparing-speed/  Cython

### Multiprocessing 

https://www.bitecode.dev/p/the-easy-way-to-concurrency-and-parallelism

https://news.ycombinator.com/item?id=37089817

https://milliams.com/courses/parallel_python/

https://superfastpython.com/ Threading, Multiprocessing, and AsyncIO

https://github.com/sybrenjansen/mpire

Combining mulithreading and multiprocessing:
https://heyashy.medium.com/blazing-fast-etls-with-simultaneous-multiprocessing-and-multithreading-214865b56516

```
 statistics
from multiprocessing  Pool

data = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [7, 6, 5, 4],
]

with Pool() as pool:
    row_means = pool.map(statistics.fmean, data)

assert row_means == [2.5, 6.5, 5.5]
```
#### Immutable types

  Integers, floats, complex numbers, and Booleans, are always immutable. 
  
  Strings, bytes and tuples are immutable 

positive_infinity = float('inf')
negative_infinity = float('-inf')
  
#### Mutable types  
  lists, dictionaries, and sets are mutable 
```  
   isinstance([1, 2, 3], list)
   issubclass(bool, int) #  True
   isinstance(True, int) # True
   isinstance(False, int)  True
   
   int(True) # 1
   int(False) # 0 
```
### translate() and maketrans()

combination of translate() and maketrans() methods provide more flexibility by allowing for simultaneous multiple-character translations. It's useful when you have a set of characters that need to be replaced. However, for simple task of removing a single character, it's smarter to stick to replace().



### Links

https://docs.python-guide.org/ 

https://stackabuse.com/guide-to-lists-in-python/ List

https://docs.python.org/3/library/devmode.html

https://realpython.com/python-iterators-iterables/

https://docs.python.org/3/library/functions.html

https://docs.python.org/3/library/index.html


https://stackoverflow.com/questions/1349332/python-passing-a-function-into-another-function


### Standard libs: contextlib and others

https://pub.towardsai.net/20-underdog-python-built-in-libraries-that-deserve-much-more-attention-6ff35baeb06c

https://towardsdatascience.com/how-to-build-custom-context-managers-in-python-31727ffe96e1

```
from contextlib  contextmanager

@contextmanager
def timer():
    # Start the timer
    start = time.time()
    # context breakdown
    yield
    # End the timer
    end = time.time()

    # Tell the user how much time elapsed
    print(f"This code block executed in {round(end - start, 3)} seconds.")

 time

with timer():
    for _ in range(10):
        time.sleep(0.5)

```

### Exceptions
```
try:
    # Some code that may raise an exception.
except <ExceptionType> as err:
    # This part will only be executed when the specified exception is raised.
else:
    # This part will only be executed when no exception is raised.
finally:
    # This part will always be excuted
```

log the traceback, rather than just the error message. 
```
import traceback

try:
    num = int("abc")
except ValueError as err:
    print(traceback.format_exc)
```
or using logging
```
import logging

logger = logging.getLogger()

try:
    num = int("abc")
except ValueError as err:
    logger.exception(err)
```

### Communicating with OS and filesystem

https://realpython.com/python-pathlib/ Pathlib module from standard library (instead of os.path and glob)
Example: search file recursively:
```
import pathlib
folder="/opt/homebrew"
fname="README"
l=list(pathlib.Path(folder).rglob(fname))

for e in l:
    basename = pathlib.Path(e).stem
    p = pathlib.Path(e).parent
    print(basename, p,  e)

# read file:

from pathlib import Path

file_contents = Path('my.log').read_text()
file_lines = Path("my.log").read_text().splitlines()  # list of lines

path = Path(__file__).parent / "config.json"  # relative to this module

if not path.exists():  # Check for existence
    path.parent.mkdir(parents=True, exist_ok=True)  # Create directories
    path.write_text("{}")  # Writing creates a new file by default

```


shutil (for copy,move, chown, which, create archive)

https://cheatography.com/mad100141/cheat-sheets/path-cheat-sheet-python/

### Running apps from python subprocess and alternatives : 

https://realpython.com/python-subprocess/

https://martinheinz.dev/blog/98

https://docs.python.org/3/library/shlex.html

sh  https://amoffat.github.io/sh/index.html https://amoffat.github.io/sh/sections/faq.html

https://www.pyinvoke.org/

### 3rd party libs

https://pythonspeed.com/articles/faster-python-json-parsing/  Fast memory-efficient Python JSON parsing with msgspec

https://www.reddit.com/r/Python/comments/16j7pj5/what_python_libraries_programs_will_blow_peoples/

https://www.youtube.com/watch?v=g_Q19NKPWR4

https://github.com/vinta/awesome-python

https://pluggy.readthedocs.io/en/latest/ Pluggy

https://github.com/Suor/funcy. A fancy and practical functional tools

https://toolz.readthedocs.io/en/latest/  https://github.com/pytoolz/cytoolz

https://martinheinz.dev/blog/96 Missing Python libs (boltons, etc)

https://pypi.org/project/ubelt/ ubely

https://medium.com/codex/boost-your-python-project-with-these-7-libraries-f8f364f6afa7

https://github.com/zx80/anodb  - Python with SQL

https://samuel-vidovich.medium.com/3-cool-python-libraries-that-will-save-you-time-and-effort-27fcdc6762d5

https://joblib.readthedocs.io/ joblib

https://news.ycombinator.com/item?id=35546804 joblib

https://www.reddit.com/r/Python/comments/12tr2sn/pythoneers_here_what_are_some_of_the_best_python/

https://towardsdatascience.com/simulating-physical-systems-with-python-dd5751e80b5c Simulating Physical Systems with Python 

### Logging

https://betterstack.com/community/guides/logging/python/python-logging-best-practices/

https://www.structlog.org/en/stable/index.html struct logging

https://steve.dignam.xyz/2023/04/09/structlog-instead-of-logging/

https://www.youtube.com/watch?v=wiGkV37Kbxk Raymond Hettinger: Numerical Marvels Inside Python

### How to contribute to open source python projects:
https://www.reddit.com/r/Python/comments/12p771v/what_can_i_contribute_to_scipy_or_other_with_my/

#### *argv and **kwargs
Writing *args is a well followed convention, but you can choose a different name - the asterisk is what makes it a variable
argument
```
def takes_any_args (*args ) :
  print (" Type of args : " + str( type ( args ) ) ) # Type of args : <class 'tuple '>
  print (" Value of args : " + str( args ) )
  
```  
The  keyword arguments won’t be captured by the *args idiom. Instead, Python provides a
different syntax - using two asterisks instead of one:
```
def print_kwargs (** kwargs ) :
  for key , value in kwargs . items () :
      print ("{} -> {}". format (key , value ) )  
```
The variable kwargs is a dictionary. (In contrast to args  that is a tuple.)

#### Usage of * and **
https://tproger.ru/translations/asterisks-in-python-what-they-are-and-how-to-use-them/

example of unpacking
```
 numbers = [2, 1, 3, 4, 7]
 more_numbers = [*numbers, 11, 18]
 print(*more_numbers, sep=', ')  # 2, 1, 3, 4, 7, 11, 18
 
 A = [1, 2, 3]
 B = (4, 5, 6)
 C = {7, 8, 9}
 L = [*A, *B, *C]
 
 a, *mid, b = [1, 2, 3, 4, 5, 6]
 print(a, mid, b)
 # 1 [2, 3, 4, 5] 6
 
```

#### Default arg - do not use mutable default args!
https://docs.python-guide.org/writing/gotchas/#mutable-default-arguments
Python’s default arguments are evaluated once when the function is defined, 
not each time the function is called.
```
    def fn(arg=[]):
        arg.append(1)
        print(arg)
        
    fn() # [1]
    fn() # [1, 1]
    fn() # [1, 1, 1]
```
This means that if you use a mutable default argument and mutate it, you will and have mutated that object for all future calls to the function as well.

Do this:
```
def append_to(element, to=None):
    if to is None:
        to = []
    to.append(element)
    return to
```

### Show all methods for the class/function

all methods of list:

name for name in dir(list) if not name.startswith("__")]

['append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']

``` 
all string methods:
[name for name in dir(str) if not name.startswith("__")]
['capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> len(_)
47
```


every object is equipped with a __dict__ attribute:
```
instance = TestClass()
print(instance.__dict__)
print(vars(instance))
```

### getattr() returns the value of the name attribute of the Company instance c:

name = getattr(c, 'name')

 However, you can provide a third argument to getattr(), which will be returned if the attribute is not found, thus avoiding the error:

location = getattr(c, 'location', 'Not available')
print(location)


### reversed()  takes a sequence as an argument and returns an iterator

but .. 
The  list .reverse() method reverses a list in place: it returns None. 

https://realpython.com/python-reverse-list/

```
s = 'Python'
print(list(reversed(s)))

# Output: ['n', 'o', 'h', 't', 'y', 'P']
``` 

Reversing the list: 
```
digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
digits[::-1]   Result: [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
```

#### Stack, queue, priority queue (heapq)  
 https://realpython.com/queue-in-python/ <br>
 https://realpython.com/python-deque/ <br>
https://favtutor.com/blogs/heap-in-python <br>

#### dequeue

```
from collections import deque
# create an empty queue
queue = deque()
# add elements to the queue
queue.append("apple")
queue.append("banana")
queue.append("cherry")
# remove and return the first element from the queue
print(queue.popleft()) # prints "apple"
print(queue.popleft()) # prints "banana"
```
You also can use appendleft() for adding element at left and pop() for removing element from right.

if you try to use the popleft() method on an empty queue, it will raise an IndexError
in the worst case scenario, the time complexity of popleft() operation on a deque object is O(n) because it's implemented as a cyclic buffer, so if we constantly add elements and remove elements from one end, the buffer will be reallocated every time it becomes full and this operation can be costly.

In summary, using collections.deque as a queue in Python has an O(1) time complexity on average for both the enqueue and dequeue operations, making it an efficient data structure for queue operations, but in the worst case the time complexity could be O(n).



#### defautdict()
https://realpython.com/python-defaultdict/
```
from collections import defaultdict
def def_value():
    return "Not Present"
d = defaultdict(def_value)
d["a"] = 1
d["b"] = 2
  
print(d["a"])
print(d["b"])
print(d["c"])    
```
When the list class is passed as the default_factory argument, then a defaultdict is created with the values that are list.
```
from collections import defaultdict
  
  
# Defining a dict
d = defaultdict(list)
  
for i in range(5):
    d[i].append(i)
```
When the int class is passed as the default_factory argument, then a defaultdict is created with default value as zero.

```
d = defaultdict(int)
   
L = [1, 2, 3, 4, 2, 4, 1, 2]
   
# Iterate through the list
# for keeping the count
for i in L:
       
    # The default value is 0
    # so there is no need to 
    # enter the key first
    d[i] += 1
```    

### attr

https://www.attrs.org/en/stable/

#### Named tuples
```
from collections import namedtuple

NamedTupleCard = namedtuple('NamedTupleCard', ['rank', 'suit'])
```

#### Dataclass
```
The @dataclass decorator (introduced in Python 3.7) can automatically generate several special methods for a class,
such as __init__, __repr__, __eq__, __lt__, and so on.
```
https://realpython.com/python-data-classes/

https://earthly.dev/blog/python-data-classes/

https://betterprogramming.pub/9-python-dataclass-best-practices-to-improve-the-development-process-8a68df446580

```
@dataclass
class DataClassCard:
    rank: str
    suit: str
    
queen_of_hearts = DataClassCard('Q', 'Hearts')    
```
Without dataclass the code above will be implemented as:
```
class RegularCard:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
```

@dataclass(slots=True)

@dataclass(slots=True, frozen=True)

### itertools
https://realpython.com/python-itertools/

https://www.kdnuggets.com/2023/08/4-python-itertools-filter-functions-probably-didnt-know.html 

https://www.youtube.com/watch?v=aumxFs2DO5o

#### itertools product()
```
from itertools import product

list_a = [1, 2020, 70]
list_b = [2, 4, 7, 2000]
list_c = [3, 70, 7]


for a, b, c in product(list_a, list_b, list_c):
    if a + b + c == 2077:
        print(a, b, c)
```   
     
 
#### Logging exception

The logging module has a function called exception, which will log your message
along with the full stack trace of the current exception. So you can write code like this:
```
import logging
def get_number () :
   return int('foo ')
try:
   x = get_number ()
except :
    logging . exception ('Caught an error ')
``` 

#### Sorting: sorted() and .sort()

https://tproger.ru/translations/python-sorting/

list.sort(reverse=True/False) - in place, returns None

sorted(any_iterable_object, key=..., reverse=True/False) - returns new sorted object

Example: find median in unordered list:
```
 def median(samples):
      n = len(samples)
      middle_index = n // 2
      sorted_samples = sorted(samples)
      # Odd number of values
      if n % 2:
          return sorted_samples[middle_index]
 
      # Even number of values
      lower, upper = middle_index - 1, middle_index + 1
      return sum(sorted_samples[lower:upper]) / 2

 median([3, 5, 1, 4, 2])
```

Example: Use key=
```
student_tuples = [
        ('john', 'A', 15),
        ('jane', 'B', 12),
        ('dave', 'B', 10),
    ]
sorted(student_tuples, key=lambda student: student[2])   # sort by age

[('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]
```

A key function is a function that takes exactly one argument - an element in the list. 
It returns the derived value used in the comparison.

```
nums = ["12", "7", "30", "14", "3"]
max( nums ) # '7'
max(nums , key= int) # '30'
min( nums ) # '12 '
sorted ( nums ) # ['12 ', '14 ', '3', '30 ', '7']

# And with a key function (cast to int):
min(nums , key= int) # '3'

sorted (nums , key= int)
['3', '7', '12 ', '14 ', '30 ']
```
We can create the custom key function as well
```
def get_gpa ( who) :
 return who[" gpa"]

sorted ( students , key= get_gpa )
```

### operator()
https://realpython.com/python-operator-module/

 Alternatively, the operator module’s
_itemgetter_ creates and returns a key function that looks up a named dictionary field:
```
 from operator import itemgetter
 # Sort by GPA:
 sorted ( students , key= itemgetter ("gpa") )
```
This is how you use itemgetter when the sequence elements are dictionaries. It also works when
the elements are tuples or lists - just pass a number index instead:

  Same data, but as a list of tuples:
```
 student_rows = [
   (" Joe Smith ", " physics ", 3.7) ,
   (" Jane Jones ", " chemistry ", 3.8) ,
   (" Zoe Fox", " literature ", 3.4) ,
 ]

# GPA is the 3rd item in the tuple , i.e. index 2.
# Highest GPA:
 max( student_rows , key= itemgetter (2) )
('Jane Jones ', 'chemistry ', 3.8)
```

_operator_ also provides _attrgetter_, for keying off an attribute of the element, and _methodcaller_
for keying off a method’s return value - useful when the sequence elements are instances of your
own class

Sort dict by value:
```
my_dict = {
    "Plan A": 1,
    "Plan B": 3,
    "Plan C": 2,
}

my_dict = {key: my_dict[key] for key in sorted(my_dict, key=my_dict.get)}

assert list(my_dict.keys()) == ['Plan A', 'Plan C', 'Plan B']
```

Example: sorting using functools
```
from functools import cmp_to_key
xs = ['4', '42', '46', '427', '465']
xs.sort(key=cmp_to_key(lambda a, b: int(b+a)-int(a+b)))
print(''.join(xs)) # 46546442742
```


Find biggest elements in dictionary values:

### Find the highest value in the dictionary

highest_value = max(some_dict.values())

#### Generators, yield

https://www.dabeaz.com/generators/Generators.pdf

https://andrewodendaal.com/mastering-pythons-yield-a-comprehensive-guide-to-advanced-usage/

A function is a generator function if and only if it uses "yield" instead of "return"
This generator object is an iterator, which means you can iterate through it using next() or a for
loop

The performance improvement from the use of generators is the result of the lazy (on demand) generation of values,

Generator will provide performance benefits only if we do not intend to use that set of generated values more than once

```
def gen_nums (N_MAX) :
  n = 0
  while n < N_MAX:
      yield n
      n += 1
      
sum_of_first_n = sum(gen_nums(1000000))      
```
The _yield_ statement simultaneously defines an exit point, and a re-entry point.

For generator objects, each time a new value is requested, 
the flow of control picks up on the line after the yield statement. 

 The __yield from__ statement is used specifically in generator functions, when they yield values directly from another generator object (or, equivalently, by calling another generator function)
 

### Convert Json to CSV

```
import json
if __name__ == '__main__':
    try:
        with open('input.json', 'r') as f:
            data = json.loads(f.read())

        output = ','.join([*data[0]])  ### what is it?
        for obj in data:
            output += f'\n{obj["Name"]},{obj["age"]},{obj["birthyear"]}'

        with open('output.csv', 'w') as f:
            f.write(output)
    except Exception as ex:
        print(f'Error: {str(ex)}')
```
#### Generate last day of month

```
from datetime import datetime, timedelta

def last_day_of_month(year):
 last_days=[]   
 for i in range(2,13):
    dt = datetime(year, i, 1)
    previous_month = dt - timedelta(days=1)
    print(i, previous_month.date())
    last_days.append(str(previous_month.date()))
    
 last_days.append(str(datetime(year, 12, 31).date()))
 return last_days               
                  
result=last_day_of_month(2022)
print(result)
``` 

#### List and dictionary comprehensions

The structure is
[ EXPR for VAR in SEQUENCE if CONDITION ]

```
squares = [ n*n for n in range (6) ]
print ( squares )
[0 , 1 , 4 , 9 , 16 , 25]

blocks = { n: "x" * n for n in range (5) }
print ( blocks )
{0: '', 1: 'x', 2: 'xx ', 3: 'xxx ', 4: 'xxxx '}
```
Any list comprehension you can write, you can use to create an equivalent generator
object, just by swapping "(" and ")" for "[" and "]".
```
#  This
many_squares = ( n*n for n in range ( NUM_SQUARES ) )
# ... is EXACTLY EQUIVALENT to this :
def gen_many_squares ( limit ) :
  for n in range ( limit ) :
     yield n * n
many_squares = gen_many_squares ( NUM_SQUARES )


```
#### map 
```
numbers = ["2", "9", "5", "1", "6"]
numbers = list(map(int, numbers)) # cast to int
# result: [2, 9, 5, 1, 6]

numbers = [1 , 2 , 3]
def double (n) :
  return 2 * n
  
mapped = map( double , numbers )
for num in mapped : print ( num)

names = ['yAnG', 'MASk', 'thoMas', 'LISA']
names = map(str.capitalize, names)
print(list(names))
# ['Yang', 'Mask', 'Thomas', 'Lisa']
```

### filter()
https://realpython.com/python-filter-function/
```
integers = [20, 31, 52, 6, 17, 8, 42, 55]
even_numbers = list(filter(lambda number: number % 2 == 0, integers))

def is_even (n) :
  return n % 2 == 0
  
filtered = filter ( is_even , numbers )
for num in filtered : print (num)
```
### zip() allows to iterate over multiple lists in parallel
https://realpython.com/python-zip-function/


It’s possible that the iterables you pass in as arguments aren’t the same length.
In these cases, the number of elements that zip() puts out will be equal to the length of the shortest iterable.
The remaining elements in any longer iterables will be totally ignored by zip()
```
integers = [1, 2, 3]
letters = ["a", "b", "c"]
floats = [4.0, 5.0, 6.0]

for i, l, f in zip(integers, letters, floats):
    print(i, l, f)
```
 zip() function creates an iterator that will aggregate elements from two or more iterables.
```
zipped = zip( numbers , big_numbers ) # createszipped  iterator
for pair in zipped : print ( pair )
```

If trailing or unmatched values are important to you, then you can use itertools.zip_longest() instead of zip().
With this function, the missing values will be replaced with whatever you pass to the fillvalue argument (defaults to None). 
The iteration will continue until the longest iterable is exhausted:
```
from itertools import zip_longest
numbers = [1, 2, 3]
letters = ['a', 'b', 'c']
longest = range(5)
zipped = zip_longest(numbers, letters, longest, fillvalue='?')
list(zipped)
[(1, 'a', 0), (2, 'b', 1), (3, 'c', 2), ('?', '?', 3), ('?', '?', 4)]
`` 

#### Recursion limit
```
import sys
sys.getrecursionlimit() ## 1000

sys.setrecursionlimit(5000) 
```



####  Common elements in lists
```
result = list(filter(lambda elem: elem in b, a))
result = [elem for elem in a if elem in b]
result = list(set(a) & set(b))
```
### Elements in list A which are not in list B
```
set_1 = set(['White', 'Black', 'Red'])
set_2 = set(['Red', 'Green'])

print(set_1 - set_2)
```

#### Sort dictionary by value
```
import operator
d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}

result_ascended = dict(sorted(d.items(), key=operator.itemgetter(1)))
result_descended = dict(sorted(d.items(), key=operator.itemgetter(1), reverse=True))

my_dict = {
    "Plan A": 1,
    "Plan B": 3,
    "Plan C": 2,
}

my_dict = {key: my_dict[key] for key in sorted(my_dict, key=my_dict.get)}

assert list(my_dict.keys()) == ['Plan A', 'Plan C', 'Plan B']
```
### find 3 keys with max values
```
my_dict = {'a':500, 'b':5874, 'c': 560,'d':400, 'e':5874, 'f': 20}
result = sorted(my_dict, key=my_dict.get, reverse=True)[:3]


from heapq import nlargest
result = nlargest(3, my_dict, key=my_dict.get)
```
#### check  whether the given list has duplicates:
```
 def all_unique(lst):
    return len(lst) == len(set(lst))
```    

####  check if   strings is e palindrome:
```
def is_palindrome(string):
    return string == string[::-1]

def is_palindrome(string):
    return string == ''.join(reversed(string))
```

####  check if two strings are anagrams:
```
from collections import Counter

def anagram(first, second):
    return Counter(first) == Counter(second)
```

Another approach: build dictionary(char->count) for one string and traverse other string to decrease counter, if some counter < 0 then answer is False


### How many times some char present in string
```
string = 'Python Software Foundation'
string.count('o') 
```




#### check the memory usage of an object
```
import sys 

variable = 30 
print(sys.getsizeof(variable)) # 24
```
#### length of a string in bytes
```
def byte_size(string):
    return(len(string.encode('utf-8')))
```
#### chunk a list into smaller lists of a specified size.
```
def chunk(list, size):
    return [list[i:i+size] for i in range(0,len(list), size)]

```
#### Decapitalize
```
def decapitalize(str):
    return str[:1].lower() + str[1:]
  
decapitalize('FooBar') # 'fooBar'
decapitalize('FooBar') # 'fooBar'
```

#### remove falsy values (False, None, 0 and “”) from a list by using filter().
```
def compact(lst):
    return list(filter(None, lst))
  
  
compact([0, 1, False, 2, '', 3, 'a', 's', 34]) # [ 1, 2, 3, 'a', 's', 34 ]
```

#### transpose a 2D array:
```
array = [['a', 'b'], ['c', 'd'], ['e', 'f']]
transposed = zip(*array)
print(transposed) # [('a', 'c', 'e'), ('b', 'd', 'f')]
```
#### turn a list of strings into a single string with each element from the list separated by commas
```
hobbies = ["basketball", "football", "swimming"]

print("My hobbies are:") # My hobbies are:
print(", ".join(hobbies)) # basketball, football, swimming
```


#### flatten a potentially deep list using recursion.
```
def spread(arg):
    ret = []
    for i in arg:
        if isinstance(i, list):
            ret.extend(i)
        else:
            ret.append(i)
    return ret

def deep_flatten(xs):
    flat_list = []
    [flat_list.extend(deep_flatten(x)) for x in xs] if isinstance(xs, list) else flat_list.append(xs)
    return flat_list


deep_flatten([1, [2], [[3], 4], 5]) # [1,2,3,4,5]
```
 
#### finds the difference between two iterables by keeping only the values that are in the first one.
```
def difference(a, b):
    set_a = set(a)
    set_b = set(b)
    comparison = set_a.difference(set_b)
    return list(comparison)


difference([1,2,3], [1,2,4]) # [3]
 ```
#### Return the difference between two lists after applying a given function to each element of both lists.
```
def difference_by(a, b, fn):
    b = set(map(fn, b))
    return [item for item in a if fn(item) not in b]


from math import floor
difference_by([2.1, 1.2], [2.3, 3.4], floor) # [1.2]
difference_by([{ 'x': 2 }, { 'x': 1 }], [{ 'x': 1 }], lambda v : v['x']) # [ { x: 2 } ]
```
#### Chained function call - You can call multiple functions inside a single line.
```
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

a, b = 4, 5
print((subtract if a > b else add)(a, b)) # 9   
```

#### check whether a list has duplicate values by using the fact that set() contains only unique elements.
```
def has_duplicates(lst):
    return len(lst) != len(set(lst))
    
    
x = [1,2,3,4,5,5]
y = [1,2,3,4,5]
has_duplicates(x) # True
has_duplicates(y) # False
```
####  Merge  dictionaries
```
def merge_two_dicts(a, b):
    c = a.copy()   # make a copy of a 
    c.update(b)    # modify keys and values of a with the ones from b
    return c

In code above in case of keys collision between 2 dictionaries the last update wins

a = { 'x': 1, 'y': 2}
b = { 'y': 3, 'z': 4}
print(merge_two_dicts(a, b)) # {'y': 3, 'x': 1, 'z': 4}
```
In Python 3.5 and above, you can also do it like the following:
```
def merge_dictionaries(a, b)
   return {**a, **b}


a = { 'x': 1, 'y': 2}
b = { 'y': 3, 'z': 4}
print(merge_dictionaries(a, b)) # {'y': 3, 'x': 1, 'z': 4}


result = {}
for d in (dict_a, dict_b, dict_c):
    result.update(d)
    
Merge 3 dictionaries:    
result = {**dict_a, **dict_b, **dict_c}    

Python 3.9 way:

cities = cities_us | cities_uk
cities_us |= cities_uk  # in place
```
#### Convert two lists into a dictionary
```
def to_dictionary(keys, values):
    return dict(zip(keys, values))
    

keys = ["a", "b", "c"]    
values = [2, 3, 4]
print(to_dictionary(keys, values)) # {'a': 2, 'c': 4, 'b': 3}
```
   

#### Calculate the time it takes to execute a particular code.
```
import time

start_time = time.time()

a = 1
b = 2
c = a + b
print(c) #3

end_time = time.time()
total_time = end_time - start_time
print("Time: ", total_time)

# ('Time: ', 1.1205673217773438e-05)
```


#### You can have an else clause as part of a try/except block, which is executed if no exception is thrown.
```
try:
    2*3
except TypeError:
    print("An exception was raised")
else:
    print("Thank God, no exceptions were raised.")

#Thank God, no exceptions were raised.
```

#### The most frequent element that appears in a list.
```
def most_frequent(list):
    return max(set(list), key = list.count)
  

numbers = [1,2,1,2,3,2,1,4,2]
most_frequent(numbers)  
```
#### checks whether a given string is a palindrome.
```
def palindrome(a):
    return a == a[::-1]


palindrome('mom') # True
```
#### Calculator without if-else
```
import operator
action = {
    "+": operator.add,
    "-": operator.sub,
    "/": operator.truediv,
    "*": operator.mul,
    "**": pow
}
print (action['-'](50, 25)) # 25
````
#### randomize the order of the elements in a list. Note that shuffle works in place, and returns None.
```
from random import shuffle

foo = [1, 2, 3, 4]
shuffle(foo) 
print(foo) # [1, 4, 3, 2] , foo = [1, 2, 3, 4]
28. Spread
This method flattens a list similarly like [].concat(…arr) in JavaScript.

def spread(arg):
    ret = []
    for i in arg:
        if isinstance(i, list):
            ret.extend(i)
        else:
            ret.append(i)
    return ret


spread([1,2,3,[4,5,6],[7],8,9]) # [1,2,3,4,5,6,7,8,9]
```

###  Swap values without having to use an additional one
```
a, b = -1, 14
a, b = b, a

print(a) # 14
print(b) # -1
```
### Get default value for missing keys
```
d = {'a': 1, 'b': 2}

print(d.get('c', 3)) # 3
```



### Python functions

```
def f():
    """Print something to standard out."""
    print('something')

print(dir(f))
```
Result:
```

['__call__', '__class__', '__closure__', '__code__', '__defaults__',
'__delattr__', '__dict__', '__doc__', '__format__', '__get__',
 '__getattribute__', '__globals__', '__hash__', '__init__', 
 '__module__', '__name__', '__new__', '__reduce__', '__reduce_ex__', 
 '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 
'func_closure', 'func_code', 'func_defaults', 'func_dict', 'func_doc',
'func_globals', 'func_name']
```
Example: print  function attribute __name__
```
def func_name(function):
    return function.__name__

func_name(f)
```

### Decorators

https://habr.com/ru/articles/750312/

https://www.poeticdev.com/data/python-decorators-when-to-use-and-when-to-avoid-them/

https://soshace.com/understanding-python-decorators-and-how-to-use-them-effectively/

https://medium.com/techtofreedom/9-python-built-in-decorators-that-optimize-your-code-significantly-bc3f661e9017

https://betterprogramming.pub/six-advanced-decorator-patterns-5ffe67552691

https://python.plainenglish.io/five-python-wrappers-that-can-reduce-your-code-by-half-af775feb1d5

If d is decorator it means :
x = d(x)

The d above should be callable: have method __call__
```
def printlog ( func ) :
  def wrapper (* args , ** kwargs ) :
      print (" CALLING : " + func . __name__ )
      return func (* args , ** kwargs )
  return wrapper

@printlog
 def foo(x) :
    print (x + 2)

#--------------------------------
from time import ctime   
def logged(_func):
    def _wrapped():
        print('Function %r called at: %s' % (
            _func.__name__, ctime()))
        return _func()
    return _wrapped
    
@logged
def foo():
    print('foo() called')

#  printing the inputs and outputs of each function
#--------------------------------------------------
def debug(func):
    def wrapper(*args, **kwargs):
        # print the fucntion name and arguments
        print(f"Calling {func.__name__} with args: {args} kwargs: {kwargs}")
        # call the function
        result = func(*args, **kwargs)
        # print the results
        print(f"{func.__name__} returned: {result}")
        return result
    return wrapper

#---------------------------------    
    
def running_average ( func ) :
  data = {" total " : 0 , " count " : 0}
  def wrapper (* args , ** kwargs ) :
      val = func (* args , ** kwargs )
      data [" total "] += val
      data [" count "] += 1
      print (" Average of {} so far: {:.01 f}". format (func . __name__ , data [" total "] / data [" count "]) )
  return func (* args , ** kwargs )
  
return wrapper    
    
```
### Retry decorator
```
import time
from functools import wraps

def retry(max_tries=3, delay_seconds=1):
    def decorator_retry(func):
        @wraps(func)
        def wrapper_retry(*args, **kwargs):
            tries = 0
            while tries < max_tries:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    tries += 1
                    if tries == max_tries:
                        raise e
                    time.sleep(delay_seconds)
        return wrapper_retry
    return decorator_retry
    

@retry(max_tries=5, delay_seconds=2)
def call_dummy_api():
    response = requests.get("https://jsonplaceholder.typicode.com/todos/1")
    return response
```
### Timing decorator
```
import time

def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Function {func.__name__} took {end_time - start_time} seconds to run.")
        return result
    return wrapper
    
@timing_decorator
def my_function():
    # some code here
    time.sleep(1)  # simulate some time-consuming operation
    return    
```
Now, whenever the code is executed, you’d see an output similar to this:
```
INFO:root:Executing extract_data
INFO:root:Finished executing extract_data
INFO:root:Executing transform_data
INFO:root:Finished executing transform_data
INFO:root:Executing load_data
INFO:root:Finished executing load_data
```
### Combining decorators
```
@log_execution
@timing_decorator
def my_function(x, y):
    time.sleep(1)
    return x + y
```    

### Loggging decorator
https://towardsdatascience.com/python-decorators-for-data-science-6913f717669a
```
import logging
import functools

logging.basicConfig(level=logging.INFO)

def log_execution(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        logging.info(f"Executing {func.__name__}")
        result = func(*args, **kwargs)
        logging.info(f"Finished executing {func.__name__}")
        return result
    return wrapper

@log_execution
def extract_data(source):
    # extract data from source
    data = ...

    return data

@log_execution
def transform_data(data):
    # transform data
    transformed_data = ...

    return transformed_data

@log_execution
def load_data(data, target):
    # load data into target
    ...

def main():
    # extract data
    data = extract_data(source)

    # transform data
    transformed_data = transform_data(data)

    # load data
    load_data(transformed_data, target)
```

### Enumeration
https://florian-dahlitz.de/articles/why-you-should-use-more-enums-in-python

```
from dataclasses import dataclass
from enum import Enum, unique

@unique
class CarBrand(Enum):
    VOLVO = "volvo"
    BMW = "bmw"
    VW = "volkswagen"


@dataclass
class Car:
    brand: CarBrand


volvo = Car(brand="volvo")
```

### Working with binary files: BytesIO 

https://github.com/lingeringwillx/StructIO

### Context manager
implements __enter__() and __exit__()

```
class timer(object):
    def __enter__(self):
        self.t = time.clock()
        return self

    def __exit__(self, type, value, traceback):
        self.e = time.clock()

    def __float__(self):
        return float(self.e - self.t)

# Use timer:
with timer() as t1:
    …
    foo(...)
    …
print(t1)
```

Decorator @contextmanager returns object with automatically created  __enter__() и __exit__()
```
# scrapy\scrapy\utils\misc.py
@contextmanager
def set_environ(**kwargs):
    """Temporarily set environment 
       variables inside the context … """

    original_env = {k: os.environ.get(k) for k in kwargs}
    os.environ.update(kwargs)
    try:
        yield
    finally:
        for k, v in original_env.items():
            if v is None:
                del os.environ[k]
            else:
                os.environ[k] = v

# Usage
…
with set_environ(SCRAPY_CHECK='true'):
    for spidername in args or spider_loader.list():
        spidercls = spider_loader.load(spidername)
…
```

### Numpy

https://github.com/rougier/numpy-100

https://github.com/ajcr/100-pandas-puzzles

### Savitzy-Golay (Savgol) filter:
from scipy.signal import savgol_filter
```
For any given datapoint (datapoint k for example), a window/subset of the data is selected around the datapoint. 
A polynomial is then fit through this window of data and the corresponding filtered output datapoint is computed by evaluating the best-fit polynomial at time t[k] 
``` 
https://medium.com/@nhemenway2013/my-favorite-way-to-smooth-noisy-data-with-python-bd28abe4b7d0 Smoothing noisy data

### Performance
Slow:
```
list_of_numbers = list(range(10000))
%%timeit
result = 0
for i in list_of_numbers:
    result += i
```    
Faster
```    
 %timeit sum(list_of_numbers)   
```
Very slow:
```
import numpy as np
%timeit np.sum(list_of_numbers)
```
However, if you can somehow obtain your data in the form of NumPy arrays from the start, 
or if you perform many operations that might compensate for the conversion time, 
the gain in performance can be considerable:
```
ndarray_of_numbers = np.array(list_of_numbers)
%timeit np.sum(ndarray_of_numbers)
```
