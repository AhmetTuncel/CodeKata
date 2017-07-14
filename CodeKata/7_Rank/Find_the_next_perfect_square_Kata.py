"""
Complete the findNextSquare method that finds the next integral perfect square after the one passed as a parameter. Recall that an integral perfect square is an integer n such that sqrt(n) is also an integer.

If the parameter is itself not a perfect square, than -1 should be returned. You may assume the parameter is positive.
"""
def find_next_square(sq):
    r = sq ** 0.5
    if r.is_integer():
        return (r + 1)**2
    return -1



#print (accum("ZpglnRxqenU"))
