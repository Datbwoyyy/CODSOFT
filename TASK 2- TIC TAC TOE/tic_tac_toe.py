# Making A Tic-Tac-Toe Game.
'''About Of the Game: 
1.The user is Always X while the computer is O
2. The Game Will be Unbeatable 
3. GUI with Tkinter
-  The game board is displayed as a grid of buttons.
-  Players click buttons to make their moves.
-  The game automatically updates the GUI after each   move.
-  A popup announces the winner or a draw.

4.Minimax Algorithm
-  The AI uses Minimax to choose the best possible moves.
-  It checks all possible outcomes and makes moves that minimize the opponent's chances of winning.

I added Game levels , Easy, Medium and Hard
5.Check for a Winner

'''
## Importing libraries dependencies
import tkinter as tk
from tkinter import messagebox
import math
import pygame
import random

## Creating the Class function connecting the sound Effects 
class TicTacToe:
    def __init__(self):
        # Initialize pygame for sound effects
        pygame.mixer.init()
        self.move_sound = pygame.mixer.Sound("move.wav")
        self.win_sound = pygame.mixer.Sound("win.wav")
        self.draw_sound = pygame.mixer.Sound("draw.wav")

        # Creating the main window
        self.window = tk.Tk()
        self.window.title("Tic-Tac-Toe")
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        self.current_player = "X"
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.create_buttons()

        # Adding a new function for difficulty level
        self.difficulty = tk.StringVar(value="Hard")
        tk.Label(self.window, text="Difficulty:").grid(row=3, column=0)
        tk.OptionMenu(self.window, self.difficulty, "Easy", "Medium", "Hard").grid(row=3, column=1)

        # Adding a Restart button
        tk.Button(self.window, text="Restart", command=self.restart_game).grid(row=3, column=2)

    ## Function to create buttons random moves
    def create_buttons(self):
        for row in range(3):
            for col in range(3):
                self.buttons[row][col] = tk.Button(
                    self.window, text=" ", font=("Arial", 24), width=5, height=2,
                    command=lambda r=row, c=col: self.make_move(r, c)
                )
                self.buttons[row][col].grid(row=row, column=col)
## The Function to check a  player move
    def make_move(self, row, col):
        if self.board[row][col] == " " and self.current_player == "X":
            self.play_sound(self.move_sound)
            self.board[row][col] = "X"
            self.buttons[row][col].config(text="X")
            if self.check_winner():
                return
            self.current_player = "O"
            self.ai_move()
## The Ai Move
    def ai_move(self):
        if self.difficulty.get() == "Easy":
            move = self.random_move()
        elif self.difficulty.get() == "Medium":
            move = self.medium_ai()
        else:
            move = self.best_move()

        if move:
            row, col = move
            self.play_sound(self.move_sound)
            self.board[row][col] = "O"
            self.buttons[row][col].config(text="O")
        if self.check_winner():
            return
        self.current_player = "X"

    def random_move(self):
        # Easy difficulty: AI makes a random move
        available_moves = self.get_available_moves()
        return random.choice(available_moves) if available_moves else None

    def medium_ai(self):
        # Medium difficulty: AI makes a move based on a simple strategy (blocks player)
        available_moves = self.get_available_moves()
        for move in available_moves:
            row, col = move
            self.board[row][col] = "O"
            if self.check_winner(return_winner=True) == "O":
                self.board[row][col] = " "
                return move  # Block the player
            self.board[row][col] = " "
        return self.random_move()  # If no immediate block, make a random move

    def best_move(self):
        best_score = -math.inf
        best_move = None
        for row, col in self.get_available_moves():
            self.board[row][col] = "O"
            score = self.minimax(0, False)
            self.board[row][col] = " "
            if score > best_score:
                best_score = score
                best_move = (row, col)
        return best_move

    def get_available_moves(self):
        return [(row, col) for row in range(3) for col in range(3) if self.board[row][col] == " "]
## Implementing the unbeatable Ai moves .. available in Hard
    def minimax(self, depth, is_maximizing):
        winner = self.check_winner(return_winner=True)
        if winner == "X":
            return -1
        elif winner == "O":
            return 1
        elif winner == "Draw":
            return 0

        if is_maximizing:
            max_eval = -math.inf
            for row, col in self.get_available_moves():
                self.board[row][col] = "O"
                eval = self.minimax(depth + 1, False)
                self.board[row][col] = " "
                max_eval = max(max_eval, eval)
            return max_eval
        else:
            min_eval = math.inf
            for row, col in self.get_available_moves():
                self.board[row][col] = "X"
                eval = self.minimax(depth + 1, True)
                self.board[row][col] = " "
                min_eval = min(min_eval, eval)
            return min_eval

    def check_winner(self, return_winner=False):
        # Check rows and columns
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != " ":
                self.play_sound(self.win_sound)
                return self.board[i][0] if return_winner else self.show_winner(self.board[i][0])
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != " ":
                self.play_sound(self.win_sound)
                return self.board[0][i] if return_winner else self.show_winner(self.board[0][i])

        # Check diagonals
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != " ":
            self.play_sound(self.win_sound)
            return self.board[0][0] if return_winner else self.show_winner(self.board[0][0])
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != " ":
            self.play_sound(self.win_sound)
            return self.board[0][2] if return_winner else self.show_winner(self.board[0][2])

        # Check for a draw
        if all(self.board[row][col] != " " for row in range(3) for col in range(3)):
            self.play_sound(self.draw_sound)
            return "Draw" if return_winner else self.show_winner("Draw")

        return None

    def play_sound(self, sound):
        sound.play()

    def show_winner(self, winner):
        if winner == "Draw":
            messagebox.showinfo("Tic-Tac-Toe", "It's a draw!")
        else:
            messagebox.showinfo("Tic-Tac-Toe", f"{winner} wins!")
        self.restart_game()

    def restart_game(self):
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        for row in range(3):
            for col in range(3):
                self.buttons[row][col].config(text=" ")
        self.current_player = "X"

    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    game = TicTacToe()
    game.run()
