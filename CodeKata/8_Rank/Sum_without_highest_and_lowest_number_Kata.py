"""

Sum all the numbers of the array  except the highest and the lowest element (the value, not the index!).
(The highest/lowest element is respectively only one element at each edge, even if there are more than one with the same value!)

"""

def sum_array(arr):
    if not arr or len(arr) <= 2:
        return 0
    else:
        arr.sort()
        return sum(arr[1:-1])