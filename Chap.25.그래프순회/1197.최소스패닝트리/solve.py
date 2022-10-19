import sys
input = sys.stdin.readline
from heapq import heappush, heappop

def find(a):
    global disjointset
    if a != disjointset[a]:
        disjointset[a] = find(disjointset[a])
    return disjointset[a]

def union(a, b):
    global disjointset
    if a < b:
        disjointset[b] = a
    else:
        disjointset[a] = b
        
def kruskal(n, E):
    F = []
    while len(F) < n - 1:
        e = heappop(E)[1]
        p = find(e[0])
        q = find(e[1])
        if p != q:
            union(p, q)
            F.append(e)
    return F

n, m = map(int, input().split())
E = []
for _ in range(m):
    u, v, w = map(int, input().split())
    heappush(E, (w, (u, v, w)))
disjointset = [i for i in range(n + 1)]
F = kruskal(n, E)
s = 0
for i in range(len(F)):
    s += F[i][2]
print(s)
    
