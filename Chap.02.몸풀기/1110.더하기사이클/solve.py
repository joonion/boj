def solve(n):
    m = n
    count = 1
    while (True):
        s = sum(map(int, list(str(m))))
        m = (m % 10) * 10 + (s % 10)
        if m == n:
            break
        count += 1
    return count

N = int(input())
answer = solve(N)
print(answer)