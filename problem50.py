from time import time
start = time()
roof = 1000000

def primes(n):
    sieve = [True] * n
    for i in xrange(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)/(2*i)+1)
    return [2] + [i for i in xrange(3,n,2) if sieve[i]]

primes = primes(1000000)
cumsum = [0]

suma = 0
for p in primes:
    suma += p
    cumsum.append(suma)
    
primes = set(primes)

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