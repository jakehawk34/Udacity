from functools import update_wrapper

def disabled(f):
    return f

def decorator(d):
    #Make function d a decorator: d wraps a function fn
    def _d(fn):
        return update_wrapper(d(fn), fn)
    update_wrapper(_d, d)
    return _d

@decorator
def memo(f):
    #Decorator that caches the return value for each call to f(args)
    #Whenever it is called again with the same args, we can just look it up
    cache = {}
    def _f(*args):
        try:
            return cache[args]
        except KeyError:
            cache[args] = result = f(*args)
            return result
        except TypeError:
            return f(args)
    return _f

@decorator
def countcalls(f):
    #Decorator that makes the function counts calls to it, in callcounts[f]
    def _f(*args):
        callcounts[_f] += 1
        return f(*args)
    callcounts[_f] = 0
    return _f

callcounts = {}


@decorator
def trace(f):
    indent = '   '
    def _f(*args):
        signature = f"{f.__name__}({', '.join(map(repr, args))})"
        print(f'{trace.level*indent}--> {signature}')
        trace.level += 1
        try:
            result = f(*args)# your code here
            print(f'{(trace.level-1)*indent}<-- {signature} == {result}')
        finally:
            trace.level -= 1# your code here
        return result# your code here
    trace.level = 0
    return _f


#Fibonacci function for nth term in the sequence
@countcalls
@memo
@trace
def fib(n): 
    if n <= 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

fib(30)


for f, count in callcounts.items():
    print("Number of calls to {} : {}".format(f.__name__, count))
