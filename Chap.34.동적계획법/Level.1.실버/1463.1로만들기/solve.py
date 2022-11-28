N = int(input())
T = [0, 0, 1, 1] + [0] * (N - 3)
for i in range(4, N + 1):
    T[i] = T[i-1] + 1
    if i % 2 == 0:
        T[i] = min(T[i], T[i // 2] + 1)
    if i % 3 == 0:
        T[i] = min(T[i], T[i // 3] + 1)
print(T[N])