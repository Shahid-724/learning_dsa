# This is a dfs approach using memoization for mouse and maze

# Use this for coding, cuz this is efficient

def find_if_possible(memoization, visited, grid, row_no, col_no):
    if row_no == -1 or row_no == len(grid) or col_no == len(grid[0]) or col_no == -1 or visited[row_no][col_no] or grid[row_no][col_no] == 0:
        return False

    if grid[row_no][col_no] == 9:
        return True

    if memo_grid[row_no][col_no] is not None:
        return memo_grid[row_no][col_no]

    visited[row_no][col_no] = True

    can_find_cheese = False

    can_find_cheese = find_if_possible(memoization, visited, grid, row_no - 1, col_no) or can_find_cheese
    can_find_cheese = find_if_possible(memoization, visited, grid, row_no + 1, col_no) or can_find_cheese
    can_find_cheese = find_if_possible(memoization, visited, grid, row_no, col_no + 1) or can_find_cheese
    can_find_cheese = find_if_possible(memoization, visited, grid, row_no, col_no - 1) or can_find_cheese

    visited[row_no][col_no] = False
    memoization[row_no][col_no] = can_find_cheese
    return can_find_cheese


grid = [[1,0,1,1,1,0,0,1],[1,0,0,0,1,1,1],[1,0,0,0,0,0,0,0],[1,0,1,0,9,0,1,1], [1,1,1,0,1,0,0,1], [1,0,1,0,1,1,0,1], [1,0,0,0,0,1,0,1], [1,1,1,1,1,1,1,1]]
visited = [[False] * len(grid[0]) for row in range(len(grid))]
memo_grid = [[None] * len(grid[0]) for row in range(len(grid))]
print(find_if_possible(memo_grid, visited, grid, 0, 0))

# 1 0 1 1 1 0 0 1
# 1 0 0 0 1 1 1 1
# 1 0 0 0 0 0 0 0 
# 1 0 1 0 9 0 1 1
# 1 1 1 0 0 0 0 1
# 1 0 1 0 1 1 0 1
# 1 0 0 0 0 1 0 1
# 1 0 0 0 0 1 0 1
# 1 1 1 1 1 1 1 1