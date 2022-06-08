T = int(input())
for _ in range(T):
    n, s = input().split()
    S = ""
    n = int(n)
    for i in range(len(s)):
        S += s[i] * n
    print(S)