https://www.pythonmorsels.com/time-complexities/

https://www.mattlayman.com/blog/2024/layman-guide-python-built-in-functions/

https://news.ycombinator.com/item?id=41450824 obscure Python standard libs

https://www.gauge.sh/blog/how-to-visualize-your-python-projects-dependency-graph  Visualize Puthon dependency

https://www.trickster.dev/post/lesser-known-parts-of-python-standard-library/

https://habr.com/ru/articles/842792/ working with big files

https://habr.com/ru/articles/830098/ msgspec. Библиотека для сериализации и десериализации чего угодно

https://habr.com/ru/articles/830158/ Python. Внутреннее устройство множеств set и словарей dict. Часть 2 из 2

https://habr.com/ru/companies/yandex/articles/828956/ What is new in Python

https://habr.com/ru/articles/829760/ Python internals 

high - quality python code:
https://news.ycombinator.com/item?id=40085887

working with parquet files:
https://www.blog.pythonlibrary.org/2024/05/06/how-to-read-and-write-parquet-files-with-python/


### Build a dictionary with list elements as keys and their indices as values

my_dict = {item: index for index, item in enumerate(my_list)}

#### Immutable types

  Integers, floats, complex numbers, and Booleans, are always immutable. 
  
  Strings, bytes and tuples are immutable 

positive_infinity = float('inf')
negative_infinity = float('-inf')

### Bytes 

https://www.thepythoncodingstack.com/p/bytes-python-built-in-unicode-utf-8-encoding
```
A bytes object is an immutable sequence of integers. But not just any integers. 
The elements in a bytes object are integers in the range 0 to 255. 
These are the numbers that can be represented by eight bits, where each bit is either 0 or 1. 
The largest 8-bit number is the number that has eight 1's in binary:
 ```
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


### Exception handling
https://realpython.com/python-built-in-exceptions/
```
try:
       # Some Code.... 
except ZeroDivisionError:
    print("You cannot divide by zero.")
except ValueError:
    print("Invalid input. Please enter a valid number.")        
except Exception as e:
       # optional block
       # Handling of exception (if required)
else:
       # execute if no exception
finally:
      # Some code .....(always executed)
      #  Even if you return in the except block still the finally block will execute
 ```


#### Example 1
```
 try:
     l = ["a", "b"]
     int(l[2])
 except (ValueError, IndexError) as e:
     pass
```


#### Example 2: log the traceback, rather than just the error message. 
```
import traceback
try:
    num = int("abc")
except ValueError as err:
    print(traceback.format_exc)
```
#### Example 3: using logging
```
import logging

logger = logging.getLogger()

try:
    num = int("abc")
except ValueError as err:
    logger.exception(err)
```

### Основные типы распределений вероятностей в примерах
https://habr.com/ru/articles/801101/



### f-string
https://pybit.es/articles/python-f-string-codes-i-use-every-day/
```
print(f"Example 2: {year}") # Example 2: 2022
print(f"Example 3: {2 + 2}") # Example 3: 4
text = "Data Science Blog"
print(f"{text=}")  # text='Data Science Blog'
```
### Python notes

https://hynek.me/til/python-portable-binaries/  Python Portable binaries

https://norvig.com/python-iaq.html

https://github.com/gto76/python-cheatsheet



https://www.pythonlikeyoumeanit.com/index.html

https://wiki.python.org/moin/TimeComplexity

https://habr.com/ru/companies/kaspersky/articles/762788/ Функциональное программирование в Python

https://github.com/nyggus/tracemem  memory used by a Python session

https://www.pixelstech.net/article/1702794038-Where-Have-You-Installed-Your-Python-Packages

https://www.reddit.com/r/Python/comments/18nrst3/some_easy_open_source_python_projects_to/

https://medium.datadriveninvestor.com/mastering-advanced-python-40-pro-level-snippets-for-2024-85f5b9359103

Read large file:  
https://tonylixu.medium.com/python-tips-how-to-hand-large-files-84fbbc464a75


### Dunder methods __xxx___

https://www.pythonmorsels.com/every-dunder-method/

https://habr.com/ru/companies/otus/articles/801595/


