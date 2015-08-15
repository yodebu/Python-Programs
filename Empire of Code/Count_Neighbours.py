#Count Neighbours

def g(grid,i,j):
    if i<0 or j<0:
        return 0
    try:
        return grid[i][j]
    except IndexError:
        return 0

def count_neighbours(grid, r, c):
    return g(grid,r-1,c)+\
            g(grid,r-1,c+1)+\
            g(grid,r,c+1)+\
            g(grid,r+1,c+1)+\
            g(grid,r+1,c)+\
            g(grid,r+1,c-1)+\
            g(grid,r,c-1)+\
            g(grid,r-1,c-1)



print(count_neighbours(((1, 1, 1), (1, 1, 1), (1, 1, 1)), 0, 2))
