class Solution:
    def minOperations(self, logs: list[str]) -> int:
        
        stack = []
        res = 0

        for i in logs:
            if stack and i == '../':
                stack.pop()
                res -= 1
            elif i == './':
                continue
            elif i != '../' and i != './':
                stack.append(i)
                res += 1

        return res
    
# Time - O(N)
# Space - O(N)