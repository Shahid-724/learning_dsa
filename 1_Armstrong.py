# This code is used to check if a given number is armstrong number

def is_armstrong(num):

    # Calculating the no of digits
    temp = num
    digit_count = 0
    while temp:
        digit_count += 1
        temp //= 10

    # Calculating the armstrong sum
    armstrong_sum = 0
    temp = num
    while temp:
        armstrong_sum += (temp % 10) ** digit_count
        temp //= 10

    # Checking and printing the output
    if num == armstrong_sum:
        return 'Armstrong Number'
    return 'Not an Armstrong Number'

n = int(input('Enter a number: '))
print(is_armstrong(n))