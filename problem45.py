from time import time
start = time()

def tri(n):
    return n * (n + 1) / 2

def pen(n):
    return n * (3 * n - 1) / 2

def hxa(n):
    return n * (2 * n - 1)

t = []
p = set()
h = set()

for a in xrange(165, 100000):
    p.add(pen(a))

for b in xrange(143, 100000):
    h.add(hxa(b))

for c in xrange(286, 100000):
    num = tri(c)
    if (num in p) & (num in h):
        print num
        break

print "Time: {0} secs".format(time()-start)