import sys
input = sys.stdin.readline

N = int(input())
nums = [0] * N
for i in range(N):
    nums[i] = int(input())
nums.sort()
for i in range(N):
    print(nums[i])