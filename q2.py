def matrixStringConversion(X):
    result = []
    for i in X:
        cur = ''
        for j in i:
            if j == 0:
                cur += '.'
            else:
                cur += chr(j + 64)
        result.append(cur)
    return result

X = [[0, 2, 0, 1], [3, 0, 4, 0], [0, 0, 0, 0]]
print(matrixStringConversion(X))