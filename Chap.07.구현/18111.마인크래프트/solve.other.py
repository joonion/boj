N,M,B=map(int,input().split())
A=[[*map(int,input().split())] for _ in range(N)]
ans,glevel=1e9,0
for i in range(257): #땅 높이
    use_block = 0
    take_block = 0
    for x in range(N):
        for y in range(M):
            if A[x][y] > i:
                take_block += A[x][y] - i
            else:
                use_block += i - A[x][y]
    if use_block > take_block + B:
        continue
    count = take_block * 2 + use_block
    if count <= ans:
        ans = count
        glevel = i
print(ans, glevel)