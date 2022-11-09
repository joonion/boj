def f(s):
 t=[];j=0;n=len(s)
 for x in range(1,n+1):
  t+=[x]
  while t and j<n and t[-1]==s[j]:t.pop();j+=1
 return j==n
while (a:=input())!='0':
 while (b:=input())!='0':
  print("Yes"if f(list(map(int,b.split())))else"No")
 print()