# This code is used to count the occurances of word in a string

# Approach 1 using list
def count_occ(s, word):
    s = s.split()
    count = 0
    for i in s:
        if i == word:
            count += 1
    return count

# Approach 2 using count
def count_occ2(s, word):
    return s.count(word)

s = input('Enter a string: ')
word = input('Enter a word: ')
print(count_occ(s, word))
print(count_occ2(s, word))