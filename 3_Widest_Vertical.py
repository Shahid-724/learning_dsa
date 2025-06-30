class Solution:
    def maxWidthOfVerticalArea(self, points) -> int:
        
        # Sort the points on the basis of x coordinates
        points.sort(key = lambda x: x[0])

        # Calculating the widest vertical area
        res = 0
        for i in range(len(points) - 1):
            res = max(res, points[i + 1][0] - points[i][0])

        # Returning the result
        return res
    
# Time - O(N logN)
# Space - O(1)