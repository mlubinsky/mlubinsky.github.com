Book which I bought:
https://powerfulpython.com/ Vantive99!

Good book to read: 
cosmic_python https://www.cosmicpython.com/book/preface.html

https://habr.com/ru/articles/782266/   many good interview questions

python -m py_compile yourfile.py   # chech what code is valid

Serialization /desiarizatiom - very good article
https://realpython.com/python-serialize-data/

https://habr.com/ru/companies/tensor/articles/790282/

python CLI:
https://medium.com/@martin.heinz/python-cli-tricks-that-dont-require-any-code-whatsoever-e7bdb9409aeb

Generate dates in range
```
import datetime
def generate_dates_in_range(start_date, end_date, range="DAY"):
  start = datetime.datetime.strptime(start_date, "%Y-%m-%d")
  all_dates=[start_date] 
  str_next=start_date

  if range == "DAY": 
        interval=1
  elif range =="WEEK": 
        interval=7
  else:
        print("Unknown range ", range)
        return None
    
  while str_next < end_date:
    next = start + datetime.timedelta(days=interval)
    str_next=str(next)[0:10]
    all_dates.append(str_next)
    start=next
    
  return all_dates
```

### env var

```
import os
if 'HOME' in os.environ:
    v = os.environ.get('HOME')
```



https://github.com/AbdulMalikDev/PythonCheatSheet

https://www.reddit.com/r/Python/comments/wyl1lp/which_not_so_well_known_python_packages_do_you/

https://www.reddit.com/r/Python/comments/x3z0lp/what_packages_replaced_standard_library_modules/

https://medium.datadriveninvestor.com/mastering-advanced-python-40-pro-level-snippets-for-2024-85f5b9359103

https://realpython.com/queue-in-python/

https://realpython.com/sort-python-dictionary/

https://www.jjinux.com/2022/08/python-my-favorite-python-tricks-for.html

https://mathspp.com/blog/pydonts/dunder-methods   dunder metods (with double undescore)   __aa__

https://mathspp.com/blog/how-to-create-a-python-package-in-2022 

https://awesome-python.com/

https://python-patterns.guide/

https://practicalpython.yasoob.me/toc.html  free Book

https://inventwithpython.com/bigbookpython/ free Book

### any() all() and generators

https://martinheinz.dev/blog/80

https://habr.com/ru/company/wunderfund/blog/681426/

https://www.python-unleashed.com/blog

https://cjolowicz.github.io/tags/python/

https://realpython.com/python-hash-table/ Build hash table in Python

https://medium.com/@siddharth.sahu/must-know-python-concepts-for-experienced-developers-4554ceea3d95

https://www.amazon.com/dp/B09MV4X8TV Python Architecture patterns

https://www.wilbertom.com/tutorial/use-signals-to-safely-stop-a-process/

https://lukasz.langa.pl/f15a8851-af26-4e94-a4b1-c146c57c9d20/.  datasette with plot

https://instructobit.com/tutorial/116/Remotely-running-commands-or-scripts-with-python . SSH Paramico

https://stackoverflow.com/questions/68584868/python3-datetime-datetime2021-05-09-does-not-support-leading-0-but-it-works

https://www.reddit.com/r/Python/comments/r6aqji/how_do_you_deploy_python_applications/

https://blog.guilatrova.dev/

https://pypi.org/project/parquet-tools/

https://antonz.org/compact-objects/

### Build-ins  
https://www.pythonmorsels.com/built-in-functions-in-python/.  

https://sadh.life/post/builtins/

### Operator itemgetter how to sort
https://stackoverflow.com/questions/18595686/how-do-operator-itemgetter-and-sort-work

https://docs.python.org/3/library/operator.html#operator.itemgetter

https://wiki.python.org/moin/HowTo/Sorting/#Key_Functions


### Collection classes
https://codesolid.com/useful-collection-classes-in-python-you-may-not-know/ 

https://bas.codes/posts/python-dict-slots Understanding Attributes, Dicts and Slots in Python

https://betterprogramming.pub/4-anti-patterns-in-python-a6d5023c8473

https://github.com/scottrogowski/code2flow


Use
@dataclasses (especially with frozen=True) 

```
a_items = [1,2,3]
b_items = [4,5,6]

for a in a_items:
    for b in b_items:
        print(f'{a} x {b} = {a*b}')

print()
#  Better way
from itertools import product
for a,b in product(a_items, b_items):
    print(f'{a} x {b} = {a*b}')
```
### Important: 

Pointers with python: https://yurichev.com/news/20211223_Py_ptrs/


 python -m py_compile my.py   # Check file syntax
 

 
