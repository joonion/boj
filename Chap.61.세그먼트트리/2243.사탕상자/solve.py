import sys
input = sys.stdin.readline

def update(v, l, r, pos, val, T):
    if l == r:
        T[v] += val
    else:
        m = (l + r) // 2
        if pos <= m:
            update(2*v, l, m, pos, val, T)
        else:
            update(2*v+1, m+1, r, pos, val, T)
        T[v] = T[2*v] + T[2*v+1]

def query(v, l, r, k, T):
    if l == r:
        return l
    else:
        m = (l + r) // 2
        if k <= T[2*v]:
            return query(2*v, l, m, k, T)
        else:
            return query(2*v+1, m+1, r, k-T[2*v], T)

n = int(input())
MAX = 1000000
T = [0] * (4*MAX+1)
for _ in range(n):
    num = list(map(int, input().split()))
    if num[0] == 1:
        candy = query(1, 1, MAX, num[1], T)
        print(candy)
        update(1, 1, MAX, candy, -1, T)
    else:
        update(1, 1, MAX, num[1], num[2], T)
