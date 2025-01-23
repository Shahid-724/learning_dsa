def contains_dup_2(arr, k):
    hashmap = dict()
    for i in range(len(arr)):
        if arr[i] in hashmap and abs(i - hashmap[arr[i]]) <= k:
            return True
        hashmap[arr[i]] = i
    return False

print(contains_dup_2([1, 2, 3, 1], 3))