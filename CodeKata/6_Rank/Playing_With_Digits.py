def dig_pow(n, p):
      
    arr = list(str(n))
    b = 0
    for i in arr:
        
        a = int(i) ** p
        b = b + a 
        p = p + 1

    if b % n == 0:
        return int(b/n)
    else:
        return -1    