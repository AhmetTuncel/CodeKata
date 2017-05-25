"""
How to write function accum:

Examples:

accum("abcd")    # "A-Bb-Ccc-Dddd"
accum("RqaEzty") # "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
accum("cwAt")    # "C-Ww-Aaa-Tttt"

"""
def accum(s):
    x = s[0].capitalize()
    for i in range(1, len(s)):
        x += "-" + (s[i] * (i + 1)).capitalize()
    return x


#print (accum("ZpglnRxqenU"))
