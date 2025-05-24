class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        
        # Defining a function for calc digit product
        def digit_prod(num):
            res = 1
            while num:
                res *= num % 10
                num //= 10
            return res

        # Iterating to get the result
        while n:
            if digit_prod(n) % t == 0:
                return n
            n += 1

# Time - O(k * log10(n + k))
# Space - O(1)