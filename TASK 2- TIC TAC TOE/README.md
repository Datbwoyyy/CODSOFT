# Tic-Tac-Toe Game with AI and Sound Effects

## Overview
This project is a **Tic-Tac-Toe game** built using **Python's Tkinter library** for the GUI and **Pygame** for sound effects. The game includes features such as difficulty levels for the AI, a restart button, and sound effects for various game events.

## Features
- **Graphical User Interface (GUI)** using Tkinter
- **Three difficulty levels** for AI: Easy, Medium, and Hard
- **Sound effects** for moves, wins, and draws
- **Restart button** to reset the game without closing the application

## Installation
To run this project, you need to have **Python 3.7+** installed along with the required libraries.

### Required Libraries:
- **tkinter**
- **pygame**

### Steps to Install Pygame:
```bash
pip install pygame
```

## How to Run the Game
1. Clone the repository or download the source code.
2. Ensure that your terminal or command prompt is open in the directory containing the **TicTacToe.py** file.
3. Run the following command:
```bash
python TicTacToe.py
```

## Game Controls
- **Click on the buttons** to make your move.
- **Select difficulty level** from the dropdown menu before starting.
- **Click the Restart button** to reset the game.

## How the AI Works
The AI uses the **Minimax algorithm** to make optimal moves:
- **Easy**: Random moves
- **Medium**: A mix of random and strategic moves
- **Hard**: Fully optimized using Minimax

## Sound Effects
The game includes the following sound effects:
- **Move Sound**: Played when a player makes a move
- **Win Sound**: Played when a player wins the game
- **Draw Sound**: Played when the game ends in a draw

### Adding Your Own Sound Effects
To customize the sounds, replace the **move.wav**, **win.wav**, and **draw.wav** files in the project directory with your own .wav files.

## Code Explanation
The main game logic is implemented in the **TicTacToe** class. Here are some key methods:

- **`create_buttons()`**: Creates the game board buttons.
- **`make_move(row, col)`**: Handles player moves and updates the board.
- **`ai_move()`**: Handles the AI's move based on the selected difficulty.
- **`check_winner()`**: Checks if there is a winner or a draw.
- **`restart_game()`**: Resets the game board.

## File Structure
```
TicTacToe/
├── TicTacToe.py    # Main game file
├── move.wav        # Sound effect for moves
├── win.wav         # Sound effect for winning
├── draw.wav        # Sound effect for draws
└── README.md       # Project documentation
```

## License and References
This project is released under the **MIT License**, meaning you are free to use, modify, and distribute the code, provided that the original authors are credited.

### References:
- **Tkinter Documentation**: https://docs.python.org/3/library/tkinter.html
- **Pygame Documentation**: https://www.pygame.org/docs/
- **Minimax Algorithm**: https://en.wikipedia.org/wiki/Minimax

This project was created as a learning exercise in building Python applications with GUI and AI components. The code and assets provided are free for educational and non-commercial use.

