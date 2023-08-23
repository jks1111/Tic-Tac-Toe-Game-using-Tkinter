import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")
        self.current_player = "X"
        self.board = [["" for _ in range(3)] for _ in range(3)]
        
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        for i in range(3):
            for j in range(3):
                self.buttons[i][j] = tk.Button(root, text="", font=("Helvetica", 24), width=5, height=2,
                                              command=lambda row=i, col=j: self.make_move(row, col))
                self.buttons[i][j].grid(row=i, column=j)
        
    def make_move(self, row, col):
        if self.board[row][col] == "" and not self.check_winner():
            self.board[row][col] = self.current_player
            self.buttons[row][col]["text"] = self.current_player
            self.buttons[row][col]["state"] = "disabled"  # Disable the button after making a move
            if self.check_winner():
                for i in range(3):
                    for j in range(3):
                        self.buttons[i][j]["state"] = "disabled"  # Disable all buttons after game over
                messagebox.showinfo("Game Over", f"Player {self.current_player} wins!")
            elif all(self.board[i][j] != "" for i in range(3) for j in range(3)):
                messagebox.showinfo("Game Over", "It's a draw!")
            else:
                self.current_player = "O" if self.current_player == "X" else "X"
        
    def check_winner(self):
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != "":
                return True
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != "":
                return True
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != "":
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != "":
            return True
        return False

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
