N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]
F = {i:set() for i in range(N)}
for j in range(5):
    T = {k:[] for k in range(1, 10)}
    for i in range(N):
        T[A[i][j]].append(i)
    for i in range(N):
        for t in T[A[i][j]]:
            F[i].add(t)
print(sorted(F.items(), key = lambda x: (-len(x[1]), x[0]))[0][0] + 1)
