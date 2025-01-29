def ramanAndHisPet(n, l):
    result = 1 
    if l[0] == 1:
        result += 1
    for i in range(1, len(l)):
        print(result, i)
        if l[i] == 0:
            if l[i - 1] == 0:
                return -1
        else:
            if l[i - 1] == 1:
                result += 5
            else:
                print('last else')
                result += 1
    return result

n = 3
l = [1, 0, 1, 1]
print(ramanAndHisPet(n, l))