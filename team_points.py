# This code takes 3 integers as input
# Prints the points of the team

# Defining the function
def team_points(points_list):
    return int(points_list[0]) * 4 + int(points_list[1]) * 2 - int(points_list[2]) * 1

# Taking input from the user
points = input('Enter comma seperated numbers: ')

# Converting the string into a list
points = points.split(',')

# Calling the function and storing the result
result = team_points(points)

# Printing the result
print(result)