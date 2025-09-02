# This is the code for ncr
# This is the basic template you can use

def ncr(r, c):

    r -= 1
    c -= 1

    res = 1

    for i in range(c):
        res *= r - i
        res //= i + 1

    return res

r = 5
c = 3
print(ncr(r, c))

# You need to repeat this n times to get the second pattern
def pt2(n):

    res = []

    for c in range(1, n + 1):

        res.append(ncr(n, c))

    return res

print(pt2(5))