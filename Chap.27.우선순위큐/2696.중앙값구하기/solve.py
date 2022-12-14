from heapq import heappush, heappop

def solve(n, A):
    M, maxheap, minheap = [], [], []
    for i in range(n):
        heappush(minheap, A[i])
        if maxheap and -maxheap[0] > minheap[0]:
            heappush(maxheap, -heappop(minheap))
            heappush(minheap, -heappop(maxheap))
        if i % 2 == 0:
            M.append(minheap[0] if len(maxheap) < len(minheap) else -maxheap[0])
        else:
            heappush(maxheap, -heappop(minheap))
    print(len(M))
    for i in range(len(M) // 10 + 1):
        for j in range(i * 10, min(i*10 + 10, len(M))):
            print(M[j], end = " ")
        print()
    
for _ in range(int(input())):
    N = int(input())
    A = []
    for i in range(N // 10 + 1):
        A += list(map(int, input().split()))
    solve(N, A)