n = 5

for i in range(n):
    print(' ' * i, end='')
    for j in range(2 * n - 2 * i - 1):
        print('*', end='')
    print()