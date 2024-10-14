from abc import ABC, abstractmethod
import pygame
from chessPieces import*
#from http.client import MOVED_PERMANENTLY

#Abstract class piece to create all the chess pieces
class piece(ABC): 
    @abstractmethod
    def move(self):
        pass
    @abstractmethod
    def __init__(self, pos, val, color):
        pass

    def boundCheck (self, end):
        i=0
        x=len(end)
        while (i<x):
            if(end[i] > 7 or end[i]<0 or end[i+1] > 7 or end[i+1]<0):
                end.pop(i)
                end.pop(i)
                x-=2
                continue
            i+=2
		
        return end
    value = 0
    color = 0
    img=""
    
#Pawn class
class pawn(piece):
    
    color=1
    #pos should be a two-element array for the piece's internal position tracker. Color should either be 1 for white or -1 for black. This allows proper move calculations. Val is the desired piece's value, Chess.com values are defualt
    def __init__(self, pos, color, val=1 ):
        self.position = {"col": -1, "row": -1}
        self.value=val
        """ if[val]:
            self.color*=-1 """
        self.color=color
        self.moved=False
        if (color==1):
            self.img=whiteFlunkeyImage
            self.rect=whiteFlunkeyRect
        else:
            self.img=blackFlunkeyImage
            self.rect=blackFlunkeyRect
        self.setPos(pos)
        self.moved = False


    def move(self):
        end=[]
        end.append(self.position["col"])
        end.append(self.position["row"]+2*self.color)
        end.append(self.position["col"])
        end.append(self.position["row"]+self.color)

        end.append(self.position["col"]+self.color)
        end.append(self.position["row"]+self.color)
        end.append(self.position["col"]-self.color)
        end.append(self.position["row"]+self.color)
        if(self.moved):
            end.pop(0)
            end.pop(0)
        end = self.boundCheck(end)
        return end
    def setPos(self, nPos):
        self.position["col"]=nPos[0]
        self.position["row"]=nPos[1]
        self.rect.left=nPos[0]*60
        self.rect.top=nPos[1]*60
        self.moved=True
    
    def __str__(self):
        return "p"
    
class rook(piece):

    def __init__(self, pos, color, val=4, ):
        self.position = {"col": -1, "row": -1}
        self.value=val
        self.color=color
        self.moved=False
        if (color==1):
            self.img=whiteCastleImage
            self.rect=whiteCastleRect
        else:
            self.img=blackCastleImage
            self.rect=blackCastleRect
        self.setPos(pos)
        self.moved=False

    def move(self):
        end=[]
        for i in range(8):
            end.append(self.position["col"])
            end.append(i-1)
        for i in range(8):
            end.append(i-1)
            end.append(self.position["row"])
        end = self.boundCheck(end)
        return end

    def setPos(self, nPos):
        self.position["col"]=nPos[0]
        self.position["row"]=nPos[1]
        self.rect.left=nPos[0]*60
        self.rect.top=nPos[1]*60
        self.moved=True

    def __str__(self):
        return "r"

class knight(piece):
    def __init__(self, pos, color, val=3, ):
        self.position = {"col": -1, "row": -1}
        self.value=val
        self.color=color
        if (color==1):
            self.img=whiteHorseyImage
            self.rect=whiteHorseyRect
        else:
            self.img=blackHorseyImage
            self.rect=blackHorseyRect
        self.setPos(pos)

    def move(self):
        end=[]
        end.append(self.position["col"]+self.color)
        end.append(self.position["row"]+2*self.color)
        end.append(self.position["col"]-self.color)
        end.append(self.position["row"]-2*self.color)
        end.append(self.position["col"]+2*self.color)
        end.append(self.position["row"]+self.color)
        end.append(self.position["col"]-2*self.color)
        end.append(self.position["row"]-self.color)
        end=self.boundCheck(end)
        return end

        
    def setPos(self, nPos):
        self.position["col"]=nPos[0]
        self.position["row"]=nPos[1]
        self.rect.left=nPos[0]*60
        self.rect.top=nPos[1]*60
    
    def __str__(self):
        return "n"

