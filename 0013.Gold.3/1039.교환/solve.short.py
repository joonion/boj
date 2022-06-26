n,k=input().split()
m=len(n)
a={n}
for _ in[0]*int(k):
 b=set()
 for p in a:
  q=list(p)
  for i in range(m):
   for j in range(i+1,m):
    r=q[:];r[i],r[j]=r[j],r[i]
    if r[0]!='0':b.add(''.join(r))
 a=b
print(max(a)if len(a)>0 else -1)