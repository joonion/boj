N,K,*A=map(int,open(0).read().split())
for i in range(N-1,0,-1):
 j=A.index(max(A[:i+1]))
 if i!=j:
  A[i],A[j]=A[j],A[i];K-=1
  if K==0:exit(print(*A))
print(-1)