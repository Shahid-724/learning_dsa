class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        
        left = 0
        for right in range(len(nums)):
            if nums[right] != val:
                nums[left] = nums[right]
                left += 1

        return left
    
# Time - O(N)
# Space - O(1)