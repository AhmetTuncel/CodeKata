"""
You get an array of numbers, return the sum of all of the positives ones.

Example [1,-4,7,12] => 1 + 7 + 12 = 20

Note: array may be empty, in this case return 0.

"""
def positive_sum(arr):
    x = 0
    for i in arr:
    	if i > 0: 
	      x += i
    return x