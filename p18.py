n = 5

for i in range(n):
    val = 65
    
    for j in range(i + 1):
        print(chr(val + n - i - 1), end=' ')
        val += 1
    print()