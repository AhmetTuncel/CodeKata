"""
Return the digits of this number within an array in reverse order.

"""
def digitize(n):
    return [int(i) for i in str(n)[::-1]]