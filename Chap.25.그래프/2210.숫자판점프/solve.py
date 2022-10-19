mi = [0, 1, -1, 0]
mj = [1, 0, 0, -1]

def dfs(i, j, d, s, nums, B):
    if d == 5:
        nums.add(int(s))
    else:
        for k in range(4):
            ni, nj = i + mi[k], j + mj[k]
            if 0 <= ni < 5 and 0 <= nj < 5:
                dfs(ni, nj, d+1, s+str(B[ni][nj]), nums, B)

def solve(B):
    nums = set([])
    for i in range(5):
        for j in range(5):
            dfs(i, j, 0, str(B[i][j]), nums, B)
    return len(nums)
    
B = [list(map(int, input().split())) for _ in range(5)]
print(solve(B))