### Custom Context manager
https://www.kdnuggets.com/how-to-create-custom-context-managers-in-python
```
import sqlite3
from typing import Optional

# Writing a context manager class
class ConnectionManager:
    def __init__(self, db_name: str):
        self.db_name = db_name
        self.conn: Optional[sqlite3.Connection] = None

    def __enter__(self):
        self.conn = sqlite3.connect(self.db_name)
        return self.conn

    def __exit__(self, exc_type, exc_value, traceback):
        if self.conn:
        self.conn.close()
```
Usage of code above:
```
db_name = "library.db"

# Using ConnectionManager context manager directly
with ConnectionManager(db_name) as conn:
	cursor = conn.cursor()

	# Create a books table if it doesn't exist
	cursor.execute("""
    	CREATE TABLE IF NOT EXISTS books (
        	id INTEGER PRIMARY KEY,
        	title TEXT,
        	author TEXT,
        	publication_year INTEGER
    	)
	""")

	# Insert sample book records
	books_data = [
    	("The Great Gatsby", "F. Scott Fitzgerald", 1925),
    	("To Kill a Mockingbird", "Harper Lee", 1960),
    	("1984", "George Orwell", 1949),
    	("Pride and Prejudice", "Jane Austen", 1813)
	]
	cursor.executemany("INSERT INTO books (title, author, publication_year) VALUES (?, ?, ?)", books_data)
	conn.commit()

	# Retrieve and print all book records
	cursor.execute("SELECT * FROM books")
	records = cursor.fetchall()
	print("Library Catalog:")
	for record in records:
    	    book_id, title, author, publication_year = record
    	    print(f"Book ID: {book_id}, Title: {title}, Author: {author}, Year: {publication_year}")
            cursor.close()
```
### Default arguments pitfall - do not use mutable default args!

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


```
def foo( bar=[]):
    bar.append("x")
    return bar

foo()     ["x"]
foo()     ["x","x"]
foo()     ["x","x","x"]


значение по умолчанию для функции инициализируется только один раз, во время определения функции.
Таким образом, аргумент bar инициализируется по умолчанию (т. е. пустым списком) только тогда, 
когда foo() определен впервые, но последующие вызовы foo() 
(т. е. без указания аргумента bar) продолжат использовать тот же список, 
который был создан для аргумента bar в момент первого определения функции.

Solution:

 def foo(bar=None):
    if bar is None:		# or if not bar:
        bar = []
   bar.append("baz")
   return bar

```


### Examples

```
lists A and B of the same lenght logically related by index.
We creating sorted list from A and we also want to create somehow the new list from B to preserve the by index relation between A_sorted and B_new

Here are two common approaches to create a new list from B that preserves the matching with the sorted A_sorted list in Python:

1. Using Dictionary Comprehension:

Python
A = [3, 1, 4, 1]
B = ["apple", "banana", "cherry", "date"]

A_sorted = sorted(A)

# Create a dictionary with sorted elements from A as keys and corresponding elements from B as values
B_sorted = {element: B[A.index(element)] for element in A_sorted}

print(B_sorted)  # Output: {'banana': 'banana', 'date': 'date', 'apple': 'apple', 1: 'cherry'}

# Sort the dictionary by keys to get B_sorted in the same order as A_sorted
B_sorted = list(dict(sorted(B_sorted.items())).values())

print(B_sorted)  # Output: ['banana', 'date', 'apple', 'cherry']
 
Explanation:

Create a dictionary where keys are elements from the sorted A_sorted list and values are the corresponding elements from B at the same index using dictionary comprehension.
Optionally, sort the dictionary by keys using sorted(B_sorted.items()) to ensure the order aligns with A_sorted.
Extract the values from the sorted dictionary using list(dict(...).values()) to get the final B_sorted list.

2. Using zip and List Comprehension:

Python
A = [3, 1, 4, 1]
B = ["apple", "banana", "cherry", "date"]

A_sorted = sorted(A)

# Use zip and list comprehension to create B_sorted based on the order in A_sorted
B_sorted = [B[A.index(element)] for element in A_sorted]

print(B_sorted)  # Output: ['banana', 'date', 'apple', 'date']
 
Explanation:

Use zip to create an iterator of paired elements from A_sorted and B.
Use list comprehension to iterate through the zipped pairs and access the corresponding element from B using the index obtained from A.index(element).
This creates a new list B_sorted containing elements from B in the same order as the sorted A_sorted list.

```

