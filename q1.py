def evaluation(S):
    g, n, b = 0, 0, 0
    for i in S:
        if i == 'g':
            g += 1
        elif i == 'n':
            n += 1
        else:
            b += 1
    if g >= 1 and b == 0:
        return 'Pass'
    return 'Fail'

S = input()
print(evaluation(S))