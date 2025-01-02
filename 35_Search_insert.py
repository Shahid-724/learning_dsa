def search_insert(arr, val):
    left = 0
    right = len(arr) - 1
    result = 0
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == val:
            return mid
        elif arr[mid] < val:
            left = mid + 1
            result = left
        else:
            right = mid - 1
    return result

print(search_insert([1, 3, 5, 6], 7))