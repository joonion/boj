n, p = map(int, input().split())
for k in range(p, 1000000001, p):
    f = 1
    for m in range(2, p):
        if k % m == 0:
            f = 0
            break
    n -= f
    if n == 0:
        exit(print(k))
print(0)
    