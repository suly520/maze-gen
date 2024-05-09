from graphics import Point, Line

class Cell:
    
    def __init__(self, x1, y1, x2, y2, top=True, bottom=True, right=True, left=True):
        self._point_1 = Point(x1, y1)
        self._point_2 = Point(x2, y1)
        self._point_3 = Point(x2, y2)
        self._point_4 = Point(x1, y2)
        # self._win = win
        self.top = top
        self.bottom = bottom
        self.right = right
        self.left = left
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

    def draw_move(self, to_cell, undo=False):

