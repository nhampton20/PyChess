import pygame, time
#from classes import*

#Below are many constants used to load the game

clock = pygame.time.Clock()

screenWidth=480
screenHeight=480
screen = pygame.display.set_mode((screenWidth, screenHeight))
defaultPieceSize = (60,60)

whiteHorseyImage = pygame.image.load("chessPng/whiteKnight.png")
whiteHorseyImage = pygame.transform.scale(whiteHorseyImage, defaultPieceSize)
blackHorseyImage = pygame.image.load("chessPng/blackKnight.png")
blackHorseyImage = pygame.transform.scale(blackHorseyImage, defaultPieceSize)
whiteHorseyRect = whiteHorseyImage.get_rect()
blackHorseyRect = blackHorseyImage.get_rect()

whiteCastleImage = pygame.image.load("chessPng/whiteRook.png")
blackCastleImage = pygame.image.load("chessPng/blackRook.png")
whiteCastleImage = pygame.transform.scale(whiteCastleImage, defaultPieceSize)
blackCastleImage = pygame.transform.scale(blackCastleImage, defaultPieceSize)
whiteCastleRect = whiteCastleImage.get_rect()
blackCastleRect = blackCastleImage.get_rect()

whitePopeImage = pygame.image.load("chessPng/whiteBishop.png")
blackPopeImage = pygame.image.load("chessPng/blackBishop.png")
whitePopeImage = pygame.transform.scale(whitePopeImage, defaultPieceSize)
blackPopeImage = pygame.transform.scale(blackPopeImage, defaultPieceSize)
whitePopeRect = whitePopeImage.get_rect()
blackPopeRect = blackPopeImage.get_rect()

whiteWomanImage = pygame.image.load("chessPng/whiteQueen.png")
blackWomanImage = pygame.image.load("chessPng/blackQueen.png")
whiteWomanImage = pygame.transform.scale(whiteWomanImage, defaultPieceSize)
blackWomanImage = pygame.transform.scale(blackWomanImage, defaultPieceSize)
whiteWomanRect = whiteWomanImage.get_rect()
blackWomanRect = blackWomanImage.get_rect()

whiteManImage = pygame.image.load("chessPng/whiteKing.png")
blackManImage = pygame.image.load("chessPng/blackKing.png")
whiteManImage = pygame.transform.scale(whiteManImage, defaultPieceSize)
blackManImage = pygame.transform.scale(blackManImage, defaultPieceSize)
whiteManRect = whiteManImage.get_rect()
blackManRect = blackManImage.get_rect()

whiteFlunkeyImage = pygame.image.load("chessPng/whitePawn.png")
blackFlunkeyImage = pygame.image.load("chessPng/blackPawn.png")
whiteFlunkeyImage = pygame.transform.scale(whiteFlunkeyImage, defaultPieceSize)
blackFlunkeyImage = pygame.transform.scale(blackFlunkeyImage, defaultPieceSize)
whiteFlunkeyRect = whiteFlunkeyImage.get_rect()
blackFlunkeyRect = blackFlunkeyImage.get_rect()

moveCircleImage = pygame.image.load("chessPng/moveCircle.png")
moveCircleImage = pygame.transform.scale(moveCircleImage, defaultPieceSize)
moveCircleRect = moveCircleImage.get_rect()

class Piece:
    def __init__(self, type) -> None:
        x=type.position["col"]
        y=type.position["row"]
        if type.color == 1:
            if type.__str__()== "p":
                whiteFlunkeyRect.left = x
                whiteFlunkeyRect.top = y
            elif type.__str__()=="r":
                whiteCastleRect.left = x
                whiteCastleRect.top = y
            elif type.__str__()=="n":
                whiteHorseyRect.left = x
                whiteHorseyRect.top = y
            elif type.__str__()=="b":
                whitePopeRect.left = x
                whitePopeRect.top = y
            elif type.__str__()=="q":
                whiteWomanRect.left = x
                whiteWomanRect.top = y
            elif type.__str__()=="k":
                whiteManRect.left = x
                whiteManRect.top = y
        if type.color == -1:
            if type.__str__()== "p":
                blackFlunkeyRect.left = x
                blackFlunkeyRect.top = y
            elif type.__str__()=="r":
                blackCastleRect.left = x
                blackCastleRect.top = y
            elif type.__str__()=="n":
                blackHorseyRect.left = x
                blackHorseyRect.top = y
            elif type.__str__()=="b":
                blackPopeRect.left = x
                blackPopeRect.top = y
            elif type.__str__()=="q":
                blackWomanRect.left = x
                blackWomanRect.top = y
            elif type.__str__()=="k":
                blackManRect.left = x
                blackManRect.top = y
            
            screen.blit(type.img, (x,y))
