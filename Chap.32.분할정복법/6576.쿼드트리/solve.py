idx = -1
def get_next(s):
    global idx
    idx += 1
    return s[idx]

def quadtree(i, j, n, s, T):
    head = get_next(s)
    if head == 'W': 
        return # already initialized to 0
    elif head == 'B':
        for r in range(i, i + n):
            for c in range(j, j + n):
                T[r][c] = 1
    else:
        m = n // 2
        quadtree(i, j, m, s, T)
        quadtree(i, j+m, m, s, T)
        quadtree(i+m, j, m, s, T)
        quadtree(i+m, j+m, m, s, T)
        
def solve(n, s):
    T = [[0] * n for _ in range(n)]
    quadtree(0, 0, n, s, T)
    for i in range(n):
        for j in range(n // 8):
            t = int("".join(map(str, T[i][j*8:j*8+8][::-1])), 2)
            print(hex(t>>4) + hex(t&0xf)[2:], end = ",")
        print()

n = int(input())
S = input()
print("#define quadtree_width", n)
print("#define quadtree_height", n)
print("static char quadtree_bits[] = {")
solve(n, S)
print("};")
