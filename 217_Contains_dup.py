def contains_dup(arr):
    hashset = set()
    for i in arr:
        if i in hashset:
            return True
        hashset.add(i)
    return False

print(contains_dup([1, 2, 3, 1]))