python -m json.tool my_json.json   # json beautifier - warning: will sort the keys ard remove .0 !


 ### JSON processing tools
 
 https://bcmullins.github.io/parsing-json-python/. extract element from json
 
 https://pythonspeed.com/articles/faster-python-json-parsing/ 
 
 https://github.com/dcmoura/spyql  very fast
 
 process big json files
 https://pythonspeed.com/articles/json-memory-streaming/
 
 
 Preserve the json key orders 
 ```
 import json
import collections

def pp_json(json_thing, sort=False, indents=4):
    if type(json_thing) is str:
      #  print(json.dumps(json.loads(json_thing), sort_keys=sort, indent=indents))
        print(json.dumps(json.loads(json_thing, object_pairs_hook=collections.OrderedDict), sort_keys=sort, indent=indents))
    else:
        print(json.dumps(json_thing, sort_keys=sort, indent=indents))
    return None

fname="ascii_without_last_char.json"
# fname='test.txt'
with open(fname, 'r') as handle:
  json_string_or_dict = handle.read()
  #json_string_or_dict = json.load(handle)

pp_json(json_string_or_dict, False, 2)

```
 
Another useful python json processing script: https://replit.com/@gabrielsroka/Bash#pj.py
```
""" (space/comma)-delimited list of dotted values, eg
echo "$r" | python pj.py 'id profile.login profile.email'
or
echo "$r" | python pj.py 'id,profile.login,profile.email'

where $r is a JSON object or an array of objects
"""

import json
import sys

def main():
    for d in [', ', ',', ' ']: # these are in order
        keys = sys.argv[1].split(d)
        if len(keys) > 1:
            break

    j = json.load(sys.stdin)
    os = j if (type(j) is list) else [j]
    for o in os:
        print(d.join(dot(o, key) for key in keys))

def dot(v, key):
    """dot({a:{b:'c'}}, 'a.b') -> 'c'."""
    for k in key.split('.'):
        v = v.get(k)
        if not v:
            return ''
    return v

main()
```
 
 
 
 https://sadh.life/post/builtins/
 

 
 ####  Python Libraries
``` 
from stdlib_list import stdlib_list
 
# Change this 3.7 to version of Python
libraries = stdlib_list("3.7")
 
# Printing libraries
print('[%s]' % '\n'.join(map(str, libraries))
``` 
 
 #### Collection
 
  Once the deque is full, every time you add a new element at the end(using append, 
  like for lists) the first element will be removed.
  a deque is also more efficient than lists for adding and removing values at both ends. 
  There are the methods append, appendleft, pop, popleftthat all take O(1). 
  On the other hand, accessing elements in the middle is more expensive, approximately O(n).
``` 
 from collections import deque
 a = deque(maxlen=10)
``` 
#### Counter
```
from collections import Counter
c = (“aaabbccdaaa”)
print(c)
#Output: Counter({'a': 6, 'b': 2, 'c': 2, 'd': 1})
```
 
```
from collections import Counter
text = 'and another long text but interesting and fun'

c = Counter()
for word in text.split(" "):
  c[word] += 1
print(c)
```
Actually we can do even better using the Counter’s constructor:
```
from collections import Counter
text = 'and another long text but interesting and fun'
c = Counter(text.split(" "))
print(c)
```


#### Counter most_common()

The most_common method: Print the 3 most common words, along with their count
```
print(c.most_common(3))
 
there is a very useful method in Counter called most_common().
 to print the first two letters that are used most often, the most_common() method can help:

from collections import Counter
chars = Counter(title)
print(chars.most_common(2))
# [(' ', 9), ('a', 6)]
 
to count how many times each letter is used in a piece of text

from collections import Counter

title = "3 Variants of Python Dictionaries That Make Your Coding Easier"
chars = Counter(title)
print(chars)
# Counter({' ': 9, 'a': 6, 'i': 6, 'o': 5, 'r': 4, 'n': 4, 't': 4, 's': 3, 'e': 3, 'h': 2, '3': 1, 'V': 1, 'f': 1, 'P': 1, 'y': 1, 'D': 1, 'c': 1, 'T': 1, 'M': 1, 'k': 1, 'Y': 1, 'u': 1, 'C': 1, 'd': 1, 'g': 1, 'E': 1})
```

#### Square all numbers
```
numbers = [1,2,3,4,5,6,7]
output = [num**2 for num in numbers]
```
#### Flatten a list of lists
```
input_list = [[1], [2,3,4], [5,6], [7,8], [9]]
output_list = [item for sublist in input_list for item in sublist]
print(output_list)

Output:
[1, 2, 3, 4, 5, 6, 7, 8, 9]
```

