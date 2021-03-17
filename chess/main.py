import pygame as p
import engine

WIDTH = HEIGHT = 512
DIMENSION = 8
SQUARESIZE = WIDTH // DIMENSION
IMAGES = {}  # dictionary of images
FPS = 15
p.init()
"""
because loading images everytime can be expensive, use dictionary to load them in all at first
"""


def loadImages():
    pieces = ["wP", "wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR", "bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR",
              "bP"]
    for piece in pieces:
        # u can iterate each things without using pieces[1] or pieces[2] cause python is sickkkkkkkkkk
        IMAGES[piece] = p.transform.scale(p.image.load("images/" + piece + ".png"), (SQUARESIZE - 3, SQUARESIZE - 3))
    # now all images are saved inside, so we can access it like IMAGES["wP"] or IMAGES["bN"]


def main():
    screen = p.display.set_mode((WIDTH, HEIGHT))  # takes in a tuple and sets a square/rectangle with the given size
    clock = p.time.Clock()
    screen.fill(p.Color("white"))
    gs = engine.gameState()
    print(gs.board)
    loadImages()
    sqSelected = ()  # a tuple of row,column where the user clicked
    playerSelected = []  # 2 tuples, one for the beginning place, other for where the piece go
    # can use this to check if the moves you input it is valid
    running = True
    while running:
        for event in p.event.get():
            if event.type == p.QUIT:
                running = False
            elif event.type == p.MOUSEBUTTONDOWN:
                location = p.mouse.get_pos()  # gets the location of the mouse (x,y)
                column = location[0] // SQUARESIZE
                row = location[1] // SQUARESIZE
                if sqSelected == (row, column): # if user selects the same square, clear it
                    sqSelected = ()
                    playerSelected = []
                else:
                    sqSelected = (row, column)
                    playerSelected.append(sqSelected)
                    if gs.board[row][column] == "--" and len(playerSelected) == 1:
                        playerSelected = []
                        sqSelected = ()
                if len(playerSelected) == 2:
                    move = engine.move(playerSelected[0], playerSelected[1], gs)
                    print(move.getNotation())
                    gs.makeMove(move)
                    # reset after making a move
                    sqSelected = ()
                    playerSelected = []
                    # move the piece to the second square
                    # the clear the selected squares
        drawGameState(screen, gs)
        clock.tick(FPS)
        p.display.flip()


# graphics of the game
def drawGameState(screen, gs):
    drawBoard(screen)  # draw the entire board with squares
    drawPieces(screen, gs)  # draw the pieces on top of the square


def drawBoard(screen):
    colors = [p.Color("white"), p.Color("light gray")]
    for row in range(DIMENSION):
        for column in range(DIMENSION):
            # (row+column)%2 gives u whether its a white space or not
            squareColor = colors[((row + column) % 2)]
            p.draw.rect(screen, squareColor, p.Rect(column * SQUARESIZE, row * SQUARESIZE, SQUARESIZE, SQUARESIZE))


def drawPieces(screen, gs):
    for row in range(DIMENSION):
        for column in range(DIMENSION):
            piece = gs.board[row][column]
            if piece != "--":
                screen.blit(IMAGES[piece], p.Rect(column * SQUARESIZE, row * SQUARESIZE, SQUARESIZE, SQUARESIZE))


if __name__ == "__main__":
    main()
