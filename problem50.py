from time import time
start = time()

primes = set()
cumsum = [0]
roof = 1000000

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

cs = 0
for i in xrange(0,roof):
    if is_prime(i):
        cs += i
        primes.add(i)
        cumsum.append(cs)

print "Init: {0} secs".format(time()-start)

def check(a, b, cumsum, primes, roof):
    res = cumsum[b] - cumsum[a]
    cnt = b - a
    if res > roof:
        return (0, 0)
    if res in primes:
        return (res, cnt)
    else:
        return (0, 0)

mxm = (0, 0)

for i in xrange(0, len(cumsum)):
    for j in xrange(i + 50, len(cumsum)/100):
        res = check(i, j, cumsum, primes, roof)
        if (res[1] > mxm[1]):
            mxm = res

print mxm[0]

print "Time: {0} secs".format(time()-start)