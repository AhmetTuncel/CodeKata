def find_even_index(arr):
    
    leftSum = 0
    rightSum = sum(arr)

    for i, j in enumerate(arr):
        rightSum -= j
        if leftSum == rightSum:
            return i
        else:
            leftSum += j
    return -1   