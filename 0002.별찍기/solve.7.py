N = int(input())
for i in range(N):
    print(" " * (N - i - 1), end = "")
    print("*" * (i*2 + 1))
for i in range(1, N):
    print(" " * i, end = "")
    print("*" * ((N-i)*2 - 1))
