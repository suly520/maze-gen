from graphics import Window
from cell import Cell
from maze import Maze

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

    # first_cell = Cell(win)
    # first_cell.has_right = False
    # first_cell.draw(x1=50, y1=50, x2=100, y2=100)

    # second_cell = Cell(win)
    # second_cell.has_bottom = False
    # second_cell.draw(x1=100, y1=50, x2=150, y2=100)

    # third_cell = Cell(win)
    # third_cell.has_bottom = False
    # third_cell.draw(x1=150, y1=50, x2=200, y2=100)
    
    # first_cell.draw_move(second_cell)

    maze = Maze(x1=0, y1=0, num_rows=10, num_cols=10, cell_size_x=20, cell_size_y=20, win=win)

    win.wait_for_close()
