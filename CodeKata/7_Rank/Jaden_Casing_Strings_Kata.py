"""
Convert strings to capitalized originally typed them.

"""
def toJadenCase(string):
    x = " ".join([i.capitalize() for i in string.split(" ")])    
    return x
