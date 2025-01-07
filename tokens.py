# -*- coding: utf-8 -*-
import tkinter as tk

def drawToken(canvas, x, y, shape, size, color, border):
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
        Type of shape that should be drawn. Options are round or sqaure.
    size : string
        Size of shape. Options are small or large.
    color : string
        Color of shape. Options are blue or red.
    border : string
        Border type of shape. Options are solid or dashed.
    Returns
    -------
    None.

    """
    
    

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Quarto Game Tokens")
    canvas = tk.Canvas(root, width=800, height=800)
    canvas.pack()
    root.mainloop()