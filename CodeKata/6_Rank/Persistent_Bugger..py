"""
Write a function, persistence, that takes in a positive parameter num and returns its multiplicative persistence, which is the number of times you must multiply the digits in num until you reach a single digit. 
"""
from functools import reduce
import operator

def persistence(n):
    if len(str(n)) == 1:
        return 0
    else:
      val = reduce(operator.mul, map(int, str(n)))
      x = 1 + persistence(val)
    return x
