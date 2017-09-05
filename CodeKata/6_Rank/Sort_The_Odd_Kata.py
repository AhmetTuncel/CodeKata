"""
You have an array of numbers.
Your task is to sort ascending odd numbers but even numbers must be on their places.

Zero isn't an odd number and you don't need to move it. If you have an empty array, you need to return it.
"""
def sort_array(source_array):
    oddarry = []
    evenarry = []

    for i,j in enumerate(source_array):
        if j%2 != 0:
            oddarry.append(j)
        else:
            evenarry.append((i,j))
    oddarry.sort()

    for i,j in evenarry:
        oddarry.insert(i,j)
    return oddarry