#### DefaultDict
``` 
from collections import defaultdict

dict_of_list = defaultdict(list)
dict_of_list[key].append(element)

toAdd =[("key1", 3), ("key2", 5), ("key3", 6), ("key2", 7)]
d = defaultdict(list)
for key, val in toAdd:
  d[key].append(val)
  
  
city = defaultdict(str)
city['UK'] = 'London'
print(city['Italy'] == '')
True  
```


 ```
 last element of array:
  s[-1]
  
 reverse string
 s[::-1]
 
 l='abcdaa'
 set(l)
 set(['a', 'c', 'b', 'd'])
 
sorted(l)
['a', 'a', 'a', 'b', 'c', 'd']
 
 l=['1','2','3']
 ' '.join(l)
'1 2 3'

first = [0,1,2]
second = [*a,3] # first is unchanged, second = [0,1,2,3]


list to dictionary

number = ['eins','zwei','drei',1,2,3]
print(dict(zip(number[:3], number[3:])))  

number = ['eins',1,'zwei',2,'drei',3]
print(dict(zip(number[0::2], number[1::2]))) 

The list.sort() method is only defined for lists. In contrast, the sorted() function accepts any iterable.

Note that both list.sort() and sorted() have a key parameter t
```
### Merging 2 dictionaries
``` 
dict1 = {'a':2 , 'b': 20}
dict2 = {'c':15 , 'a': 40}
merged_dict = {**dict1, **dict2}
print(merged_dict)
{'a': 40, 'b': 20, 'c': 15}
 

```
### dot product:
```
 def dotProduct(listA,listB): 
    return sum( [x*y] for x,y in zip(listA, listB)]
    
 if vectors are sparse there is optimized solution:
 
    def dotProduct(vec1, vec2) :
        sparse_nums= {i: n for i, n in enumerate(nums) if n != 0}
        result = 0
        for i, n in sparce_nums.items():
            result += n * vec2.nums.get(i, 0)
        return result
```	
### Anagram 	
```
    from collections import Counter

    def anagram(first, second):
         return Counter(first) == Counter(second)
	 
    def anagram(first, second):
         return first == second[::-1]	 
```
### size in bytes
```
    import sys 
    variable = 30 
    print(sys.getsizeof(variable))
```    
### check whether two lists contain the same elements or not,
```
   def compare(l1, l2):
    if len(l1) != len(l2):
        return False
    else: 
         return l1.sort() == l2.sort()
```    
   
###  splits the list into smaller lists of the specified size:
```
   def chunk(list, size):
    return [list[i:i+size] for i in range(0,len(list), size)]
    
   lstA = [1,2,3,4,5,6,7,8,9,10]
   lstSize = 3
   chunk(lstA, lstSize)
```   
### flatten the nested arrays:
```
   def flatten(items):
    for item in items:
        if isinstance(item, list):
            yield from flatten(item)
        else:
            yield item

items = [1, [2], [[3], 4], 5]
assert list(flatten(items)) == [1, 2, 3, 4, 5]
```   
   # Removal of False Values
```
   def compact(lst):
      return list(filter(bool, lst))
    
   compact([0, 1, False, 2, '',' ', 3, 'a', 's', 34])
 ```  
 ###  Convert a list of Strings to a single String, where each item from the list is separated by commas:
 ```  
   hobbies = ["singing", "soccer", "swimming"]
   print("My hobbies are:") # My hobbies are:
   print(", ".join(hobbies)) # singing, soccer, swimming
```	
###  Return  the difference between the two lists after applying this function to each element of both lists:
```
   def difference_by(a, b, fn):
      b = set(map(fn, b))
      return [item for item in a if fn(item) not in b]
    
  from math import floor
  print(difference_by([2.1, 1.2], [2.3, 3.4],floor)) # [1.2]
  print(difference_by([{ 'x': 2 }, { 'x': 1 }], [{ 'x': 1 }], lambda v : v['x'])) # [ { x: 2 } ]

  
  def has_duplicates(lst):
    return len(lst) != len(set(lst))
	
```  	
 
 #### String fuctions
 ```
 s.find(pattern).  If a substring cannot be found, a -1 will be returned.
 
 s.rfind(pattern)
 
 s.index() function will raise an exception (ValueError) if pattren not found


find() function can only be used on strings. 
But the index() function can also be used on lists or tuples.
```

### Dictionary

Transpose of a matrix
```
mat = [[1,2,3], [4,5,6], [7,8,9]]
transpose_matrix = [list(item) for item in zip(*mat)]
print(transpose_matrix)
```

Swap Keys and Values in a dictionary

