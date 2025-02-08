# This code is used to check if two strings are anagrams

def anagram(s, t):

    s_map = dict()
    t_map = dict()

    for i in s:
        if i in s_map:
            s_map[i] += 1
        else:
            s_map[i] = 1
    
    for i in t:
        if i in t_map:
            t_map[i] += 1
        else:
            t_map[i] = 1

    if s_map == t_map:
        return 'Anagram'
    return 'Not Anagram'

s = input('Enter first string: ')
t = input('Enter second string: ')
print(anagram(s, t))