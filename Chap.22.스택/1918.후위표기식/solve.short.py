t=input();p="( ) +-*/";r="";s=[]
for x in t:
 if x in p:
  i=p.index(x)
  while i and s and i//2<=p.index(s[-1])//2:r+=s.pop()
  if i==2:s.pop()
  else:s+=[x]
 else:r+=x
print(r+''.join(s[::-1]))