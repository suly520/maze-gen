from graphics import Window
from cell import Cell

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

    first_cell = Cell(x1=50, y1=50, x2=100, y2=100)
    second_cell = Cell(x1=100, y1=50, x2=150, y2=100, bottom=False)
    third_cell = Cell(x1=150, y1=50, x2=200, y2=100, top=False)
    win.draw_cell(first_cell)
    win.draw_cell(second_cell)
    win.draw_cell(third_cell)
    

    win.wait_for_close()
