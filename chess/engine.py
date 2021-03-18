class gameState():
    def __init__(self):
        #a 2d array representing the board
        self.board = [["bR","bN","bB","bQ","bK","bB","bN","bR"],
                      ["bP","bP","bP","bP","bP","bP","bP","bP"],
                      ["--","--","--","--","--","--","--","bR"],
                      ["--","--","--","--","--","--","--","--"],
                      ["--","--","--","--","--","--","--","--"],
                      ["wR","--","--","--","--","--","--","--"],
                      ["wP","wP","wP","wP","wP","wP","wP","wP"],
                      ["wR","wN","wB","wQ","wK","wB","wN","wR"],
        ]
        self.whiteToMove = True
        self.moveLog = []
        self.getMoves = {'P': self.getPawnMove, 'R': self.getRookMove, 'N': self.getKnightMove, 'B': self.getBishopMove,
                         'K': self.getKingMove, 'Q': self.getQueenMove}
    def makeMove(self, move):
        # take in the move object
        self.board[move.startRow][move.startCol] = "--"
        self.board[move.endRow][move.endCol] = move.pieceMoved
        self.moveLog.append(move)
        self.whiteToMove = not self.whiteToMove  # swap players

    def undoMove(self):
        if len(self.moveLog) != 0:
            ogPiece = self.moveLog.pop()
            self.board[ogPiece.startRow][ogPiece.startCol] = ogPiece.pieceMoved
            self.board[ogPiece.endRow][ogPiece.endCol] = ogPiece.pieceCaptured

    def validMoves(self):
        return self.allPossibleMoves()

    def allPossibleMoves(self):
        self.moves = []
        for row in range(len(self.board)):
            for column in range(len(self.board[row])):
                color = self.board[row][column][0]
                if (color == 'w' and self.whiteToMove) or (color == 'b' and not self.whiteToMove):
                    piece = self.board[row][column][1]
                    self.getMoves[piece](row, column)
        return self.moves
    def getPawnMove(self, row, column):
        if self.whiteToMove:
            if self.board[row-1][column] == "--":
                self.moves.append(move((row,column), (row-1, column), gameState()))
                # need to check for the first pawn move
                if row == 6 and self.board[row-2][column] == "--":
                    self.moves.append(move((row, column), (row-2, column), gameState()))
            # captures
            if column-1 >= 0:
                # left capture
                if self.board[row-1][column-1][0] == 'b':
                    self.moves.append(move((row, column), (row-1, column-1), gameState()))
            if column+1 <= 7:
                # right capture
                if self.board[row-1][column+1][0] == 'b':
                    self.moves.append(move((row, column), (row-1, column+1), gameState()))
                # do en passant
        else:
            if self.board[row+1][column] == "--":
                self.moves.append(move((row,column), (row+1, column), gameState()))
                # need to check for the first pawn move
                if row == 1 and self.board[row+2][column] == "--":
                    self.moves.append(move((row, column), (row+2, column), gameState()))
            # captures
            if column-1 >= 0:
                # left capture
                if self.board[row+1][column-1][0] == 'w':
                    self.moves.append(move((row, column), (row+1, column-1), gameState()))
            # right capture
            if column+1 <= 7:
                if self.board[row+1][column+1][0] == 'w':
                    self.moves.append(move((row, column), (row+1, column+1), gameState()))
                # do en passant
    def getStraightMove(self, row, column, length):
        if self.whiteToMove:
            # going up
            i = row + 1
            while i <= length:
                if self.board[i][column][0] == 'w':
                    break
                else:
                    self.moves.append(move((row, column), (i, column), gameState()))
                    if self.board[i][column][0] == 'b':
                        break
                i += 1
            # going down
            i = row - 1
            while i >= 0:
                if self.board[i][column][0] == 'w':
                    break
                else:
                    self.moves.append(move((row, column), (i, column), gameState()))
                    if self.board[i][column][0] == 'b':
                        break
                i -= 1
            # going right
            i = column + 1
            while i <= length:
                if self.board[row][i][0] == 'w':
                    break
                else:
                    self.moves.append(move((row, column), (row, i), gameState()))
                    if self.board[row][i][0] == 'b':
                        break
                i += 1
            # going left
            i = column - 1
            while i >= 0:
                if self.board[row][i][0] == 'w':
                    break
                else:
                    self.moves.append(move((row, column), (row, i), gameState()))
                    if self.board[row][i][0] == 'b':
                        break
                i -= 1
        else:
            # going up
            i = row + 1
            while i <= length:
                if self.board[i][column][0] == 'b':
                    break
                else:
                    self.moves.append(move((row, column), (i, column), gameState()))
                    if self.board[i][column][0] == 'w':
                        break
                i += 1
            # going down
            i = row - 1
            while i >= 0:
                if self.board[i][column][0] == 'b':
                    break
                else:
                    self.moves.append(move((row, column), (i, column), gameState()))
                    if self.board[i][column][0] == 'w':
                        break
                i -= 1
            # going right
            i = column + 1
            while i <= length:
                if self.board[row][i][0] == 'b':
                    break
                else:
                    self.moves.append(move((row, column), (row, i), gameState()))
                    if self.board[row][i][0] == 'w':
                        break
                i += 1
            # going left
            i = column - 1
            while i >= 0:
                if self.board[row][i][0] == 'b':
                    break
                else:
                    self.moves.append(move((row, column), (row, i), gameState()))
                    if self.board[row][i][0] == 'w':
                        break
                i -= 1
    def getRookMove(self, row, column):
        self.getStraightMove(row, column, len(self.board)-1)

    def getKnightMove(self, row, column):
        pass
    def getBishopMove(self, row, column):
        pass
    def getKingMove(self, row, column):
        pass
    def getQueenMove(self, row, column):
        pass
class move():
    ranksToRows = {"1": 7, "2": 6, "3": 5, "4": 4, "5": 3, "6": 2, "7": 1, "8": 0}
    rowsToRanks = {i: j for j, i in ranksToRows.items()}
    filesToCol = {"a": 0, "b": 1, "c": 2, "d": 3, "e": 4, "f": 5, "g": 6, "h": 7}
    colToFiles = {i: j for j, i in filesToCol.items()}
    def __init__(self, startSq, endSq, gs):
        self.startRow = startSq[0]
        self.startCol = startSq[1]
        self.endRow = endSq[0]
        self.endCol = endSq[1]
        self.pieceMoved = gs.board[self.startRow][self.startCol]
        self.pieceCaptured = gs.board[self.endRow][self.endCol]
        self.moveID = self.getNotation()

    def __eq__(self, other):
        if isinstance(other, move):
            return self.moveID == other.moveID
        return False
    def getNotation(self):
        return self.getRankFile(self.startRow, self.startCol) + "-" + self.getRankFile(self.endRow, self.endCol)

    def getRankFile(self, r, c):
        return self.colToFiles[c] + self.rowsToRanks[r]