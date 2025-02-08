# This code is used to check if a given string is palindrome

# Two pointer approach
def ip(s):
    left = 0
    right = len(s) - 1
    while left <= right:
        if s[left] != s[right]:
            return 'Not Palindrome'
        left += 1
        right -= 1
    return 'Palindrome'

s = input('Enter a string: ')
print(ip(s))