from heapq import heappush, heappop

def solve(S):
    H = {}
    for i in range(len(S)):
        k = "".join(sorted(S[i]))
        H[k] = [i] if k not in H else H[k] + [i]
    PQ = []
    for key in H.keys():
        heappush(PQ, ((-len(H[key]), key), H[key]))
    for i in range(min(5, len(H))):
        G = []
        for j in heappop(PQ)[1]:
            G.append(S[j])
        G.sort()
        print(f"Group of size {len(G)}: " + " ".join(G) + " .")

S = []
while True:
    try:
        S.append(input())
    except:
        break
solve(S)