# This code is used to convert words to numbers

def words_to_num(s):
    hashmap = {
        'zero': '0',
        'one': '1', 
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9'
    }
    words = s.split()
    result = ''
    for i in words:
        result += hashmap[i]
    return result

s = input('Enter a number in words: ')
print(words_to_num(s))

# Time Complexity: O(n)
# Space Complexity: O(n)