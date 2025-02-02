n = 5

for i in range(n):

    val = 65
    print(' ' * (n - i - 1), end='')

    for j in range(2 * i + 1):

        if j < i + 1:
            print(chr(val), end='')
            val += 1
            
        else:
            print(chr(val - 2), end='')
            val -= 1
    print()