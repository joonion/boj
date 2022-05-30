def sierpinski(n, T, row, col):
    if n == 3:
        T[row][col] = 1
        T[row + 1][col - 1] = T[row + 1][col + 1] = 1
        for i in range(-2, 3):
            T[row + 2][col + i] = 1
    else:
        m = n // 2
        sierpinski(m, T, row, col)
        sierpinski(m, T, row + m, col - m)
        sierpinski(m, T, row + m, col + m)
    
def solve(n):
    T = [[0] * (2*n - 1) for _ in range(n)]
    sierpinski(n, T, 0, n - 1)
    s = ""
    for i in range(N):
        for j in range(2*N - 1):
            s += "*" if T[i][j] == 1 else " "
        s += "\n"
    print(s)

N = int(input())
solve(N)

