N,K,*A=map(int,open(0).read().split())
for i in range(1,N):
 j,t=i-1,A[i]
 while j>=0 and A[j]>t:
  A[j+1]=A[j];K-=1;j-=1
  if K==0:exit(print(A[j+1]))
 if j+1!=i:A[j+1]=t;K-=1
 if K==0:exit(print(A[j+1]))
print(-1)