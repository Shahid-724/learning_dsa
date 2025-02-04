n = 5

print('* ' * n)

for i in range(n - 2):
    print('* ', end='')
    for j in range(n - 2):
        print('  ', end='')
    print('* ')

print('* ' * n)