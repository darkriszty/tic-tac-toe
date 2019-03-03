from tkinter import *

class BoardPainter:
    _board_width = 150
    _board_height = 150

    def __init__(self):
        self._tk = Tk()
        self._tk.title("Tic Tac Toe")
        #tk.resizable(False, False)
        self._tk.wm_attributes("-topmost", 1)
        self._canvas = Canvas(self._tk, width=800, height=600, bg="#eeeeee")
        self._canvas.pack()

    def paint(self, board):
        self._paint_empty_board(0, 0)
        for rowIndex in range(len(board)):
            for colIndex in range(len(board[rowIndex])):
                self._paint_sign(board[rowIndex][colIndex], rowIndex, colIndex)
        #self._tk.update_idletasks()
        #self._tk.update()
        self._tk.mainloop()

    def _paint_empty_board(self, x, y):
        self._canvas.create_rectangle(x, y, self._board_width, self._board_height, fill="#dddddd", outline="")
        self._canvas.create_line(self._board_width/3, y, self._board_width/3, self._board_height)
        self._canvas.create_line(self._board_width/1.5, y, self._board_width/1.5, self._board_height)
        self._canvas.create_line(x, self._board_height/3, self._board_width, self._board_height/3)
        self._canvas.create_line(x, self._board_height/1.5, self._board_width, self._board_height/1.5)

    def _paint_sign(self, sign, col, row):
        if sign == "": return
        x = row * self._board_width / 3 + self._board_width / 6
        y = col * self._board_height / 3 + self._board_height / 6
        x1 = x - self._board_width / 10
        y1 = y - self._board_height / 10
        x2 = x + self._board_width / 10
        y2 = y + self._board_height / 10
        if sign == "0":
            self._canvas.create_oval(x1, y1, x2, y2)
        if sign == "X":
            self._canvas.create_line(x1, y1, x2, y2)
            self._canvas.create_line(x2, y1, x1, y2)
    
    def _debug_print(self, text):
        self._canvas.create_text(200, 200, anchor=W, font="Tahoma", text=text)

if __name__ == '__main__':
    painter = BoardPainter()
    painter.paint([
            ["X", "X", "X"],
            ["0", "", "0"],
            ["", "", "X"]
    ])