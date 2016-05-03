# The only reason over the choice of techniques used here is learning them. 
import sys
from time import time
sys.setrecursionlimit(1500)
start = time()

def getlength(a, b, c, d, e):
    rem = a % b    
    if (rem in c) | (d > e):
        return d
    else:
        c.append(rem)
        return getlength(rem*10, b, c, d + 1, e)

arr = {x+1: getlength(1, x+1, [0], 0, x+1) for x in range(1000)}

print "d = %d" % max(arr, key=arr.get)
print "Time: {0} secs".format(time()-start)