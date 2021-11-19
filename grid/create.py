def create_grid(width, height, default_value=""):
    """
    Creates a grid that is width by height
    """
    grid = []
    for row in range(height):
        grid.append([])
        for column in range(width):
            grid[row].append(default_value)
    return grid