def solve(s, v):
    stack = []
    for i in range(len(s)):
        if s[i].isalpha():
            stack.append(v[ord(s[i])-65])
        elif s[i] == '+':
            stack.append(stack.pop() + stack.pop())
        elif s[i] == '*':
            stack.append(stack.pop() * stack.pop())
        elif s[i] == '-':
            stack.append(-stack.pop() + stack.pop())
        elif s[i] == '/':
            t = stack.pop()
            stack.append(stack.pop() / t)
    return stack.pop()

N = int(input())
S = input()
V = [int(input()) for _ in range(N)]
print(f"{solve(S, V):.2f}")