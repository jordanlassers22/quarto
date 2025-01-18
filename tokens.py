# -*- coding: utf-8 -*-
import tkinter as tk
import math

class Token:
    """
   Represents a game token that can be placed on a board.

   Attributes:
   _x : int
       The x-coordinate of the top-left corner of the token.
   _y : int
       The y-coordinate of the top-left corner of the token.
   color : str
       The color of the token ("blue" or "red").
   has_hole : bool
       Indicates whether the token has a hole in the middle.
   size : str
       The size of the token, either "small" or "large".
   diameter : int
       The diameter of the token in pixels (70 for "small", 45 for "large").
   shape : str
       The shape of the token, either "circle" or "square".
   centerCords : tuple
       The (x, y) coordinates of the center of the token.

   Methods:
   getX()
       Returns the x-coordinate of the token's top-left corner.
   getY()
       Returns the y-coordinate of the token's top-left corner.
   setX(newX)
       Updates the x-coordinate of the token's top-left corner and recalculates its center.
   setY(newY)
       Updates the y-coordinate of the token's top-left corner and recalculates its center.
   updateCords(newX, newY)
       Updates both the x- and y-coordinates of the token's top-left corner and recalculates its center.
   getCords()
       Returns the (x, y) coordinates of the token's top-left corner.
   _updateCenterCords()
       Recalculates the token's center coordinates based on its current position.
   """


    def __init__(self, x, y, color, has_hole, size, shape="circle"):
        """
        Initialize a Token instance.
        
        Parameters:
        ----------
        _x : int
            The x-coordinate of the top left of the token.
        _y : int
            The y-coordinate of the top left of token.
        color : str
            The color of the token (e.g., "blue", "red").
        has_hole : bool
            Whether the token has a hole in the middle.
        size : str
            The size of the token ("small" or "large").
        shape : str
            The shape of the token ("circle" or "square"). Default is "circle".
        """
        self._x = x
        self._y = y
        self.color = color
        self.has_hole = has_hole
        self.shape = shape
        
        if size == "small":
            self.size = size
            self.diameter = 70
        elif size == "large":
            self.size = size
            self.diameter = 45
        else:
            raise ValueError("Size must be 'small' or 'large'.")

        
        self._updateCenterCords()
    
    def getX(self):
        return self._x
    
    def getY(self):
        return self._y
    
    def setY(self, newY):
        """Use setter to ensure self.centerCords value is updated."""
        self._y = newY
        self._updateCenterCords()
        
    def setX(self, newX):
        """Use setter to ensure self.centerCords value is updated."""
        self._x = newX
        self._updateCenterCords()

        
    def updateCords(self, newX, newY):
        """Use setter to ensure self.centerCords value is updated."""
        self._x = newX
        self._y = newY
        self._updateCenterCords()
        
    def getCords(self):
        return self._x, self._y
    
    def _updateCenterCords(self):
        self.centerCords = (self._x + self.diameter // 2, self._y + self.diameter // 2)

        

def drawToken(canvas, token, gridCoords=None, square=None):
    """
    Draws a token on the canvas. If a grid square is specified, it will place the token in that square. Allows for both initial placement of tokens, and for drawing them on board.
    
    Parameters
    ----------
    canvas : tkinter Canvas
        The canvas on which to draw the token.
    token : Token
        The token instance to draw.
    optional gridCoords : dict,
        Dictionary of grid square coordinates.
    optional square : str
        The grid square label ("A1") where the token should be placed.
    
    Returns
    -------
    None
    """
    
    # Use grid square if placing piece on board
    if gridCoords and square:
        if square in gridCoords:
            token.updateCords(gridCoords[square][0],gridCoords[square][1])
            # Adjust position to center the token within the square
            token.setX(token.getX() + (100 - token.diameter) // 2)
            token.setY( token.getY() + (100 - token.diameter) // 2)
        else:
            print(f"Invalid square: {square}")
            return

    # Draw the token's shape
    if token.shape == "circle":
        canvas.create_oval(token.getX(), token.getY(), token.getX() + token.diameter, token.getY() + token.diameter, fill=token.color)
        if token.has_hole: #Decided to hollow out shape using white fill.
            hole_diameter = token.diameter // 2
            holeX = token.getX() + (token.diameter - hole_diameter) // 2
            holeY = token.getY() + (token.diameter - hole_diameter) // 2
            canvas.create_oval(holeX, holeY, holeX + hole_diameter, holeY + hole_diameter, fill="white")
            
    elif token.shape == "square":
        canvas.create_rectangle(
            token.getX(), token.getY(), token.getX() + token.diameter, token.getY() + token.diameter, fill=token.color)
        if token.has_hole:
            hole_diameter = token.diameter // 2
            holeX = token.getX() + (token.diameter - hole_diameter) // 2
            holeY = token.getY() + (token.diameter - hole_diameter) // 2
            canvas.create_rectangle(holeX, holeY, holeX + hole_diameter, holeY + hole_diameter, fill="white")
    else:
        print(f"Invalid shape: {token.shape}")

def drawBoard(canvas):
    """
    *Needs Implimented. Will draw an empty 4x4 gameboard on the canvas.
    Parameters
    ----------
    canvas : TK Object
        Canvas that board will be drawn on.
    Returns
    -------
    None.
    """
    #sizing the board
    board_x = 100
    board_y = 100
    cell = 100
    grid = 4

    # Create dictionary for each square
    center_coords = {}

    # Each square has a column and row
    columns = ['A', 'B', 'C', 'D']
    for row in range(grid):
        for col in range(grid):
            # Calculate the center coords of the current square
            top_left_x = board_x + col * cell
            top_left_y = board_y + row * cell

            # Create the label for the square 
            label = f"{columns[col]}{row + 1}"

            # Add to dict
            center_coords[label] = (top_left_x, top_left_y)

            # Draw each square
            canvas.create_rectangle(
                board_x + col * cell, board_y + row * cell,
                board_x + (col + 1) * cell, board_y + (row + 1) * cell,
                outline="black", width=2
            )

    # Return coords
    return center_coords

def isOnToken(mouseX, mouseY, unplacedTokenList):
    """Helper function. Can be used with highlightToken and other functions that require users mouse to be inside of a token for an action."""
        
    #Checks to see if mouse is inside any token
    for token in unplacedTokenList:
        centerX, centerY = token.centerCords
        tokenRadius = token.diameter // 2
        #Calculate the distance from token center to mouse
        distance = math.sqrt((mouseX - centerX) ** 2 + (mouseY - centerY) ** 2)
        #If the calculated distance is smaller than the radius of the token, the mouse must be inside the token.
        if distance <= tokenRadius:
            return token
        
def highlightToken(event):
    mouseX = event.x
    mouseY =  event.y
    token = isOnToken(mouseX, mouseY, unplacedTokenList)
    canvas.delete("highlight") #Deletes the highlight if mouse no longer inside token.
    if token: #If token detected, highlight it.
        if token.shape == "circle":
            canvas.create_oval(token.getX(), token.getY(), token.getX() + token.diameter, token.getY() + token.diameter, outline="yellow", width=3, tags="highlight")
        else:
            canvas.create_rectangle(token.getX(), token.getY(), token.getX() + token.diameter, token.getY() + token.diameter, outline="yellow", width=3, tags="highlight")

    return None
    

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Quarto Game Tokens")
    canvas = tk.Canvas(root, width=1000, height=600)
    canvas.pack()
    placed_board_pieces = [] #list of objects that have been placed on board
    

    # Get squares
    dict_coords = drawBoard(canvas)
    
    placedTokenList = []
    unplacedTokenList = [ #Be sure token is removed from list, and placed into placedTokenList when it is played.
    Token(550, 100, "blue", False, "small", "circle"),
    Token(650, 100, "blue", True, "small", "circle"),
    Token(750, 100, "blue", False, "large", "circle"),
    Token(850, 100, "blue", True, "large", "circle"),
    Token(550, 200, "blue", False, "small", "square"),
    Token(650, 200, "blue", True, "small", "square"),
    Token(750, 200, "blue", False, "large", "square"),
    Token(850, 200, "blue", True, "large", "square"),
    Token(550, 300, "red", False, "small", "circle"),
    Token(650, 300, "red", True, "small", "circle"),
    Token(750, 300, "red", False, "large", "circle"),
    Token(850, 300, "red", True, "large", "circle"),
    Token(550, 400, "red", False, "small", "square"),
    Token(650, 400, "red", True, "small", "square"),
    Token(750, 400, "red", False, "large", "square"),
    Token(850, 400, "red", True, "large", "square")
    ]
    
    #Initially draws tokens on screen.
    for token in unplacedTokenList:
        drawToken(canvas, token)
    
    #How to draw token on canvas using new method. Please remove once no longer needed
    # drawToken(canvas, unplacedTokenList[0], dict_coords, "A1")
    # drawToken(canvas, unplacedTokenList[2], dict_coords, "B2")
    # drawToken(canvas, unplacedTokenList[7], dict_coords, "C3")
    # drawToken(canvas, unplacedTokenList[8], dict_coords, "D4")
    
    canvas.bind("<Motion>", highlightToken)  #Checks for highlight on mouse movement. Binds highlight token function to mouse movement.


    
    root.mainloop()
