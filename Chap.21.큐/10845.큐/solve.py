from sys import stdin
next(stdin)
queue = []
for line in stdin:
    cmd = line.strip().split()
    if cmd[0] == "push":
        queue.append(cmd[1])
    elif cmd[0] == "pop":
        print(-1 if len(queue) == 0 else queue.pop(0))
    elif cmd[0] == "size":
        print(len(queue))
    elif cmd[0] == "empty":
        print(1 if len(queue) == 0 else 0)
    elif cmd[0] == "front":
        print(-1 if len(queue) == 0 else queue[0])
    elif cmd[0] == "back":
        print(-1 if len(queue) == 0 else queue[-1])
