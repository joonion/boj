n=int(input());q=[*range(1,n+1)];i=0
for t in range(1,n):q.pop(i:=(i+t**3-1)%len(q))
print(*q)