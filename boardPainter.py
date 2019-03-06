class BoardPainter:
    _width = 150
    _height = 150
    _canvas = None
    _board = None

    def __init__(self, canvas, board, left, top):
        self._left = left
        self._top = top
        self._canvas = canvas
        self._board = board
        self._canvas.pack()
        self._board.on_next_move = self._paint
        self._paint()

    def translateCoordinates(self, x, y):
        row = 2
        col = 2
        #TODO create the actual mapping
        return row, col

    def _paint(self):
        self._paint_empty_board()
        for rowIndex in range(len(self._board.data)):
            for colIndex in range(len(self._board.data[rowIndex])):
                self._paint_sign(self._board.data[rowIndex][colIndex], colIndex, rowIndex)

    def _paint_empty_board(self):
        self._canvas.create_rectangle(self._left, self._top, self._left + self._width, self._top + self._height, fill="#dddddd", outline="")
        # vertical lines
        self._canvas.create_line(self._left + self._width/3, self._top, self._left + self._width/3, self._top + self._height)
        self._canvas.create_line(self._left + self._width/1.5, self._top, self._left + self._width/1.5, self._top + self._height)
        # horizontal lines
        self._canvas.create_line(self._left, self._top + self._height/3, self._left + self._width, self._top + self._height/3)
        self._canvas.create_line(self._left, self._top + self._height/1.5, self._left + self._width, self._top + self._height/1.5)

    def _paint_sign(self, sign, row, col):
        if sign == "": return
        x = row * self._width / 3 + self._width / 6 + self._left
        y = col * self._height / 3 + self._height / 6 + self._top
        x1 = x - self._width / 10
        y1 = y - self._height / 10
        x2 = x + self._width / 10
        y2 = y + self._height / 10
        if sign == "0":
            self._canvas.create_oval(x1, y1, x2, y2)
        if sign == "X":
            self._canvas.create_line(x1, y1, x2, y2)
            self._canvas.create_line(x2, y1, x1, y2)
