from tkinter import Tk, Canvas
from game import *
from boardPainter import *
from board import *

#TODO: maybe a separate window handler can be extracted from this class
class GameController:
    _tk = None
    _canvas = None
    _allowUserInput = False

    def __init__(self):
        tk = Tk()
        tk.title("Tic Tac Toe")
        #tk.resizable(False, False)
        tk.wm_attributes("-topmost", 1)
        tk.bind("<Button 1>", self._click_handler)
        
        self._canvas = Canvas(tk, width=800, height=600, bg="#eeeeee")
        self._tk = tk

    def run(self):
        self._board = Board()
        self._game = Game(self._board)
        self._boardPainter = BoardPainter(self._canvas, self._board, 50, 50)
        self._advance()
        self._tk.mainloop()

    def _advance(self):
        if self._game.is_over:
            self._allowUserInput = False
            return

        if self._game._next_player == PlayerType.COMPUTER:
            self._allowUserInput = False
            self._game.make_next_move()
            self._game._next_player = PlayerType.HUMAN
            self._allowUserInput = True
        else:
            self._allowUserInput = True

    def _click_handler(self, eventorigin):
        if not self._allowUserInput: return
        row, col = self._boardPainter.translateCoordinates(eventorigin.x, eventorigin.y)
        if self._user_selection_valid(row, col):
            self._board.add_next_move(row, col, "X")
            self._game._next_player = PlayerType.COMPUTER
            self._advance()
    
    def _user_selection_valid(self, row, col):
        return row != None and col != None and self._game.is_empty(row, col)

