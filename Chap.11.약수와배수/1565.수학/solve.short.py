import math as m
d,_,*n=map(int,open(0).read().split())
L,G=m.lcm(*n[:d]),m.gcd(*n[d:])
c=0
for i in range(1,int(G**.5)+1):
 if G%i==0:c+=1*(i%L==0)+(G//i%L==0)-(i*i==G)*(i%L==0)
print(c)