from collections import Counter
def second_frequent(nums):
    counter = Counter(nums).most_common()
    if len(counter) > 1 and counter[0][1] == counter[1][1]:
        return counter[1][0]
    else:
        return counter[0][0]

import sys
input = sys.stdin.readline
N = int(input())
nums = [0] * N
for i in range(N):
    nums[i] = int(input())
nums.sort()
print(round(sum(nums) / N))
print(nums[N // 2])
print(second_frequent(nums))
print(nums[-1] - nums[0])