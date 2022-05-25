def part(n, srow, scol, row, col):
    m = n // 2
    if row < srow + m and col < scol + m:
        return 1
    elif row < srow + m and col >= scol + m:
        return 2
    elif row >= srow + m and col < scol + m:
        return 3
    else: # row >= srow + m and col >= scol + m:
        return 4

def fill(where, srow, scol, floor):
    global tile
    if where != 1:
        floor[srow][scol] = tile
    if where != 2:
        floor[srow][scol + 1] = tile
    if where != 3:
        floor[srow + 1][scol] = tile
    if where != 4:
        floor[srow + 1][scol + 1] = tile
    tile += 1

def tromino(n, srow, scol, row, col, floor):
    where = part(n, srow, scol, row, col)
    if n == 2:
        fill(where, srow, scol, floor)
    else:
        m = n // 2
        fill(where, srow + m - 1, scol + m - 1, floor)
        (nrow, ncol) = (row, col) if where == 1 else (srow + m - 1, scol + m - 1)
        tromino(m, srow, scol, nrow, ncol, floor)
        (nrow, ncol) = (row, col) if where == 2 else (srow + m - 1, scol + m)
        tromino(m, srow, scol + m, nrow, ncol, floor)
        (nrow, ncol) = (row, col) if where == 3 else (srow + m, scol + m - 1)
        tromino(m, srow + m, scol, nrow, ncol, floor)
        (nrow, ncol) = (row, col) if where == 4 else (srow + m, scol + m)
        tromino(m, srow + m, scol + m, nrow, ncol, floor)

def solve(n, row, col):
    floor = [[-1] * (n + 1) for _ in range(n + 1)]
    tromino(n, 1, 1, row, col, floor)
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            print(floor[i][j], end = " ")
        print()

K = int(input())
x, y = map(int, input().split())
n = 2**K
tile = 1
solve(n, n - y + 1, x)
