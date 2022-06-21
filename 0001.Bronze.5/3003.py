p = [1, 1, 2, 2, 2, 8]
a = list(map(int, input().split()))
b = [p[i] - a[i] for i in range(6)]
print(" ".join(map(str, b)))