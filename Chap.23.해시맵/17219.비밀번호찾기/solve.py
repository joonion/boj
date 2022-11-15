import sys
input = sys.stdin.readline

def solve(A, B):
    T = dict(A)
    for i in B: 
        print(T[i])
        
n, m = map(int, input().split())
A = [input().strip().split() for _ in range(n)]
B = [input().strip() for _ in range(m)]
solve(A, B)
