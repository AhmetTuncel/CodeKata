"""
Return the middle character of the word. If the word's length is odd, return the middle character. If the word's length is even, return the middle 2 characters.
"""
def get_middle(s):
    x = len(s)
    if(x%2==0):
        return s[x/2-1:x/2+1]
    else:
        return s[x/2]


