n=int(input())
print(sum([max((3*i-n+2)//2,0)for i in range((n+1)//2)]))