from time import time
import string
start = time()
roof = 1000000

def primes(n):
    sieve = [True] * n
    for i in xrange(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)/(2*i)+1)
    return [2] + [i for i in xrange(3,n,2) if sieve[i]]

primes = primes(roof)
isprime = set(primes)

def solve(primes, isprime):
    for p in primes:
        string = str(p)
        strlen = len(string)

        for c in set(string):
            if (len(string.replace(c,"")) != strlen - 3):
                continue

            lst = set()
            for j in "0123456789":
                num = int(string.replace(c, j))
                if ((num in isprime) & (len(str(num)) == strlen)):
                    lst.add(num)
            if len(lst) == 8:
                return min(lst)
    return 0

print "Result is: %d" % solve(primes, isprime)

print "Time: {0} secs".format(time()-start)