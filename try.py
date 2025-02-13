mat = [[0, 1, 1, 1], 
       [0, 0, 0, 1], 
       [1, 1, 1, 1], 
       [0, 0, 0, 0]]


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


def row_with_max_ones(mat):
    result = 0
    count = 0

    for row in range(len(mat)):
        cur_count = binary_search(mat[row])
        if cur_count != -1 and len(mat[row]) - cur_count > count:
            count = len(mat[row]) - cur_count
            result = row

    return result

print(row_with_max_ones(mat))


def libraryFine(d1, m1, y1, d2, m2, y2):
    # Write your code here
    if y1 > y2:
        return 10000
    elif m1 > m2:
        return 500 * (m1 - m2)
    elif d1 > d2:
        return 15 * (d1 - d2)
    else:
        return 0
    
print(libraryFine(15, 7, 2014, 1, 7, 2015))