from time import time
start = time()

arr = [1] + [0] * 200

for x in [1, 2, 5, 10, 20, 50, 100, 200]:
    for y in range(x, 201):
        arr[y] += arr[y - x]

print arr[200]
print "Time: {0} secs".format(time() - start)