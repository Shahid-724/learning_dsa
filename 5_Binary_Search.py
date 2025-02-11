# This is the code for binary search using recursion
# Taking input for the array and the search key
arr = list(map(int, input('Enter space seperated numbers: ').split()))
key = int(input('Enter the search key: '))

# Defining the function for binary search using recursion
def binary_search(nums, search_key, start, end):
    
    # These are the two base cases
    if start > end:
        return -1
    mid = (start + end) // 2
    if nums[mid] == search_key:
        return mid
    
    # These are the two recursive calls
    elif nums[mid] < search_key:
        return binary_search(nums, search_key, mid + 1, end)
    return binary_search(nums, search_key, start, end - 1)
    
# Calling the function and printing the output
print(binary_search(arr, key, 0, len(arr) - 1))