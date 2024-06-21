from graphics import Point, Line
import math

class Cell:
    
    def __init__(self, win=None):
        # self._point_1 = self._point_2 = self._point_3 = self._point_4 = None
        self.line_1 = self.line_2 = self.line_3 = self.line_4 = None
        self._win = win
        self.boarders = {
                "top": {"active": True, "neighbor": None},
                "right": {"active": True, "neighbor": None},
                "bottom": {"active": True, "neighbor": None},
                "left": {"active": True, "neighbor": None}
            }
        self.visited = False
        self.row = None
        self.col = None
    
    def draw(self, x1, y1, x2, y2, color="black"):
        if not self._win:
            return
        self.line_1 = Line(Point(x1, y1), Point(x2, y1))
        self.line_2 = Line(Point(x2, y1), Point(x2, y2))
        self.line_3 = Line(Point(x2, y2), Point(x1, y2))
        self.line_4 = Line(Point(x1, y2), Point(x1, y1))
        self.redraw(color)


    def redraw(self, active_color="black", default_color=None):
        if not self._win:
            return
        default_color = self._win.canvas_bg if not default_color else default_color
        sides = [
            ("top", self.line_1),
            ("right", self.line_2),
            ("bottom", self.line_3),
            ("left", self.line_4)
        ]

        for side, line in sides:
            self._win.draw_line(line, active_color if self.boarders[side]["active"] else default_color)
    
    def draw_move(self, to_cell, undo=False):
        color = "red"
        if undo:
            color = "gray"
        
        line = Line(self.get_center(), to_cell.get_center())
        self._win.draw_line(line, color)
    
    def get_center(self):
        diag_line = Line(self.line_1.point1, self.line_2.point2)
        return diag_line.get_middle_point()

