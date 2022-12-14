from itertools import*
n,*a=map(int,open(0).read().split())
o='+'*a[-4]+'-'*a[-3]+'*'*a[-2]+'/'*a[-1]
m=1e9;M=-m
for p in set(permutations(o)):
 v=a[0]
 for i in range(n-1):v=eval(f'int({v}{p[i]}{a[i+1]})')
 m=min(m,v);M=max(M,v)
print(M)
print(m)