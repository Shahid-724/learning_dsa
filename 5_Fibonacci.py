class Solution:
    def fib(self, n: int) -> int:

        if not n:
            return 0
        
        first = 0
        second = 1

        for i in range(n - 1):
            temp = first + second
            first, second = second, temp

        return second
    
# Time - O(N)
# Space - O(1)