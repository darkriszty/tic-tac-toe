class ComputerPlayer:
    def __init__(self, board):
        self._board = board

    #TODO: replace with actual logic
    def getNextMove(self):
        for rowIndex in range(len(self._board.data)):
            for colIndex in range(len(self._board.data[rowIndex])):
                if self._board.isEmpty(rowIndex, colIndex):
                    return rowIndex, colIndex
        return None, None