from enum import Enum

#TODO: this class does not make a lot of sense in its current form; refactor/rename/remove
class Game:
    _board = None

    def __init__(self, board):
        self._board = board
        self.nextPlayer = PlayerType.HUMAN

    def addNextMove(self, row, col):
        didAdvance = self._board.setMove(row, col, self._currentPlayerSign())
        if didAdvance: self._switchPlayer()
        return didAdvance

    def isOver(self):
        return self._board.isFull()

    def _currentPlayerSign(self):
        if self.nextPlayer == PlayerType.COMPUTER:
            return "0"
        return "X"

    def _switchPlayer(self):
        if self.nextPlayer == PlayerType.COMPUTER:
            self.nextPlayer = PlayerType.HUMAN
        else:
            self.nextPlayer = PlayerType.COMPUTER

    def move_valid(self, row, col):
        return row != None and col != None and self._board.isEmpty(row, col)



class PlayerType(Enum):
    HUMAN = 1
    COMPUTER = 2