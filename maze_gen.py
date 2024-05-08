from tkinter import Tk, BOTH, Canvas
import time


class Window(Tk):

    def __init__(self, width, height):
        super().__init__()
        self.geometry(f"{width}x{height}")
        self.title("Maze generator")
        self.canvas = Canvas()
        self.canvas.pack()
        self.running = True
        self.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.update_idletasks()
        self.update()

    def wait_for_close(self):
        while self.running:
            self.redraw()

    def close(self):
        self.running = False

    def draw_line(self, line, fill_color):
        line.draw(self.canvas, fill_color)
    
    def draw_cell(self, cell, fill_color="black"):
        cell.draw(self.canvas, fill_color)

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def position(self):
        return self.x, self.y

class Line:

    def __init__(self, v1:Point, v2:Point) -> None:
        self.point1 = v1
        self.point2 = v2

    def draw(self, canvas:Canvas, fill_color:str) -> None:
        canvas.create_line(
                self.point1.position(),
                self.point2.position(),
                fill=fill_color,
                width=2
        )

class Cell:
    
    def __init__(self, x1, y1, x2, y2):
        self._point_1 = Point(x1, y1)
        self._point_2 = Point(x2, y1)
        self._point_3 = Point(x2, y2)
        self._point_4 = Point(x1, y2)
        # self._win = win
        self.bottom = True
        self.top = True
        self.right = True
        self.left = True
        self.line_1 = self.line_2 = self.line_3 = self.line_4 = None
    
    def draw(self, canvas, color):
        if self.top:
            self.line_1 = Line(self._point_1, self._point_2)
            self.line_1.draw(canvas, color)
        if self.right:
            self.line_2 = Line(self._point_2, self._point_3)
            self.line_2.draw(canvas, color)
        if self.bottom:
            self.line_3 = Line(self._point_3, self._point_4)
            self.line_3.draw(canvas, color)
        if self.left:
            self.line_4 = Line(self._point_4, self._point_1)
            self.line_4.draw(canvas, color)





if __name__ == '__main__':
    win_x_max = 400
    win_y_max = 400

    win = Window(win_x_max, win_y_max)

    # point_1 = Point(200, 60)
    # point_2 = Point(30, 220)
    # point_3 = Point(320, 180)

    # color_1 = "blue"
    # color_2 = "red"
    # color_3 = "green"

    # line_1 = Line(point_1, point_2)
    # line_2 = Line(point_2, point_3)
    # line_3 = Line(point_1, point_3)

    # win.draw_line(line=line_1, fill_color=color_1)
    # win.draw_line(line=line_2, fill_color=color_2)
    # win.draw_line(line=line_3, fill_color=color_3)

    first_cell = Cell(50, 50, 100, 100)
    win.draw_cell(first_cell)

    win.wait_for_close()
