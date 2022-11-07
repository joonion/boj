def p(n):
 for i in range(2,int(n**.5)+1):
  if n%i==0:return 0
 return 1
t,*m=open(0)
for k in m:
 L=S=int(k)
 while 1:
  if p(L):break
  L+=1
 while 1:
  if p(S):break
  S-=1
 print(L-S)