class Solution:
    def checkStraightLine(self, coordinates: list[list[int]]) -> bool:
        
        def slope(p1, p2):
            x = p1[0] - p2[0]
            y = p1[1] - p2[1]
            if x:
                return y / x
            return float('inf')

        initial_slope = slope(coordinates[0], coordinates[1])

        for i in range(len(coordinates) - 1):
            cur_slope = slope(coordinates[i], coordinates[i + 1])
            if initial_slope != cur_slope:
                return False

        return True
    
# Time - O(N)
# space - O(1)