def majority_element(arr):
    result = 0
    count = 0
    for i in arr:
        if not count:
            result = i
        count += (1 if result == i else -1)
    return result

print(majority_element([2,2,1,1,1,2,2]))