# This code is used to check if a product subarray exists in an array

def product_check(nums, target):
    left = 0
    right = 0
    prod = nums[left]
    while right < len(nums):
        if prod == target:
            return True
        elif prod < target:
            right += 1
            prod *= nums[right]
        else:
            if left + 1 == len(nums):
                break
            prod //= nums[left]
    return False

nums = list(map(int, input('Enter space separated nums: ').split()))
target = int(input('Enter the target: '))
print(product_check(nums, target))