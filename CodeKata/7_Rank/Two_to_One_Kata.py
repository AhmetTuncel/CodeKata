"""
Take 2 strings s1 and s2 including only letters from ato z. Return a new sorted string, the longest possible, containing distinct letters,

each taken only once - coming from s1 or s2. #Examples: ``` a = "xyaabbbccccdefww" b = "xxxxyyyyabklmopq" longest(a, b) -> "abcdefklmopqwxy"
a = "abcdefghijklmnopqrstuvwxyz" longest(a, a) -> "abcdefghijklmnopqrstuvwxyz" ```
"""
from collections import OrderedDict

def longest(s1, s2):

    mergestring = s1 +s2
    od = OrderedDict.fromkeys(mergestring).keys()            
    joinorderedstring = "".join(sorted(od))
    return joinorderedstring



print(longest("aretheyhere", "yestheyarehere"))

