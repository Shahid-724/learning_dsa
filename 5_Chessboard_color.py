class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        return ord(coordinates[0]) % 2 != int(coordinates[1]) % 2
    
# Time - O(1)
# Space - O(1)