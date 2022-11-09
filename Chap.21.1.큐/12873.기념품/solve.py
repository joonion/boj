def solve(n):
    q = [i for i in range(1, n + 1)]
    i = 0; t = 1
    while len(q) > 1:
        i = (i + t**3 - 1) % len(q)
        q.pop(i)
        t += 1
    return q[0]

N = int(input())
print(solve(N))