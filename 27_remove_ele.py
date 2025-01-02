def remove_ele(arr, val):
    left = 0
    for right in range(len(arr)):
        if arr[right] != val:
            arr[left] = arr[right]
            left += 1
    print(arr) # Printing only for verification
    return left

print(remove_ele([0,1,2,2,3,0,4,2], 2))