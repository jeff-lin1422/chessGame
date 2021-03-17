class gameState():
    def __init__(self):
        #a 2d array representing the board
        self.board = [["bR","bN","bB","bQ","bK","bB","bN","bR"],
                      ["bP","bP","bP","bP","bP","bP","bP","bP"],
                      ["--","--","--","--","--","--","--","--"],
                      ["--","--","--","--","--","--","--","--"],
                      ["--","--","--","--","--","--","--","--"],
                      ["--","--","--","--","--","--","--","--"],
                      ["wP","wP","wP","wP","wP","wP","wP","wP"],
                      ["wR","wN","wB","wQ","wK","wB","wN","wR"],
        ]
        self.whiteToMove = True;
        self.moveLog = []
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
        moves = [move((6,4),(4,4),gameState())]
        for row in range(len(self.board)):
            for column in range(len(self.board[row])):
                color = self.board[row][column][0]
                if (color == 'w' and self.whiteToMove) or (color == 'b' and not self.whiteToMove):
                    piece = self.board[row][column][1]
                    if piece == 'P':
                        pass
                    elif piece == 'R':
                        pass
                    elif piece == 'N':
                        pass
                    elif piece == 'B':
                        pass
                    elif piece == 'Q':
                        pass
                    elif piece == 'K':
                        pass
        return moves
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