def np(x, y):
    """
    Count all simple paths (backtracking)
    from the bottom left (coordinate (x-1, 0))
    to the top right (coordinate (0, y-1))
    of an x*y grid. Each cell may be visited only once.
    
    Example: np(2,3) should return 38.
    """
    # Create an  grid to track visited cells.
    visited = [[False] * y for _ in range(x)]
    # Valid Moves
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    #Endpoint
    target = (0, y - 1)

    # Debugging array to track paths
    debug_paths = []

    def dfs(i, j, path):
        # If we reached the target, we found one valid path.
        if (i, j) == target:
            debug_paths.append(path + [(i, j)])  # Add the path to debug array
            return 1
        visited[i][j] = True
        total_paths = 0
        for di, dj in directions:
            ni, nj = i + di, j + dj
            # Check bounds and that we haven't visited the cell.
            if 0 <= ni < x and 0 <= nj < y and not visited[ni][nj]:
                total_paths += dfs(ni, nj, path + [(i, j)])
        visited[i][j] = False  # Backtrack.
        return total_paths

    total_paths = dfs(x - 1, 0, [])
    print("Debugging paths:", debug_paths)  # Print all paths for debugging
    return total_paths

# Test for a 2x3 grid.
result = np(2, 3)
print("Number of all paths in a 2x3 grid:", result)  # Expected output: 38