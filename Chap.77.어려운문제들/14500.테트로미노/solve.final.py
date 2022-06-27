import sys
input = sys.stdin.readline

def rotate(s):
    h, w = len(s[0]), len(s)
    shape = [[0] * w for _ in range(h)]
    for i in range(h):
        for j in range(w):
            shape[i][j] = s[w - 1 - j][i]
    return shape    

def shape(k, s):
    if k == 0:    s = [[1, 1], [1, 1]] # rect
    elif k == 1:  s = [[1, 1, 1, 1]] # straight
    elif k == 3:  s = [[1, 1, 1], [0, 1, 0]] # T-shape
    elif k == 7:  s = [[1, 1, 0], [0, 1, 1]] # skewed - 1
    elif k == 9:  s = [[0, 1, 1], [1, 1, 0]] # skewed - 2
    elif k == 11: s = [[1, 0, 0], [1, 1, 1]] # L - 1
    elif k == 15: s = [[1, 1, 1], [1, 0, 0]] # L - 2
    else: s = rotate(s)
    return len(s), len(s[0]), s

def value(i, j, h, w, s, A):
    val = 0
    for r in range(h):
        for c in range(w):
            if s[r][c] == 1:
                val += A[i + r][j + c]
    return val

def solve(n, m, A):
    opt, s = 0, []
    for k in range(19):
        h, w, s = shape(k, s)
        for i in range(n - h + 1):
            for j in range(m - w + 1):
                opt = max(opt, value(i, j, h, w, s, A))
    return opt    
    
n, m = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(n)]
print(solve(n, m, A))
