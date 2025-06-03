class Solution:
    def countLargestGroup(self, n: int) -> int:
        
        def digit_sum(num):
            res = 0
            while num:
                res += num % 10
                num //= 10
            return res

        hashmap = dict()
        count = 0
        res = 0

        for i in range(1, n + 1):

            temp = digit_sum(i)
            hashmap[temp] = 1 + hashmap.get(temp, 0)
            
            if hashmap[temp] > count:
                count = hashmap[temp]
                res = 1
            
            elif hashmap[temp] == count:
                res += 1

        return res
    
# Time - O(N logN)
# Space - O(logN)