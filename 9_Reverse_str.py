# This code is used to reverse a string using recursion

def reverse_str(s):
    if not s:
        return ''
    return reverse_str(s[1:]) + s[0]

s = input('Enter a string: ')
print(reverse_str(s))