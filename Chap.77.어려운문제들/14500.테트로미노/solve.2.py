shapes = [
    [[1, 1], [1, 1]], # 네모
    [[1, 1, 1, 1]], # 길쭉이 1
    [[1, 1, 1], [0, 1, 0]], # T-모양 1
    [[1, 1, 0], [0, 1, 1]], # 꺽은 모양 1
    [[1, 1, 1], [0, 0, 1]], # L-모양 1
]

def place(shape, i, j, A):
    val = 0
    for r in range(len(shape)):
        for c in range(len(shape[0])):
            val += shape[r][c] * A[i + r][j + c]
    return val

def flip(s):
    h, w = len(s), len(s[0])
    shape = [[0] * w for _ in range(h)]
    for i in range(h):
        for j in range(w):
            shape[i][w - 1 - j] = s[i][j]
    return shape

def rotate(s):
    h, w = len(s[0]), len(s)
    shape = [[0] * w for _ in range(h)]
    for i in range(h):
        for j in range(w):
            shape[i][j] = s[w - 1 - j][i]
    return shape

def maximize(shape, n, m, A):
    opt = 0
    for i in range(n - len(shape) + 1):
        for j in range(m - len(shape[0]) + 1):
            opt = max(opt, place(shape, i, j, A))
    return opt

def get_shape(shape, k):
    if k == 0: return shapes[0]
    elif k == 1: return shapes[1]
    elif k == 3: return shapes[2]
    elif k == 7: return shapes[3]
    elif k == 11: return shapes[4]
    elif k in [9, 15]: return flip(shape)
    else: return rotate(shape)

def solve(n, m, A):
    opt = 0
    shape = []
    for k in range(19):
        shape = get_shape(shape, k)
        opt = max(opt, maximize(shape, n, m, A))
    return opt
    
n, m = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(n)]
print(solve(n, m, A))