class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        
        # A function to calculate digit sum
        def digit_sum(num):
            res = 0
            while num:
                res += (num % 10)
                num //= 10
            return res

        # Declaring variables
        res = 0
        hashmap = dict()

        # Iterating the range 
        for i in range(lowLimit, highLimit + 1):
            temp = digit_sum(i)
            hashmap[temp] = 1 + hashmap.get(temp, 0)
            res = max(res, hashmap[temp])

        # Returning the result
        return res
    
# Time - O(N logN base 10)
# Space - O(N)