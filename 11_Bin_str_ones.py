class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        
        count = 0
        prev = 1

        for i in s:
            if i == '0' and prev:
                count += 1
                prev = 0
            elif i == '1':
                prev = 1

        if prev:
            count += 1

        return count == 1
    
# Time - O(N)
# Space - O(1)