def merge_sorted(arr1, arr2, m, n):
    last = m + n - 1
    while m and n:
        if arr1[m - 1] > arr2[n - 1]:
            arr1[last] = arr1[m - 1]
            m -= 1
        else:
            arr1[last] = arr2[n - 1]
            n -= 1
        last -= 1
    while n:
        arr1[last] = arr2[n - 1]
        n -= 1
        last -= 1
    print(arr1) # Printing just for verification

print(merge_sorted([1, 2, 3, 0, 0, 0], [2, 5, 6], 3, 3))