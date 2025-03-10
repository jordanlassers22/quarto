# -*- coding: utf-8 -*-
import tkinter as tk
import math
from tkinter import ttk
from tkinter import messagebox
import random

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

    # Players
    current_player = None 
    p1 = None
    p2 = None

    # Selecting piece for other player
    selected_piece = None
    piece_selected_for_placement = False # track if piece has been selected by other player
    
    is_ai_opponent = False # Flag to signal whether AI is turned off or on
    
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
    global selected_token, selected_piece, current_player, p1, p2, piece_selected_for_placement #a global variable that stores the selected token
    mouseX = event.x
    mouseY =  event.y
    token = isOnToken(mouseX, mouseY, unplacedTokenList)

    # If piece has already been chosen, skip
    if piece_selected_for_placement:
        return

    # Only allow token selection if it's the current player's turn to select
    if token and token not in placed_board_pieces:
        selected_piece = token  # Set the selected piece
        piece_selected_for_placement = True
        canvas.delete("select") # Remove old select

        if token: #if the token is detected then it will be selecteed
            selected_token = token
            canvas.delete("select") #removes the prev. selection
            if token.shape == "circle":
                canvas.create_oval(token.getX(), token.getY(), token.getX() + token.diameter, token.getY() + token.diameter, outline="green", width=5, tags="select")
            else:
                canvas.create_rectangle(token.getX(), token.getY(), token.getX() + token.diameter, token.getY() + token.diameter, outline="green", width=5, tags="select")

        # Update the status bar
        update_status_bar_message(f"{current_player}, place the selected piece on the board.")

def placeToken(event):
    """places the token in an unsused slot on the grid"""
    global selected_token, current_player, p1, p2, selected_piece, piece_selected_for_placement
    if not selected_piece: #if a token is not selected then leave
        return

    # if no piece to place just skip
    if not selected_piece or not piece_selected_for_placement:
        return
    
    mouseX = event.x
    mouseY =  event.y
    grid = isOnGrid(mouseX, mouseY, dict_coords)
    if grid and grid not in placed_board_pieces: #if a grid is found and it is not occupied then place the valid token
        print(f"Clicked at: ({mouseX}, {mouseY}), Grid: {grid}") #debugging
        print(f"{selected_piece.get_id()} placed at {grid}") # debugging
        row, col = int(grid[1]) - 1, ord(grid[0]) - ord('A')
        board[row][col] = selected_piece.get_id()  # Update the board with tokens id. ID looks is a string with each of the following representing size(L,S), shape(C,S), color(B,R), hole(0,X)
        deleteToken(canvas, selected_piece)
        drawToken(canvas, selected_piece, dict_coords, grid)
        placed_board_pieces.append(grid)
        unplacedTokenList.remove(selected_piece)
        selected_piece = None #resets selected token
        piece_selected_for_placement = False
        canvas.delete("select")#removes the tokens highlight

        # Switch turns
        current_player = p2 if current_player == p1 else p1
        # Update the status bar
        update_status_bar_message(f"{p2 if current_player == p1 else p1}, select a token for {current_player} to place.")
        
        #If there is an AI opponent and it is player 1s turn, have ai select token for player 1
        if is_ai_opponent and current_player != "AI":
            root.after(1000, handle_ai_turn)  # Delay for 1 second to make it feel natural

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
    for token_id in board[row]: #Make sure entire row contains tokens.
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
        
