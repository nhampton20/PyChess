import math
import classes
class board:
    
    turn = True
    whiteScore=0
    blackScore=0
    selected=[]
    def __init__ (self, size=8):
            self.area = []
            for i in range(size):
                self.area.append([])
                for j in range(size):
                    if(j==1):
                        self.area[i].append(classes.pawn([i,j],1))
                        
                    elif(j==size-2):
                        self.area[i].append(classes.pawn([i,j],-1))
                        
                    elif(i==0 and j ==0 or i==size-1 and j==0):
                        self.area[i].append(classes.rook([i,j], 1))

                    elif(i==0 and j ==size-1 or i==size-1 and j==size-1):
                        self.area[i].append(classes.rook([i,j], -1))
                        
                    elif(j==0 and i== math.floor(math.floor(size/2))):
                        self.area[i].append(classes.king([i,j], 1))
                        
                    elif(j==size-1 and i ==math.floor(size/2)):
                        self.area[i].append(classes.king([i,j], -1))
                        
                    elif(j==0 and i==math.floor(size/2)-1):
                        self.area[i].append(classes.queen([i,j], 1))
                        
                    elif(j==size-1 and i ==math.floor(size/2)-1):
                        self.area[i].append(classes.queen([i,j], -1))
                        
                    elif(j==0 and i==math.floor(size/2)+1 or j==0 and i==math.floor(size/2)-2):
                        self.area[i].append(classes.bishop([i,j], 1))
                        
                    elif(j==size-1 and i==math.floor(size/2)+1 or j==size-1 and i==math.floor(size/2)-2):
                        self.area[i].append(classes.bishop([i,j], -1))
                        
                    elif(j==0):
                        self.area[i].append(classes.knight([i,j], 1))
                    elif(j==size-1):
                        self.area[i].append(classes.knight([i,j], -1)) 
                    else:
                        self.area[i].append(0)

    def moveList(self, pos):
        self.selected=pos
        moves = self.area[pos[0]][pos[1]].move()
        remove=[]
        for i in range(0, len(moves)-3, 2):
            if (self.area[moves[i]][moves[i+1]]!=0):
                remove.insert(0, i)
        for i in range(len(remove)):
            moves.pop(remove[i])

        return moves
    
    def movePiece(self, piece, pos):
        if (self.area[pos[0]][pos[1]]!=0):
            if(self.turn):
                self.whiteScore+=self.area[pos[0]][pos[1]].value
            else:
                self.blackScore+=self.area[pos[0]][pos[1]].value
        self.area[pos[0]][pos[1]]=self.area[piece[0]][piece[1]]
        self.area[piece[0]][piece[1]]=0
        self.area[pos[0]][pos[1]].setPos(pos)
        self.turn= not self.turn
        self.selected = []
        return
    
    def clear(self):
        self.area = [[0 for i in range(len(self.area[x]))] for x in range(len(self.area))]
        return
    

    def addPiece(self, piece: int, pos):
        if (piece==0):
            if(self.turn):
                self.area[pos[0]][pos[1]]=classes.pawn(pos, 1)
            else:
                self.area[pos[0]][pos[1]]=classes.pawn(pos, -1)
        elif (piece == 1):
            if(self.turn):
                self.area[pos[0]][pos[1]]=classes.knight(pos, 1)
            else:
                self.area[pos[0]][pos[1]]=classes.knight(pos, -1)
        elif (piece == 2):
            if(self.turn):
                self.area[pos[0]][pos[1]]=classes.bishop(pos, 1)
            else:
                self.area[pos[0]][pos[1]]=classes.bishop(pos, -1)
        elif(piece==3):
            if(self.turn):
                self.area[pos[0]][pos[1]]=classes.rook(pos, 1)
            else:
                self.area[pos[0]][pos[1]]=classes.rook(pos, -1)
        elif (piece == 4):
            if(self.turn):
                self.area[pos[0]][pos[1]]=classes.queen(pos, 1)
            else:
                self.area[pos[0]][pos[1]]=classes.queen(pos, -1)
        else:
            self.area[pos[0]][pos[1]]=classes.moveLocation(pos)