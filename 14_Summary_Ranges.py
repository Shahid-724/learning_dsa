class Solution:
    def summaryRanges(self, nums: list[int]) -> list[str]:

        # Base Case
        if not nums:
            return []
        
        # Declaring variables
        res = []
        start = nums[0]
        cur = start

        # Iterating over nums
        for i in range(1, len(nums)):
            if nums[i] != cur + 1:
                if start != cur:
                    res.append(f'{start}->{cur}')
                else:
                    res.append(str(start))
                start = nums[i]
                cur = start
            else:
                cur += 1

        if start != cur:
            res.append(f'{start}->{cur}')
        else:
            res.append(str(start))

        # Returning the result
        return res
    
# Time - O(N)
# Space - O(N)