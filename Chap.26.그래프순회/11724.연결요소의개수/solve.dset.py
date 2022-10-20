def find(a, DS):
    if a != DS[a]:
        DS[a] = find(DS[a], DS)
    return DS[a]

def union(a, b, DS):
    if a < b:
        DS[b] = a
    else:
        DS[a] = b

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
DS = [i for i in range(N + 1)]
for _ in range(M):
    u, v = map(int, input().split())
    p = find(u, DS)
    q = find(v, DS)
    if p != q:
        union(p, q, DS)
for i in range(1, len(DS)):
    find(i, DS)
print(len(set(DS)) - 1)