```
dict = {'Name': 'Joy', 'Age': 25, 'Language':'Python'}
result = {v:k for k, v in dict.items()}
print(result)


 city = {'UK':'London','Japan':'Tokyo'}
 print(city['Italy'])
  KeyError: 'Italy'
  
One solution to avoid the above issue is using the get() function to require a value by a key:
city = {'UK':'London','Japan':'Tokyo'}
print(city.get('Italy'))  get() function can return a None instead of raising an exception when a key doesn’t exist.
  None
  


to combine two dictionaries:

def merge_dictionaries(a, b):
    return {**a,**b}
    
a = { 'x': 1, 'y': 2}
b = { 'y': 3, 'z': 4}
print(merge_dictionaries(a, b)) # {'y': 3, 'x': 1, 'z': 4}


Convert Two Lists to a Dictionary


def to_dictionary(keys, values):
    return dict(zip(keys, values))
    
keys = ["a", "b", "c"]    
values = [2, 3, 4]
print(to_dictionary(keys, values)) # {'a': 2, 'c': 4, 'b': 3}

In python < 3.7 to preserve inser order:

from collections import OrderedDict
nums = OrderedDict()

if you are using Python 3.7+, the insertion-order preservation 
applies to the normal dictionaries as well







Regexep to find leading 0 in month, just after year:
```
grep -E 'datetime\([[:space:]]*2\d{3}[[:space:]]*,[[:space:]]*0' datetime.txt
```

Regexep to find leading 0 in day, just after month:
```
grep -E 'datetime\([[:space:]]*2\d{3}[[:space:]]*,[[:space:]]*\d+,[[:space:]]*0' datetime.txt
```

### Data structures 
https://betterprogramming.pub/stop-using-python-lists-everywhere-consider-using-deques-instead-74d37441be4e

https://mymasterdesigner.com/2021/07/06/data-structures-with-python-big-guide/

https://anothertechs.com/programming/python/python-data-structure-cheat-sheet-2021/

https://habr.com/ru/company/otus/blog/573164/ functools

https://lwn.net/SubscriberLink/861910/67bbe2390d2e0c93/ API, slots, etc

### Dataclasses
https://habr.com/ru/company/otus/blog/650257/

https://death.andgravity.com/namedtuples named tuples vs dataclasses

<https://florimond.dev/blog/articles/2018/10/reconciling-dataclasses-and-properties-in-python/> DataClasses

https://habr.com/ru/company/numdes/blog/581374/. make single exe from Python (Nuitka, etc)

### Pipeline using generators and yield

https://medium.com/programming-for-beginners/how-to-use-python-generators-to-efficiently-process-large-data-sets-38e18bd8ae29

https://betterprogramming.pub/3-data-processing-pipelines-you-can-build-with-python-generators-dc0d2019b177

https://towardsdatascience.com/python-pandas-data-pipelines-515bcc678570

### Download from youtube
```
# pip install pytube
import pytube
link = input('Enter Youtube Video URL')
yt = pytube.Youtube(link)
yt.streams.first().download()
print('downloaded', link)
```

```
Now, Python is usually considered to be an interpreted language. 
When you run a Python code, the Python interpreter reads the file line-by-line and runs it.

But behind-the-scenes, the source code is compiled into bytecode. 
These are similar to CPU instructions, but instead of being run by the actual CPU, 
these are executed by a software called a Virtual Machine (VM), 
which acts as a pseudo-microprocessor that runs the bytecodes. 
The advantage is that you can run Python on any platform as long as the VM is installed.

When you run a Python code, the interpreter implicitly compiles the code into bytecode and interprets it with the VM. 
The reason Python is regarded to be an interpreted language is because the compilation step is implicit. 
You don’t have to invoke a compiler manually.

