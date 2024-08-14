from graphics import Window
from maze import Maze

def main():
    win = Window(800, 600)
    maze = Maze(x1 = 10, y1 = 10, num_rows = 5, num_cols = 5, cell_size_x= 30, cell_size_y = 30, win = win)
    maze.solve()
    win.wait_for_close()


if __name__ == "__main__":
    main()
