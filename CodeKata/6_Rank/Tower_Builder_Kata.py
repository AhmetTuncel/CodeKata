"""
Build Tower by the following given argument:
number of floors (integer and always greater than 0).
"""
def tower_builder(n_floors):
    array = []
    for i in range(n_floors):
        array.append(("*" * (2 * i + 1)).center(2 * n_floors - 1, " "))
    return array

