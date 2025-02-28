# This code is used to print n rows of a pascal triangle

def pascal_triangle(n):
    result = [1]

    for i in range(n):
        print(' ' * (n - i - 1), end='')

        for j in result:
            print(j, end=' ')

        print()

        temp = [0] + result + [0]
        cur = []
        for j in range(len(temp) - 1):
            cur.append(temp[j] + temp[j + 1])
        result = cur

n = int(input('Enter a number: '))
pascal_triangle(n)