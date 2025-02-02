n = 5

for i in range(n):
    
    for j in range(i + 1):
        print(j + 1, end='')

    print(' ' * 2 * (n - i - 1), end='')

    for j in range(i + 1):
        print(i - j + 1, end='')

    print()