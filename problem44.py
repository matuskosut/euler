from time import time
start = time()
# I left this one open,
# it returns n, the sum of pj a pk
# the algorithm is fast enough
# you just have to determine which
# of the variables is the D

def pentagon(n):
    return (n * ((3 * n) - 1)) / 2

def check(ptg, n):
    a = pentagon(n)
    for i in ptg:
        c = a - i
        b = c - i
        if (c in ptg) & (abs(b) in ptg):
            ptg.add(a)
            return True
    ptg.add(a)
    return False

ptgls = set()

for n in range(1,3000):
    if check(ptgls, n):
        print "n = %d" % n
        break

print "Time: {0} secs".format(time()-start)