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

def rotate(num):
    length = len(str(num))
    for i in range(length):
        if prime(num):
            frst =(num % 10) * 10 ** (length - 1)
            last = num/10
            num = frst + last
        else:
            return False
    return True

sum = 1
for i in range(3,1000000,2):
    if rotate(i):
        sum += 1

print sum
print "Time: {0} secs".format(time()-start)