def check_board_button_function():
    # Get dropdown win
    win_condition = win_combobox.get()
    # Get the dropdown selection
    row_col_selection = row_combobox.get()

    characteristic_map = {
        "Same Size": "size",
        "Same Color": "color",
        "Same Shape": "shape",
        "Same Fill": "hole"
    }
    characteristic = characteristic_map.get(win_condition, None)

    if not characteristic:
        print("Please select a valid win condition.")
        return

    # Map correspondingly
    row_col_map = {
        "1st row": (0, "row"),
        "2nd row": (1, "row"),
        "3rd row": (2, "row"),
        "4th row": (3, "row"),
        "1st column": (0, "column"),
        "2nd column": (1, "column"),
        "3rd column": (2, "column"),
        "4th column": (3, "column"),
        "Left to Right Diagonal": ("first_diagonal", "diagonal"),
        "Right to Left Diagonal": ("second_diagonal", "diagonal")
    }
    row_col_info = row_col_map.get(row_col_selection, None)

    if not row_col_info:
        print("Please select a valid row/column/diagonal.")
        return

    # Check for a win
    if row_col_info[1] == "row":
        if check_row(board, row_col_info[0], characteristic):
            print(f"Win detected in {row_col_selection} with {win_condition}!")
            congratulations(current_player)
    elif row_col_info[1] == "column":
        if check_column(board, row_col_info[0], characteristic):
            print(f"Win detected in {row_col_selection} with {win_condition}!")
            congratulations(current_player)
    elif row_col_info[1] == "diagonal":
        if check_diagonal(board, row_col_info[0], characteristic):
            print(f"Win detected in {row_col_selection} with {win_condition}!")
            congratulations(current_player)
            
def congratulations(player):
    """message box will appear and will congratulate user and ask to play again"""
    response = messagebox.askyesno("Quarto!", "Congratulations! You won!\n\nPlay again?")
    if response:  # yes
        show_name_screen()  #reset the game
    else:  #no
        root.destroy() #exit game
    
def check_column(board, column, characteristic):
    #Id string letter options. size(L,S), shape(C,S), color(B,R), hole(0,X) ie. LCB0 -> Large, Circle, Blue, Hole
    for row in range(4): #Make sure entire column contains tokens
        if (board[row][column]) == None:
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
    
    letter_to_check = board[0][column][letter_index]
    for row in range(4): 
        if board[row][column][letter_index] != letter_to_check:
            return False
    return True
    
def check_column_button_function():
    print(check_column(board, 0, "color"))
    
def check_diagonal(board, diagonal, characteristic):
    """
    it will check a diagonal win from top left to bottom right
    or top right to bottom left
    """

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
    
    if diagonal == "first_diagonal": #top left to bottom right
        position = [(i,i) for i in range(4)]
    if diagonal == "second_diagonal":
        position = [(i,3-i) for i in range(4)] #top right to bottom left

    for row, column in position: #Make sure entire column contains tokens
        if board[row][column] == None:
            return False
        
    letter_to_check = board[position[0][0]][position[0][1]][letter_index]
    for row, column in position:  # Iterate over the diagonal and check for consistency
        if board[row][column][letter_index] != letter_to_check:
            return False
    return True

def check_win(board, characteristic):
    """ Check a win for a specific characteristic in one way """
    # Check all rows for a win
    for row in range(4):
        if check_row(board, row, characteristic):
            print(f"Win found row {row}, {characteristic}")
            return True
    
    # Check all columns for a win
    for col in range(4):
        if check_column(board, col, characteristic):
            print(f"Win found column {col}, {characteristic}")
            return True
    
    # Check the first diagonal
    if check_diagonal(board, "first_diagonal", characteristic):
        print(f"Win found first diagonal,{characteristic}")
        return True
    
    # Check the second diagonal
    if check_diagonal(board, "second_diagonal", characteristic):
        print(f"Win found second diagonal,{characteristic}")
        return True
    
    # If no win found, return False
    return False

def check_win_in_any_position(board):
    """ Checks if a player has won based on any of the four characteristics: size, shape, color, or hole. """
    characteristics = ["size", "shape", "color", "hole"]
    
    # Loop through each characteristic
    for characteristic in characteristics:
        if check_win(board, characteristic):
            return True

    # Return False if no win is found for any characteristic
    return False

def check_board_state():
    for row in board:
        print(row)
        
