import time
from cell import Cell

class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self.__cells = []
        self.__create_cells()

    def __create_cells(self):
        self.__cells = [[Cell(self.win) for j in range(self.num_cols)] for i in range(self.num_rows)]
        for i in range(self.num_rows):
            for j in range(self.num_cols):
                self._draw_cell(i, j)

    def _draw_cell(self, i, j):
        # x1, y1 is the top left corner of the Maze itself
        self.__cells[i][j].draw(x1 = self.x1 + i * self.cell_size_x, 
                                y1 = self.y1 + j * self.cell_size_y, 
                                x2 = self.x1 + (i + 1) * self.cell_size_x, 
                                y2 = self.y1 + (j + 1) * self.cell_size_y)
    
    def __animate(self):
        self.win.redraw()
        time.sleep(0.05)