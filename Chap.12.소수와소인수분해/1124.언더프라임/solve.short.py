a,b=map(int,input().split())
c=0
for n in range(a,b+1):
 d=0
 for i in range(2,int(n**.5)+1):
  while n%i==0:d+=1;n//=i
 d+=n!=1
 c+=d in[2,3,5,7,11,13]
print(c)