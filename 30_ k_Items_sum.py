class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        
        res = 0

        while k and numOnes:
            k -= 1
            res += 1
            numOnes -= 1
        
        while k and numZeros:
            k -= 1
            numZeros -= 1

        while k and numNegOnes:
            res -= 1
            k -= 1
            numNegOnes -= 1

        return res
    
# Time - O(K)
# Space - O(1)