When you import a module into your code, Python compiles those modules into bytecode for caching purposes. 
These are stored in a directory named __pycache__ in the current directory, which contains compiled .pyc files.
```

https://earthly.dev/blog/python-makefile/

https://mitelman.engineering/blog/python-best-practice/automating-python-best-practices-for-a-new-project/

https://habr.com/ru/company/yandex_praktikum/blog/553900/ . Best python books

https://github.com/fredrik-corneliusson/click-web

### Exceptions  
<https://medium.com/analytics-vidhya/6-exceptionally-common-pitfalls-of-python-exception-handling-44871d6afbc7> Error handling

https://blog.guilatrova.dev/handling-exceptions-in-python-like-a-pro/



https://habr.com/ru/post/560072/ interesting features

https://habr.com/ru/post/566920/  Algebraic data types in Python



https://habr.com/ru/post/559560/ . hex arhitecture in python

https://luminousmen.com/post/python-interview-questions-senior


https://awesome-python.com/


https://habr.com/ru/company/skillfactory/blog/528232/  57 отборных репозиториев для всех разработчиков Python

 
https://www.youtube.com/watch?v=oNalXg67XEE.  Observer pattern

https://levelup.gitconnected.com/python-tricks-i-can-not-live-without-87ae6aff3af8 useful tips

https://proproprogs.ru/ai



https://news.ycombinator.com/item?id=24565499. python internals


https://gto76.github.io/python-cheatsheet/  Cheetsheet

### f-strings:
<https://miguendes.me/amp/73-examples-to-help-you-master-pythons-f-strings>

https://www.pythonmorsels.com/string-formatting/

https://martinheinz.dev/blog/70

<https://habr.com/ru/post/462179/> f-strings (Python > 3.6)



### get IP address

IP = requests.get('https://api.ipify.org').text


### Import

https://mathspp.com/blog/how-to-create-a-python-package-in-2022

use importlib

https://habr.com/ru/post/678488/ Как универсально организовать импорты в проекте, независимо от того, где находятся модули?

https://pythonhowtoprogram.com/better-organization-of-your-projects-with-python-imports/ 

https://antonz.org/python-packaging/

https://tenthousandmeters.com/blog/python-behind-the-scenes-11-how-the-python-import-system-works/
```
import math
math.pi

from math import pi
pi

from math import pi, sqrt


 from math import sqrt
 from cmath import sqrt as csqrt 

import math as m
```

## Date arithmetic:

```
from datetime import datetime, timedelta
start_date='2020-05-12'
n=5
plus_n_date = (datetime.strptime(start_date, '%Y-%m-%d') + timedelta(days=n)).strftime('%Y-%m-%d')
```

https://github.com/pytransitions/transitions . finite state machine in Python

### SQLite

SQLite connection <http://blog.rtwilson.com/a-python-sqlite3-context-manager-gotcha/>

<https://habr.com/ru/company/ruvds/blog/514538/> SQLite


### SymPy SimPy

http://www.doc.mmu.ac.uk/STAFF/S.Lynch/Python_for_A_Level_Mathematics_and_Beyond.html

https://towardsdatascience.com/simulate-real-life-events-in-python-using-simpy-e6d9152a102f SimPy

### Python instead bash

https://davidoha.medium.com/avoiding-bash-frustration-use-python-for-shell-scripts-44bba8ba1e9e

### FFT in SciPy
https://realpython.com/python-scipy-fft/

## Docker vs virtualenv

https://sourcery.ai/blog/python-docker/

https://www.codementor.io/@adrianogalello/quit-virtualenv-and-use-docker-1at0e0olud

https://pythonspeed.com/articles/activate-virtualenv-dockerfile/

https://www.thoughtworks.com/insights/blog/reproducible-work-environments-using-docker

https://medium.com/@stephen.odaibo/docker-containers-python-virtual-environments-virtual-machines-d00aa9b8475

 


<http://www.iakovlev.org/index.html?p=5791&m=1&l1=2> All Python in single page

<https://www.pythonforbeginners.com/basics/most-common-python-interview-questions-for-2020> 

<https://github.com/dabeaz-course/practical-python/blob/main/Notes/Contents.md>

<https://habr.com/ru/post/510294/> better python

<https://pythonspeed.com/articles/python-object-memory/>.  use slots !!! and other tips



<https://news.ycombinator.com/item?id=23386537> debugging



<https://realpython.com/python-mmap/> memory map files

<https://github.com/giannitedesco/minotaur>  inotify wrapper



## Context managers ( beyond with )
 
<https://medium.com/better-programming/context-managers-in-python-go-beyond-with-open-as-file-85a27e392114>

## ML papers with code
https://paperswithcode.com/

<https://paperswithcode.com/paper/causalml-python-package-for-causal-machine> CasualML

## Decorator

https://bytepawn.com/python-decorators-for-data-scientists.html

https://news.ycombinator.com/item?id=31476521

https://towardsdatascience.com/10-fabulous-python-decorators-ab674a732871

https://medium.com/techtofreedom/7-levels-of-using-decorators-in-python-370473fcbe76

https://habr.com/ru/post/524052/

https://habr.com/ru/post/648967/


## Static Method in Python: @staticmethod @classmethod @property
https://djangocentral.com/classmethod-and-staticmethod-explained/
https://djangocentral.com/property-decorator-explained/

```
A @staticmethod is a method that knows nothing about the class or instance it was called on unless explicitly given.
It just gets the arguments that were passed, no implicit first argument and It’s definition is immutable via inheritance.

