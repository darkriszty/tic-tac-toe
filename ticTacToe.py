def nextMove(board, ownSign):
    return 1

def doesWin(board, sign):
    for row in board:
        if valuesMatch(row, sign): #check horizontal row
            return True
        for colIndex in range(len(row)):
            if valuesMatch(list(map(lambda x: x[colIndex], board)), sign): #check vertical column
                return True

    #main diagonal
    if valuesMatch([ board[i][i] for i in range(len(board)) ], sign):
        return True
    #secondary diagonal
    if valuesMatch([ row[-i-1] for i, row in enumerate(board) ], sign):
        return True
    return False


def valuesMatch(values, sign):
    return all(sign == v for v in values)

def printBoard(board):
    for row in board:
        for v in row:
            value = (v, " ")[v == ""]
            print(value, "| " , end="")
        print()
