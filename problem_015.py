def lattice_paths(grid_size):
    n = grid_size + 1
    grid = [[0] * n for _ in range(n)]
    for i in range(n):
        grid[i][-1] = 1
        grid[-1][i] = 1
    
    for i in range(2, n + 1):
        for j in range(2,n + 1):
            grid[-i][-j] = grid[-i][-j + 1] + grid[-i + 1][-j]
    
    return grid[0][0]

print(lattice_paths(20))