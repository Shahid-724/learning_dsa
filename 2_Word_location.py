# This code is used to find the location of a word in a string

def word_location(s, target):
    words = s.split()
    for i in range(len(words)):
        if words[i] == target:
            return i + 1
    return -1

s = input('Enter a string: ')
target = input('Enter target: ')
print(word_location(s, target))

# Time Complexity: O(n)
# Space Complexity: O(n)