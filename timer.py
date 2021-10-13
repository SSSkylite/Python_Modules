import time
from functools import wraps


def timer(func):
    @wraps(func)
    def timed(*args, **kwargs):
        print("---TIMER--- TIMER START")
        ts = time.time()
        result = func(*args, **kwargs)
        te = time.time()
        print("---TIMER--- %2.4f seconds to complete." % (te-ts))
        #print('func:%r args:[%r, %r] took: %2.4f sec' %(func.__name__, args, kwargs, te-ts))
        return result
    return timed
