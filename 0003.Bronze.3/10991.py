N = int(input())
for i in range(N):
    print(" " * (N - 1 - i), end = "")
    for j in range(i):
        print("*", end = " ")
    print("*")