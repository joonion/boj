while n:=int(input()):
 T={}
 for _ in range(n):
  s=input()
  t="".join(sorted(s))
  if t in T:T[t][1]+=1
  else:T[t]=[s,0]
 M=max(T.values(),key=lambda x:x[1])
 print(M[0],M[1])