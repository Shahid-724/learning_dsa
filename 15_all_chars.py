# This code is used print all chars present in both string

def all_chars(s1, s2):
    result = list(set(s1) | set(s2))
    return result

s1 = input('Enter the first string: ')
s2 = input('Enter the second string: ')
print(all_chars(s1, s2))