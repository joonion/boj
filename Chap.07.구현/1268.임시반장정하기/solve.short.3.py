n=int(input());r=range(n);b=[0]*n
a=[[*map(int,input().split())]for _ in r]
for i in r:
 for j in r:
  for k in range(5):
   if a[i][k]==a[j][k]:b[i]+=1;break
print(b.index(max(b))+1)