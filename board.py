class Board:
    data = None
    on_next_move = lambda: None

    def __init__(self):
        self.data = [
            ["", "", ""],
            ["", "", ""],
            ["", "", ""]
        ]

    def setMove(self, row, col, sign):
        if self.data[row][col] != "": return False

        self.data[row][col] = sign
        self.on_next_move()

        return True

    def isEmpty(self, row, col):
        return self.data[row][col] == ""

    def isFull(self):
        for rowIndex in range(len(self.data)):
            for colIndex in range(len(self.data[rowIndex])):
                if self.isEmpty(rowIndex, colIndex):
                    return False
        return True