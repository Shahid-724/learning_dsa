# This code is to check if a given number is perfect

def is_strong(num):

    # Defining a function to compute fact
    def fact(n):
        fact = 1
        for i in range(1, n + 1):
            fact *= i
        return fact
    
    # Computing the digit factorial sum
    temp = num
    digit_fact_sum = 0
    while temp:
        digit_fact_sum += fact(temp % 10)
        temp //= 10
    
    # Returning the output
    if num == digit_fact_sum:
        return 'Strong Number'
    return 'Not Strong Number'

n = int(input('Enter a number: '))
print(is_strong(n))