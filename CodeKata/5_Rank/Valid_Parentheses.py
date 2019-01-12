import re 


def valid_parentheses(string):

    string = re.sub("[a-z]", "",string)    
    dicPrnt = {"[": "]", "{": "}", "(": ")"}
    
    list = []
    for i in string:
        if i in dicPrnt:

            list.append(dicPrnt[i])
        elif not list or i != list.pop():
            return False
    return not list

# print(valid_parentheses("  ("))
# print(valid_parentheses(")test"))
# print(valid_parentheses("hi())("))
# print(valid_parentheses("hi(hi)()"))
# print(valid_parentheses(""))