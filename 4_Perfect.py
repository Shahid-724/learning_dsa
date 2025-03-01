# This code is used to check if a number is perfect

def is_perfect(num):

    factor_sum = 0
    for i in range(1, (num // 2) + 1):
        if num % i == 0:
            factor_sum += i
    
    if num == factor_sum:
        return 'Perfect'
    return 'Not Perfect'

n = int(input('Enter a number: '))
print(is_perfect(n))