### List
 use dir([]) to look up the functions that operate on a List.
```

>>> dir([])
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__',
'__delslice__', '__doc__', '__eq__', '__format__', '__ge__', 
'__getattribute__', '__getitem__', '__getslice__', '__gt__', '__hash__',
'__iadd__', '__imul__', '__init__', '__iter__', '__le__', '__len__',
'__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__',
'__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__',
'__setslice__', '__sizeof__', '__str__', '__subclasshook__', 'append',
'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']

>>> help([].sort)
Help on built-in function sort:
     
sort(...)
    L.sort(cmp=None, key=None, reverse=False) -- stable sort *IN PLACE*;
    cmp(x, y) -> -1, 0, 1
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

#### The most frequent element that appears in a list.
```
def most_frequent(list):
    return max(set(list), key = list.count)

numbers = [1,2,1,2,3,2,1,4,2]
most_frequent(numbers)

from collections import Counter
letters = ['a', 'b', 'c', 'a', 'c', 'a', 't', 'p', 'b', 'a', 'y', 't', 'c']
letter_counts = Counter(letters)
print(letter_counts.most_common(1)) # [('a', 4)]  this is array of tuples(char, count)
letter_counts.most_common(1)[0][0] # tale 1st element from array of tuples and take 1st item in the tuple(which is char)
```



### List comprehention  [expression for item in list if conditional]

list comprehension is the process of creating a new list from an existing list. Or, you can say that it is Python's unique way of appending a for loop to a list
```
list_b = [i**2 for i in range(1, 20)]
```
### List as stack or queue
https://realpython.com/how-to-implement-python-stack/

https://stackabuse.com/guide-to-stacks-in-python/

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

### System path manipulation
```
import sys
sys.path.insert(0, os.path.abspath('..'))
sys.path.append(os.getcwd())
```
### Any

Check what string has no specific values:

if not any(value in line for value in ("StatusRequest", "StatusResponse")):

if "StatusRequest" not in line and "StatusResponse" not in line:




### String
```
strings = [string1, string2, string3]
string1 = "".join(strings)
string1 = f"{string1}{string2}{string3}"
reverse_string = input_string[::-1]

def reverse_string(input_string):
    return ''.join(reversed(input_string))

for i in reversed(range(5)):  # range(10)[::-1]
    print(i)
```

#### checks whether a given string is a palindrome.
```
def palindrome(a):
    return a == a[::-1]


