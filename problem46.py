from time import time
import math
start = time()

def roof(n):
    return int(math.sqrt(n / 2))

def is_prime(n):    
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

def check(n):
    r = roof(n)
    for i in xrange(1, r + 1):
        if is_prime(n - 2 * (i * i)):
            return True
    return False

for x in xrange(33, 10000, 2):
    if not is_prime(x):
        if not check(x):
            print x
            break

print "Time: {0} secs".format(time()-start)