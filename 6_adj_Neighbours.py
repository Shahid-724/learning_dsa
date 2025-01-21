# This code is for 8 adjacent neighbours

def neighbours(nums, days):
    result = nums.copy()
    for i in range(days):
        temp = [0] + result + [0]
        cur = []
        for i in range(1, len(temp) - 1):
            if temp[i - 1] == temp[i + 1]:
                cur.append(0)
            else:
                cur.append(1)
        result = cur.copy()
    return result

nums = list(map(int, input().split()))
days = int(input())
print(neighbours(nums, days))