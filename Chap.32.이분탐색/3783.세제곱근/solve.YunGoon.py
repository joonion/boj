for _ in range(int(input())):
    n = int(input() + '0' * 30)
    print(n)
    s, e = 0, n
    while s <= e:
        m = (s + e) // 2
        if m ** 3 > n: 
            e = m - 1
        else: 
            s = m + 1
    print('%d.%010d' % (e // 10 ** 10, e % 10 ** 10))