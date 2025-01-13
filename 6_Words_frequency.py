# This code is used to get the frequencies of each word in a string

def word_freq(s):
    words = s.split()
    hashmap = dict()
    for i in words:
        if i in hashmap:
            hashmap[i] += 1
        else:
            hashmap[i] = 1
    return hashmap

s = 'Gfg Gfg Gfg'
print(word_freq(s))

# Time Complexity: O(n)
# Space Complexity: O(n)