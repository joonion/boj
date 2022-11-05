def solve(s):
    for i in range(len(s)):
        if s[i:] == s[i:][::-1]:
            return (len(s) - i) + 2*i

S = input()
print(solve(S))