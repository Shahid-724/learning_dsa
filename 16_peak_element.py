# This code is used to find the peak element in a list

def peak_element(nums):
    nums = [float('-inf')] + nums + [float('-inf')]
    for i in range(1, len(nums) - 1):
        if nums[i] > nums[i + 1] and nums[i] > nums[i - 1]:
            return i - 1
    
nums = [10, 20, 15, 2, 23, 90, 80]
print(peak_element(nums))