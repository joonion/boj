n=int(input());s=[[*input().split()]for _ in range(n)]
for x in input().split():
 t=1
 for i in range(n):
  if len(s[i]) and x==s[i][0]:s[i].pop(0);t=0
 if t:exit(print("Impossible"))
print(['Imp','P'][sum([len(i)for i in s])==0]+"ossible")