# This code takes an integer as input
# Prints the states of bulbs after n visits

# Taking input from the user
n = int(input('Enter the no. of rooms: '))

# Declaring a variable for rooms
rooms = []

# Getting the initial state of the rooms
for i in range(n):
    if i % 2 == 0:
        rooms.append(0)
    else:
        rooms.append(1)

# Visiting the rooms, changing the state of bulbs and printing
for i in range(n):
    for j in range(n):
        if rooms[j] == 0:
            rooms[j] = 1
        elif rooms[j] == 1:
            rooms[j] = 0
    for j in rooms:
        print(j, end=' ')
    print()