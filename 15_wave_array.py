# This code is used to sort the array into a wave like format

def wave_array(nums):
    for i in range(1, len(nums) - 1, 2):
        nums[i], nums[i - 1] = nums[i - 1], nums[i]
    return nums

nums = [1, 2, 3, 4, 5]
print(wave_array(nums))