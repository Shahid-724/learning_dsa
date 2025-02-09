# This code is used to check which string is larger without lib funcs

def larger(s1, s2):

    # Function to get the length of a string:
    def length(s):
        count = 0
        for i in s:
            count += 1
        return count
    
    if length(s1) > length(s2):
        return s1
    return s2

s1 = input('Enter the first string: ')
s2 = input('Enter the second string: ')
print(larger(s1, s2))