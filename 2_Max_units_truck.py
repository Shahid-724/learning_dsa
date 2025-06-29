class Solution:
    def maximumUnits(self, boxTypes, truckSize: int) -> int:
        
        # Sorting the box types list
        boxTypes.sort(key = lambda x: x[1], reverse=True)

        # Calculating the no. of units
        res = 0
        for boxes, units in boxTypes:
            if boxes <= truckSize:
                res += boxes * units
                truckSize -= boxes
                print(boxes, units ,truckSize)
            else:
                res += truckSize * units
                break

        return res
    
# Time - O(N logN)
# Space - O(1)