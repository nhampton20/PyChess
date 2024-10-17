import pygame, os
from pieces import Piece

# Helper function to calculate size and position for the board squares
def getBoardSquareInfo(screen: pygame.Surface, numSides: int) -> tuple[float, float, float]:
    width, height = screen.get_size()
    rectSize = min(width, height) / numSides
    rectColPos = (width - rectSize * numSides) / 2
    rectRowPos = (height - rectSize * numSides) / 2
    return rectSize, rectColPos, rectRowPos

# Place pieces on the board in their starting position
def addStartingPieces(numSides: int) -> list[list[Piece]]:
    def Place(pieceType: str, row: int, col: int, isFourWay: bool) -> None:
        # Calculate mirrored row and column positions
        row = [row, numSides - row - 1]
        col = [col, numSides - col - 1]
        
        # Place black and white pieces
        pieces[row[0]][col[0]] = Piece.createPiece(pieceType, "black", (col[0], row[0]))
        pieces[row[1]][col[0]] = Piece.createPiece(pieceType, "white", (col[0], row[1]))
        if isFourWay: # if four-way symmetry applies, place those pieces too
            pieces[row[0]][col[1]] = Piece.createPiece(pieceType, "black", (col[1], row[0]))
            pieces[row[1]][col[1]] = Piece.createPiece(pieceType, "white", (col[1], row[1]))
    
    pieces = [[None for _ in range(numSides)] for _ in range(numSides)] # Empty board initialization
    
    # Place pieces in their starting position
    Place("king", 0, int(numSides // 2), False)
    Place("queen", 0, int(numSides // 2 - 1), False)
    Place("rook", 0, 0, True)
    Place("knight", 0, 1, True)
    Place("bishop", 0, 2, True)
    # Place pawns in the second row on both sides
    for i in range(numSides):
        Place("pawn", 1, i, False)
        
    return pieces

# Draw the board, pieces, and valid moves
def drawBoardPiecesMoves(screen: pygame.Surface, pieces: list[list[Piece]], moveSet: list[tuple[int, int]], numSides: int) -> None:
    screen.fill("gray50") # Backgound color
    
    # Calculate size and position for the board squares
    rectSize, rectColPos, rectRowPos = getBoardSquareInfo(screen, numSides)
    
    for row in range(numSides):
        for col in range(numSides):
            # Create a rectangle for the current board square
            drawRect = pygame.Rect(rectColPos + col * rectSize, rectRowPos + row * rectSize, rectSize, rectSize)
            
            # Draw the board square
            color = "gray20" if (row + col) % 2 else "gray80"
            pygame.draw.rect(screen, color, drawRect, 0, int(rectSize / 10))
            
            # If there is a piece on that square, draw it
            if pieces[row][col]:
                pieceImage = pygame.image.load(pieces[row][col].pieceImage)
                pieceImage = pygame.transform.scale(pieceImage, (rectSize, rectSize))
                screen.blit(pieceImage, drawRect)
                
            # If the square is a valid move piece, draw an indicator to show that
            if (col, row) in moveSet:
                image = os.path.join(os.path.dirname(__file__), "chessPNGs", "moveCircle.png")
                pieceImage = pygame.image.load(image)
                pieceImage = pygame.transform.scale(pieceImage, (rectSize, rectSize))
                screen.blit(pieceImage, drawRect)
                
    return

# Get the column and row of the board from a mouse click position
def getMousePos(screen: pygame.Surface, currPos: list[tuple[int, int]], numSides: int) -> tuple[int, int]:
    # Calculate size and position for the board squares
    rectSize, rectColPos, rectRowPos = getBoardSquareInfo(screen, numSides)
    
    # Calculate the row and column based on the mouse click position
    row = int((currPos[1] - rectRowPos) // rectSize)
    col = int((currPos[0] - rectColPos) // rectSize)
    
    return (col, row)

# Print the game results and determine the winner
def printResults(score: dict[str, int]) -> None:
    # Print score for both players
    for color, value in score.items():
        print(f"{color}: {value}", end = "\t")
    print()
    
    # Print the winner
    if score["white"] > score["black"]:
        print("White wins!")
    elif score["black"] > score["white"]:
        print("Black wins!")
    else:
        print("It's a draw!")