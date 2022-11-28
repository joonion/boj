def solve(S):
    opening = "[{("
    closing = "]})"
    stack = []
    for s in S:
        if s in opening:
            stack.append(s)
        elif stack and opening.index(stack[-1]) == closing.index(s):
            stack.pop()
        else:
            return False
    return len(stack) == 0

N = int(input())
S = input()
T = [S[i] for i in range(len(S)) if S[i] != "?"]
print(T)
# print("Yes" if solve(S) else "No")