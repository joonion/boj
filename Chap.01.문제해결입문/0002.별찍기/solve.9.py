N = int(input())
for i in range(N - 1):
    M = 2 * (N - i) - 1
    print(" " * i, end = "")
    print("*" * M)
for i in range(1, N + 1):
    M = 2 * i - 1
    print(" " * ((2*N - M)//2), end = "")
    print("*" * M)
    
