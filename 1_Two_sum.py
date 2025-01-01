def two_sum(arr, target):
    hashmap = dict()
    for i in range(len(arr)):
        if target - arr[i] in hashmap:
            return [i, hashmap[target - arr[i]]]
        hashmap[arr[i]] = i

print(two_sum([2, 7, 11, 15], 9))