# -*- coding: utf-8 -*-
import tkinter as tk

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
            canvas.create_oval(x_hole, y_hole, x_hole + hole_size, y_hole + hole_size, fill = "blue")
            
    #Need to draw a sqaure if shape == "square"
    elif shape == "square":
        canvas.create_rectangle(x, y, x + shapeSize, y + shapeSize, fill=fill)
        #Need to draw a square hole if isHole == True
        if isHole: 
            hole_size = shapeSize // 2
            x_hole = x + (shapeSize - hole_size) // 2
            y_hole = y + (shapeSize - hole_size) // 2
            canvas.create_rectangle(x_hole, y_hole, x_hole + hole_size, y_hole + hole_size, fill = "blue")
    else:
        raise ValueError(f"{shape} is invalid... it needs to be a circle or a square")
        
    
    

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Quarto Game Tokens")
    canvas = tk.Canvas(root, width=800, height=800)
    canvas.pack()
    
    token1 = drawToken(canvas, 50, 50, "circle", "small", "blue", isHole = True)
    token2 = drawToken(canvas, 50, 200, "circle", "large", "red", isHole = False)
    token3 = drawToken(canvas, 50, 50, "square", "small", "blue", isHole = True)
    token4 = drawToken(canvas, 350, 50, "square", "large", "red", isHole = False)
    #Once finished, need to draw all 16 shape possibilities
    root.mainloop()
