n = 5

for i in range(n):
    print(' ' * (n - i - 1), end='')
    for j in range(2 * i + 1):
        print('*', end='')
    print()