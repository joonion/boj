n,*a=map(int,[*open(0).read().split()]);b=[0]*n;c=range(n)
for i in c:
 for j in c:
  for k in range(5):
   if a[i*5+k]==a[j*5+k]:b[i]+=1;break
print(b.index(max(b))+1)