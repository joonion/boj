def solve(n, q):
    q.sort()
    for k in range(n):
        if n - k <= q[k]:
            return n - k
    return 0

n = int(input())
q = list(map(int, input().split()))
answer = solve(n, q)
print(answer)