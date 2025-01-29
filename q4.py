def removePalindromePrefix(n, s):
    n = len(s)
    operations = 0
    for i in range(n):
        for j in range(i + 1, n):
            if s[i:j+1] == s[j:i-1:-1] and j - i + 1 >= 2:
                s = s[0:i] + s[j+1:]
                n = len(s)
                operations += 1
                break
    print(s)
    print(operations, n + 1)

n = 5
s = '10110'
removePalindromePrefix(n, s)