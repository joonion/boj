def solve(s):
    stack = []
    cnt = 0
    for i in range(len(s)):
        if s[i] == '(':
            stack.append(s[i])
        elif s[i] == ')' and len(stack) > 0:
            stack.pop()
        else:
            cnt += 1
    return cnt + len(stack)
            
S = input()
print(solve(S))