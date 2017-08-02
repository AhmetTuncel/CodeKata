"""
Given two arrays of strings a1 and a2 return a sorted array r in lexicographical order of the strings of a1 which are substrings of strings of a2.
"""
def in_array(array1, array2):
    arry = []
    for i in array1:
        for j in array2:
            if i in j and arry.count(i)<1:
                arry.append(i)
                arry.sort()
    return arry    


