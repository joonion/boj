def solve(s, t):
    if not s:
        print(t)
    else:
        for i in range(len(s)):
            k = s[::]
            k.pop(i)
            solve(k, t + s[i])

for i in range(int(input())):
    print(f"Case # {i+1}:")
    solve(list(input()), "")