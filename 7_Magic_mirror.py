# This code is used to check if word1 is a right rotated version of word2

def magic_mirror(word1, word2):
    temp = word1
    for i in range(len(word1)):
        temp = temp[-1] + temp[:-1]
        if temp == word2:
            return 1
    return -1


# Use this code in exam 
# It is optimized
def magic_mirror2(word1, word2):
    if len(word1) != len(word2):
        return -1
    if sorted(word1) != sorted(word2):
        return -1
    if word2 in word1 + word1:
        return 1
    return -1

word1 = input('Enter first word: ')
word2 = input('Enter second word: ')
print(magic_mirror(word1, word2))
print(magic_mirror2(word1, word2))