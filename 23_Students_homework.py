class Solution:
    def busyStudent(self, startTime: list[int], endTime: list[int], queryTime: int) -> int:
        
        res = 0

        for i in range(len(startTime)):
            if startTime[i] <= queryTime <= endTime[i]:
                res += 1

        return res
    
# Time - O(N)
# Space - O(1)