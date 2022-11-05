N = int(input())
for i in range(N):
    S = input().upper()
    print("Yes" if S == S[::-1] else "No")