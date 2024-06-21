from tkinter import Tk, BOTH, Canvas
import math


class Window(Tk):

    def __init__(self, width, height, canvas_bg="white"):
        super().__init__()
        self.geometry(f"{width}x{height}")
        self.title("Maze generator")
        self.canvas_bg = canvas_bg
        self.canvas = Canvas(background=self.canvas_bg)
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

    def draw_line(self, line, fill_color="black"):
        line.draw(self.canvas, fill_color)

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def position(self):
        return self.x, self.y
    
    def get_distance_to(self, other_point):
        return math.sqrt(abs(other_point.x - self.x)**2 + abs(other_point.y - self.y))
    

class Line:

    def __init__(self, v1:Point, v2:Point) -> None:
        self.point1 = v1
        self.point2 = v2
        self.color = None

    def draw(self, canvas:Canvas, fill_color:str) -> None:
        self.color = fill_color
        canvas.create_line(
                self.point1.position(),
                self.point2.position(),
                fill=fill_color,
                width=2
        )
    
    def get_middle_point(self):
        return Point(abs(self.point1.x + ((self.point2.x - self.point1.x) // 2)), abs(self.point1.y + ((self.point2.y - self.point1.y) // 2)))
    
    def get_lenght(self):
        return self.point1.get_distance_to(self.point2)



