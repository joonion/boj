def solve(i, n, A):
    print(f"Case {i+1}: {n-1}", end="")
    for j in range(n):
        print(f" {(n - j)*A[j]}", end="")
    print()
    
T = int(input())
for i in range(T):
    n, *A = map(int, input().split())
    solve(i, n, A)