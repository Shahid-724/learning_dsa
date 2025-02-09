# This code is used to swap the first and last chars in a string

def swap_fl(s):
    first = s[-1]
    middle = s[1:-1]
    last = s[0]
    return first + middle + last

s = input('Enter a string: ')
print(swap_fl(s))