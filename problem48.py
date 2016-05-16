from time import time
start = time()

sum = 0
for i in range(1,1000):
    sum += i ** i


print str(sum)[-10:]

print "Time: {0} secs".format(time()-start)