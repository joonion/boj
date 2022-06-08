import sys
input = sys.stdin.readline

n = int(input())
deque = []
for _ in range(n):
    cmd = input().strip()
    if cmd.startswith("push_front"):
        deque.insert(0, cmd.split()[1])
    elif cmd.startswith("push_back"):
        deque.append(cmd.split()[1])
    elif cmd.strip() == "pop_front":
        item = None if len(deque) == 0 else deque.pop(0)
        print(-1 if item == None else item)
    elif cmd == "pop_back":
        item = None if len(deque) == 0 else deque.pop()
        print(-1 if item == None else item)
    elif cmd == "size":
        print(len(deque))
    elif cmd == "empty":
        print(1 if len(deque) == 0 else 0)
    elif cmd == "front":
        print(-1 if len(deque) == 0 else deque[0])
    elif cmd == "back":          
        print(-1 if len(deque) == 0 else deque[-1])
