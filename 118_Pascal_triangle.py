def pascal_triangle(n):
    result = [[1]]
    for i in range(n - 1):
        cur = []
        temp = [0] + result[-1] + [0]
        for i in range(len(temp) - 1):
            cur.append(temp[i] + temp[i + 1])
        result.append(cur)
    return result

print(pascal_triangle(7))