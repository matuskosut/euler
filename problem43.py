from time import time
import sys

start = time()

class Leaf:
    
    def __init__(self, value, level, used = [], children = []):
        self.value = value
        self.level = level
        self.used = used
        self.children = children
        
    def __repr__(self):
        ret = " "*self.level+repr(self.value)+"\n"
        for child in self.children:
            ret += child.__repr__()
        return ret

def generate(root, depth):
    if root.level == depth:
        return []
    for i in range(depth-1, -1, -1):
        if i not in root.used:
            addused = root.used + [i]
            num = root.value + str(i)
            add = Leaf(num, root.level + 1, addused, [])
            add = generate(add, depth)
            if add != []:
                root.children += [add]
    return root

def check(pan):
    deli = [0,2,3,5,7,11,13,17]
    for i in xrange(7, 0, -1):
        if (int(pan[i:i+3]) % deli[i] != 0):
            return False
    return True

suma = 0

def traverse(root, suma):
    if root.children:
        for i in root.children:
            suma += traverse(i, suma)
    elif check(root.value):
        print "Adding: %s" % root.value
        suma += int(root.value)
    return suma

depth = 10
for i in range(1, depth):
    print "Level: %d" % i
    a = Leaf(str(i),0,[i],[])
    a = generate(a, depth)
    suma += traverse(a, suma)
    
print "Sum of pandigitals is: %d" % suma

print "Time: {0} secs".format(time()-start)