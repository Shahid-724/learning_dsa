def solve (n, nums):

    # Defining a function to calculate sum of digits of a given no.
    def digit_sum(num):
        res = 0
        while num:
            res += num % 10
            num //= 10
        return res

    # Defining a function to calculate natural no sum
    def nat_sum(num):
        res = 0
        while num:
            res += num
            num -= 1
        return res

    # Declaring variables
    hashmap = dict()
    res = 0

    # Iterating the array and solving
    for i in nums:
        cur_sum = digit_sum(i)
        if cur_sum in hashmap:
            hashmap[cur_sum] += 1
        else:
            hashmap[cur_sum] = 1

    # Calculating the actual result
    for i in hashmap:
        res += nat_sum(hashmap[i] - 1)

    # Returning the result
    return res