from graphics import Window, Point, Line

def main():
    win = Window(800, 600)
    l = Line(Point(30,50), Point(100,200))
    win.draw_line(l, "black")
    win.wait_for_close()


if __name__ == "__main__":
    main()
