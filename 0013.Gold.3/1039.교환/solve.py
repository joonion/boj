def search(u, m, visiting):
    s = list(u)
    for i in range(m):
        for j in range(i + 1, m):
            s[i], s[j] = s[j], s[i]
            if s[0] != '0': visiting.add(''.join(s))
            s[i], s[j] = s[j], s[i]

def solve(n, m, k):
    visited = {n}
    for _ in range(k):
        visiting = set()
        for u in visited:
            search(u, m, visiting)
        if len(visiting) == 0:
            return -1
        visited = visiting
    return max(map(int, visited))

n, k = input().split()
m = len(n)
print(solve(n, m, int(k)))