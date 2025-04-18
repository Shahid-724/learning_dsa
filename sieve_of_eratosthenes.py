n = 100

sieve = [1] * 101

sieve[0] = 0
sieve[1] = 0

for i in range(2, int(n ** 0.5) + 1):
    if sieve[2]:
        j = i ** 2
        while j <= n:
            sieve[j] = 0
            j += i

print(sieve)
print(sieve[67] == 1)

# Time - O(N log(logN))
# Space - O(N)