class Solution:
    def canBeEqual(self, target, arr) -> bool:
        
        target.sort()
        arr.sort()

        return arr == target
    
# Time - O(N logN)
# Space - O(1)