"""
Consider an array of sheep where some sheep may be missing from their place. We need a function that counts the number of sheep present in the array (true means present).
"""
def positive_sum(arr):
    x = 0
    for i in arr:
    	if i > 0: 
	      x += i
    return x