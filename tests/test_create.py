from grid import create_grid

def test_create_grid():
    grid = create_grid(2, 2)
    assert grid == [['', ''], ['', '']]