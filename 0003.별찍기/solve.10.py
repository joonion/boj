def rect(n, row, col, pattern):
    if n == 3:
        for i in range(row, row + 3):
            for j in range(col, col + 3):
                pattern[i][j] = 
                
def solve(n):
    pattern = [" " * N for _ in range(N)]
    rect(n, 0, 0, pattern)
    for i in range(N):
        print(pattern[i])        

N = int(input())
solve(N)