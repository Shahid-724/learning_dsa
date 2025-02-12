# This code is for sorting an array using recursive merge sort
# Taking input from the user
arr = list(map(int, input('Enter space seperated numbers: ').split()))

# Defining a function for recursive merge sort
def merge_sort(nums, start, end):
    if start < end:
        mid = (start + end) // 2
        merge_sort(nums, start, mid)
        merge_sort(nums, mid + 1, end)
        merge(nums, start, mid, end)

# Defining a function to merge two sorted arrays
def merge(nums, start, mid, end):
    
    # Declaring variables for use in the function
    temp_nums = []
    i, j = start, mid + 1
    
    # Merging the arrays until both the sub arrays have elements
    while i <= mid and j <= end:
        if nums[i] <= nums[j]:
            temp_nums.append(nums[i])
            i += 1
        else:
            temp_nums.append(nums[j])
            j += 1

    # Adding the remaining elements of the left subarray
    while i <= mid:
        temp_nums.append(nums[i])
        i += 1

    # Adding the remaining elements of the right subarray
    while j <= end:
        temp_nums.append(nums[j])
        j += 1

    # Replacing the original array elements with the sorted elements
    k = 0
    for i in range(start, end + 1):
        nums[i] = temp_nums[k]
        k += 1

# Calling the function and printing the result
merge_sort(arr, 0, len(arr) - 1)
print(arr)