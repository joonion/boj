def solve(s, T):
    a = "".join(sorted(s))
    if a not in T:
        print(s)
        T.add(a)
        # print(T)    
    
N, *S = open(0).read().split()
T = set([])
for i in range(int(N)):
    solve(S[i], T)