class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        
        # Declaring variables
        res = 0
        l = 0
        r = len(nums) - 1

        # Using binary search to find the location
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1
                res = l
            else:
                r = mid - 1

        return res
    
# Time - O(logN)
# Space - O(1)