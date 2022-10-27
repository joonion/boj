def solve(i, w, n, s, A):
    global cnt
    if i < n:
        if w + A[i] == s:
            cnt += 1
        solve(i + 1, w + A[i], n, s, A)
        solve(i + 1, w, n, s, A)

n, s = map(int, input().split())
A = list(map(int, input().split()))
A.sort()
cnt = 0
solve(0, 0, n, s, A)
print(cnt)