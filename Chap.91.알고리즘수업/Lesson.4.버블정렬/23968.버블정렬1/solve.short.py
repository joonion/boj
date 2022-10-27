N,K,*A=map(int,open(0).read().split())
for i in range(N-1):
 for j in range(N-1-i):
  if A[j]>A[j+1]:
    A[j],A[j+1]=A[j+1],A[j];K-=1
  if K==0:exit(print(A[j],A[j+1]))
print(-1)