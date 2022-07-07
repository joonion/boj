def solve(n, X):
    Y = sorted(list(set(X)))
    d = {Y[i]:i for i in range(len(Y))}
    for x in X:
        print(d[x], end=' ')

n = int(input())
X = list(map(int, input().split()))
solve(n, X)