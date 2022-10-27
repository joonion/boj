def p(n):
 for i in range(2,int(n**0.5)+1):
  if n%i==0:return
 print(n)
n,m=map(int,input().split())
for i in range(n,min(m,10**7)+1):
 s=str(i)
 if s==s[::-1]:p(i)
print(-1)