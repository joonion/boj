precedence = {"+":0, "-":0, "*":1, "/":1}

def solve(infix):
    stack = []
    postfix = []
    for c in infix:
        if c == '(':
            stack.append(c)
        elif c == ')':
            while len(stack) > 0 and stack[-1] != '(':
                postfix.append(stack.pop())
            stack.pop() # "("
        elif c in ['+', '-', '*', '/']:
            while len(stack) > 0 and stack[-1] != "(" and precedence[stack[-1]] >= precedence[c]:
                postfix.append(stack.pop())
            stack.append(c)
        else:
            postfix.append(c)
    while len(stack) > 0:
        postfix.append(stack.pop())
    return postfix

infix = input()
postfix = solve(infix)
print("".join(postfix))