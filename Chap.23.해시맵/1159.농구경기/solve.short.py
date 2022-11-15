n,*x=open(0)
c=[s[0]for s in x]
d=set([t for t in c if c.count(t)>4])
print(''.join(sorted(d))if d else'PREDAJA')