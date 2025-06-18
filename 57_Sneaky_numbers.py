class Solution:
    def getSneakyNumbers(self, nums: list[int]) -> list[int]:
        
        res = list()
        hashset = set()

        for i in nums:
            if i in hashset:
                res.append(i)
            hashset.add(i)

        return res
    
# Time - O(N)
# Space - O(N)