import time
import random
from cell import Cell

class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win = None, seed = None):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self.seed = seed
        self._cells = []

        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
        self._reset_cells_visited()

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

    def _break_walls_r(self, i, j): # recursive function to break walls
        random.seed(self.seed) if self.seed else random.seed()

        self._cells[i][j].visited = True
        while True:
            need_to_visit = []
            # Check if the cell to the left has been visited
            if i > 0 and not self._cells[i - 1][j].visited:
                need_to_visit.append((i - 1, j))
            # Check if the cell to the right has been visited
            if i < self.num_rows - 1 and not self._cells[i + 1][j].visited:
                need_to_visit.append((i + 1, j))
            # Check if the cell above has been visited
            if j > 0 and not self._cells[i][j - 1].visited:
                need_to_visit.append((i, j - 1))
            # Check if the cell below has been visited  
            if j < self.num_cols - 1 and not self._cells[i][j + 1].visited:
                need_to_visit.append((i, j + 1))
            if len(need_to_visit) == 0:
                break
            next_x, next_y = random.choice(need_to_visit)
            
            # Break the wall between the current cell and the next cell
            if next_x == i - 1: # move left
                self._cells[i][j].has_left_wall = False
                self._cells[i - 1][j].has_right_wall = False
            elif next_x == i + 1: # move right
                self._cells[i][j].has_right_wall = False
                self._cells[i + 1][j].has_left_wall = False
            elif next_y == j - 1: # move up
                self._cells[i][j].has_top_wall = False
                self._cells[i][j - 1].has_bottom_wall = False
            elif next_y == j + 1: # move down
                self._cells[i][j].has_bottom_wall = False
                self._cells[i][j + 1].has_top_wall = False
            
            self._draw_cell(i, j)
            self._break_walls_r(next_x, next_y)

    def _reset_cells_visited(self):
        for i in range(self.num_rows):
            for j in range(self.num_cols):
                self._cells[i][j].visited = False

    def solve(self):
        return self._solve_r(0, 0)
    def _solve_r(self, i, j):
        self._animate()
        self._cells[i][j].visited = True
        if i == self.num_rows - 1 and j == self.num_cols - 1:
            return True
        
        # Check each direction
        # Move left
        # Check if there's a cell to the left and if it has a right wall and if it has been visited
        if i > 0 and not self._cells[i - 1][j].has_right_wall and not self._cells[i - 1][j].visited:
            self._cells[i][j].draw_move(self._cells[i - 1][j])
            if self._solve_r(i - 1, j):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i - 1][j], undo = True)
        # Move right
        if i < self.num_rows - 1 and not self._cells[i + 1][j].has_left_wall and not self._cells[i + 1][j].visited:
            self._cells[i][j].draw_move(self._cells[i + 1][j])
            if self._solve_r(i + 1, j):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i + 1][j], True)
        # Move up
        if j > 0 and not self._cells[i][j - 1].has_bottom_wall and not self._cells[i][j - 1].visited:
            self._cells[i][j].draw_move(self._cells[i][j - 1])
            if self._solve_r(i, j - 1):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i][j - 1], True)
        # Move down
        if j < self.num_cols - 1 and not self._cells[i][j + 1].has_top_wall and not self._cells[i][j + 1].visited:
            self._cells[i][j].draw_move(self._cells[i][j + 1])
            if self._solve_r(i, j + 1):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i][j + 1], True)
        return False