In simpler words a @staticmethod  is nothing more than a regular function defined inside a class that doesn’t have access to the instance therefore
 It is callable without instantiating the class.

Syntax:

class ClassName:
    @staticmethod
    def method_name(arg1, arg2, ...): ...

We use the @staticmethod decorator for defining a static method in Python,
here you can observe that the static method is not taking self as an argument for the method.

```

## When not to use list

<https://habr.com/ru/company/otus/blog/510350/>.  set() tuple() queue() ... dict()

https://python.plainenglish.io/queue-data-strucure-theory-and-python-implementation-e58f3582c390

Lazy eval:
<https://medium.com/better-programming/how-to-create-lazy-attributes-to-improve-performance-in-python-b369fd72e1b6>

## yield

https://medium.com/better-programming/python-7-advanced-features-that-you-may-not-know-about-generators-574a65fd6e45

<https://medium.com/livecodestream/how-to-use-generator-and-yield-in-python-c481cea097d7>

## Config and env variables
<https://whalesalad.com/blog/doing-python-configuration-right>

<https://tech.preferred.jp/en/blog/working-with-configuration-in-python/>

Working with env variables
https://www.codementor.io/@doppler/using-environment-variables-in-python-for-app-configuration-and-secrets-1irvc9qbat


<https://news.ycombinator.com/item?id=22964910>. How to config the Python app

<https://habr.com/ru/post/485236/> . Конфигурационные файлы в Python

<https://news.ycombinator.com/item?id=22969375>


<https://habr.com/ru/company/yandex/blog/498856/> lectures

<https://github.com/gto76/python-cheatsheet>

<http://michal.karzynski.pl/blog/2019/07/15/top-20-talks-from-europython-2019/>

<https://towardsdatascience.com/tour-of-python-itertools-2af84db18a5e> itertools

<https://github.com/kellyjonbrazil/jello>  JSON util

<https://www.attrs.org/en/stable/>




## Books

Python Distilled
Fluent Python

https://effectivepython.com/ 2nd edition

https://github.com/cosmicpython/book Good Free Book

Book: Python distilled by David Beazley 
https://www.amazon.com/Python-Essential-Reference-Developers-Library/dp/0134173279/   

https://www.cosmicpython.com/
https://github.com/pamoroso/free-python-books

<https://www.amazon.com/Modern-Python-Cookbook-flawless-expressive/dp/180020745X>

<https://pythonbooks.org/>

<https://leanpub.com/clean-architectures-in-python>

https://www.amazon.com/dp/B085KB31X3  Architecture Patterns with Python

https://www.amazon.com/Advanced-Python-Development-Real-World-Applications-ebook/dp/B08DMKYTNM/

https://www.amazon.com/Practices-Python-Pro-Dane-Hillard/dp/1617296082

https://www.amazon.com/Serious-Python-Black-Belt-Deployment-Scalability-ebook/dp/B074S4G1L5

<https://github.com/pamoroso/free-python-books>

<https://docs.quantifiedcode.com/python-anti-patterns/index.html> antiputterns

<https://knowledgeisle.com/wp-content/uploads/2019/10/Serious-Python_-2019.pdf> Serious Python

<https://effectivepython.com/2019/10/22/memoryview-bytearray-zero-copy-interactions>  Effective Python 2nd ed

<http://shop.oreilly.com/product/0636920268505.do> High Performance Python

<https://www.amazon.com/Pro-Python-Features-Professional-Development-ebook/dp/B07PQBH4LL/>

<https://www.packtpub.com/programming/python-parallel-programming-cookbook> 

<https://www.amazon.com/gp/product/1617295981>   Classic Computer Science Problems in Python

<https://habr.com/ru/company/piter/blog/471520/> Книга «Классические задачи Computer Science на языке Python»

<https://github.com/zedr/clean-code-python/blob/master/README.md> Clean code

### Call Shell Commands with Python

<https://janakiev.com/blog/python-shell-commands/>

## Parsing
<https://tomassetti.me/parsing-in-python/> Parsing in Python

<https://github.com/thebjorn/pydeps> show dependency using graphviz


## Unicode, chardetect

<https://blog.emacsos.com/unicode-in-python.html>

<https://docs.python.org/2/howto/unicode.html>

https://blog.fredrb.com/2022/07/31/character-encoding-utf8/

<https://stackoverflow.com/questions/18034272/python-str-vs-unicode-types/18034409>

<https://medium.com/better-programming/strings-unicode-and-bytes-in-python-3-everything-you-always-wanted-to-know-27dc02ff2686>

chardetect header.txt
header.txt: SHIFT_JIS with confidence 0.99

<https://pypi.org/project/chardet/>

iconv -f SHIFT-JIS -t UTF-8 header.txt > header-UTF-8.txt

<https://gist.github.com/clarkb7/3e7e43ab85717e81925656f70f5bae8d>

```
print ( ''.join([x.encode('utf-8') for x in map(unichr, range(0x0107, 0x0187))]) )
```

## Binding with C++

<https://iscinumpy.gitlab.io/post/tools-to-bind-to-python/>

https://pybind11.readthedocs.io/en/stable/ C++ from python

https://habr.com/ru/company/oleg-bunin/blog/518464/

https://pythonextensionpatterns.readthedocs.io/en/latest/index.html

<https://habr.com/ru/post/471618/> C++ fropm python

<https://habr.com/ru/company/otus/blog/490244/> .  ctypes

## Creating Python Package

<https://realpython.com/courses/python-modules-packages/>

<https://pypi-package-example.readthedocs.io/en/latest/>

<https://github.com/pvcraven/pypi_package_example>

<https://habr.com/ru/post/483512/>

Python Entry Points Explained: <https://amir.rachum.com/blog/2017/07/28/python-entry-points/>

## ASGI 

<https://florimond.dev/blog/articles/2019/08/introduction-to-asgi-async-python-web/>


## Binary data
<https://reachtim.com/articles/reading-binary-data-with-python.html> . reading binary data with  python

https://habr.com/ru/company/ruvds/blog/485646/ . Python Tips

## live value plotter using Matplotlib:
<https://github.com/wahtak/develocorder>

<https://www.reddit.com/r/Python/comments/euf53h/dash_django_create_a_powerful_interactive/>

<https://github.com/facebookresearch/visdom> .  Plotting from Facebook research

##  zipapp (Python 3.5) module generates a zip file that can bundle your entire python project (including a virtual environment) and run it as an executable
<http://voorloopnul.com/blog/writing-self-contained-etl-pipeline-with-python/>

## multiprocessing vs threading

https://habr.com/ru/company/skillbox/blog/685682/

<https://habr.com/ru/company/otus/blog/501056/>
```
    import random
    import time
    from concurrent.futures import ProcessPoolExecutor, as_completed

    def hello():
        seconds = random.randint(0, 5)
        print(f"Start blocking for {seconds}s")
        time.sleep(seconds)
        print(f"Stopped blocking after {seconds}s")
        return seconds

    if __name__ == "__main__":

        with ProcessPoolExecutor(max_workers=2) as exec:

            a = exec.submit(hello)
            b = exec.submit(hello)

            for future in as_completed((a, b)):
                print(future.result())
		
