class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        
        # Declaring variables
        hashset = set(nums1)
        res = []

        # Iterating over nums2 to build result
        for i in nums2:
            if i in hashset:
                res.append(i)
                hashset.remove(i)

        # Returning the result
        return res
    
# Time - O(M + N)
# Space - O(N)