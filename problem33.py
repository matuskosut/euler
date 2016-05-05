from fractions import gcd

def reduc(num,den):
    a = list(str(num))
    b = list(str(den))
    if (a == []) | (b == []):
        return False
    
    inters = set([x for x in a if x in b])
    if (inters == set(['0'])):
        return False
    
    for i in inters:
        a.remove(i)
        b.remove(i)
    
    if (a == []) | (b == []):
        return False
    
    c = float("".join(a))
    d = float("".join(b))
        
    if (float(den) == 0.0) | (d == 0.0):
        return False
    
    if (float(num)/float(den) == c/d) & (num != c):
        return True
    else:
        return False

denprod = 1
nomprod = 1

for i in range(100):
    for j in range(i+1,100):
        if reduc(i,j):
            nomprod *= i
            denprod *= j
            print "%d / %d" % (i, j)
denprod /= gcd(denprod, nomprod)
print denprod