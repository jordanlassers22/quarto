# -*- coding: utf-8 -*-
import tkinter as tk
import math
from tkinter import messagebox
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

    def get_id(self):
        """ Get unique id for each token for when we keep track of score"""
        size_code = 'S' if self.size == 'large' else 'L' # I don't know why i have to put s for large but that's what works for the code
        color_code = self.color[0].upper()  # First letter of the color 
        shape_code = self.shape[0].upper()  # First letter of the shape
        hole_code = '0' if self.has_hole else 'X'  # 0 for hole, X for no hole
        return f"{size_code}{shape_code}{color_code}{hole_code}"   

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
    
    return None
    
def isOnGrid(mouseX, mouseY, gridCoords):
    """Helper Function. Will be used for place token to make sure mouse is over a grid slot"""
    for label, (topLeftX, topLeftY) in gridCoords.items():
        slot_size = 100  # Assuming each grid slot is 100x100
        #checks mouse position accoriding to the grid
        if (topLeftX <= mouseX <= topLeftX + slot_size and
            topLeftY <= mouseY <= topLeftY + slot_size):
            return label
    return None

def highlightBoth(event):
    highlightToken(event)
    highlightGrid(event)

def highlightGrid(event):
    """
    Highlights a grid square when hovered over.
    """
    
    
    #Get the mouse coordinates
    mouseX = event.x
    mouseY = event.y
    
    token = isOnToken(mouseX, mouseY, unplacedTokenList)
    if token:
        return  # Skip grid highlighting if hovering over a token

    #Check if the mouse is over a grid square
    grid_label = isOnGrid(mouseX, mouseY, dict_coords)

    #Remove the previous highlight
    canvas.delete("grid-highlight")

    if grid_label:
        #Get the top-left corner of the grid square
        topLeftX, topLeftY = dict_coords[grid_label]

        #Highlight the square
        slot_size = 100  #Assuming each grid slot is 100x100
        canvas.create_rectangle(topLeftX, topLeftY, topLeftX + slot_size, topLeftY + slot_size,outline="yellow", width=3, tags="grid-highlight")

    
def highlightToken(event):
    """Highlights a token when it is hovered over"""
    mouseX = event.x
    mouseY =  event.y
    token = isOnToken(mouseX, mouseY, unplacedTokenList)
    canvas.delete("token-highlight") #Deletes the highlight if mouse no longer inside token.
    if token: #If token detected, highlight it.
        canvas.config(cursor="hand2")
        if token.shape == "circle":
            canvas.create_oval(token.getX(), token.getY(), token.getX() + token.diameter, token.getY() + token.diameter, outline="yellow", width=3, tags="token-highlight")
        else:
            canvas.create_rectangle(token.getX(), token.getY(), token.getX() + token.diameter, token.getY() + token.diameter, outline="yellow", width=3, tags="token-highlight")
    else:
        canvas.config(cursor="arrow")
        
def selectToken(event):
    """selects a token when clicked"""
    global selected_token #a global variable that stores the selected token
    mouseX = event.x
    mouseY =  event.y
    token = isOnToken(mouseX, mouseY, unplacedTokenList)
    if token: #if the token is detected then it will be selecteed
        selected_token = token
        canvas.delete("select") #removes the prev. selection
        if token.shape == "circle":
            canvas.create_oval(token.getX(), token.getY(), token.getX() + token.diameter, token.getY() + token.diameter, outline="green", width=5, tags="select")
        else:
            canvas.create_rectangle(token.getX(), token.getY(), token.getX() + token.diameter, token.getY() + token.diameter, outline="green", width=5, tags="select")

def placeToken(event):
    """places the token in an unsused slot on the grid"""
    global selected_token
    if not selected_token: #if a token is not selected then leave
        return
    
    mouseX = event.x
    mouseY =  event.y
    grid = isOnGrid(mouseX, mouseY, dict_coords)
    if grid and grid not in placed_board_pieces: #if a grid is found and it is not occupied then place the valid token
        print(f"Clicked at: ({mouseX}, {mouseY}), Grid: {grid}") #debugging
        print(f"{selected_token.get_id()} placed at {grid}") # debugging
        row, col = int(grid[1]) - 1, ord(grid[0]) - ord('A')
        board[row][col] = selected_token.get_id()  # Update the board with tokens id. ID looks is a string with each of the following representing size(L,S), shape(C,S), color(B,R), hole(0,X)
        deleteToken(canvas, selected_token)
        drawToken(canvas, selected_token, dict_coords, grid)
        placed_board_pieces.append(grid)
        unplacedTokenList.remove(selected_token)
        selected_token = None #resets selected token
        canvas.delete("select")#removes the tokens highlight

def deleteToken(canvas, token):
    """Deletes a token from canvas by drawing over it """
    if token.shape == "circle":
        canvas.create_oval(
            token.getX(), token.getY(), token.getX() + token.diameter, token.getY() + token.diameter, fill="white", outline="white"
        )
    elif token.shape == "square":
        canvas.create_rectangle(
            token.getX(), token.getY(), token.getX() + token.diameter, token.getY() + token.diameter, fill="white", outline="white"
        )
    else:
        print(f"Invalid shape: {token.shape}")
        
def check_row(board, row, characteristic):
    #Id string letter options. size(L,S), shape(C,S), color(B,R), hole(0,X) ie. LCB0 -> Large, Circle, Blue, Hole
    for token_id in board[row]:
        if token_id == None:
            return False
    
    if characteristic == "size":
        letter_index = 0
    elif characteristic == "shape":
        letter_index = 1 
    elif characteristic == "color":
        letter_index = 2
    elif characteristic == "hole":
        letter_index = 3
    else:
        raise ValueError(f"Must insert valid characteristic for check_row. Options are: size, shape, color, hole. You entered: {characteristic} ")
    
    letter_to_check = board[row][0][letter_index]
    
    # Check each token in the row
    for token_id in board[row]:
        if token_id[letter_index] != letter_to_check:
            return False
    
    return True #Returns True if every specific letter from token id matches. Can target different id letters by changing the index.
        
def check_row_button_function():
    print(check_row(board, 0, "size"))
    
# def check_column(board, column, characteristic):
#     #Id string letter options. size(L,S), shape(C,S), color(B,R), hole(0,X) ie. LCB0 -> Large, Circle, Blue, Hole
#     for row in range(4):
#         print(board[row][column])
    
# def check_column_button_function():
#     (check_column(board, 0, "size"))


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Quarto Game Tokens")
    canvas = tk.Canvas(root, width=1000, height=600, bg="white")
    canvas.pack()
    placed_board_pieces = [] #list of objects that have been placed on board
    
    board = [] # Represents our board. Starts out as None for all items.
    for _ in range(4):
        row = []
        for _ in range(4):
            row.append(None)
        board.append(row)

    

    # Get squares
    dict_coords = drawBoard(canvas)
    
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
        
    row_button = tk.Button(root, text="Check row 1 for size", command=check_row_button_function) #For testing purposes. Can be changed to test other win_check functions.
    row_button.pack(pady=10)
    # column_button = tk.Button(root, text="Check column 1 for color", command=check_column_button_function)
    # column_button.pack(pady=10)
    
    canvas.bind("<Motion>", highlightBoth)  #Checks for highlight on mouse movement. Binds highlight token function to mouse movement.
    canvas.bind("<Button-1>", selectToken)
    canvas.bind("<ButtonRelease-1>", placeToken)


    selected_token = None

    
    root.mainloop()
