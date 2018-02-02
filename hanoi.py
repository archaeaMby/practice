def hanoi(n, x, y, z):
    if n > 1:
        hanoi(n-1, x, z, y)
        print(x, '->', y)
        hanoi(n-1, z, y, x)
    else:
        print(x, '->', y)

a = hanoi(5, 'A', 'B', 'C')


