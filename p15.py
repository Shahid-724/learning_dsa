n = 5

val = 65
for i in range(n):
    for j in range(n - i):
        print(chr(val + j), end=' ')
    print()