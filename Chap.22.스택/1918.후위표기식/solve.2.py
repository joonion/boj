prec = {'(':0, ')':1, '+':2, '-':2, '*':3, '/':3}

def solve(X):
    stack, postfix = [], ""
    for x in X:
        if x.isalpha(): postfix += x
        elif x == '(': stack.append(x)
        else:
            while stack and prec[x] <= prec[stack[-1]]:
                postfix += stack.pop()
            if x == ')': stack.pop() # remove '('
            else: stack.append(x)
    while stack: postfix += stack.pop()
    return postfix

X = list(input())
print(solve(X))