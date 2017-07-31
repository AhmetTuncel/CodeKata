"""
Your goal in this kata is to implement an difference function, which subtracts one list from another.
It should remove all values from list a, which are present in list b.
"""
def array_diff(a, b):
    newarr = []
    for i in a:
        if i not in b:
            newarr.append(i)
    return newarr

print(array_diff([1,2],[1]))