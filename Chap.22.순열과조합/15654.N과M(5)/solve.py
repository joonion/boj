def perm(n, m, nums, selected):
    if m == 0:
        for i in range(len(selected)):
            print(nums[selected[i]], end = " ")
        print()
    else:
        for i in range(n):
            if i not in selected:
                selected.append(i)
                perm(n , m - 1, nums, selected)
                selected.pop()

def solve(n, m, nums):
    nums.sort()
    return perm(n, m, nums, [])

N, M = map(int, input().split())
nums = list(map(int, input().split()))
solve(N, M, nums)
