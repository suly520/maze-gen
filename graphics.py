from tkinter import Tk, BOTH, Canvas


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


