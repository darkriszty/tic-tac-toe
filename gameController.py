from tkinter import Tk, Canvas, messagebox
from game import *
from boardPainter import *
from board import *
from computerPlayer import *
from gameWindow import *

class GameController:
    _allowUserInput = False

    def __init__(self):
        self._gameWindow = GameWindow(self._inputHandler)

    def start(self):
        board = Board()
        self._game = Game(board)
        self._computer = ComputerPlayer(board)
        self._advance()
        self._gameWindow.setBoard(board)

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

    def _inputHandler(self, row, col):
        if not self._allowUserInput: return
        if self._game.move_valid(row, col):
            self._game.addNextMove(row, col)
            self._advance()