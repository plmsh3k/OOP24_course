def factorials(n):
    d = {}
    for i in range(1,n+1):
        d[i] = 1
        for j in range(1,i+1):
            d[i] *= j
    return d

print(factorials(4))

