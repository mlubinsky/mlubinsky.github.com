def IntToByte(x):
    n = "" if x>0 else "0"
    while x > 0:
        y = str(x % 2)
        n = y + n
        x = int(x / 2)
    #print (n)
    return n
 
for x in xrange(0,10):
     print x, IntToByte(x)
 
    