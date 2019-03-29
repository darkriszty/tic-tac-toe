from tkinter import Tk, Canvas, messagebox
from boardPainter import *

class GameWindow:
    _allowUserInput = False

    def __init__(self, inputCallback):
        self._inputCallback = inputCallback
        tk = Tk()
        tk.title("Tic Tac Toe")
        #tk.resizable(False, False)
        tk.wm_attributes("-topmost", 1)
        tk.bind("<Button 1>", self._clickHandler)

        self._canvas = Canvas(tk, width=800, height=600, bg="#eeeeee")
        self._tk = tk
        self._boardPainter = BoardPainter(self._canvas, 50, 50)

    def setBoard(self, board):
        self._boardPainter.setBoard(board)
        self._tk.mainloop()

    def _clickHandler(self, eventorigin):
        row, col = self._boardPainter.translateCoordinates(eventorigin.x, eventorigin.y)
        self._inputCallback(row, col)
