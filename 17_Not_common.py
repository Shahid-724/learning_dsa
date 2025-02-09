# This code is used to find the uncommon chars of two strings

def not_common(s1, s2):
    result = list(set(s1) ^ set(s2))
    return result

s1 = input('Enter the first string: ')
s2 = input('Enter the second string: ')
print(not_common(s1, s2))