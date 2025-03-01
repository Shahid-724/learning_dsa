# This code is used to get the prime numbers in a given range

def prime_range(lower, upper):

    # Defining a function to check if n is prime
    def is_prime(num):
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    
    # Getting the prime numbers from the given range
    result = []
    for i in range(lower, upper + 1):
        if is_prime(i):
            result.append(i)

    return result

lower = int(input('Enter the lower limit: '))
upper = int(input('Enter the upper limit: '))
print(prime_range(lower, upper))