class Solution:
    def tribonacci(self, n: int) -> int:

        if n <= 1:
            return n
        
        first = 0
        second = 1
        third = 1

        for i in range(n - 2):
            temp = first + second + third
            first, second, third = second, third, temp

        return third
    
# Time - O(N)
# Space - O(1)