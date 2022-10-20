def find(a, DS):
    if a != DS[a]:
        DS[a] = find(DS[a], DS)
    return DS[a]

def union(a, b, DS):
    a = find(a, DS)
    b = find(b, DS)
    if a < b:
        DS[b] = a
    else:
        DS[a] = b

def adjacent(i, j, ni, nj, n, m, A):
    if not (0 <= i < n and 0 <= j < m):
        return False
    if not (0 <= ni < n and 0 <= nj < m):
        return False
    if not (A[i][j] == 1 and A[ni][nj] == 1):
        return False
    return True
        
def solve(n, m, A):
    imove = [0, 1, 0, -1]
    jmove = [1, 0, -1, 0]
    DS = [i for i in range(n * m)]
    for i in range(n):
        for j in range(m):
            u = i * m + j
            for k in range(4):
                ni = i + imove[k]
                nj = j + jmove[k]
                v = ni * m + nj
                if adjacent(i, j, ni, nj, n, m, A):
                    union(u, v, DS)
    for i in range(n):
        for j in range(m):
            u = i * m + j
            if A[i][j] == 0: 
                DS[u] = -1
            else:
                find(u, DS)
    count = len(list(set(DS)))
    return  count - 1 if -1 in DS else count
    
import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N, M, K = map(int, input().split())
    A = [[0] * M for _ in range(N)]
    for _ in range(K):
        x, y = map(int, input().split())
        A[x][y] = 1
    answer = solve(N, M, A)
    print(answer)
