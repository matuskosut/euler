from time import time
start = time()

howmuch = 4
primes = set()
parr = []
roof = 200000
hook = roof / 10

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

for i in xrange(2,roof/10):
    if is_prime(i):
        primes.add(i)
        parr.append(i)

print "Init: {0} secs".format(time()-start)

def check(n, c, primes, parr, roof):
    for j in xrange(n, n + c):
        pom = j
        count = 0
        if pom in primes:
            return j + 1
        for i in parr:
            if i > pom // 2:
                if pom in primes:
                    count += 1
                break
            if pom % i == 0:
                count += 1
            if count > c:
                break
            while pom % i == 0:
                pom /= i
        if count != c:
            return j + 1
    print "<"
    print "n = %d" % n
    return n + roof

i = 1
while(i < roof):
    if ((i + 1) % hook == 0):
        print '%',
    i = check(i, howmuch, primes, parr, roof)

print "Time: {0} secs".format(time()-start)