def ai_select_token():
    """AI selects a token for the human player to place. Returns a token that is to be placed"""
    global unplacedTokenList, board
    
    #Try's to avoid selecting a piece that lets the human win immediately
    safe_tokens = []
    for token in unplacedTokenList:
        #Try placing a token in each slot and see what happens
        winning_piece = False
        for row in range(4):
            for col in range(4):
                if board[row][col] is None:
                    #Temporarily place the token
                    board[row][col] = token.get_id()
                    if check_win_in_any_position(board):
                        winning_piece = True
                    board[row][col] = None  #Undo the placed token
                    if winning_piece:
                        break
            if winning_piece:
                break
        if not winning_piece:
            safe_tokens.append(token)
    
    #If there are safe tokens, pick one. Otherwise, pick a random token
    if safe_tokens:
        print("picking a safe token from following list...")
        for token in safe_tokens:
            print(f"{token.get_id()}")
        return random.choice(safe_tokens)
    print("No safe tokens left. Randomly picking from available token list...")
    return random.choice(unplacedTokenList)
        
def ai_place_token(token):
    '''Places the selected token provided by player 1 on the board in the best possible position
    Parameters: 
        token: token to be placed on board
    '''
    pass

def handle_ai_turn():
    '''Handles the ais turn. Selects a token for the human and places a token provided by the human. '''
    global selected_piece, piece_selected_for_placement, current_player, p1, p2

    # Have AI select token for human
    selected_piece = ai_select_token()
    piece_selected_for_placement = True

    # Update status bar
    update_status_bar_message(f"{current_player}, place the selected piece on the board.")

    # Highlight the selected token on the canvas
    canvas.delete("select")  # Remove old selection
    if selected_piece.shape == "circle":
        canvas.create_oval(selected_piece.getX(), selected_piece.getY(), 
                           selected_piece.getX() + selected_piece.diameter, 
                           selected_piece.getY() + selected_piece.diameter, 
                           outline="green", width=5, tags="select")
    else:
        canvas.create_rectangle(selected_piece.getX(), selected_piece.getY(), 
                                selected_piece.getX() + selected_piece.diameter, 
                                selected_piece.getY() + selected_piece.diameter, 
                                outline="green", width=5, tags="select")

    # Switch turns
    current_player = p2 if current_player == p1 else p1
    
        
def show_name_screen():
    """ Displays a screen for players to enter their names on the root window. """
    #Clear the root window
    for widget in root.winfo_children():
        widget.destroy()

    tk.Label(root,text="QUARTO",font=("Comic Sans MS", 60, "bold"),fg="#FF5733", bg="white").pack(pady=100)
    #Add labels and input widgets for player names
    tk.Label(root, text="Player 1 Name:", font=("Arial", 18)).pack(pady=5)
    player1_entry = tk.Entry(root, font=("Arial", 18))
    player1_entry.pack(pady=5)

    tk.Label(root, text="Player 2 Name:", font=("Arial", 18)).pack(pady=5)
    player2_entry = tk.Entry(root, font=("Arial", 18))
    player2_entry.pack(pady=5)
    

    #Function runs when start_game button is clicked. Keep indented one more than parent function.
    def start_game():
        """ Start the game with entered player names. Toggles AI if player 2s name is ai """
        global is_ai_opponent
        player1 = player1_entry.get().strip() or "Player 1"
        player2 = player2_entry.get().strip() or "Player 2"
        
        if player2.upper() == "AI":
            player2 = "AI"
            is_ai_opponent = True
            

        # Clear the root window and initialize the game
        for widget in root.winfo_children():
            widget.destroy()
        initialize_game(player1, player2)

    tk.Button(root, text="Start Game", command=start_game, font=("Arial", 18)).pack(pady=10)
    esc_tooltip = tk.Label(root, text="Press ESC to Close Game", font=("Arial", 25), fg="gray")
    esc_tooltip.place(relx=0.5, rely=1.0, anchor="s", y=-100)  #Place 100 pixels from the bottom
    
