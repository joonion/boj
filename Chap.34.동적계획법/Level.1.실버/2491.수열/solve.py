def solve(n, s):
    maxinc, maxdec = 0, 0
    curinc, curdec = 0, 0
    for i in range(n - 1):
        if s[i] < s[i+1]:
            curinc += 1
            curdec = 0
        elif s[i] > s[i+1]:
            curdec += 1
            curinc = 0
        else:
            curinc += 1
            curdec += 1
        maxinc = max(curinc, maxinc)
        maxdec = max(curdec, maxdec)
    return max(maxinc, maxdec) + 1

N = int(input())
S = list(map(int, input().split()))
print(solve(N, S))