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
        return self._board.isFull() or self._doesWin("X") or self._doesWin("0")

    def _currentPlayerSign(self):
        if self.nextPlayer == PlayerType.COMPUTER:
            return "0"
        return "X"

    def _switchPlayer(self):
        if self.nextPlayer == PlayerType.COMPUTER:
            self.nextPlayer = PlayerType.HUMAN
        else:
            self.nextPlayer = PlayerType.COMPUTER

    def isMoveValid(self, row, col):
        return row != None and col != None and self._board.isEmpty(row, col)

    def _doesWin(self, sign):
        boardData = self._board.data
        for row in boardData:
            if valuesMatch(row, sign): #check horizontal row
                return True
            for colIndex in range(len(row)):
                if valuesMatch(list(map(lambda x: x[colIndex], boardData)), sign): #check vertical column
                    return True

        #main diagonal
        if valuesMatch([ boardData[i][i] for i in range(len(boardData)) ], sign):
            return True
        #secondary diagonal
        if valuesMatch([ row[-i-1] for i, row in enumerate(boardData) ], sign):
            return True
        return False

def valuesMatch(values, sign):
    return all(sign == v for v in values)

class PlayerType(Enum):
    HUMAN = 1
    COMPUTER = 2