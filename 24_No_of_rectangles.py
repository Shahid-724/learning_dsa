class Solution:
    def countGoodRectangles(self, rectangles: list[list[int]]) -> int:
        
        temp = 0
        res = 0

        for l, b in rectangles:
            side = min(l, b)
            if side > temp:
                res = 1
                temp = side
            elif side == temp:
                res += 1

        return res
    
# Time - O(N)
# Space - O(1)