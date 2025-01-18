# This code is to encrypt a secret code

def encrypt(s, n, m):
    mod1 = 10
    mod2 = 1000000007
    temp = pow(s, n, mod1)
    result = pow(temp, m, mod2)
    return result


s = int(input('Enter the secret code: '))
n = int(input('Enter the value of n: '))
m = int(input('Enter the value of m: '))

print(encrypt(s, n, m))
