import os

# Base class for all chess pieces
class Piece():
    def __init__(self, type: str, color: str, startPos: tuple[int, int], value: int):
        self.type = type # Type of chess piece
        self.color = color # White or Black
        self.pieceImage = os.path.join(os.path.dirname(__file__), "chessPNGs", f"{color}{type}.png") # Image file path
        self.startPos = startPos # Initial position
        self.value = value # Piece value for scoring
    
    def __str__(self) -> str:
        return self.color + " " + self.type
    
    def getType(self) -> str:
        return self.type
    
    def getColor(self) -> str:
        return self.color
    
    def getValue(self) -> int:
        return self.value
    
    # Create specific pieces from the Piece class by passing in piece type
    @staticmethod
    def createPiece(type: str, color: str, startPos: tuple[int, int]) -> "Piece":
        type = type.lower()
        pieceMap = {
            "king": King,
            "queen": Queen,
            "rook": Rook,
            "knight": Knight,
            "bishop": Bishop,
            "pawn": Pawn
        }
        return pieceMap[type](type, color, startPos)

    # Placeholder for specific implementations
    def possibleMoves(self, pieces: list[list["Piece"]], currPos: tuple[int, int], numSides: int) -> list[tuple[int, int]]:
        return

# Helper function to calculate directional moves (used by everything except pawn)
def getDirectionalMoves(self: Piece, pieces: list[list["Piece"]], currPos: tuple[int, int], directions: list[tuple[int, int]], maxDistance: int, numSides: int) -> list[tuple[int, int]]:
    moveSet = []
    blocked = [False] * len(directions)
    
    # Explore each direction until blocked or maxDistance is reached
    distance = 0
    while not all(blocked) and distance < maxDistance:
        distance += 1
        for index, (rowDirection, colDirection) in enumerate(directions):
            if not blocked[index]:
                row, col = currPos[1] + rowDirection * distance, currPos[0] + colDirection * distance
                
                if not (0 <= row < numSides and 0 <= col < numSides):
                    blocked[index] = True # Out of bounds
                elif pieces[row][col]:
                    if pieces[row][col].color != self.color:
                        moveSet.append((col, row)) # Capture enemy piece
                    blocked[index] = True # Stop further moves in this direction
                else:
                    moveSet.append((col, row)) # Valid empty space
                    
    return moveSet

class King(Piece):
    def __init__(self, type: str, color: str, startPos: tuple[int, int]):
        super().__init__(type, color, startPos, value = float("inf"))
        
    # One move in all directions
    def possibleMoves(self, pieces: list[list[Piece]], currPos: tuple[int, int], numSides: int) -> list[tuple[int, int]]:
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)]
        return getDirectionalMoves(self, pieces, currPos, directions, 1, numSides)

class Queen(Piece):
    def __init__(self, type: str, color: str, startPos: tuple[int, int]):
        super().__init__(type, color, startPos, value = 9)
    
    # Infinite moves in all directions
    def possibleMoves(self, pieces: list[list[Piece]], currPos: tuple[int, int], numSides: int) -> list[tuple[int, int]]:
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)]
        return getDirectionalMoves(self, pieces, currPos, directions, numSides, numSides)

class Rook(Piece):
    def __init__(self, type: str, color: str, startPos: tuple[int, int]):
        super().__init__(type, color, startPos, value = 5)
        
    # Infinite moves in straight lines
    def possibleMoves(self, pieces: list[list[Piece]], currPos: tuple[int, int], numSides: int) -> list[tuple[int, int]]:
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        return getDirectionalMoves(self, pieces, currPos, directions, numSides, numSides)

class Knight(Piece):
    def __init__(self, type: str, color: str, startPos: tuple[int, int]):
        super().__init__(type, color, startPos, value = 3)
        
    # One L-shaped move in any direction
    def possibleMoves(self, pieces: list[list[Piece]], currPos: tuple[int, int], numSides: int) -> list[tuple[int, int]]:
        directions = [(-2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2)]
        return getDirectionalMoves(self, pieces, currPos, directions, 1, numSides)

class Bishop(Piece):
    def __init__(self, type: str, color: str, startPos: tuple[int, int]):
        super().__init__(type, color, startPos, value = 3)
        
    # Infinite moves in diagonal lines
    def possibleMoves(self, pieces: list[list[Piece]], currPos: tuple[int, int], numSides: int) -> list[tuple[int, int]]:
        directions = [(-1, -1), (-1, 1), (1, 1), (1, -1)]
        return getDirectionalMoves(self, pieces, currPos, directions, numSides, numSides)
    
class Pawn(Piece):
    def __init__(self, type: str, color: str, startPos: tuple[int, int]):
        super().__init__(type, color, startPos, value = 1)
        
    def possibleMoves(self, pieces: list[list[Piece]], currPos: tuple[int, int], numSides: int) -> list[tuple[int, int]]:
        moveSet = []
        direction = 1 if self.color == "black" else -1
        
        # Move two spaces
        row, col = currPos[1] + 2 * direction, currPos[0]
        if self.startPos == currPos and not pieces[row][col]:
            moveSet.append((col, row))
            
        # Move one space
        row = currPos[1] + direction
        if not pieces[row][col]:
            moveSet.append((col, row))
        
        # Move diagonally
        for i in [-1, 1]:
            col = currPos[0] + i
            if 0 <= col < numSides and pieces[row][col] and pieces[row][col].color != self.color:
                moveSet.append((col, row))
        
        return moveSet