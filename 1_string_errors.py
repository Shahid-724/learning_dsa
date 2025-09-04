def errors(s):
    res = 0
    for i in s:
        if not i.isalnum() and not i == ' ':
            res += 1
    return res

s = 'aa a 234bc@ sad$ hsagd^'
print(errors(s))