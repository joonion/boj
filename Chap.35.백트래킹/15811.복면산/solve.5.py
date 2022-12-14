def f(w, a, c):
    n = 0
    for i in range(len(w)):
        n = n * 10 + c[a[ord(w[i]) - ord('A')]]
    return n
        
def dfs(i, n, a, b, c, w):
    if i > n:
        if f(w[0],a,c) + f(w[1],a,c) == f(w[2],a,c):
            exit(print("YES"))
    else:
        for j in range(10):
            if b[j] != 0: continue
            c[i] = j
            b[j] = i
            dfs(i + 1, n, a, b, c, w)
            b[j] = 0

w = input().split()
n, a, b, c = 0, [0] * 26, [0] * 10, [0] * 11
for i, j in enumerate(set(w[0]+w[1]+w[2]), start = 1):
    a[ord(j) - ord('A')] = i
    n += 1
if n <= 10: dfs(1, n, a, b, c, w)
print("NO")