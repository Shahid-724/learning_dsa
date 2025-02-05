# This code is used to find the sum of factorial series

def fact_series(n):

    # A function to compute factorial
    def fact(num):
        result = 1
        for i in range(1, num + 1):
            result *= i
        return result
    
    # Computing the sum
    result = 1
    for i in range(1, n + 1):
        result += 1 / fact(i)
    return round(result, 2)

n = int(input('Enter a number: '))
print(fact_series(n))