# This code is used to get the chars in first string but not in second

def first_not_second(s1, s2):
    result = list(set(s1) - set(s2))
    return result

s1 = input('Enter the first string: ')
s2 = input('Enter the second string: ')
print(first_not_second(s1, s2))