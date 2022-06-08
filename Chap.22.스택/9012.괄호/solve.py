def solve(S):
    stack = []
    for i in range(len(S)):
        if S[i] == "(":
            stack.append(S[i])
        else:
            if len(stack) == 0:
                return False
            stack.pop()
    return True if len(stack) == 0 else False

n = int(input())
for _ in range(n):
    S = input()
    print("YES" if solve(S) else "NO")