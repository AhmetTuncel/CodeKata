"""
x Simple, given a string of words, return the length of the shortest word(s).

String will never be empty and you do not need to account for different data types.

"""


def find_short(s):
    slst = s.split()
    shrtl = len(slst[0])
    for i in slst:
        if len(i) < shrtl:
            shrtl = len(i)
    return shrtl
 



print(find_short("bitcoin take over the world maybe who knows perhaps"))