N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))

S = set(A)    
for b in B:
    print(1 if b in S else 0, end=' ')