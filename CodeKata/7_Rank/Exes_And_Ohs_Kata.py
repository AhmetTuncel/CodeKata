"""
Check to see if a string has the same amount of 'x's and 'o's. The method must return a boolean and be case insensitive. The string can contains any char.

Examples input/output:

XO("ooxx") => true
XO("xooxx") => false
XO("ooxXm") => true
XO("zpzpzpp") => true // when no 'x' and 'o' is present should return true
XO("zzoo") => false

"""
def xo(s):
    
  xnumber = 0
  ohnumber = 0

  for i in s.lower():
    if i == 'x':
      xnumber += 1
    elif i == 'o':
      ohnumber += 1

  return xnumber == ohnumber


#print (xo("ooxx"))  