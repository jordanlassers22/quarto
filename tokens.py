# -*- coding: utf-8 -*-
import tkinter as tk

def drawPiece(canvas, x, y, piece):
    """
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
        drawToken(canvas, x, y, "circle", "small", "blue", isHole = False)
    elif piece == "large_blue_circle":
        drawToken(canvas, x, y, "circle", "large", "blue", isHole = False)
    elif piece == "small_red_circle":
        drawToken(canvas, x, y, "circle", "small", "red", isHole = False)
    elif piece == "large_red_circle":
        drawToken(canvas, x, y, "circle", "large", "red", isHole = False)
    elif piece == "small_blue_square":
        drawToken(canvas, x, y, "square", "small", "blue", isHole = False)
    elif piece == "large_blue_square":
        drawToken(canvas, x, y, "square", "large", "blue", isHole = False) 
    elif piece == "small_red_square":
        drawToken(canvas, x, y, "square", "small", "red", isHole = False)
    elif piece == "large_red_square":
        drawToken(canvas, x, y, "square", "large", "red", isHole = False)
    elif piece == "small_blue_circle_hole":
        drawToken(canvas, x, y, "circle", "small", "blue", isHole = True)
    elif piece == "large_blue_circle_hole":
        drawToken(canvas, x, y, "circle", "large", "blue", isHole = True) 
    elif piece == "small_red_circle_hole":
        drawToken(canvas, x, y, "circle", "small", "red", isHole = True)
    elif piece == "large_red_circle_hole":
        drawToken(canvas, x, y, "circle", "large", "red", isHole = True)
    elif piece == "small_blue_square_hole":
        drawToken(canvas, x, y, "square", "small", "blue", isHole = True)
    elif piece == "large_blue_square_hole":
        drawToken(canvas, x, y, "square", "large", "blue", isHole = True)
    elif piece == "small_red_square_hole":
        drawToken(canvas, x, y, "square", "small", "red", isHole = True)
    elif piece == "large_red_square_hole":
        drawToken(canvas, x, y, "square", "large", "red", isHole = True)
        
        
        
    
    

def drawToken(canvas, x, y, shape, size, color, isHole):
    """

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
        #Need to draw a circular hole if isHole == True
        if isHole: 
            hole_size = shapeSize // 2
            x_hole = x + (shapeSize - hole_size) // 2
            y_hole = y + (shapeSize - hole_size) // 2
            canvas.create_oval(x_hole, y_hole, x_hole + hole_size, y_hole + hole_size, fill = fill)
            
    #Need to draw a sqaure if shape == "square"
    elif shape == "square":
        canvas.create_rectangle(x, y, x + shapeSize, y + shapeSize, fill=fill)
        #Need to draw a square hole if isHole == True
        if isHole: 
            hole_size = shapeSize // 2
            x_hole = x + (shapeSize - hole_size) // 2
            y_hole = y + (shapeSize - hole_size) // 2
            canvas.create_rectangle(x_hole, y_hole, x_hole + hole_size, y_hole + hole_size, fill = fill)
    else:
        raise ValueError(f"{shape} is invalid... it needs to be a circle or a square")
        
    


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Quarto Game Tokens")
    canvas = tk.Canvas(root, width=800, height=800)
    canvas.pack()
    
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
    
    
    
    # token1 = drawToken(canvas, 50, 50, "circle", "small", "blue", isHole = True)
    # token2 = drawToken(canvas, 150, 50, "circle", "small", "blue", isHole = False)
    # token3 = drawToken(canvas, 250, 50, "circle", "large", "blue", isHole = True)
    # token4 = drawToken(canvas, 350, 50, "circle", "large", "blue", isHole = False)

    # token5 = drawToken(canvas, 50, 150, "circle", "small", "red", isHole = True)
    # token6 = drawToken(canvas, 150, 150, "circle", "small", "red", isHole = False)
    # token7 = drawToken(canvas, 250, 150, "circle", "large", "red", isHole = True)
    # token8 = drawToken(canvas, 350, 150, "circle", "large", "red", isHole = False)

    # token9 = drawToken(canvas, 50, 250, "square", "small", "blue", isHole = True)
    # token10 = drawToken(canvas, 150, 250, "square", "small", "blue", isHole = False)
    # token11 = drawToken(canvas, 250, 250, "square", "large", "blue", isHole = True)
    # token12 = drawToken(canvas, 350, 250, "square", "large", "blue", isHole = False)

    # token13 = drawToken(canvas, 50, 350, "square", "small", "red", isHole = True)
    # token14 = drawToken(canvas, 150, 350, "square", "small", "red", isHole = False)
    # token15 = drawToken(canvas, 250, 350, "square", "large", "red", isHole = True)
    # token16 = drawToken(canvas, 350, 350, "square", "large", "red", isHole = False)

    #Once finished, need to draw all 16 shape possibilities
    root.mainloop()
