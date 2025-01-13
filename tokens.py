# -*- coding: utf-8 -*-
import tkinter as tk

def drawPiece(canvas, x, y, piece):
    """
    Draws a specified gamepiece onto the canvas at inputted coordinates.
    Parameters
    ----------
    canvas : TK Object
        Canvas that shape will be drawn on.
    x : int
        Coordinate.
    y : int
        Coordinate.
    piece : string
        Name of game piece that will be drawn. Options are:
            small_blue_circle, small_blue_circle_hole,
            large_blue_circle, large_blue_circle_hole,
            small_red_circle, small_red_circle_hole,
            large_red_circle, large_red_circle_hole,
            small_blue_square, small_blue_square_hole,
            large_blue_square, large_blue_square_hole,
            small_red_square, small_red_square_hole,
            large_red_square, large_red_square_hole,
    Returns
    -------
    None.
    """
    if piece == "small_blue_circle":
        drawShape(canvas, x, y, "circle", "small", "blue", isHole = False)
    elif piece == "large_blue_circle":
        drawShape(canvas, x, y, "circle", "large", "blue", isHole = False)
    elif piece == "small_red_circle":
        drawShape(canvas, x, y, "circle", "small", "red", isHole = False)
    elif piece == "large_red_circle":
        drawShape(canvas, x, y, "circle", "large", "red", isHole = False)
    elif piece == "small_blue_square":
        drawShape(canvas, x, y, "square", "small", "blue", isHole = False)
    elif piece == "large_blue_square":
        drawShape(canvas, x, y, "square", "large", "blue", isHole = False) 
    elif piece == "small_red_square":
        drawShape(canvas, x, y, "square", "small", "red", isHole = False)
    elif piece == "large_red_square":
        drawShape(canvas, x, y, "square", "large", "red", isHole = False)
    elif piece == "small_blue_circle_hole":
        drawShape(canvas, x, y, "circle", "small", "blue", isHole = True)
    elif piece == "large_blue_circle_hole":
        drawShape(canvas, x, y, "circle", "large", "blue", isHole = True) 
    elif piece == "small_red_circle_hole":
        drawShape(canvas, x, y, "circle", "small", "red", isHole = True)
    elif piece == "large_red_circle_hole":
        drawShape(canvas, x, y, "circle", "large", "red", isHole = True)
    elif piece == "small_blue_square_hole":
        drawShape(canvas, x, y, "square", "small", "blue", isHole = True)
    elif piece == "large_blue_square_hole":
        drawShape(canvas, x, y, "square", "large", "blue", isHole = True)
    elif piece == "small_red_square_hole":
        drawShape(canvas, x, y, "square", "small", "red", isHole = True)
    elif piece == "large_red_square_hole":
        drawShape(canvas, x, y, "square", "large", "red", isHole = True)
        
def drawShape(canvas, x, y, shape, size, color, isHole):
    """
    A helper function that takes in different shape properties and draws them.
    Parameters
    ----------
    canvas : TK Object
        Canvas that shape will be drawn on.
    x : int
        Coordinate.
    y : int
        Coordinate.
    shape : string
        Type of shape that should be drawn. Options are circle or sqaure.
    size : string
        Size of shape. Options are small or large.
    color : string
        Color of shape. Options are blue or red.
    center : bool
        Whether shape has a hole. Circle shape can have a circular hole. Square shape can have a square hole.
    Returns
    -------
    None.

    """
    if size.lower() == "large":
        shapeSize = 70
    elif size.lower() == "small":
        shapeSize = 45
    else:
        raise ValueError(f"{size} is an invalid parameter. Size must either be 'small' or 'large'")
    
    if color.lower() == "blue":
        fill = "blue"
    elif color.lower() == "red":
        fill = "red"
    else:
        raise ValueError(f"{color} is an invalid parameter. Color must either be 'blue' or 'red'")
        
        
    if shape == "circle": 
        canvas.create_oval(x, y, x + shapeSize, y + shapeSize, fill=fill)
        if isHole: 
            hole_size = shapeSize // 2
            x_hole = x + (shapeSize - hole_size) // 2
            y_hole = y + (shapeSize - hole_size) // 2
            canvas.create_oval(x_hole, y_hole, x_hole + hole_size, y_hole + hole_size, fill = fill)
            
    elif shape == "square":
        canvas.create_rectangle(x, y, x + shapeSize, y + shapeSize, fill=fill)
        if isHole: 
            hole_size = shapeSize // 2
            x_hole = x + (shapeSize - hole_size) // 2
            y_hole = y + (shapeSize - hole_size) // 2
            canvas.create_rectangle(x_hole, y_hole, x_hole + hole_size, y_hole + hole_size, fill = fill)
    else:
        raise ValueError(f"{shape} is invalid... it needs to be a circle or a square")
        
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
        
    


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Quarto Game Tokens")
    canvas = tk.Canvas(root, width=800, height=800)
    canvas.pack()
    
    #Just testing that these pieces can be drawn using new method. They can be moved when drawBoard is implimented.
    token1 = drawPiece(canvas, 50, 50, "small_blue_circle")
    token2 = drawPiece(canvas, 150, 50, "large_blue_circle")
    token3 = drawPiece(canvas, 250, 50, "small_red_circle")
    token4 = drawPiece(canvas, 350, 50, "large_red_circle")
    token5 = drawPiece(canvas, 50, 150, "small_blue_square")
    token6 = drawPiece(canvas, 150, 150, "large_blue_square")
    token7 = drawPiece(canvas, 250, 150, "small_red_square")
    token8 = drawPiece(canvas, 350, 150, "large_red_square")
    
    token9 = drawPiece(canvas, 50, 250, "small_blue_circle_hole")
    token10 = drawPiece(canvas, 150, 250, "large_blue_circle_hole")
    token11 = drawPiece(canvas, 250, 250, "small_red_circle_hole")
    token12 = drawPiece(canvas, 350, 250, "large_red_circle_hole")
    token13 = drawPiece(canvas, 50, 350, "small_blue_square_hole")
    token14 = drawPiece(canvas, 150, 350, "large_blue_square_hole")
    token15 = drawPiece(canvas, 250, 350, "small_red_square_hole")
    token16 = drawPiece(canvas, 350, 350, "large_red_square_hole")
    
    root.mainloop()
