N = int(input())
for i in range(1, N + 1):
    M = 2 * (N - i)
    print("*" * i, end = "")
    print(" " * M, end = "")
    print("*" * i)
for i in range(1, N):
    M = 2 * i
    print("*" * ((2*N - M)//2), end = "")
    print(" " * M, end = "")
    print("*" * ((2*N - M)//2))
