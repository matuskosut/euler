from time import time

start = time()
primes ={}

def getprime(n):
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

def prime(num):
    try:
        return primes[num]
    except:
        pom = getprime(num)
        primes[num] = pom
        return pom
    
def left(num):
    for i in str(num):
        if not prime(num):
            return False
        num /= 10
    return True

def right(num):
    a = 0
    b = 1
    for i in str(num):
        a += b * (num % 10)
        num = num / 10
        if not prime(a):
            return False
        b *= 10
    return True

sum = 0
pom = 10
for i in range(11):
    while (True):
        pom += 1
        if left(pom) & right(pom):
            print pom
            sum += pom
            break
            
print "----"
print sum
    
print "Time: {0} secs".format(time()-start)