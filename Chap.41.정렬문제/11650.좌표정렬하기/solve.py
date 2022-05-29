import sys
lines = sys.stdin.readlines()
nums = []
for i in range(1, len(lines)):
    nums.append(list(map(int, lines[i].strip().split())))
nums.sort(key = lambda x: (x[0], x[1]))
for i in range(len(nums)):
    sys.stdout.write(" ".join(map(str, nums[i])) + "\n")
