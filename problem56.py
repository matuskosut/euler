from time import time
start = time()

def dsum(n):
    ret = 0
    while n > 0:
        ret += n % 10
        n /= 10
    return ret

print max([dsum(a ** b) for a in xrange(1,100) for b in xrange(1,100)])


print "Time: {0} secs".format(time()-start)