from graphics import Line, Point

class Cell:
    def __init__(self, win):
        self.__x1 = None
        self.__y1 = None
        self.__x2 = None
        self.__y2 = None
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.__win = win
        self.visited = False

    def draw(self, x1, y1, x2, y2, fill_color = "black"):
        if self.__win is None:
            return
        # x1, y1 is the top left corner of the cell
        # x2, y2 is the bottom right corner of the cell
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2

        # this assumes that each cell has a x and y coordinate
        # so if the user forgets to input the coordinates, the program will crash

        # Left wall
        line = Line(Point(self.__x1, self.__y1), Point(self.__x1, self.__y2))
        self.__win.draw_line(line, fill_color if self.has_left_wall else "white")
        # Right wall
        line = Line(Point(self.__x2, self.__y1), Point(self.__x2, self.__y2))
        self.__win.draw_line(line, fill_color if self.has_right_wall else "white")
        # Top wall
        line = Line(Point(self.__x1, self.__y1), Point(self.__x2, self.__y1))
        self.__win.draw_line(line, fill_color if self.has_top_wall else "white")
        # Bottom wall
        line = Line(Point(self.__x1, self.__y2), Point(self.__x2, self.__y2))
        self.__win.draw_line(line, fill_color if self.has_bottom_wall else "white")


    def draw_move(self, to_cell, undo=False):
        line = Line(Point(0.5*(self.__x1 + self.__x2), 0.5*(self.__y1 + self.__y2)), 
                    Point(0.5*(to_cell.__x1 + to_cell.__x2), 0.5*(to_cell.__y1 + to_cell.__y2)))
        self.__win.draw_line(line, "red" if not undo else "gray")