"""
Simple, remove the spaces from the string, then return the resultant string.
"""
def no_space(x):

  k = []

  for i in x:
    j = i.replace(' ','')
    k.append(j)
  
  return ''.join(k)
  