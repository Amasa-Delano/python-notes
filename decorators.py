#if you see
@something
def cool():
    #....
    return '...'

#this means

cool = something(cool)

#where something is
import functools

def something(func):
    @functools.wraps(func) #preserves info about original function
    def wrapper(*args, **kwargs):
        #put some logic or something here
        return func(*args, **kwargs)
        #put some logic or something here
    return wrapper

#example of working decorator

import time

def timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        value = func(*args, **kwargs)
        end = time.perf_counter()
        run_time = end - start
        print(f"finished running {func.__name__!r} in {run_time:.7f} seconds")
        return value
    return wrapper

#another example

def slow(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        time.sleep(1)
        return func(*args, **kwargs)
    return wrapper
