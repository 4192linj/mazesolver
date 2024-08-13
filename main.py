from graphics import Window
from maze import Maze

def main():
    win = Window(800, 600)
    maze = Maze(10, 10, 3, 3, 30, 30, win)
    win.wait_for_close()


if __name__ == "__main__":
    main()
