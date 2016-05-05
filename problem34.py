import math

def getfact(num):
    if (num < 1):
        return 0
    if (num < 10):
        return math.factorial(num)
    else:
        return math.factorial(num % 10) + getfact(num / 10)
    
res = 0
for i in range(3,1000000):
    if i == getfact(i):
        res += i
    
print res