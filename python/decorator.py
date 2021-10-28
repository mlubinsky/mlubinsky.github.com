# Look here for more examples:
# https://betterprogramming.pub/six-advanced-decorator-patterns-5ffe67552691
# https://medium.com/techtofreedom/7-levels-of-using-decorators-in-python-370473fcbe76


def measure_time(func):
    def wrapper(*args, **kwargs):
        from time import time
        start = time()
        result = func(*args, **kwargs)
        print(f'Elapsed time is {time() - start} ms')
        return result
    return wrapper
  
@measure_time
def add(x, y):
    return x + y

add(2, 5)

### sleeping

import time


@measure_time
def sleeping_func(sleep_time):
    time.sleep(sleep_time)


sleeping_func(0.5)
sleeping_func(1)
sleeping_func(1.5)
sleeping_func(2)


#### Logger decorator - shows the function name and the corresponding timestamp value that can be written.

def logger(func):
    from datetime import datetime
    def wrapper(*args, **kwargs):
        print('_' * 25)
        print(f'Run on: {datetime.today().strftime("%Y-%m-%d %H:%M:%S")}')
        print(func.__name__)
        func(*args, **kwargs)
        print('_' * 25)
    return wrapper
  
  
 @logger
def shutdown():
    print('System shutdown')


@logger
def restart():
    print('System restarts')


shutdown()
restart() 




def log_call(fun):
    """
        Decorator @log_call wraps the funtion 
        with log events.
    """
    def wrapper(*args, **kwargs):
        #Pre:
        logger.info("before function: {}".format(fun.__name__))
        result = fun(*args, **kwargs)
        #post:
        logger.info("after function: {}, result:
                   {}".format(fun.__name__,result))
        return result
    return wrapper
@log_call
def add_one(x):
    x = x+1
    return(x)
y=0
y = add_one(y)
y
