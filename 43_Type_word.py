class Solution:
    def minimumPushes(self, word: str) -> int:
        
        pushes = 0
        res = 0

        for i in range(len(word)):
            if i % 8 == 0:
                pushes += 1
            res += pushes

        return res
    
# Time - O(N)
# Space - O(1)