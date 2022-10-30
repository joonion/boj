def f(i,s):
 if i==n:print(s);return
 for j in range(26):
  if A[j]:A[j]-=1;f(i+1,s+chr(97+j));A[j]+=1

N,*S=open(0).read().split()
for s in S:
 A,n=[0]*26,len(s)
 for c in s:A[ord(c)-97]+=1
 f(0,"")