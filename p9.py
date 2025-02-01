n = 5

for i in range(n):
    print(' ' * (n - i - 1), end='')
    for j in range(2 * i + 1):
        print('*', end='')
    print()

for i in range(n):
    print(' ' * i, end='')
    for j in range(2 * n - 1 - 2 * i):
        print('*', end='')
    print()