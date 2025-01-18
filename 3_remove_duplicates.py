# This code is used to remove duplicates and return the array in the same order

def rem_dup(nums):
    hashset = set()
    result = []
    for i in nums:
        if i not in hashset:
            hashset.add(i)
            result.append(i)
    return result

nums = list(map(int, input().split()))
print(rem_dup(nums))