def update_status_bar_message(message):
    """Simplifies updating the status bar."""
    status_bar.config(text=message)
    
def initialize_game(player1, player2):
    """ Initializes the game board with the given player names."""
    global canvas, placed_board_pieces, board, unplacedTokenList, dict_coords, status_bar, current_player, p1, p2, piece_selected_for_placement, win_combobox, row_combobox

    # initialize a bunch of stuff
    p1 = player1
    p2 = player2
    current_player = player1
    piece_selected_for_placement = False

    print(f"Starting game with {player1} and {player2}.")
    tk.Label(root, text=f"Quarto: {player1} vs {player2}", font=("Arial", 20)).pack(pady=10)

    canvas = tk.Canvas(root, width=1000, height=600, bg="white")
    canvas.pack()

    placed_board_pieces = []  # List of objects that have been placed on the board

    board = []  # Represents the board. Starts out as None for all items.
    for _ in range(4):
        row = []
        for _ in range(4):
            row.append(None)
        board.append(row)

    # Get squares
    dict_coords = drawBoard(canvas)

    unplacedTokenList = [
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
        Token(850, 400, "red", True, "large", "square"),
    ]

    #Initially draw tokens on screen
    for token in unplacedTokenList:
        drawToken(canvas, token)

    #Create a Frame for aligning the button and win conditions in the same row
    controls_frame = tk.Frame(root)
    controls_frame.pack(pady=10)
    
    #Label for the Call Quarto button
    tk.Label(controls_frame, text="Actions:", font=("Arial", 14)).grid(row=0, column=0, padx=10)
    
    #Call Quarto button
    victory_button = tk.Button(controls_frame, text="Call Quarto!", font=("Arial", 14), command=check_board_button_function)
    victory_button.grid(row=1, column=0, padx=10)
    
    #Label for the Win Condition dropdown
    tk.Label(controls_frame, text="Select Win Condition:", font=("Arial", 14)).grid(row=0, column=1, padx=10)
    
    #Win Condition Combo Box
    win_conditions = ["Same Size", "Same Color", "Same Shape", "Same Fill"]
    win_combobox = ttk.Combobox(controls_frame, values=win_conditions, state="readonly", font=("Arial", 14))
    win_combobox.set("Select a win condition")  # Default text
    win_combobox.grid(row=1, column=1, padx=10)
    
    #Label for the Row Selection dropdown
    tk.Label(controls_frame, text="Choose a Row or Column:", font=("Arial", 14)).grid(row=0, column=2, padx=10)
    
    #Row Selection Combo Box
    row_conditions = ["1st row", "2nd row", "3rd row", "4th row",
                      "1st column", "2nd column", "3rd column", "4th column",
                      "Left to Right Diagonal", "Right to Left Diagonal"]
    
    row_combobox = ttk.Combobox(controls_frame, values=row_conditions, state="readonly", font=("Arial", 14))
    row_combobox.set("Select a row/column")  # Default text
    row_combobox.grid(row=1, column=2, padx=10)

    #Status bar
    status_bar = tk.Label(root, text=f"{p2}, select a token for {p1} to place.", bd=1, relief=tk.SUNKEN, anchor=tk.W, font=("Arial", 18))
    status_bar.pack(side=tk.BOTTOM, fill=tk.X)

    canvas.bind("<Motion>", highlightBoth)  # Highlight on mouse movement
    canvas.bind("<Button-1>", selectToken)
    canvas.bind("<ButtonRelease-1>", placeToken)
    
    handle_ai_turn() #See ai token selection when game first starts. Should be a better way to do this
def exit_fullscreen(event=None):
    root.destroy()  # Close the application


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Quarto Game")
    root.attributes("-fullscreen", True)  # Enable full-screen mode
    show_name_screen()  # Display the name entry screen
    root.bind("<Escape>", exit_fullscreen)
    root.mainloop()
    
