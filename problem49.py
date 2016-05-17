from time import time
start = time()
roof = 10000

def primes(n):
    sieve = [True] * n
    for i in xrange(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)/(2*i)+1)
    return [2] + [i for i in xrange(3,n,2) if sieve[i]]

primes = primes(roof)
cumsum = [0]

suma = 0
for p in primes:
    suma += p
    cumsum.append(suma)
    
isprime = set(primes)

print "Init: {0} secs".format(time()-start)

def cut(n):
    arr = set()
    while (n > 0):
        res = n % 10
        n /= 10
        arr.add(res) 
    return arr

for p in primes:
    q = p + 3330
    r = q + 3330
    if (r in isprime) & (q in isprime):
        a = cut(q)
        b = cut(r)
        c = cut(p)
        if (a == b) & (b == c):
            print "%d%d%d" % (p, q ,r)
            
print "Time: {0} secs".format(time()-start)