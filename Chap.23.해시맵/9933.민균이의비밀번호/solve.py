N = int(input())
S = [input() for _ in range(N)]
T = set([])
for s in S:
    if s in T:
        print(len(s), s[len(s)//2])
        break
    T.add(s[::-1])
    
    