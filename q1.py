def findNumber(numbers):
    while len(numbers) > 2:
        temp = []
        for i in range(len(numbers) - 1):
            temp.append(str(int(numbers[i]) + int(numbers[i + 1]))[-1])
        numbers = temp.copy()
    return str(numbers[0])[-1] + str(numbers[1])[-1]

numbers = list(map(int, input().split()))
print(findNumber(numbers))

# Time Complexity: O(n ^ 2)
# Space Complexity: O(n)