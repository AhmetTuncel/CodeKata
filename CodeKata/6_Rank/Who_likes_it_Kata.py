"""
You probably know the "like" system from Facebook and other pages. People can "like" blog posts, pictures or other items. We want to create the text that should be displayed next to such an item.

Implement a function likes :: [String] -> String, which must take in input array, containing the names of people who like an item. It must return the display text as shown in the 
"""
def likes(names):
    l = len(names)
    if l == 0:
        return "no one likes this"
    elif l == 1:
        return "%s likes this" %names[0]
    elif l == 2:
        return "%s and %s like this" %(names[0], names[1])
    elif l == 3:
        return "%s, %s and %s like this" %(names[0], names[1], names[2])
    else:
        return "%s, %s and %d others like this" %(names[0], names[1], l-2)


#print (accum("ZpglnRxqenU"))
