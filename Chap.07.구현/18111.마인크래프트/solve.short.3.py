n,m,b,*a=map(int,open(0).read().split())
p=q=9e9
for h in range(257):
 f=r=0
 for x in a:g=x-h;r+=g*(g>0);f+=-g*(g<0)
 t=2*r+f
 if(f<=r+b)*(t<=p):p,q=t,h
print(p,q)