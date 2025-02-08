# This code is used to sort hyphen separated words

def hyphen_sort(s):
    s_list = s.split('-')
    s_list.sort()
    result = '-'.join(s_list)
    return result

s = input('Enter a hyphen separated string: ')
print(hyphen_sort(s))