def remove_dup(arr):
    left = 1
    for right in range(1, len(arr)):
        if arr[left - 1] != arr[right]:
            arr[left] = arr[right]
            left += 1
    return arr[:left]

print(remove_dup([1, 2, 2, 3, 4, 4, 5]))
#                   R
# arr = 1 2 3 4 5 4 5
#                 L
