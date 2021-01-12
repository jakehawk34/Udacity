# --------------
# User Instructions
#
# Write a function, inverse, which takes as input a monotonically
# increasing (always increasing) function that is defined on the 
# non-negative numbers. The runtime of your program should be 
# proportional to the LOGARITHM of the input. You may want to 
# do some research into binary search and Newton's method to 
# help you out.
#
# This function should return another function which computes the
# inverse of the input function. 
#
# Your inverse function should also take an optional parameter, 
# delta, as input so that the computed value of the inverse will
# be within delta of the true value.

# -------------
# Grading Notes
#
# Your function will be called with three test cases. The 
# input numbers will be large enough that your submission
# will only terminate in the allotted time if it is 
# efficient enough. 

def slow_inverse(f, delta=1/128.):
    """Given a function y = f(x) that is a monotonically increasing function on
    non-negatve numbers, return the function x = f_1(y) that is an approximate
    inverse, picking the closest value to the inverse, within delta."""
    def f_1(y):
        x = 0
        while f(x) < y:
            x += delta
        # Now x is too big, x-delta is too small; pick the closest to y
        return x if (f(x)-y < y-f(x-delta)) else x - delta
    return f_1 

#Approximates the square root of a number
def newton_method(num, iters = 20):
    a = float(num)
    i = 0
    while i < iters:
        num = 0.5 * (num + a/num)
        i += 1
    return num

def inverse(f, delta = 1/1024.):
    """Given a function y = f(x) that is a monotonically increasing function on
    non-negatve numbers, return the function x = f_1(y) that is an approximate
    inverse, picking the closest value to the inverse, within delta."""
    def f_1(y):
        lo, hi = find_bounds(f, y)
        return binary_search(f, y, lo, hi, delta)
    return f_1

def find_bounds(f, y):
    #Find values lo and hi such that f(lo) <= y <= f(hi)
    #Keep doubling x until f(x) >= y, set this value to hi
    #Lo is set to either the previous x or 0
    x = 1
    while f(x) < y:
        x *= 2
    if x == 1:
        lo = 0
    else: 
        lo = x/2
    return lo, x


def binary_search(f, y, lo, hi, delta):
    '''
    Given a function f(x), a y-value, a lower bound and upper bound, and a delta.
    While the lower bound is less than the higher bound, approximate x as the average of the two.
    if f(x) is less than y, increase the lower bound by delta
    If f(x) is greater than y, decrease the upper bound by delta
    If f(x) equals y, return the x-value that corresponds to the y-value.
    When the function does not hit the exact value, return hi if the diff between 
    f(hi) and y is smaller than that of y and f(lo) and vice versa.
    '''
    while lo <= hi:
        x = (lo + hi) / 2
        if f(x) < y:
            lo = x + delta
        elif f(x) > y:
            hi = x - delta
        else:
            return f"The target x for y = {y} is located at x = {x}"
    if f(hi) - y < y - f(lo):
        return f"Best approximation for x was high and equal to {hi}"
    else:
        return f"Best approximation for x was lo and equal to {lo}"


def square(x): return x*x

def cube(x): return x ** 3

sqrt = inverse(square)

cube_root = inverse(cube)

print(sqrt(1000000000))
print(cube_root(82))








