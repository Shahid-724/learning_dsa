# This code is used to find the missing number in the array

def missing_num(nums, n):
    total_sum = sum(nums)
    expected_sum = n * (n + 1) // 2
    return expected_sum - total_sum

nums = [1, 2, 4, 6, 3, 7, 8]
n = 8
print(missing_num(nums, n))