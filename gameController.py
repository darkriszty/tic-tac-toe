from tkinter import Tk, Canvas, messagebox
from game import *
from boardPainter import *
from board import *
from computerPlayer import *

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
        tk.bind("<Button 1>", self._clickHandler)
        
        self._canvas = Canvas(tk, width=800, height=600, bg="#eeeeee")
        self._tk = tk

    def start(self):
        board = Board()
        self._game = Game(board)
        self._boardPainter = BoardPainter(self._canvas, board, 50, 50)
        self._computer = ComputerPlayer(board)
        self._advance()
        self._tk.mainloop()

    def _advance(self):
        #this should be a callback that the player types can call?
        if self._game.isOver():
            self._allowUserInput = False
            messagebox.showinfo("Title", "Game over")
            self.start()
            return

        if self._game.nextPlayer == PlayerType.COMPUTER:
            self._allowUserInput = False
            row, col = self._computer.getNextMove()
            self._game.addNextMove(row, col)
            self._allowUserInput = True
        else:
            self._allowUserInput = True

    def _clickHandler(self, eventorigin):
        if not self._allowUserInput: return
        row, col = self._boardPainter.translateCoordinates(eventorigin.x, eventorigin.y)
        if self._game.move_valid(row, col):
            self._game.addNextMove(row, col)
            self._advance()
