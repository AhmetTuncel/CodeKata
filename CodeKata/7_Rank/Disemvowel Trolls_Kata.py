"""

Write a function that takes a string and return a new string with all vowels removed.

For example, the string "This website is for losers LOL!" would become "Ths wbst s fr lsrs LL!".
"""

def disemvowel(string):
    vowel_character = ["a", "A", "e", "E", "o", "O", "i", "I", "u", "U"]
    stringreturn = ""
    i = 0
    n = len(string)

    while i < n:
        if not string[i] in vowel_character:
            stringreturn += string[i]
        i += 1
    return stringreturn

#print (disemvowel("This website is for losers LOL!"))
