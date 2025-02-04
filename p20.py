n = 5

# Upper half
for i in range(n):
    for j in range(i + 1):
        print('*', end='')
    print(' ' * 2 * (n - i - 1), end='')
    for j in range(i + 1):
        print('*', end='')
    print()

# Lower half
for i in range(n - 1):
    for j in range(n - i - 1):
        print('*', end='')
    print(' ' * 2 * (i + 1), end='')
    for j in range(n - i - 1):
        print('*', end='')
    print()