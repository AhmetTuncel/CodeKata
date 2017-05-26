"""
Return the number (count) of vowels in the given string.

Consider a, e, i, o, and u as vowels for this Kata.
"""
def getCount(inputStr):
    num_vowels = 0
    vowels = 'aeiou'
    
    for i in vowels:
        num_vowels = num_vowels + 1

    return num_vowels

