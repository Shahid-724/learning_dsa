def fibonacci(n):
    if n == 1:
        return [0]
    if n == 2:
        return [0, 1]
    first = 0
    second = 1
    result = [0]
    for i in range(n - 1):
        cur = first + second
        result.append(cur)
        first, second = cur, first
        
    return result

print(fibonacci(15))

# 0 1 1 2 3 5
# S F C