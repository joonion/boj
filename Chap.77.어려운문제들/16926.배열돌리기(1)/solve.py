def get_chain(k, n, m, A):
    chain = []
    for i in range(k, n):
        chain.append(A[i][k])
    for j in range(k, m):
        chain.append(A[n][j])
    for i in range(n, k, -1):
        chain.append(A[i][m])
    for j in range(m, k, -1):
        chain.append(A[k][j])
    return chain
    
def put_chain(k, n, m, A, chain):
    t = 0
    for i in range(k, n):
        A[i][k] = chain[t]
        t += 1
    for j in range(k, m):
        A[n][j] = chain[t]
        t += 1
    for i in range(n, k, -1):
        A[i][m] = chain[t]
        t += 1
    for j in range(m, k, -1):
        A[k][j] = chain[t]
        t += 1
            
def rotate(k, N, M, R, A):
    chain = get_chain(k, N-1-k, M-1-k, A)
    index = len(chain) - R % len(chain)
    rotated = chain[index:] + chain[:index]
    put_chain(k, N-1-k, M-1-k, A, rotated)
        
def solve(N, M, R, A):
    for k in range(min(N, M) // 2):
        rotate(k, N, M, R, A)

import sys
input = sys.stdin.readline
N, M, R = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
solve(N, M, R, A)
for i in range(N):
    print(" ".join(map(str, A[i])))
    