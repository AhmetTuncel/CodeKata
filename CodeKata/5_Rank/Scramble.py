from collections import Counter

def scramble(str1, str2):

    a= Counter(str1)
    b = Counter(str2)

   
    return all(b[i] <= a[i] for i in b)
