rectangle = [[[1, 1], [1, 1]]]

straight = [[[1, 1, 1, 1]], 
            [[1], [1], [1], [1]]]

skewed = [[[1, 1, 0], [0, 1, 1]], 
          [[0, 1, 1], [1, 1, 0]], 
          [[1, 0], [1, 1], [0, 1]], 
          [[0, 1], [1, 1], [1, 0]]]

tshape = [[[1, 1, 1], [0, 1, 0]],
          [[0, 1, 0], [1, 1, 1]],
          [[1, 0], [1, 1], [1, 0]],
          [[0, 1], [1, 1], [0, 1]]]

lshape = [[[1, 1, 1], [0, 0, 1]], 
          [[0, 0, 1], [1, 1, 1]], 
          [[1, 1, 1], [1, 0, 0]], 
          [[1, 0, 0], [1, 1, 1]], 
          [[1, 1], [1, 0], [1, 0]], 
          [[1, 1], [0, 1], [0, 1]], 
          [[1, 0], [1, 0], [1, 1]], 
          [[0, 1], [0, 1], [1, 1]]]

shapes = [rectangle, straight, skewed, tshape, lshape]

def place(tile, i, j, A):
    value = 0
    for r in range(len(tile)):
        for c in range(len(tile[0])):
            if tile[r][c] == 1:
                value += A[i + r][j + c]
    return value

def maxwith(shape, n, m, A):
    maxval = 0
    for k in range(len(shape)):
        height, width = len(shape[k]), len(shape[k][0])
        for i in range(n - height + 1):
            for j in range(m - width + 1):
                maxval = max(maxval, place(shape[k], i, j, A))
    return maxval

def solve(n, m, A):
    opt = 0
    for k in range(len(shapes)):
        opt = max(opt, maxwith(shapes[k], n, m, A))
    return opt

import sys
input = sys.stdin.readline
                
N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
answer = solve(N, M, A)
print(answer)
