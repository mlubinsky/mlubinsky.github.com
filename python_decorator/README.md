https://habr.com/ru/articles/750312/

https://habr.com/ru/articles/814217/
```
The @dataclass decorator (introduced in Python 3.7) can automatically generate several special methods for a class,
such as __init__, __repr__, __eq__, __lt__, and so on.
```

### Decorators

https://medium.com/techtofreedom/9-python-built-in-decorators-that-optimize-your-code-significantly-bc3f661e9017

https://medium.com/codex/unwrapping-the-power-of-python-a-quick-guide-to-wrappers-and-decorators-db442dd89ae2

https://medium.com/@ayush-thakur02/python-decorators-that-can-reduce-your-code-by-half-b19f673bc7d8

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

https://jacobpadilla.com/articles/Functools-Deep-Dive
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


