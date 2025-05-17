class Solution:
    def subsetXORSum(self, nums) -> int:
        
        self.res = 0
        n = len(nums)
        
        def backtrack(i, temp=0):

            if i == n:
                self.res += temp
                return None

            backtrack(i + 1, temp)

            temp ^= nums[i]
            backtrack(i + 1, temp)
            temp ^= nums[i]

        backtrack(0)
        return self.res
    
# Time - O(2 ^ N)
# Space - O(N)