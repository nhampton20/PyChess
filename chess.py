import sys, pygame
import classes
from gameboard import board
from chessPieces import*


"""y = board(8)

movelist = y.area[5][1].move()
print(movelist)

y.movePiece([5,1], [movelist[0],movelist[1]])

y.movePiece([6,6], [6,4])

movelist = y.area[5][3].move()
print(movelist)
y.movePiece([5,3],[6,4])

for i in range(len(y.area)):
    for j in range(len(y.area[i])):
        print(y.area[j][i], end=" ")
    print()"""
game=board()
moveBoard=board()
moveBoard.clear()
pygame.init()
gameOn=True
update=True
size = width, height = 480, 480
screen = pygame.display.set_mode(size)
background = pygame.image.load("chessPng/Chess_Board.png")
background = pygame.transform.scale(background, size)
#background = pygame.transform.rotate(background, 90 )
place = (0,60)
while gameOn:
    clock
    for event in pygame.event.get():
        if event.type == pygame.QUIT: print("White score: " + str(game.whiteScore) + "\nBlack score: " + str(game.blackScore)) & sys.exit()
    
    if pygame.mouse.get_pressed()[0]:
        mouse=pygame.mouse.get_pos()
        pygame.event.clear()
        if moveBoard.area[int(mouse[0]/60)][int(mouse[1]/60)]!=0:
            game.movePiece(game.selected, [int(mouse[0]/60),int(mouse[1]/60)])
            update=True
            moveBoard.clear()

        elif (game.area[int(mouse[0]/60)][int(mouse[1]/60)]!=0):
            moveBoard.clear()
            #update=True
            moves=game.moveList([int(mouse[0]/60),int(mouse[1]/60)])
            for i in range(0,int(len(moves)/2),2):
                moveBoard.addPiece(5, [moves[i],moves[i+1]])
                screen.blit(moveBoard.area[moves[i]][moves[i+1]].img, (moves[i]*60, moves[i+1]*60))

    if(update):
        screen.blit(background, (0, 0))
        for i in range(len(game.area)):
            for j in range(len(game.area[i])):
                if(game.area[j][i]!=0):
                    screen.blit(game.area[j][i].img, (j*60, i*60))
        update=False
    
    pygame.display.flip()

"""The board should keep a record of the postion of the pieces, 
but each piece should also know where itself is, move should return an array of index locations that it can move to, 
not bothering to check if there is anything in the way. Then the board should filter out any locations that are blocked by another piece.
Clicking on a piece highlights where it can go. Clicking on a highlighted spot should move it there (no animations that is too hard)
pawn are going to be special because their moveset changes depending on if there is angled to them, 
so they should always return the three spots in from of them and on the first move the one two spots ahead as well. 
Let the board filter out what is not allowed """