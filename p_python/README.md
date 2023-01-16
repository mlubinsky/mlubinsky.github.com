### Python snippets

check  whether the given list has duplicates:
```
 def all_unique(lst):
    return len(lst) == len(set(lst))
```    
 check if two strings are anagrams:
```
from collections import Counter

def anagram(first, second):
    return Counter(first) == Counter(second)
```
 check the memory usage of an object.
```
import sys 

variable = 30 
print(sys.getsizeof(variable)) # 24
```
length of a string in bytes.
```
def byte_size(string):
    return(len(string.encode('utf-8')))
```
chunk a list into smaller lists of a specified size.
```
def chunk(list, size):
    return [list[i:i+size] for i in range(0,len(list), size)]

```

removes falsy values (False, None, 0 and “”) from a list by using filter().
```
def compact(lst):
    return list(filter(None, lst))
  
  
compact([0, 1, False, 2, '', 3, 'a', 's', 34]) # [ 1, 2, 3, 'a', 's', 34 ]
```

transpose a 2D array:
```
array = [['a', 'b'], ['c', 'd'], ['e', 'f']]
transposed = zip(*array)
print(transposed) # [('a', 'c', 'e'), ('b', 'd', 'f')]
```
turn a list of strings into a single string with each element from the list separated by commas.
```
hobbies = ["basketball", "football", "swimming"]

print("My hobbies are:") # My hobbies are:
print(", ".join(hobbies)) # basketball, football, swimming
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
