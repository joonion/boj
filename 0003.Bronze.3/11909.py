N = int(input())
for i in range(N):
    print(" " * (N - 1 - i), end = "*")
    if i > 0:
        print(" " * (2*i - 1), end = "*")
    print()
    
        
        