"""
A string of space separated numbers, and have to return the highest and lowest number.
"""
def high_and_low(numbers):

    x = [int(i) for i in numbers.split(" ")]
    y = "%i %i" % (max(x),min(x))

    return y
