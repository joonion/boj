x=10**6
n=int(input())
T=[0,x,1,x,2,1]+[x]*n
for i in range(6,n+1):
 T[i]=1+min(T[i-2],T[i-5])
print(T[n]if T[n]<x else-1)