# Calculating the average of n numbers
# Taking input for the no. of numbers
n = int(input('How many numbers: '))
sum = 0

# Loop to take the numbers as input
for i in range(0, n):
    number = float(input('Enter the no.: '))
    sum += number

average = sum / n
print(average)