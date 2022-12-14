from heapq import*
i=heappush;o=heappop
H,h=[],[]
for a in[*open(0)][1:]:
 i(H,-(x:=int(a)));i(h,-o(H))
 if len(h)-len(H):i(H,-o(h))
 print(-H[0])