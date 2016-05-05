from time import time

start = time()
primes ={}

def isPalindrome(num):
    string = str(num)
    return string == string[::-1]

def dec_to_bin(x):
    return int(bin(x)[2:])

res = 0

for i in range(1000000):
    if isPalindrome(i) & isPalindrome(dec_to_bin(i)):
        res += i

print res

print "Time: {0} secs".format(time()-start)