palindrome('mom') # True
```
### Calculate number of occurance for every char in string
```
mystring="abcdafff"
print(set(mystring)

for c in set(mystring):
     print (c, mystring.count(c))
```

###  factorial 
```
from math import factorial
factorial(3)
6
```

### bisect 
   https://betterprogramming.pub/everything-you-can-do-with-pythons-bisect-module-40bdaadbc22f
### Converting string to list of chars 
```
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




####
https://www.bitecode.dev/p/you-are-comfy-with-python-basics

https://lobste.rs/s/sns4mr/comfy_with_python_basic_tooling_now_what

 

### By value or by reference?

https://medium.com/techtofreedom/python-is-neither-call-by-value-nor-call-by-reference-2a0c8f6f4a8f

https://www.pythonmorsels.com/variables-are-pointers/

https://nedbatchelder.com/blog/202403/does_python_have_pointers.html

https://codebeez.nl/blogs/the-memory-footprint-of-your-python-application/
```
An object’s identity is a unique identifier that distinguishes it from other objects. 
ou can use the built-in id() function to get the identity of any Python object.
```
### Alias vs copy
```
In Python, you can create aliases of variables using the assignment operator (=). 
Assignments don’t create copies of objects in Python. 
Instead, they create bindings between the variable and the object involved in the assignment. 
Therefore, when you have several aliases of a given list, changes in an alias will affect the rest of the aliases.

a=[1,2,3]
b=a
a.append(4)
print(a)   #[1, 2, 3, 4]
print(b)  # [1, 2, 3, 4]
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

### Array
https://realpython.com/python-array/
```
Unlike the classic array data structure with a fixed length, Python’s array data type is dynamically sized.
Therefore, you can add elements to an empty array later, and it’ll automatically resize itself accordingly.
There are thirteen numeric types in the array module, each represented by a single-letter type code, which you can reveal by accessing the typecodes variable:

 import array
 array.typecodes
'bBuhHiIlLqQfd'


TypeCode	C_Type	Minimum Size in Bytes
b	signed char	1
B	unsigned char	1
h	signed short	2
H	unsigned short	2
i	signed int	2
I	unsigned int	2
l	signed long	4
L	unsigned long	4
q	signed long long	8
Q	unsigned long long	8
f	float	4
d	double	8
u	wchar_t	2


array("i").itemsize
4
 array("i").typecode
'i'
``` 


#### Stack, queue, priority queue  
 https://realpython.com/queue-in-python/ <br>
 https://realpython.com/python-deque/ <br>

#### heapq 
https://favtutor.com/blogs/heap-in-python <br>

https://stackabuse.com/guide-to-heaps-in-python/

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


### Queue
https://realpython.com/queue-in-python/

https://stackabuse.com/guide-to-queues-in-python/

deque is implemented using a doubly-linked list. It supports fast O(1) appends and pops from both ends
```
from collections import deque
queue = deque()
# Enqueue
queue.append('A')
queue.append('B')
queue.append('C')
print(queue)  # Output: deque(['A', 'B', 'C'])

# Dequeue
queue.popleft()
print(queue)  # Output: deque(['B', 'C'])


dq.appendleft('A')  # add to the front
dq.append('B')      # add to the rear
dq.pop()            # remove from the rear
dq.popleft()        # remove from the front
```
#### Implementing a Circular Queue
```
A circular queue (or ring buffer) is an advanced data structure where the last element is connected to the first, ensuring a circular flow. deque can mimic this behavior using its maxlen property:

from collections import deque

circular_queue = deque(maxlen=3)
circular_queue.append(1)
circular_queue.append(2)
circular_queue.append(3)

# Now the queue is full, adding another element will remove the oldest one
circular_queue.append(4)
print(circular_queue)  # Output: deque([2, 3, 4], maxlen=3)
```



#### queue module in Python provides a more specialized approach to queue management, catering to various use cases:
```
SimpleQueue - A basic FIFO queue
LifoQueue - A LIFO queue, essentially a stack
PriorityQueue - Elements are dequeued based on their assigned priority
 
import queue
q = queue.SimpleQueue() ## FIFO
# Enqueue
q.put('A')
q.put('B')
q.put('C')
print(q.queue)  # Output: ['A', 'B', 'C']

# Dequeue
q.get()
print(q.queue)  # Output: ['B', 'C']

import queue

q = queue.SimpleQueue()

try:
    item = q.get_nowait()
except queue.Empty:
    print("Queue is empty!")

pq = queue.PriorityQueue()
pq.put((2, "Task B"))
pq.put((1, "Task A"))  # Lower numbers denote higher priority
pq.put((3, "Task C"))

while not pq.empty():
    _, task = pq.get()
    print(f"Processing: {task}")


```
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

https://medium.com/techtofreedom/7-uses-of-python-functools-that-make-your-code-more-professional-a42f55bacd44

https://florian-dahlitz.de/articles/introduction-to-pythons-functools-module

https://jacobpadilla.com/articles/Functools-Deep-Dive

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
https://www.techbeamers.com/python-reduce/
```
from functools import reduce
# pattern of usage:
result = reducing(binary_func, seq, init_val=None)

prices = [100, 50, 30, 80, 120]
def apply_discount(total, price):
    return total - (price * 0.1)
discounted_total = reduce(apply_discount, prices)
print("Original Total:", sum(prices))
print("Discounted Total:", discounted_total)

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

from collections import defaultdict
dd = defaultdict(int)
#dd = collections.defaultdict(int)
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

https://github.com/pyutils/line_profiler

https://docs.python.org/3/library/profile.html

https://github.com/plasma-umass/scalene  high-performance, high-precision CPU, GPU, and memory profiler

https://pypi.org/project/scalene 

https://habr.com/ru/companies/ruvds/articles/757336/ cProfile  / profile

https://realpython.com/python-profiling/

### Fast python, multiprocessing

https://habr.com/ru/articles/803607/  multiprocessing

https://habr.com/ru/companies/sberbank/articles/829098/

https://habr.com/ru/articles/804799/

https://habr.com/ru/articles/804917/

https://github.com/plasma-umass/scalene  memory profiler

https://bloomberg.github.io/memray/index.html memory profiler

https://github.com/joerick/pyinstrument

https://habr.com/ru/articles/773376/

https://pythonbooks.org/python-high-performance-second-edition/

https://habr.com/ru/companies/otus/articles/771346/

https://www.amazon.com/High-Performance-Python-Performant-Programming/dp/1492055026/

https://www.amazon.com/Python-Science-Tiago-Rodrigues-Antao/dp/1617297933

https://pythonspeed.com/

https://coderslegacy.com/cython-vs-cpython-comparing-speed/  Cython

### Multiprocessing 

https://habr.com/ru/articles/789904/

https://news.ycombinator.com/item?id=39490747

https://www.bitecode.dev/p/the-easy-way-to-concurrency-and-parallelism

https://news.ycombinator.com/item?id=37089817

https://milliams.com/courses/parallel_python/

https://habr.com/ru/articles/825206/

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

https://github.com/pomponchik/suby

https://docs.python.org/3/library/shlex.html

sh  https://amoffat.github.io/sh/index.html https://amoffat.github.io/sh/sections/faq.html

https://www.pyinvoke.org/


```
This function on should  call the Windows bat file using subprocess module.
The output of .bat file should be visible in console and at the same time
it should be captured into variable which is returned by subprocess.
If the called .bat file fails or the return code of .bat file is not 0 then
print the error message.

Using run()
------------
import subprocess

def run_bat_file(bat_file_path):
    try:
        # Run the .bat file and capture output
        result = subprocess.run(
            [bat_file_path],
            capture_output=True,
            text=True,
            shell=True
        )

        # Print the output to the console
        print(result.stdout)

        # Check if the return code is not 0 and print error message
        if result.returncode != 0:
            print(f"Error: The bat file failed with return code {result.returncode}")
            print(result.stderr)

        return result.stdout

    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
output = run_bat_file('path_to_your_bat_file.bat')
print(output)


Example 2
----------
import subprocess

def call_bat_file(bat_file_path):
  """Calls a Windows .bat file and captures output while handling errors.

  Args:
      bat_file_path (str): The path to the .bat file.

  Returns:
      str: The captured output of the .bat file, or an error message if execution fails.
  """

  try:
    # Use run() for simpler execution
    completed_process = subprocess.run(
        bat_file_path,
        capture_output=True,  # Capture output
        shell=True,         # Allow shell interpretation (optional)
        text=True,          # Decode output to string automatically
    )

    if completed_process.returncode != 0:
      raise subprocess.CalledProcessError(returncode=completed_process.returncode, cmd=[bat_file_path])

    return completed_process.stdout

  except subprocess.CalledProcessError as e:
    error_msg = f"Error running '{bat_file_path}': {e}"
    print(error_msg)
    return error_msg

  except Exception as e:
    error_msg = f"An unexpected error occurred: {e}"
    print(error_msg)
    return error_msg
```



### Another approach: Popen() and communicate()
```
Reasons for using subprocess.Popen():

More control: Popen() offers finer-grained control over the process. You can manage its standard input, output, and error streams independently, allowing you to interact with the running process if needed.
 This might be useful in situations where you need to send data to the .bat file or read its output line by line.

using subprocess.Popen() with subprocess.communicate() can provide more flexibility compared to subprocess.run().

Here are some advantages of using subprocess.Popen() and subprocess.communicate():

Real-time Output: With subprocess.Popen(), you can capture the output in real-time, which can be useful for long-running processes where you want to see the output as it is generated.

More Control:
subprocess.Popen() gives you more control over the process execution, including the ability to handle stdin, stdout, and stderr streams separately, send input to the process, or terminate it if needed.

Non-blocking Execution:
You can achieve non-blocking execution by periodically checking the process status,
which is useful for monitoring and interacting with the process while it is running.


Reasons to prefer subprocess.run() (generally):

Simpler execution: run() simplifies the process execution by handling its lifecycle internally. You provide the command and capture the output and return code in a single call.
It's great when you just want to run a command, wait for it to finish, and get the results without needing to manage the process streams explicitly.
Error handling: run() automatically checks the return code and raises an exception if the command fails. This simplifies error handling compared to manually checking the return code with Popen().
When to choose which:

For simple execution and capturing output: Use subprocess.run(). It's the recommended approach for most cases.
For more control over the process and its streams: Use subprocess.Popen() if you need to interact with the running process or manage its input/output explicitly.

import subprocess

def run_bat_file(bat_file_path):
    try:
        # Open the subprocess and redirect stdout and stderr
        process = subprocess.Popen(
            [bat_file_path],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            shell=True
        )

        # Capture output in real-time
        stdout, stderr = process.communicate()

        # Print the output to the console
        if stdout:
            print(stdout)
        if stderr:
            print(stderr)

        # Check if the return code is not 0 and print error message
        if process.returncode != 0:
            print(f"Error: The bat file failed with return code {process.returncode}")
            print(stderr)

        return stdout

    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
output = run_bat_file('path_to_your_bat_file.bat')
print(output)






import subprocess

def call_bat_file(bat_file_path):
  """Calls a Windows .bat file and captures output while handling errors.

  Args:
      bat_file_path (str): The path to the .bat file.

  Returns:
      str: The captured output of the .bat file, or an error message if execution fails.
  """

  try:
    # Use Popen for more control over the process
    process = subprocess.Popen(
        [bat_file_path],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,  # Combine stdout and stderr for easier handling
        shell=True  # Allow shell interpretation for complex .bat files (optional)
    )

    # Capture output and potential errors
    output, _ = process.communicate()  # Read combined stdout and stderr
    output = output.decode('utf-8')  # Decode bytes to string

    # Check return code for errors
    if process.returncode != 0:
      raise subprocess.CalledProcessError(returncode=process.returncode, cmd=[bat_file_path])

    return output

  except subprocess.CalledProcessError as e:
    error_msg = f"Error running '{bat_file_path}': {e}"
    print(error_msg)
    return error_msg

  except Exception as e:
    error_msg = f"An unexpected error occurred: {e}"
    print(error_msg)
    return error_msg

# Example usage
bat_file_path = "C:\\path\\to\\your\\bat_file.bat"  # Replace with your actual path
output = call_bat_file(bat_file_path)

if output.startswith("Error"):
  print("The .bat file failed to execute.")
else:
  print("The .bat file output:\n", output)


```
### 3rd party libs

DiskCache efficiently makes gigabytes of storage space available for caching. 
By leveraging rock-solid database libraries and memory-mapped files, cache performance can match and exceed industry-standard solutions. 
https://grantjenks.com/docs/diskcache/

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

### Scheduling
https://docs.python.org/3/library/sched.html

https://pypi.org/project/schedule/ job scheduling 

https://gaurav-adarshi.medium.com/different-ways-to-schedule-tasks-in-python-45e03d5411ee

### Logging

https://betterstack.com/community/guides/logging/python/python-logging-best-practices/

https://www.structlog.org/en/stable/index.html struct logging

https://steve.dignam.xyz/2023/04/09/structlog-instead-of-logging/

https://www.youtube.com/watch?v=wiGkV37Kbxk Raymond Hettinger: Numerical Marvels Inside Python

### How to contribute to open source python projects:
https://www.reddit.com/r/Python/comments/12p771v/what_can_i_contribute_to_scipy_or_other_with_my/

#### *args and **kwargs
args is always a tuple, which can be empty.
Writing *args is a well followed convention, but you can choose a different name - the asterisk is what makes it a variable
argument
```
def takes_any_args (*args ) :
  print (" Type of args : " + str( type ( args ) ) ) # Type of args : <class 'tuple '>
  print (" Value of args : " + str( args ) )
  print(f"args is a {type(args)} with {len(args)} elements.") # args is a <class 'tuple'> with 2 elements.


def add(*numbers_to_add):
  added = 0
  for number in numbers_to_add:
      added += number
  return added

add(1, 2, 3, 4, 5)
15  
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

https://levelup.gitconnected.com/9-things-i-never-knew-about-itertools-python-until-recently-b98fbed92d2f

https://medium.com/techtofreedom/10-python-itertools-to-make-your-code-neater-cleaner-and-better-5e1aada5e13e

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

https://levelup.gitconnected.com/python-generators-how-to-efficiently-fetch-data-from-databases-25f1947f56c0

https://towardsdatascience.com/python-for-data-engineers-f3d5db59b6dd

https://www.dabeaz.com/generators/Generators.pdf

https://www.speakeasy.com/post/python-http-clients-requests-vs-httpx-vs-aiohttp

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

 
### Enumeration

https://roarepally.com/blog/python-311-enums

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

 

### Numpy

https://realpython.com/search?q=numpy

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

### Others

https://www.reddit.com/r/Python/comments/1egg99j/what_are_some_unusual_but_useful_python_libraries/

### Billion rows challange
https://levelup.gitconnected.com/python-libraries-take-the-billion-row-challenge-7c108611a9ad

###  file watcher
https://github.com/samuelcolvin/watchfiles

https://pypi.org/project/watchdog/

### Litestar: ans ASGI web framework batteries included, faster and better than FastApi. It is well designed and supports a layered architecture.

### Sortedcontainers: Sorted datastructures like set and dict, very fast for lookups

### Diskcache: file based cache, very useful for heavy calculations and db results caching

#### Task runners

https://just.systems/man/en/chapter_1.html

https://taskfile.dev/

https://pydoit.org/

https://github.com/TekWizely/run


### Data Tools

https://datatable.readthedocs.io/en/latest/

https://pola.rs/posts/polars_birds_eye_view/

https://www.jetbrains.com/dataspell/ JetBrains

https://deepnote.com/compare

https://colab.research.google.com/

Spider

https://holoviz.org/

https://dataprep.ai/

https://codeandquery.com/build-scalable-data-pipelines-in-python-using-dlt-5e8275fd3371  DLT

https://towardsdev.com/five-killer-optimization-techniques-that-most-pandas-arent-aware-of-f1e31af2257a

### Postgres Dashboard (Panels and others)

https://mljar.com/blog/postgresql-dashboard-python/

## Plotting: Seaborn, GnuPlot and others

https://realpython.com/python-seaborn/

https://realpython.com/pandas-plot-python/

 http://www.gnuplot.info/

 https://github.com/dkogan/gnuplotlib

 https://github.com/bedbad/justpyplot

 https://github.com/man-group/dtale
 

### Pipeline tools

https://hamilton.dagworks.io/en/latest/

https://pipefunc.readthedocs.io/en/latest/

https://pathway.com/

### Tree algo 

https://queelius.github.io/AlgoTree/introduction.html

### Query CSV, JSON and Parquet files

https://github.com/luminousmen/data-toolset   Avro and Parquet 

 Query CSV, JSON and Parquet files with SQL
 
https://github.com/MarkyMan4/filequery  https://pypi.org/project/filequery/

### Log viewers

https://news.ycombinator.com/item?id=39317580

https://github.com/Textualize/toolong

https://github.com/dloss/klp

https://lnav.org/

https://logdy.dev/

https://github.com/kernc/diff-logs

### Linting Python in Visual Studio Code

https://code.visualstudio.com/docs/python/linting

https://devblogs.microsoft.com/python/python-linting-video/

https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html#cheat-sheet-py3

### Get IP
```
import socket
def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # doesn't even have to be reachable
        s.connect(('10.255.255.255', 1))
        IP = s.getsockname()[0]
    except Exception:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP
```

## Working with MS Excel

https://hakibenita.com/fast-excel-python

https://www.datacamp.com/tutorial/python-excel-tutorial

https://kahemchu.medium.com/automate-excel-chart-with-python-d7bec97df1e5

https://pandas-xlsxwriter-charts.readthedocs.io/

https://forum.codewithmosh.com/t/creating-a-graph-in-excel/21607/2

https://support.microsoft.com/en-us/office/create-python-in-excel-plots-and-charts-798b5e8d-ce45-4451-8da3-f269cdad5cff

https://www.pyxll.com/docs/userguide/plotting/index.html
