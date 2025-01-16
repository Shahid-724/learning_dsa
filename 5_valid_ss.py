def countValidSubstrings(S, minLength, maxLength):
    def is_valid(substring):
        for i in range(len(substring) - 1):
            if substring[i] == substring[i + 1]:
                return False
        return True

    n = len(S)
    count = 0

    for length in range(minLength, maxLength + 1):
        for i in range(n - length + 1):
            substring = S[i:i + length]
            if is_valid(substring):
                count += 1

    return count

# Example usage
S = "1011"
minLength = 2
maxLength = 3
print(countValidSubstrings(S, minLength, maxLength))