class bishop(piece):
    def __init__(self, pos, color, val=3, ):
        self.position = {"col": -1, "row": -1}
        self.value=val
        self.color=color
        if (color==1):
            self.img=whitePopeImage
            self.rect=whitePopeRect
        else:
            self.img=blackPopeImage
            self.rect=blackPopeRect
        self.setPos(pos)
    
    def move(self):
        end=[]
        for i in range(1,9):
            end.append(self.position["col"]+i*self.color)
            end.append(self.position["row"]+i*self.color)
            end.append(self.position["col"]-i*self.color)
            end.append(self.position["row"]-i*self.color)
            end.append(self.position["col"]-i*self.color)
            end.append(self.position["row"]+i*self.color)
            end.append(self.position["col"]+i*self.color)
            end.append(self.position["row"]-i*self.color)
        end = self.boundCheck(end)
        return end
    
    def setPos(self, nPos):
        self.position["col"]=nPos[0]
        self.position["row"]=nPos[1]
        self.rect.left=nPos[0]*60
        self.rect.top=nPos[1]*60

    def __str__(self):
        return "b"

class queen(piece):
    def __init__(self, pos, color, val=3, ):
        self.position = {"col": -1, "row": -1}
        self.value=val
        self.color=color
        if (color==1):
            self.img=whiteWomanImage
            self.rect=whiteWomanRect
        else:
            self.img=blackWomanImage
            self.rect=blackWomanRect
        self.setPos(pos)
    
    def move(self):
        end=[]
        for i in range(8):
            end.append(self.position["col"])
            end.append(i)
        for i in range(8):
            end.append(i)
            end.append(self.position["row"])
            
        
        for i in range(1,9):
            end.append(self.position["col"]+i*self.color)
            end.append(self.position["row"]+i*self.color)
            end.append(self.position["col"]-i*self.color)
            end.append(self.position["row"]-i*self.color)
            end.append(self.position["col"]-i*self.color)
            end.append(self.position["row"]+i*self.color)
            end.append(self.position["col"]+i*self.color)
            end.append(self.position["row"]-i*self.color)

        end = self.boundCheck(end)
        return end

    def setPos(self, nPos):
        self.position["col"]=nPos[0]
        self.position["row"]=nPos[1]
        self.rect.left=nPos[0]*60
        self.rect.top=nPos[1]*60

    def __str__(self):
        return "q"

class king(piece):
    
    def __init__(self, pos, color, val=3, ):
        self.position = {"col": -1, "row": -1}
        self.value=val
        self.color=color
        self.moved=False
        if (color==1):
            self.img=whiteManImage
            self.rect=whiteManRect
        else:
            self.img=blackManImage
            self.rect=blackManRect
        self.setPos(pos)
        self.moved=False

    def move(self):
        end=[]
        i=1
        end.append(self.position["col"])
        end.append(self.position["row"]+i)
        end.append(self.position["col"])
        end.append(self.position["row"]-i)
       
        end.append(self.position["col"]+i)
        end.append(self.position["row"])
        end.append(self.position["col"]-i)
        end.append(self.position["row"])
        
        end.append(self.position["col"]+i*self.color)
        end.append(self.position["row"]+i*self.color)
        end.append(self.position["col"]-i*self.color)
        end.append(self.position["row"]-i*self.color)
        end.append(self.position["col"]-i*self.color)
        end.append(self.position["row"]+i*self.color)
        end.append(self.position["col"]+i*self.color)
        end.append(self.position["row"]-i*self.color)

        
        end=self.boundCheck(end)
        return end

    def setPos(self, nPos):
        self.position["col"]=nPos[0]
        self.position["row"]=nPos[1]
        self.rect.left=nPos[0]*60
        self.rect.top=nPos[1]*60
        self.moved=True
    
    def __str__(self):
        return "k"

class moveLocation:

    def __init__(self, pos):
        self.position = {"col": -1, "row": -1}
        self.img=moveCircleImage
        self.rect=moveCircleRect
        self.setPos(pos)

    def setPos(self, nPos):
        self.position["col"]=nPos[0]
        self.position["row"]=nPos[1]
        self.rect.left=nPos[0]*60
        self.rect.top=nPos[1]*60
    
    def __del__(self):
        del self.rect
        del self.img

