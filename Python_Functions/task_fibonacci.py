def fibs(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a+b
    return a


ab = [fibs(n) for n in range(1000)]
# print(fibs(10000))

print(ab)
