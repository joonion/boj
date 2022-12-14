from heapq import*
h=[]
for x in[*open(0)][1:]:heappush(h,(abs(y),y))if(y:=int(x))else print(len(h)and heappop(h)[1])