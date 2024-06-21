import unittest
from maze import Maze


class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_cols, num_rows, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols*num_rows,
        )
    
    def test_maze_break_entrance_and_exit(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_cols, num_rows, 10, 10)
        self.assertEqual(
            m1._cells[0].boarders["left"]["active"],
            False,
        )
        self.assertEqual(
            m1._cells[-1].boarders["right"]["active"],
            False,
        )

    def test_boarders(self):
        num_cols = 3
        num_rows = 3
        m1 = Maze(0, 0, num_cols, num_rows, 10, 10)
        # test first cell
        self.assertEqual(
            m1._cells[0],
            m1._cells[num_cols].boarders["top"]["neighbor"],
            f"test1: current: {m1._cells[0].row}, {m1._cells[0].col} bottom: {m1._cells[num_cols].row}, {m1._cells[num_cols].col}"
        )   
        # test middle top cell 
        self.assertEqual(
            m1._cells[1],
            m1._cells[num_cols+1].boarders["top"]["neighbor"],
            f"test2: current: {m1._cells[1].row}, {m1._cells[1].col} bottom: {m1._cells[num_cols+1].row}, {m1._cells[num_cols+1].col}"
        )   
        
        # test end coll 
        self.assertEqual(
            m1._cells[num_cols-2],
            m1._cells[num_cols-1].boarders["left"]["neighbor"],
            f"test3: current: {m1._cells[num_cols-2].row}, {m1._cells[num_cols-2].col} right: {m1._cells[num_cols-1].row}, {m1._cells[num_cols-1].col}"
        )   
        # test fisrt cell second row
        self.assertEqual(
            m1._cells[num_cols+1],
            m1._cells[num_cols+2].boarders["left"]["neighbor"],
            f"test4: current: {m1._cells[0].row}, {m1._cells[0].col} bottom: {m1._cells[num_cols].row}, {m1._cells[num_cols].col}"
        )   
        
        
        


if __name__ == "__main__":
    unittest.main()










