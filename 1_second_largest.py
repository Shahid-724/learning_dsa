def second_largest(arr):
    max1 = arr[0]
    max2 = arr[0]
    for i in arr:
        if i >= max1:
            max1, max2 = i, max1
        elif max1 >= i >= max2:
            max2 = i
    return max2

print(second_largest([1, 2, 3, 4, 5, 6, 7, 8, 9]))

# arr = 1 2 3 4 5 6 7 8 9
#             ^
# max1 = 9
# max2 = 8