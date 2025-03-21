# This code takes a list of strings as input
# Prints whether they belong to a family or not

# Taking input for the no of test cases
n = int(input('Enter the no of test cases: '))

# Declaring a variable for final result
final_result = ''

# Looping n no of times
for i in range(n):

    # Taking input from the user
    m = int(input('Enter the no of words: '))
    words = input('Enter space seperated words: ').split()

    # Declaring a variable for storing result
    result = 'Family'

    # Getting the input
    for j in range(len(words) - 1):
        if len(words[j]) == len(words[j + 1]):
            equal_count = 0
            for k in range(len(words[j])):
                if words[j][k] == words[j + 1][k]:
                    equal_count += 1
            if equal_count != len(words[j]) - 1:
                result = 'Not a Family'
        elif len(words[j]) == len(words[j + 1]) + 1 or len(words[j]) == len(words[j + 1]) - 1:
            if words[j] in words[j + 1] or words[j + 1] in words[j]:
                continue
        else:
            result = 'Not a family'

    # Printing the result
    final_result += result
    if i < n - 1:
        final_result += '\n'

# Printing the final result
print(final_result)