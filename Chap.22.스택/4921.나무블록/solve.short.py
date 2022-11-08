a=0;M=[[],[4,6],[4,6],[1,3],[1,3],[8],[8],[5,7]]
for s in [*open(0)][:-1]:
 a+=1;x=list(map(int,s[:-1]));t=1
 if x[0]!=1 or x[-1]!=2:t=0
 for i in range(1,len(x)):
  if x[i-1] not in M[x[i]-1]:t=0
 print(f"{a}.","VALID" if t else "NOT")