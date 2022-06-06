import sys
input = sys.stdin.readline

def nearest(length, n, m, A):
    

def solve(n, m, k, A):
    length = [[INF] * m for _ in range(n)]
    length[0][0] = -1
    for _ in range(n * m - 1):
        ui, uj = nearest(length, n, m, A)
        for vi in range(n):
            for vj in range(m):
                if length[ui][uj] + weight(ui, uv, vi, vj) < length[vi][vj]:
                    length[vi][vj] = length[ui][uj] + weight(ui, uj, vi, vj)
    return length[n - 1][m - 1] < 
    
n, m, k = map(int, input().split())
A = [input.strip() for _ in range(n)]
INF = 4 * n * m
print("Yes" if solve(n, m, k, A) else "No")
