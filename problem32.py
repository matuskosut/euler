def obsah(text):
    ss = set([1,2,3,4,5,6,7,8,9])
    try:
        for i in range(len(text)):
            ss.remove(int(text[i]))
    except:
        return False
    if len(ss) == 0:
        return True
    else:
        return False

def sum(list):
    if len(list) == 0:
        return 0
    a = list.pop()
    return a + sum(list)

vsetko = set()

for i in range(1,100):
    for j in range(100,10000):
        prod = i * j
        compose = str(i) + str(j) + str(prod)
        if obsah(compose):
            vsetko.add(prod)

print sum(vsetko)