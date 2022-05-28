def perm(i, n, m, nums):
    if m == 0:
        for j in range(i):
            print(nums[j], end = " ")
        print()
    else:
        for j in range(i, n):
            nums[i], nums[j] = nums[j], nums[i]
            perm(i + 1, n , m - 1, nums)
            nums[i], nums[j] = nums[j], nums[i]

def solve(n, m, nums):
    nums.sort()
    return perm(0, n, m, nums)

N, M = map(int, input().split())
nums = list(map(int, input().split()))
solve(N, M, nums)
