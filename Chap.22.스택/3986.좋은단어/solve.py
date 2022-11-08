def goodword(word):
    stack = []
    for w in word:
        if len(stack) > 0 and w == stack[-1]:
            stack.pop()
        else:
            stack.append(w)
    return len(stack) == 0

def solve(n, W):
    cnt = 0
    for i in range(n):
        cnt += goodword(W[i])
    return cnt

N = int(input())
W = [input() for _ in range(N)]
print(solve(N, W))