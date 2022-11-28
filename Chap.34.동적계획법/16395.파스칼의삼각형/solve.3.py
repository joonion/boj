def binom(n, k):
    k = min(k, n - k)
    B = [1] + [0] * k
    for i in range(n + 1):
        for j in range(min(i, k), 0, -1):
            B[j] += B[j-1]
    return B[k]

n, k = map(int, input().split())
print(binom(n - 1, k - 1))