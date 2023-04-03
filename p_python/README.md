### Python notes

https://www.stationx.net/python-data-structures-cheat-sheet/

#### Immutable types

  Integers, floats, complex numbers, and Booleans, are always immutable. 
  
  Strings, bytes and tuples are immutable 
  
  lists, dictionaries, and sets are mutable 
```  
   isinstance([1, 2, 3], list)

   issubclass(bool, int) #  True
   
   isinstance(True, int) # True

   isinstance(False, int)  True

    int(True) # 1

   int(False) # 0 
```
### Links

https://docs.python-guide.org/ 

https://realpython.com/python-iterators-iterables/

https://docs.python.org/3/library/functions.html

https://docs.python.org/3/library/index.html

https://github.com/Suor/funcy. A fancy and practical functional tools

https://stackoverflow.com/questions/50821312/meaning-of-python-m-flag

https://www.youtube.com/watch?v=wiGkV37Kbxk Raymond Hettinger: Numerical Marvels Inside Python

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



### reversed()
```
s = 'Python'
print(list(reversed(s)))

# Output: ['n', 'o', 'h', 't', 'y', 'P']
``` 

#### Stack, queue, priority queue (heapq)  
 https://realpython.com/queue-in-python/ <br>
 https://realpython.com/python-deque/

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

https://realpython.com/python-data-classes/

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
#### product()
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

#### Sorting

https://tproger.ru/translations/python-sorting/

list.sort(reverse=True/False) - in place, returns None

sorted(any_iterable_object, key=..., reverse=True/False) - returns new sorted object

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

 Alternatively, the operator module’s
_itemgetter_ creates and returns a key function that looks up a named dictionary field:
```
 from operator import itemgetter
 # Sort by GPA:
 sorted ( students , key= itemgetter ("gpa") )
```
This is how you use itemgetter when the sequence elements are dictionaries. It also works when
the elements are tuples or lists - just pass a number index instead:

  Same data , but as a list of tuples .
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

#### Generators, yield
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
#### map, filter, zip
```
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
```
def is_even (n) :
  return n % 2 == 0
  
filtered = filter ( is_even , numbers )
for num in filtered : print (num)
```
### zip()
```
zipped = zip( numbers , big_numbers )
for pair in zipped : print ( pair )
```
### reduce()
```
from functools import reduce

city = ['L', 'o', 'n', 'd', 'o', 'n', 2, 0, 2, 0]
city_to_str = reduce(lambda x, y: str(x) + str(y), city)
print(city_to_str)
# London2020
```
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

### Enumeration
https://florian-dahlitz.de/articles/why-you-should-use-more-enums-in-python

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
