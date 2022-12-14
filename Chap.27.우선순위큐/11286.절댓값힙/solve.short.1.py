from heapq import*
h=[]
for x in[*open(0)][1:]:heappush(h,(abs(y),y))if(y:=int(x))else print(heappop(h)[1]if h else 0)
for i in[*open(0)][1:]:heappush(h,(abs(a),a))if(a:=int(i))else print(len(h)and heappop(h)[1])
# from heapq import heappush, heappop
# import sys
# input = sys.stdin.readline
# h=[]

# N = int(input())
# for _ in range(N):
#     x = int(input())
#     if x == 0:
#         if heap: print(heappop(heap)[1])
#         else: print(0)
#     else:
#         heappush(heap, ((abs(x), x), x))