def f(K,A):
 if K==0:exit(print(*A))
N,K,*A=map(int,open(0).read().split())
for i in range(1,N):
 j,t=i-1,A[i]
 while j>=0 and A[j]>t:A[j+1]=A[j];K-=1;j-=1;f(K,A)
 if j+1!=i:A[j+1]=t;K-=1;f(K,A)
print(-1)