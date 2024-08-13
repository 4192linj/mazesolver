import time
from cell import Cell

class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win = None):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self._cells = []

        self._create_cells()
        self._break_entrance_and_exit()

    def _create_cells(self):
        self._cells = [[Cell(self.win) for j in range(self.num_cols)] for i in range(self.num_rows)]
        for i in range(self.num_rows):
            for j in range(self.num_cols):
                self._draw_cell(i, j)

    def _draw_cell(self, i, j):
        if self.win is None:
            return
        # x1, y1 is the top left corner of the Maze itself
        self._cells[i][j].draw(x1 = self.x1 + i * self.cell_size_x, 
                                y1 = self.y1 + j * self.cell_size_y, 
                                x2 = self.x1 + (i + 1) * self.cell_size_x, 
                                y2 = self.y1 + (j + 1) * self.cell_size_y)
        self._animate()
    
    def _animate(self):
        if self.win is None:
            return
        self.win.redraw()
        time.sleep(0.05)

    def _break_entrance_and_exit(self):
        # Entrance is always at the top left corner
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0, 0)
        # Exit is always at the bottom right corner
        self._cells[-1][-1].has_bottom_wall = False
        self._draw_cell(self.num_rows - 1, self.num_cols - 1)