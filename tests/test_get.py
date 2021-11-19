from grid import get_tile

def test_get_tile():
    grid = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    assert get_tile(grid, 0, 0) == 0
    assert get_tile(grid, 1, 1) == 0
    assert get_tile(grid, 2, 2) == 0
    assert get_tile(grid, 0, 1) == 0
    assert get_tile(grid, 1, 0) == 0
    assert get_tile(grid, 2, 1) == 0
    assert get_tile(grid, 1, 2) == 0
    assert get_tile(grid, 2, 0) == 0
    assert get_tile(grid, 0, 2) == 0
    assert get_tile(grid, 2, 0) == 0
    assert get_tile(grid, 0, 2) == 0