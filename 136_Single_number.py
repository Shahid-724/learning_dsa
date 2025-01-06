def single_number(arr):
    result = 0
    for i in arr:
        result ^= i
    return result

print(single_number([4, 1, 2, 1, 2]))