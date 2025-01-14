def findMaximumChange(temperatureChange):
    result = float('-inf')
    left = 0
    total = sum(temperatureChange)
    for i in range(len(temperatureChange)):
        right = total - left
        left += temperatureChange[i]
        temp = max(left, right)
        result = max(temp, result)
    return result

temperatureChange = list(map(int, input().split()))
print(findMaximumChange(temperatureChange))

# Time Complexity: O(n)
# Space Complexity: O(1)