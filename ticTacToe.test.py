import unittest
import ticTacToe

class TestDoesWin(unittest.TestCase):
    def test_empty_board_no_win(self):
        self.assertFalse(ticTacToe.doesWin([["", "", ""], ["", "", ""], ["", "", ""]], "0"))
        self.assertFalse(ticTacToe.doesWin([["", "", ""], ["", "", ""], ["", "", ""]], "X"))

    def test_draw_no_win(self):
        self.assertFalse(ticTacToe.doesWin([["X", "0", "X"], ["0", "X", "0"], ["0", "X", "0"]], "X"))
        self.assertFalse(ticTacToe.doesWin([["X", "0", "X"], ["0", "X", "0"], ["0", "X", "0"]], "0"))

    def test_first_row_win(self):
        self.assertTrue(ticTacToe.doesWin([
            ["X", "X", "X"],
            ["0", "", "0"],
            ["", "", "X"]],
        "X"))

    def test_second_row_win(self):
        self.assertTrue(ticTacToe.doesWin([
            ["X", "", "X"],
            ["0", "0", "0"],
            ["", "", "X"]],
        "0"))

    def test_thrid_row_win(self):
        self.assertTrue(ticTacToe.doesWin([
            ["X", "", "X"],
            ["0", "", "0"],
            ["0", "0", "0"]],
        "0"))

    def test_diagonal_win(self):
        self.assertTrue(ticTacToe.doesWin([
            ["X", "0", "X"], 
            ["0", "X", "0"], 
            ["", "", "X"]], 
        "X"))

    def test_secondary_diagonal_win(self):
        self.assertTrue(ticTacToe.doesWin([
            ["X", "0", "0"], 
            ["0", "0", "0"], 
            ["0", "", "X"]], 
        "0"))

    def test_first_col_win(self):
        self.assertTrue(ticTacToe.doesWin([
            ["X", "", "X"],
            ["X", "", "0"],
            ["X", "", "X"]],
        "X"))

    def test_second_col_win(self):
        self.assertTrue(ticTacToe.doesWin([
            ["X", "0", "X"],
            ["", "0", "0"],
            ["", "0", "X"]],
        "0"))

    def test_thrid_col_win(self):
        self.assertTrue(ticTacToe.doesWin([
            ["X", "", "0"],
            ["0", "", "0"],
            ["0", "0", "0"]],
        "0"))

    def test_multiple_wins_win(self):
        self.assertTrue(ticTacToe.doesWin([
            ["0", "", "0"],
            ["0", "0", "0"],
            ["0", "0", "0"]],
        "0"))

if __name__ == '__main__':
    unittest.main(exit=False)