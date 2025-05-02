# Quarto

Quarto is a two-player strategy game with simple rules and alot of strategy. This Python implementation features an interactive GUI using `tkinter`, mouse-based gameplay, AI opponents, and win condition verification tools.

## Features

- Two-player support (Human vs. Human or Human vs. AI)
- AI difficulty levels: Easy, Medium, Hard
- Drag-and-drop-like interaction using mouse hover and click
- 16 unique tokens based on:
  - Color: Red or Blue
  - Shape: Circle or Square
  - Size: Small or Large
  - Fill: Hollow or Solid
- "Call Quarto!" feature lets players declare a win based on selected criteria
- Visual highlights and selection animations
- Win condition dropdowns and board inspection tools

## How to Play

1. **Objective:** Get 4 pieces in a line (row, column, or diagonal) that share *any one* characteristic.
2. **Turn Rules:**
   - Your opponent selects a token for you to place.
   - You place that token anywhere on the board.
   - Then, you select the next token for your opponent.
3. **Victory:** Press "Call Quarto!" and select the row/column/diagonal and characteristic to check for a win.
4. **AI Mode:** Type `ai_easy`, `ai_medium`, or `ai_hard` for Player 2's name to play against the computer.

## Getting Started

### Requirements

- Python 3
- `tkinter`
- No external libraries needed

### Running the Game

```bash
python quarto.py
