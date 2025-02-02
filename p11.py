n = 5

for i in range(n):
    if i % 2 == 0:
        val = 1
    else: 
        val = 0
    for j in range(i + 1):
        print(val, end=' ')

        if val == 0:
            val = 1
        else:
            val = 0

    print()