import pygame
from pieces import Piece, King, Queen, Rook, Knight, Bishop, Pawn
from chessFunctions import addStartingPieces, drawBoardPiecesMoves, getMousePos, printResults

# Track score
score = {"white": 0, "black": 0}

# Environment variables
width = height = 600 # Window size
numSides = 8 # Number of squares per side

# Create window and add pieces to the board
screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)
pieces = addStartingPieces(numSides) # Initial piece configuration
moveSet = [] # Valid moves for selected piece
selectedPiecePos = (-1, -1) # Position of selected piece
turn = "white"

# Initialize Pygame
pygame.init()

# Draw Initial Board
drawBoardPiecesMoves(screen, pieces, moveSet, numSides) # Redraw the board with updated positions
pygame.display.flip() # Refresh the screen

# Game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            running = False # Exit game if window is closed

        if event.type == pygame.VIDEORESIZE:
            drawBoardPiecesMoves(screen, pieces, moveSet, numSides) # Redraw the board with updated positions
            pygame.display.flip() # Refresh the screen
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Get the clicked position on the board
            col, row = currPos = getMousePos(screen, pygame.mouse.get_pos(), numSides)

            if currPos in moveSet:
                oldCol, oldRow = selectedPiecePos
                if pieces[row][col]:
                    score[pieces[oldRow][oldCol].getColor()] += pieces[row][col].getValue() # Modify score if piece is captured
                
                # If a pawn reaches the last row, turn it to a queen
                if row in [0, numSides - 1] and pieces[oldRow][oldCol].getType() == "pawn":
                    pieces[row][col] = Piece.createPiece("queen", pieces[oldRow][oldCol].getColor(), (col, row))
                else:
                    pieces[row][col] = pieces[oldRow][oldCol] # Move the piece
                pieces[oldRow][oldCol] = None # Remove the piece from the old position
                moveSet = [] # Clear the valid moves after moving
                
                # Switch turn
                turn = {"black": "white", "white": "black"}[turn]
                
            elif pieces[row][col] and pieces[row][col].getColor() == turn:
                moveSet = pieces[row][col].possibleMoves(pieces, currPos, numSides) # Store the valid moves for the selected piece
                selectedPiecePos = currPos # Store the position of the selected piece
                
            else:
                moveSet = [] # empty moveSet
            drawBoardPiecesMoves(screen, pieces, moveSet, numSides) # Redraw the board with updated positions
            pygame.display.flip() # Refresh the screen
    

# Print the final score and determine the winnder
printResults(score)

# Close Pygame
pygame.quit()

'''
To Do List

Take everything within mousebuttondown event and move it to a function in chessFunctions: handleMousePress()
Show the winner on screen
Make the scoring system better
Castling
Undo
Implement a menu of some sort that allows for a new game
    This could have options and a lot of settings
Time Consuming / Difficult : implement system to check for when a king is in check and don't allow moves except to get out of check
Obviously, check for checkmate as well
'''