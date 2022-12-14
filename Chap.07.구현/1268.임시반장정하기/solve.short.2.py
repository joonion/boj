n=int(input())
a=[[*map(int,input().split())]for _ in range(n)]
b=[0]*n
for k in range(n):
 for i in range(n):
  for j in range(5):
   if a[k][j]==a[i][j]:b[k]+=1;break
print(b.index(max(b))+1)