```

### multiprocessing, asyncio

https://habr.com/ru/company/skillbox/blog/685682/

https://towardsdatascience.com/parallelizing-python-code-3eb3c8e5f9cd

<http://www.blog.pythonlibrary.org/2016/08/02/python-201-a-multiprocessing-tutorial/>

<https://www.packtpub.com/programming/python-parallel-programming-cookbook> 

<https://habr.com/ru/company/ruvds/blog/475246/>

<http://pljung.de/posts/easy-concurrency-in-python/> . concurrency

<https://zacs.site/blog/linear-python.html>

<https://www.integralist.co.uk/posts/python-asyncio/>

<https://trio.readthedocs.io/en/stable/> asyncio alternative

<https://lucumr.pocoo.org/2020/1/1/async-pressure/>

https://news.ycombinator.com/item?id=24390116

multiprocessing vs threading
<https://sumit-ghosh.com/articles/multiprocessing-vs-threading-python-data-science/>



## Stats / Numpy

<https://realpython.com/pandas-python-explore-dataset/>

<https://realpython.com/python-statistics/>

<https://pbpython.com/natural-breaks.html>

## Other topics
 



### Requests lib

<https://findwork.dev/blog/advanced-usage-python-requests-timeouts-retries-hooks/> . requests lib

<https://requests.readthedocs.io/en/master/user/advanced/>

<https://toolbelt.readthedocs.io/en/latest/>





<https://github.com/benfred/py-spy>  py-spy: Sampling profiler for Python programs

<https://opensource.com/article/19/11/awk-to-python>

<https://habr.com/ru/company/edison/blog/474622/> . Libs

<http://blog.rtwilson.com/five-new-ish-python-things-part-1/> 

<https://habr.com/ru/company/ruvds/blog/472858/> request

<https://pydantic-docs.helpmanual.io/> . data validation

## Logging

<https://habr.com/ru/company/skillfactory/blog/556942/>

https://habr.com/ru/post/649033/

<https://kanoki.org/2019/10/16/python-logging/> 

<https://julien.danjou.info/how-to-log-properly-in-python/>

## Unclassified

<https://news.python.sc/> daily feed

<https://dev.libreneitor.com/expert-python-topics-you-should-know/>

<https://www.blog.duomly.com/20-essential-python-tips-and-tricks-you-should-know/>

<https://pysnakeblog.blogspot.com/>

<https://blog.richard.do/2019/10/17/supercharge-your-python-testing-workflow/> . Testing



## Python tools


<https://spiegelmock.com/2020/01/04/python-2020-modern-best-practices/>


## Slots
<https://habr.com/ru/company/ruvds/blog/480356/>
```
Если вы когда-нибудь писали программы, которые создают по-настоящему большие количества экземпляров некоего класса, то вы могли заметить, что таким программам неожиданно может понадобиться очень много памяти. Происходит это из-за того, что Python использует словари для представления атрибутов экземпляров классов. Это хорошо сказывается на производительности, но, с точки зрения потребления памяти, это неэффективно. Обычно, правда, проблем эта особенность не вызывает. Однако если вы столкнулись в подобной ситуации с нехваткой памяти — можете попробовать воспользоваться атрибутом __slots__:

