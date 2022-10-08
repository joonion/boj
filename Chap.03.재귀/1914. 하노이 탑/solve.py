def hanoi(n, src, dst, via):
    if n == 1:
        print(src, dst)
    else:
        hanoi(n - 1, src, via, dst)
        hanoi(1, src, dst, via)
        hanoi(n - 1, via, dst, src)
    
def solve(n):
    hanoi(n, 1, 3, 2)
    
    
N = int(input())
print(2 ** N - 1)
if N <= 20:
    solve(N)
