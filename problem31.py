count = 0
for a in range(0, 201, 200):
    for b in range(a, 201, 100):
        for c in range(b, 201, 50):
            for d in range(c, 201, 20):
                for e in range(d, 201, 10):
                    for f in range(e, 201, 5):
                        for g in range(f, 201, 2):
                            count = count + 1
print count