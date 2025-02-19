# Harmonic Progression
# Taking input from the user
n = int(input('Enter the no. of terms in the harmonic progression: '))
sum = 0

# The logic for the sum
for i in range(1, n + 1):
    sum += 1 / i

print(f'The harmonic progression of {n} terms is {sum:.3}') 
