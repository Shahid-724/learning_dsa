# This code is used to form a string with first and last two chars

def first_last(s):
    first_two = s[:2]
    last_two = s[-2:]
    return first_two + last_two

s = input('Enter a string: ')
print(first_last(s))