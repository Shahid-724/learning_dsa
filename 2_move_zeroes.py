def move_zeroes(arr):
    left = 0
    for right in range(1, len(arr)):
        if arr[left] == 0 and arr[right] != 0:
            arr[left], arr[right] = arr[right], arr[left]
        if arr[left] != 0:
            left += 1
    return arr

print(move_zeroes([0, 1, 0, 3, 12])) 