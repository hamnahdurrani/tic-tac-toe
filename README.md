# Tic-Tac-Toe Game

A simple two-player Tic-Tac-Toe game implemented in Python.

## Table of Contents

1. [Example Gameplay](#example-gameplay)
2. [How to Play](#how-to-play)
3. [Installation and Running](#installation)
4. [Game Rules](#game-rules)
5. [Features](#features)
6. [Future Improvements](#future-improvements)
   
---
## Example Gameplay

```
Enter Name of Player 1: Alice
Enter Name of Player 2: Bob
Alice moves
Enter row: 1
Enter column: 1

  |   |  
----------
  | X |  
----------
  |   |  
```

---

## How to Play

- The game is played on a 3x3 grid.
- Player 1 uses **X**, and Player 2 uses **O**.
- Players take turns choosing a tile by entering a row and column number (0, 1, or 2).
- The game continues until one player wins or all tiles are occupied.

---

## Installation

No installation required! Just make sure you have Python installed.

## Running the Game

To start the game, run the following command in your terminal:

```bash
python tic-tac-toe.py
```

---

## Game Rules

1. Players input their names at the start.
2. On each turn, a player selects a row and column.
3. If the chosen tile is already occupied or out of bounds, the player must re-enter their choice.
4. The game board updates after every valid move.
5. The game checks for a win in rows, columns, and diagonals after each move.
6. If a player completes a row, column, or diagonal, they win.
7. If all tiles are filled without a winner, the game ends in a draw.

---

## Features

- User-friendly console-based interface.
- Prevents invalid moves.
- Automatically checks for a win after each move.
- Displays an updated board after every turn.

---

## Future Improvements

- Add an AI opponent.
- Implement a GUI version using Tkinter or Pygame.
- Enhance input validation with exception handling.


