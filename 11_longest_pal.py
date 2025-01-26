# # This code is used to find the longest palindrome number in an array
# # Taking input from the user for the array
# nums = list(map(int, input('Enter space separated numbers: ').split()))

# # Defining a function to check if a number is palindrome
# def is_palindrome(num):

#     div = 1
#     while div * 10 <= num:
#         div *= 10

#     while num:
#         if num % 10 != num // div:
#             return False
#         num = (num % div) // 10
#         div //= 100

#     return True

# # Defining a function to get the length of a number
# def get_length(num):
#     length = 0
#     while num:
#         length += 1
#         num //= 10
#     return length

# # Declaring a variable to store the longest palindrome length
# result = 0

# # Iterating through the array to find the longest palindrome
# for i in nums:
#     if is_palindrome(i):
#         result = max(result, get_length(i))

# # Printing the output
# print(f'The longest palindrome is of length {result}')

def longest_palindrome(nums):
    
    def is_palindrome(n):
        if n < 0:
            return False
        return str(n) == str(n)[::-1]
    
    result = float('-inf')
    for i in nums:
        if is_palindrome(i) and i > result:
            result = i

    return result

nums = [1, 232, 5545455, 909090, 161]
print(longest_palindrome(nums))