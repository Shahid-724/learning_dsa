class Solution:
    def checkIfExist(self, arr) -> bool:
        
        hashset = set()

        for i in arr:
            if i * 2 in hashset or i / 2 in hashset:
                return True
            hashset.add(i)

        return False
    
# Time - O(N)
# Space - O(N)