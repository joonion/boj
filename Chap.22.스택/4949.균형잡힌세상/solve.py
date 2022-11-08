opening = "(["
closing = ")]"

def solve(s):
    stack = []
    for i in range(len(s)):
        if s[i] in opening:
            stack.append(s[i])
        elif s[i] in closing:
            if len(stack) == 0:
                return False
            elif closing.index(s[i]) != opening.index(stack.pop()):
                return False
    return len(stack) == 0
    
while True:
    s = input()
    if s == '.': break
    print("yes" if solve(s) else "no")
