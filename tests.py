import unittest
from maze import Maze


class TestMaze(unittest.TestCase):
    def test_maze_create_cells(self):
        maze = Maze(x1 = 10, y1 = 10, num_rows = 10, num_cols = 10, cell_size_x = 30, cell_size_y = 30)
        
        # Test the number of rows and columns
        self.assertEqual(maze.num_rows, 10)
        self.assertEqual(maze.num_cols, 10)
        # Test the cell size
        self.assertEqual(maze.cell_size_x, 30)
        self.assertEqual(maze.cell_size_y, 30)

    def test_maze_entrance_and_exit(self):
        maze = Maze(x1 = 0, y1 = 0, num_rows = 10, num_cols = 10, cell_size_x = 30, cell_size_y = 30)
        self.assertEqual(maze._cells[0][0].has_top_wall, False)
        self.assertEqual(maze._cells[-1][-1].has_bottom_wall, False)

    def test_maze_cells_reset(self):
        maze = Maze(x1 = 0, y1 = 0, num_rows = 10, num_cols = 10, cell_size_x = 30, cell_size_y = 30)
        for i in range(maze.num_rows):
            for j in range(maze.num_cols):
                self.assertEqual(maze._cells[i][j].visited, False)

if __name__ == "__main__":
    unittest.main()