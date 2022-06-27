N = int(input())
n = map(int, input().split())
M = int(input())
m = map(int, input().split())

S = set()
for i in n:
    S.add(i)
    
for i in m:
    print(1 if i in S else 0, end=' ')
