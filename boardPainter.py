from tkinter import *

class BoardPainter:
    _width = 150
    _height = 150

    def __init__(self, left, top):
        self._left = left
        self._top = top
        #TODO extract the window creation from here

        self._tk = Tk()
        self._tk.title("Tic Tac Toe")
        #tk.resizable(False, False)
        self._tk.wm_attributes("-topmost", 1)
        self._canvas = Canvas(self._tk, width=800, height=600, bg="#eeeeee")
        self._canvas.pack()

    def paint(self, board):
        self._paint_empty_board()
        for rowIndex in range(len(board)):
            for colIndex in range(len(board[rowIndex])):
                self._paint_sign(board[rowIndex][colIndex], colIndex, rowIndex)
        #self._tk.update_idletasks()
        #self._tk.update()
        self._tk.mainloop()

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

if __name__ == '__main__':
    painter = BoardPainter(50, 50)
    painter.paint([
            ["X", "X", "X"],
            ["0", "", "0"],
            ["", "", "X"]
    ])