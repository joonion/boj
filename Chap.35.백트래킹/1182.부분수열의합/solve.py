cnt = 0

def solve(i, w, n, s, A):
    global cnt
    if i == n and w == s:
        cnt += 1
    elif i < n:
        solve(i + 1, w + A[i], n, s, A)
        solve(i + 1, w, n, s, A)

n, s = map(int, input().split())
A = list(map(int, input().split()))
A.sort()
solve(0, 0, n, s, A)
print(cnt if s != 0 else cnt - 1)