"""
Given two integers, which can be positive and negative, find the sum of all the numbers between including them too and return it. If both numbers are equal return a or b.

Note! a and b are not ordered!
"""


def get_sum(a, b):
    x = (a + b) * (abs(a - b) + 1) // 2
    return x