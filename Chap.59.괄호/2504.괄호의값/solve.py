def value(s, stack):
    if len(s) == 0:
        return 1
    elif s[0] == "(":
        stack.append(s[0])
        return value(s[1:], stack)
    elif s[0] == "[":
        stack.append(s[0])
        return value(s[1:], stack)
    elif s[0] == ")":
        return 0 if stack.pop() != "(" else 2 * value(s[1:], stack)
    elif s[0] == "]":
        return 0 if stack.pop() != "[" else 3 * value(s[1:], stack)

def solve(s):
    stack = []
    return value(s, stack)

s = input()
print(solve(s))