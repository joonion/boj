def check(i, j):
    black, white = 0, 0
    for r in range(8):
        for c in range(8):
            white += (BOARD[i + r][j + c] != WHITE[r][c])
            black += (BOARD[i + r][j + c] != BLACK[r][c])
    return min(white, black)

n, m = map(int, input().split())
A = [input() for _ in range(n)]
BOARD = [[0] * m for _ in range(n)]
for i in range(n):
    for j in range(m):
        BOARD[i][j] = "BW".index(A[i][j])

BLACK = [[(i + j) % 2 for j in range(8)] for i in range(8)]
WHITE = [[(i + j + 1) % 2 for j in range(8)] for i in range(8)]

opt = 50 * 50 + 1
for i in range(n - 8 + 1):
    for j in range(m - 8 + 1):
        opt = min(opt, check(i, j))
print(opt)
