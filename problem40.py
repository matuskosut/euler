from time import time

start = time()

global arr
arr = []

def walk(num, i):
    for a in str(num):
        i += 1
        if (i in [1, 10, 100, 1000, 10000, 100000, 1000000]):
            arr.append(int(a))
    return i

i = 0
iter = 1
while (i <= 1000000):
    i = walk(iter, i)
    iter += 1

print "Product: %d" % reduce(lambda x,y: x*y, arr)
print "Time: {0} secs".format(time()-start)