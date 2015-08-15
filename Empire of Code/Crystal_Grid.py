def get(g,i,j):
    if i<0 or j<0:
        return "Y"
    try:
        return g[i][j]
    except IndexError:
        return "Y"

def check_grid(grid):
    for i in range(len(grid)):
        for j in  range(len(grid[i])):
            c = grid[i][j]
            if c==get(grid,i-1,j) or c==get(grid,i+1,j) or c==get(grid,i,j-1) or c==get(grid,i,j+1) :
                return False
    return True

print(check_grid([["X", "X"], ["X", "X"]]))
