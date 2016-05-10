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
        ret = "\t"*self.level+repr(self.value)+"\n"
        for child in self.children:
            ret += child.__repr__()
        return ret



def generate(root, depth):
    if root.level == depth:
        return []
    for i in range(depth, 0, -1):
        if i not in root.used:
            addused = root.used + [i]
            num = root.value * 10 + i
            add = Leaf(num, root.level + 1, addused, [])
            add = generate(add, depth)
            if add != []:
                root.children += [add]
    return root


def is_prime(n):    
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

def traverse(root):
    res = False
    if root.children:
        for i in root.children:
            res |= traverse(i)
            if res:
                break
    elif is_prime(root.value):
        print "Maximum pandigital prime is: %d" % root.value
        return True
    return False | res

for x in range (9, 1, -1):
    brk = False
    for y in range(x, 0, -1):
        print "Generate depth: %d rootval: %d" % (x, y)
        panroot = Leaf(y, 0, [y], [])
        generate(panroot, x)
        if traverse(panroot):
            brk = True
            break
    if brk:
        break


print "Time: {0} secs".format(time()-start)