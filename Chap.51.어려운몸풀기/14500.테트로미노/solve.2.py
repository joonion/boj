shapes = [[[1, 1], [1, 1]],
          [[1, 1, 1, 1]],
          [[1], [1], [1], [1]],
          [[1, 1, 0], [0, 1, 1]],
          [[0, 1, 1], [1, 1, 0]],
          [[1, 0], [1, 1], [0, 1]],
          [[0, 1], [1, 1], [1, 0]],
          [[1, 1, 1], [0, 1, 0]],
          [[0, 1, 0], [1, 1, 1]],
          [[1, 0], [1, 1], [1, 0]],
          [[0, 1], [1, 1], [0, 1]],
          [[1, 1, 1], [0, 0, 1]],
          [[0, 0, 1], [1, 1, 1]],
          [[1, 1, 1], [1, 0, 0]],
          [[1, 0, 0], [1, 1, 1]],
          [[1, 1], [1, 0], [1, 0]],
          [[1, 1], [0, 1], [0, 1]],
          [[1, 0], [1, 0], [1, 1]],
          [[0, 1], [0, 1], [1, 1]]]

import sys
input = sys.stdin.readline

def place(shape, i, j, A):
    val = 0
    for r in range(len(shape)):
        for c in range(len(shape[0])):
            if shape[r][c] == 1:
                val += A[i + r][j + c]
    return val

def maxwith(shape, n, m, A):
    maxval = 0
    for i in range(n - len(shape) + 1):
        for j in range(m - len(shape[0]) + 1):
            maxval = max(maxval, place(shape, i, j, A))
    return maxval

def solve(n, m, A):
    opt = 0
    for k in range(len(shapes)):
        opt = max(opt, maxwith(shapes[k], n, m, A))
    return opt

N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
answer = solve(N, M, A)
print(answer)
