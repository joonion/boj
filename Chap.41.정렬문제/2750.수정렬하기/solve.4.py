import sys
input = sys.stdin.readline

N = int(input())
nums = [int(input()) for _ in range(N)]
S = sorted(nums)
for i in range(N):
    print(nums[i])