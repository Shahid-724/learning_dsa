def summaryRanges(nums):
    if not nums:
        return []
    start = nums[0]
    end = nums[0]
    result = []
    for i in range(len(nums) - 1):
        if nums[i] + 1 == nums[i + 1]:
            end = nums[i + 1]
        else:
            if start == end:
                result.append(str(start))
            else:
                result.append(str(start) + '->' + str(end))
            start = nums[i + 1]
            end = nums[i + 1]
    if start != nums[-1]:
        result.append(str(start) + '->' + str(nums[-1]))
    else:
        result.append(str(start))
    return result

print(summaryRanges([0,1,2,4,5,7]))