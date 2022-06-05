import sys
input = sys.stdin.readline

D = "URDL"
imv = [-1, 0, 1, 0]
jmv = [0, 1, 0, -1]

def move(d, t, i, j, L, R):
    x = D.index(d)
    if 1 <= t <= 3: # rotate left
        x = (x - t) % 4
        L = L - t
    elif 4 <= t <= 6: # rotate right
        x = (x + t - 3) % 4
        R = R - t + 3
    return i + imv[x], j + jmv[x], L, R

def promising(i, j, L, R, M):
    return 0 <= i < n and 0 <= j < m and L >= 0 and R >= 0 and M[i][j] == 0
    
def dfs(i, j, L, R, n, m, A, M):
    if i == n - 1 and j == m - 1: return True
    else:
        for t in range(7):
            ni, nj, nL, nR = move(A[i][j], t, i, j, L, R)
            if promising(ni, nj, nL, nR, M):
                M[ni][nj] = 1
                if dfs(ni, nj, nL, nR, n, m, A, M):
                    return True
                M[ni][nj] = 0
        return False

n, m, k = map(int, input().split())
A = [input().strip() for _ in range(n)]
M = [[0] * m for _ in range(n)]
M[0][0] = 1
print("Yes" if dfs(0, 0, k, k, n, m, A, M) else "No")