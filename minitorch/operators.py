"""Collection of the core mathematical operators used throughout the code base."""

import math

# ## Task 0.1
from typing import Callable, Iterable

#
# Implementation of a prelude of elementary functions.

# Mathematical functions:
# - mul
def mul(x,y):
    return x * y
# - id
def id(x):
    return x
# - add
def add(x,y):
    return x + y
# - neg
def neg(x):
    return -x
# - lt
def lt(x,y):
    return x < y
# - eq
def eq(x,y):
    return x == y
# - max
def max(x,y):
    return x if x > y else y
# - is_close
def is_close(x,y):
    return abs(x - y) < 1e-2
# - sigmoid
def sigmoid(x):
    return 1 / (1 + math.exp(-x))
# - relu
def relu(x):
    return x if x > 0 else 0
# - log
def log(x):
    return math.log(x)
# - exp
def exp(x):
    return math.exp(x)
# - log_back
def log_back(x,y):
    return y/x
# - inv
def inv(x):
    return 1 / x
# - inv_back
def inv_back(x,y):
    return -x / math.pow(y,2)
# - relu_back
def relu_back(x, y):
    return y if x > 0 else 0

#
# For sigmoid calculate as:
# $f(x) =  \frac{1.0}{(1.0 + e^{-x})}$ if x >=0 else $\frac{e^x}{(1.0 + e^{x})}$
# For is_close:
# $f(x) = |x - y| < 1e-2$


# TODO: Implement for Task 0.1.


# ## Task 0.3

# Small practice library of elementary higher-order functions.

# Implement the following core functions
# - map
def map(fn):
    def process(ls):
        arr = []
        for item in ls:
            arr.append(fn(item))
        return arr
    return process
# - zipWith
def zipwith(fn):
    def process(a,b):
        arr = []
        for x,y in zip(a,b):
            arr.append(fn(x,y))
        return arr
    return process
# - reduce
def reduce(fn,start):
    def process(ls):
        ans  = start
        for item in ls:
            ans = fn(ans,item)
        return ans
    return process

#
# Use these to implement
# - negList : negate a list
def negList(list):
    return map(neg)(list)
# - addLists : add two lists together
def addLists(list1,list2):
    return zipwith(add)(list1,list2)
# - sum: sum lists
def sum(list):
    return reduce(add,0)(list)
# - prod: take the product of lists
def prod(list):
    return reduce(mul,1)(list)

# TODO: Implement for Task 0.3.
