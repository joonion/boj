N = int(input())
nums = [int(input()) for _ in range(N)]
nums.sort(reverse = True)
for i in range(N):
    print(nums[i])
