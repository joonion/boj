def solve(cmd):
    global S
    if len(cmd.split()) == 1:
        opcode = cmd.strip()
        if opcode == "all":
            S = set([i for i in range(1, 21)])
        elif opcode == "empty":
            S = set([])
    else:
        opcode, operand = cmd.split()
        x = int(operand)
        if opcode == "add":
            S.add(x)
        elif opcode == "remove":
            S.discard(x)
        elif opcode == "toggle":
            if x in S:
                S.remove(x)
            else:
                S.add(x)
        elif opcode == "check":
            print(1 if x in S else 0)

import sys
input = sys.stdin.readline            
M = int(input())
S = set([])
for _ in range(M):
    cmd = input()
    solve(cmd)
