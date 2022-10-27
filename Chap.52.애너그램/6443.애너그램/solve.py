def dfs(i, n, s, A):
    if i == n:
        print(s)
    else:
        for j in range(26):
            if A[j] > 0:
                A[j] -= 1
                dfs(i + 1, n, s + chr(ord('a')+j), A)
                A[j] += 1

def solve(s):
    A = [0] * 26
    for i in range(len(s)):
        A[ord(s[i])-ord('a')] += 1
    dfs(0, len(s), "", A)

N = int(input())
for _ in range(N):
    solve(input())