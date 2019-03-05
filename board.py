class Board:
    data = None
    on_next_move = lambda: None

    def __init__(self):
        self.data = [
            ["", "", ""],
            ["", "", ""],
            ["", "", ""]
        ]

    def add_next_move(self, row, col, sign):
        if self.data[row][col] != "": return False

        self.data[row][col] = sign
        self.on_next_move()

        return True
