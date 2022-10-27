N,*S=open(0).read().split()
T=set([])
for s in S:
 t="".join(sorted(s))
 if t not in T:T.add(t);print(s)