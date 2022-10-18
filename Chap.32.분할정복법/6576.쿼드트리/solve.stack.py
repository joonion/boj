stack = []

def quadtree(i, s, T):
    if i < len(s):
        r, c, n = stack.pop()
        if s[i] == 'W':
            pass # already filled with 0
        elif s[i] == 'B':
            for y in range(r, r + n):
                for x in range(c, c + n):
                    T[y][x] = '1'
        else: # s[i] == 'Q'
            m = n // 2
            stack.append((r+m, c+m, m))
            stack.append((r+m, c, m))
            stack.append((r, c+m, m))
            stack.append((r, c, m))
        quadtree(i + 1, s, T)

def solve(n, s):
    T = [['0']*n for _ in range(n)]
    stack.append((0, 0, n))
    quadtree(0, s, T)
    for i in range(n):
        for j in range(0, n, 8):
            x = int("".join(T[i][j:j+8][::-1]),2)
            print(hex(x>>4) + hex(x&0xf)[2:], end=",")
        print()
    
n = int(input())
s = input()
print(f"#define quadtree_width {n}")
print(f"#define quadtree_height {n}")
print("static char quadtree_bits[] = {")
solve(n, s)
print("};")
