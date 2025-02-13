def binary_search(row):
    start = 0
    end = len(row) - 1
    index = -1
    while start <= end:
        mid = (start + end) // 2
        if row[mid] == 1:
            index = mid
            end = mid - 1
        else:
            start = mid + 1
    return index

result = binary_search([0, 0, 1, 1, 1])
print(5 - result)