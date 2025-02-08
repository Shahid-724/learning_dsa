# This code is used to get odd palindromes in a given range

def odd_palindromes(lower, upper):

    for i in range(lower, upper + 1):
        if i % 2 == 1 and str(i) == str(i)[::-1]:
            print(i)

lower = int(input('Enter first num: '))
upper = int(input('Enter second num: '))
odd_palindromes(lower, upper)