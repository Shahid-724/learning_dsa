def magical_no(n):
    
    # Converting dec to binary
    def dec_bin(num):
        result = ''
        while num:
            result = str((num % 2) + 1) + result
            num //= 2
        return int(result)
    
    # Calc the sum of digits
    def digit_sum(num):
        result = 0
        while num:
            result += num % 10
            num //= 10
        return result
    
    # The actual loop
    result = 0
    for i in range(1, n + 1):
        binary = dec_bin(i)
        digit_sums = digit_sum(binary)
        if digit_sums % 2 == 1:
            result += 1
    return result

print(magical_no(5))