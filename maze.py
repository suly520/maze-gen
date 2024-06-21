from cell import Cell
import random
import time





class Maze:
        
    def __init__(self, win, x1, y1, num_cols, num_rows, cell_size_x, cell_size_y, seed=None): 
        self._x1 = x1 + 3
        self._y1 = y1 + 3
        self._win = win
        self._num_cols = num_cols
        self._num_rows = num_rows
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._cells: list[Cell] = None
        self._seed = random.seed(seed) if seed else 0
        self.breaking = False

        self.update_canvas_size()
        self._create_cells()
        self._open_start_and_exit()
        self._break_walls_r()
    
    def reset_maze(self):
        self._reset_cells()
        self._open_start_and_exit()
        self._break_walls_r()
    
    def _reset_cells(self):
        for cell in self._cells:
            cell.boarders["top"]["active"] = True
            cell.boarders["bottom"]["active"] = True
            cell.boarders["right"]["active"] = True
            cell.boarders["left"]["active"] = True
            cell.visited = False
            cell.redraw()
    
    def update_canvas_size(self):
        if not self._win:
            return
        can_width = self._x1 + self._cell_size_x * self._num_cols
        can_height = self._y1 + self._cell_size_y * self._num_rows
        self._win.canvas.configure(width=can_width, height=can_height)
    
    def _create_cells(self):
        self._cells = [Cell(self._win) for _ in range(self._num_rows * self._num_cols)]
        for i, cell in enumerate(self._cells):
            self._draw_cell(index=i, cell=cell)

    def _draw_cell(self, index, cell:Cell):
        cell.row = (index // self._num_cols) + 1
        cell.col = (index % self._num_cols) + 1
        
        if not cell.row == 1:
            cell.boarders["top"]["neighbor"] = self._cells[index-self._num_cols]
        if not cell.col == 1:
            cell.boarders["left"]["neighbor"] = self._cells[index-1]
        if not cell.row == self._num_rows:
            cell.boarders["bottom"]["neighbor"] = self._cells[index+self._num_cols]
        if not cell.col == self._num_cols:
            cell.boarders["right"]["neighbor"] = self._cells[index+1]

        pos_nx = self._x1 + self._cell_size_x * (cell.col - 1)
        pos_ny = self._y1 + self._cell_size_y * (cell.row - 1)
        cell.draw(x1=pos_nx, y1=pos_ny , x2=pos_nx + self._cell_size_x , y2=pos_ny + self._cell_size_y)
        self._animate()

    def _animate(self):
        if not self._win:
            return
        self._win.redraw()
        time.sleep(0.001)
    
    def _open_start_and_exit(self):
        self._cells[0].boarders["left"]["active"] = False
        self._cells[0].redraw()
        self._cells[-1].boarders["right"]["active"] = False
        self._cells[-1].redraw()
        print(self._cells[-1].col)
    
    def _break_wall(self, cell:Cell):
        cell.visited = True
        available_paths = ["top", "right", "bottom", "left"]
        top_neigh = cell.boarders["top"]["neighbor"]
        left_neigh = cell.boarders["left"]["neighbor"]
        bottom_neigh = cell.boarders["bottom"]["neighbor"]
        right_neigh = cell.boarders["right"]["neighbor"]




        if cell.row == 1 or not top_neigh or top_neigh.visited:
            available_paths.remove("top")
        if cell.col == 1 or not left_neigh or left_neigh.visited:
            available_paths.remove("left")
        if cell.row == self._num_rows or not bottom_neigh or bottom_neigh.visited:
            available_paths.remove("bottom")
        if cell.row == self._num_cols-1 or not right_neigh or right_neigh.visited:
            available_paths.remove("right")
        
        if available_paths:
            used_path = random.choice(available_paths)
        else:
            print("stuck there")
            self.reset_maze()
        
        neighbor_cell = cell.boarders[used_path]["neighbor"]

        if cell.row == self._num_cols-1 and cell.row == self._num_rows:
            print("you got it")
            return False

        def get_counter(used_path):
            couter_paths = {"top":"bottom", "bottom":"top", "right":"left", "left":"right",}
            return couter_paths[used_path]

        counter_path = get_counter(used_path)

        cell.boarders[used_path]["active"] = False
        neighbor_cell.boarders[counter_path]["active"] = False
        cell.redraw()
        self._win.redraw()
        time.sleep(0.0001)
        if cell != self._cells[-1] and available_paths:
            self._break_wall(neighbor_cell)
        else:
            return False

    
    def _break_walls_r(self):
        self.breaking = True
        while self.breaking:
            self.breaking = self._break_wall(self._cells[0])


        # if "left" in available_paths and self._cells[index-2].visited:
        #     available_paths.remove("left")
        
        # if "right" in available_paths and self._cells[index].visited:
        #     available_paths.remove("right")
            
        # if "top" in available_paths and self._cells[index-self._num_cols-1].visited:
        #     available_paths.remove("top")

        # if "bottom" in available_paths and self._cells[index+self._num_cols-1].visited:
        #     available_paths.remove("bottom")
        


        
        # for available in available_paths:
            
            
        


