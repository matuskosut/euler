# The only reason over the choice of techniques used here is learning them. 
# There is always a way to do it more efficiently.
from time import time

start = time()

def prime(n):
    n = abs(int(n))
    
    if n < 2:
        return False
    if n == 2:
        return True
    if not n & 1:
        return False
    for x in range(3, int(n**0.5) + 1, 2):
        if n % x == 0:
            return False
    return True

def c(x, y, depth):
    num = depth**2 + depth * x + y
    if prime(num):
        return c(x, y, depth + 1)
    else:
        return depth
    
arr = [((a-1000)*(b-1000), c(a-1000,b-1000,0)) for a in range(2000) for b in range(2000)]

#print c(-79,1601,0)
#print c(1,41,0)
print "a*b = %d" % max(arr,key=lambda item:item[1])[0]
print "Time: {0} secs".format(time()-start)