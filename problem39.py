from time import time

start = time()

def is_solution(a,b,c):
    return ((a**2 + b**2) == (c**2))

def count_solutions(p):
    res = 0
    for x in range(1,p/2):
        for y in range(x+1,p/2):
            for z in range(y+1,p/2):
                if ((x + y + z) == p) & is_solution(x, y, z):
                    res += 1
    return res

#print is_solution(20, 48, 52)
#print is_solution(24, 45, 51)
#print is_solution(30, 40, 50)
#print count_solutions(120)

arr = [(x, count_solutions(x)) for x in range(835, 845)]
#print arr
print "p = %d (%d solutions)" % max(arr,key=lambda item:item[1])
print "Time: {0} secs".format(time()-start)
