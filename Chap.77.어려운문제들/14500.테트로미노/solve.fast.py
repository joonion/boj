import sys
input = sys.stdin.readline

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

def solve():
    n, m = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(n)]
    opt = 0
    for k in range(len(shapes)):
        h = len(shapes[k])
        w = len(shapes[k][0])
        for i in range(n - h + 1):
            for j in range(m - w + 1):
                val = 0
                for r in range(h):
                    for c in range(w):
                        if shapes[k][r][c] == 1:
                            val += A[i + r][j + c]
                opt = max(opt, val)
    print(opt)

solve()
