n,m,b,*a=map(int,open(0).read().split())
p=q=9e9
for h in range(257):
 f=r=0
 for x in a:
  g=x-h
  if g>0:r+=g
  else:f+=-g
 t=2*r+f
 if f<=r+b and t<=p:p,q=t,h
print(p,q)