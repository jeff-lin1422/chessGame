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

    def getNotation(self):
        return self.getRankFile(self.startRow, self.startCol) + "-" + self.getRankFile(self.endRow, self.endCol)

    def getRankFile(self, r, c):
        return self.colToFiles[c] + self.rowsToRanks[r]