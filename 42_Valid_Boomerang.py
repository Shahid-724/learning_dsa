class Solution:
    def isBoomerang(self, points: list[list[int]]) -> bool:
        
        def slope(p1, p2):
            x = p1[0] - p2[0]
            y = p1[1] - p2[1]
            if x:
                return y / x
            return float('inf')
    
        initial_slope = slope(points[0], points[1])
        same_line = True

        for i in range(len(points) - 1):
            cur_slope = slope(points[i], points[i + 1])
            if cur_slope != initial_slope:
                same_line = False
            if points[i] == points[i + 1]:
                return False
            
        return not same_line