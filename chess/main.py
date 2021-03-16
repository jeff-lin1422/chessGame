import pygame as p
import chess
WIDTH = HEIGHT = 512
DIMENSION = 8
SQUARESIZE = WIDTH//DIMENSION
IMAGES = {} #dictionary of images
"""
because loading images everytime can be expensive, use dictionary to load them in all at first
"""

def loadImages():
    pieces = ["wP","wR","wN","wB","wQ","wK","wB","wN","wR","bR","bN","bB","bQ","bK","bB","bN","bR","bP"]
    for piece in pieces:
        #u can iterate each things without using pieces[1] or pieces[2] cause python is sickkkkkkkkkk
        IMAGES[piece] = p.image.load("images/"+piece+".png")
    #now all images are saved inside, so we can access it like IMAGES["wP"] or IMAGES["bN"]