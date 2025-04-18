def create_sieve(n):

    sieve = [1] * (n + 1)
    sieve[0], sieve[1] = 0, 0

    for i in range(2, int(n ** 0.5) + 1):

        if sieve[i] == 1:
            for j in range(i * i, n + 1, i):
                sieve[j] = 0

    return sieve

n = 100
primes = create_sieve(n)

for i in range(len(primes)):
    if primes[i] == 1:
        print(i, end=' ')

# Time - O(N log(logN))
# Space - O(N)