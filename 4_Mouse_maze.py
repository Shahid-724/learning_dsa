def find_cheese(maze, row, col):

    if maze[row][col] == 9:
        return True

    maze[row][col] = -1

    moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    for move in moves:
        new_row = row + move[0]
        new_col = col + move[1]

        if 0 <= new_row < len(maze) and 0 <= new_col < len(maze[0]) and maze[new_row][new_col] != -1:
            if find_cheese(maze, new_row, new_col):
                return True

    return False

rows, cols = 8, 8
maze = [[1, 0, 1, 1, 1, 0, 0, 1], [1, 0, 0, 0, 1, 1, 1, 1], [1, 0, 0, 0, 0, 0, 0, 0], [1, 0, 1, 0, 9, 0, 1, 1], [1, 1, 1, 0, 1, 1, 0, 1], [1, 0, 1, 0, 1, 1, 0, 1], [1, 0, 0, 0, 0, 1, 0, 1], [1, 1, 1, 1, 1, 1, 1, 1]]


# Find the cheese
if find_cheese(maze, 0, 0):
    print(1)
else:
    print(0)

# Time - O(m * n)
# Space - O(m * n)

