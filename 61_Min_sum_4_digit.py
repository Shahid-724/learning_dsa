class Solution:
    def minimumSum(self, num: int) -> int:
        
        arr = []

        while num:
            d = num % 10
            arr.append(d)
            num //= 10

        arr.sort()

        n1 = arr[0] * 10 + arr[2]
        n2 = arr[1] * 10 + arr[3]

        return n1 + n2
    
# Time - O(1)
# Space - O(1)
# This is because the input is always a four digit number