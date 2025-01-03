def plusOne(arr):
    arr = arr[::-1]
    carry = 1
    for i in range(len(arr)):
        if arr[i] + carry < 10:
            arr[i] += carry
            carry = 0
            break
        else:
            arr[i] = 0
    if carry:
        arr.append(1)
    arr = arr[::-1]
    return arr

print(plusOne([5, 4, 3, 2, 9]))