class Person:
 __slots__ = ["first_name", "last_name", "phone"]
 def __init__(self, first_name, last_name, phone):
  self.first_name = first_name
  self.last_name = last_name
  self.phone = phone

Здесь, когда мы объявляем атрибут __slots__, Python использует для хранения атрибутов не словарь, а маленький массив фиксированного размера. Это серьёзно сокращает объём памяти, необходимый для каждого из экземпляров класса. У применения атрибута __slots__ есть и некоторые недостатки. Так, пользуясь им, мы не можем объявлять новые атрибуты, мы ограничены только теми, которые имеются в __slots__. Кроме того, классы c атрибутом __slots__ не могут использовать множественное наследование.
```
## Import

<https://www.pythonforthelab.com/blog/complete-guide-to-imports-in-python-absolute-relative-and-more/>

<http://python-notes.curiousefficiency.org/en/latest/python_concepts/import_traps.html>

## Collections:NamedTuples (but better use Dataclasses in Python 3.7!) , Counter, DefaultDict, OrderedDict
<https://habr.com/ru/post/478934/>

## defaultdict

Task: group words by their 1st letter.
The structure we’re looking for here is a dictionary of lists, 
having the initials as key and a list of words as value, something like this:
```
{
	"a": ["all", "although", "average"],
	"b": ["best", "both"],
    ...
}
```
Solution without defaultdict
```
text = 'a long text but very interesting and fun'

data = {}
# Cycle through each word, appending it to the correct list
for word in text.split(" "):
    if word[0] in data:
        data[word[0]].append(word)
    else:
        data[word[0]] = [word]
```
Solution without defaultdict:
we completely removed the if check  because we replaced the dictionary with a defaultdict, 
specifying list as the default value ( meaning an empty list ).
```
from collections import defaultdict
text = 'a long text but very interesting and fun'

data = defaultdict(list)
# Cycle through each word, appending it to the correct list
for word in text.split(" "):
    data[word[0]].append(word)
```


<https://gto76.github.io/python-cheatsheet/>

<https://github.com/sharpden/python-infrastructure>

<https://seddonym.me/2019/08/03/ioc-techniques/> inversion of control

How to start python http server:

python -m SimpleHTTPServer <8000> (python2)

python3 -m http.server <8000> (python3)



<https://habr.com/ru/post/426277/>

<https://habr.com/ru/post/457348/> . deploying from github to PythonAnyware

<https://www.techrepublic.com/google-amp/article/how-netflix-uses-python-streaming-giant-reveals-its-programming-language-libraries-and-frameworks/>



<https://www.blog.duomly.com/20-essential-python-tips-and-tricks-you-should-know/>


### Use Jinja template to generate dynamic SQL

https://realpython.com/primer-on-jinja-templating/

<https://medium.com/analytics-and-data/jinja-the-sql-way-of-the-ninja-9a64fc815564> (see pdf file in this folder)


```
from jinja2 import Template
template = Template('Hello {{ name }}!')
x=template.render(name='John Doe')
print(x)

template2 = Template(
"""
Static  begin
<ul>
{% for user in users %}
 x= {{ user.x }}
 y= {{ user.y }}
{% endfor %}
Static end
"""
)

m_users=list()

user1={
 "x": 22,
 "y": 10,
  "pose": "sitting",
}
user2={
 "x": 220,
 "y": 100,
  "pose": "sitting",
}
m_users.append(user1)
m_users.append(user2)

print (user1)
print (user2)


y=template2.render(users = m_users)
print(y)
```

