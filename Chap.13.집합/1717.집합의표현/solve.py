def find(a):
    global disjointset
    if a != disjointset[a]:
        disjointset[a] = find(disjointset[a])
    return disjointset[a]

def union(a, b):
    global disjointset
    a, b = find(a), find(b)
    if a < b:
        disjointset[b] = a
    else:
        disjointset[a] = b

"""
이 문제는 sys.stdin.readline 함수를 쓰지 않으면
시간초과가 걸리는 문제였음
"""        
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, m = map(int, input().split())
disjointset = [i for i in range(n + 1)] # initialize disjoint set
for _ in range(m):
    op, a, b = map(int, input().split())
    if op == 0:
        union(a, b)
    elif op == 1:
        print("YES" if find(a) == find(b) else "NO")
        