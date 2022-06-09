def part(i, j, n, r, c):
    m = n // 2
    if r < i + m:
        if c < j + m: return 0
        else: return 1
    else:
        if c < j + m: return 2
        else: return 3
        
def solve(i, j, n, r, c):
    if n == 1:
        return 0
    else:
        m = n // 2
        where = part(i, j, n, r, c)
        if where == 0:
            return solve(i, j, m, r, c)
        elif where == 1:
            return 1 * m * m + solve(i, j + m, m, r, c)
        elif where == 2:
            return 2 * m * m + solve(i + m, j, m, r, c)
        elif where == 3:
            return 3 * m * m + solve(i + m, j + m, m, r, c)
    
n, r, c = map(int, input().split())
print(solve(0, 0, 2**n, r, c))