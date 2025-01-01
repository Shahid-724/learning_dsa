def rem_dups(arr):
    left = 1
    for right in range(1, len(arr)):
        if arr[left - 1] != arr[right]:
            arr[left] = arr[right]
            left += 1
    print(arr) # Printing only for verification
    return left

print(rem_dups([0,0,1,1,1,2,2,3,3,4]))