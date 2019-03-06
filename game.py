from enum import Enum

#TODO: this class does not make a lot of sense in its current form; refactor/rename/remove
class Game:
    is_over = False
    _board = None

    def __init__(self, board):
        self.is_over = False
        self._board = board
        self._next_player = PlayerType.HUMAN

    def make_next_move(self):
        #TODO: replace with actual logic
        for rowIndex in range(len(self._board.data)):
            for colIndex in range(len(self._board.data[rowIndex])):
                if self._board.data[rowIndex][colIndex] == "":
                    self._board.add_next_move(rowIndex, colIndex, "0")
                    return

class PlayerType(Enum):
    HUMAN = 1
    COMPUTER = 2