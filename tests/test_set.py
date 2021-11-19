from p_grid import set_tile


def test_set_tile():
    grid = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    assert set_tile(grid, 0, 0, 1) == [[1, 0, 0], [0, 0, 0], [0, 0, 0]]
    assert set_tile(grid, 1, 1, 1) == [[1, 0, 0], [0, 1, 0], [0, 0, 0]]
    assert set_tile(grid, 2, 2, 1) == [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
