def solve(s):
    stack = []
    cnt = 0
    for i in range(len(s)):
        if s[i] == "*":
            cnt = -cnt
        elif s[i] == "(":
            stack.append(s[i])
            if cnt >= 0: cnt += 1
        else:
            stack.pop()
            if cnt >= 0: cnt -= 1
    return -cnt

S = input()
print(solve(S))