def large_small(arr):
    max1 = max2 = float('-inf')
    min1 = min2 = float('inf')
    for i in range(len(arr)):
        if i % 2 == 0:
            if arr[i] >= max1:
                max1, max2 = arr[i], max1
            elif max1 >= arr[i] >= max2:
                max2 = arr[i]
        else:
            if arr[i] <= min1:
                min1, min2 = arr[i], min1
            elif min1 <= arr[i] <= min2:
                min2 = arr[i]
    return max2 + min2

print(large_small([1, 8, 0, 2, 3, 5, 6]))