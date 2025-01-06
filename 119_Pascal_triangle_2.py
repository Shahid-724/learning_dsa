def pascal_triangle_2(n):
    result = [1]
    for i in range(n):
        temp = [0] + result + [0]
        cur = []
        for i in range(len(temp) - 1):
            cur.append(temp[i] + temp[i + 1])
        result = cur
    return result

print(pascal_triangle_2(3))