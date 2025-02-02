n = 5

val = 65
for i in range(n):
    for j in range(i + 1):
        print(chr(val + i), end=' ')
    print()