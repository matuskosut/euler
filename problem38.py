from time import time

start = time()

def isPandigital(text):
    ss = set(range(1,10))
    try:
        for i in range(len(text)):
            ss.remove(int(text[i]))
    except:
        return False
    if len(ss) == 0:
        return True
    else:
        return False

def conprod(num):
    string = ""
    for i in range(1,10):
        string += str(num * i)
        if len(string) > 8:
            break
    if (len(string) == 9) & isPandigital(string):
        return int(string)
    else:
        return False

ss = set()

for i in range(10000):
    var = conprod(i)
    if var != False:
        ss.add(var)
    
print max(ss)

#print conprod(192)
print "Time: {0} secs".format(time()-start)