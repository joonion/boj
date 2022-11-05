for r in [0]*int(input()):
 s=input();l=0;h=len(s)-1
 while l<h:
  if s[l]!=s[h]:u=s[l:h];v=s[l+1:h+1];r=1 if u==u[::-1]or v==v[::-1]else 2;break
  l+=1;h-=1
 print(r)