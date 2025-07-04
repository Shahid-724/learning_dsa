class Solution:
    def findTheDistanceValue(self, arr1, arr2, d: int) -> int:
        
        res = 0

        for i in arr1:
            temp = False
            for j in arr2:
                if abs(i - j) <= d:
                    temp = True
                    break
            if not temp:
                res += 1

        return res
    
# Time = O(M * N)
# Space - O(1)