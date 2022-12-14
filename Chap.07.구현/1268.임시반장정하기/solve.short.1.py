n=int(input())
a=[[*map(int,input().split())]for _ in range(n)]
f={i:set()for i in range(n)}
for b in zip(*a):
 for i in range(n):
  for j in range(i+1,n):
   if b[i]==b[j]:f[i].add(j);f[j].add(i)
print(sorted(f.items(),key=lambda x:(-len(x[1]),x[0]))[0][0]+1)