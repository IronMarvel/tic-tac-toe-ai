import tkinter as tk
from tkinter import messagebox
import math

class TicTacToeGUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Tic Tac Toe - AI Opponent")
        self.window.resizable(False, False)

        # Game state
        self.board = [' '] * 9          # 0..8 for positions
        self.current_player = 'X'       # Human starts with X
        self.game_active = True

        # UI elements
        self.buttons = []
        self.create_board()

        # Status label
        self.status_label = tk.Label(self.window, text="Your turn (X)", font=('Arial', 14))
        self.status_label.grid(row=3, column=0, columnspan=3, pady=10)

        # Reset button
        reset_btn = tk.Button(self.window, text="New Game", font=('Arial', 12), command=self.reset_game)
        reset_btn.grid(row=4, column=0, columnspan=3, pady=10)

        self.window.mainloop()

    def create_board(self):
        """Create 3x3 grid of buttons."""
        for i in range(9):
            btn = tk.Button(
                self.window,
                text=' ',
                font=('Arial', 24, 'bold'),
                width=5,
                height=2,
                command=lambda idx=i: self.on_click(idx)
            )
            btn.grid(row=i // 3, column=i % 3, padx=5, pady=5)
            self.buttons.append(btn)

    def on_click(self, idx):
        """Handle player's move."""
        if not self.game_active:
            return
        if self.board[idx] != ' ':
            return
        if self.current_player != 'X':
            return

        # Make move
        self.make_move(idx, 'X')

        # Check game over
        if self.check_game_over():
            return

        # AI move
        self.window.after(500, self.ai_move)   # slight delay for better UX

    def ai_move(self):
        """Computer makes a move using minimax."""
        if not self.game_active:
            return
        if self.current_player != 'O':
            return

        best_score = -math.inf
        best_move = None
        for i in range(9):
            if self.board[i] == ' ':
                self.board[i] = 'O'
                score = self.minimax(self.board, 0, False, -math.inf, math.inf)
                self.board[i] = ' '
                if score > best_score:
                    best_score = score
                    best_move = i

        if best_move is not None:
            self.make_move(best_move, 'O')
            self.check_game_over()

    def minimax(self, board, depth, is_maximizing, alpha, beta):
        """
        Minimax with alpha-beta pruning.
        is_maximizing = True for AI (O), False for player (X).
        """
        winner = self.check_winner_state(board)
        if winner == 'O':
            return 10 - depth   # Prefer faster win
        elif winner == 'X':
            return depth - 10   # Prefer slower loss
        elif self.is_draw_state(board):
            return 0

        if is_maximizing:
            max_eval = -math.inf
            for i in range(9):
                if board[i] == ' ':
                    board[i] = 'O'
                    eval = self.minimax(board, depth + 1, False, alpha, beta)
                    board[i] = ' '
                    max_eval = max(max_eval, eval)
                    alpha = max(alpha, eval)
                    if beta <= alpha:
                        break
            return max_eval
        else:
            min_eval = math.inf
            for i in range(9):
                if board[i] == ' ':
                    board[i] = 'X'
                    eval = self.minimax(board, depth + 1, True, alpha, beta)
                    board[i] = ' '
                    min_eval = min(min_eval, eval)
                    beta = min(beta, eval)
                    if beta <= alpha:
                        break
            return min_eval

    def make_move(self, idx, player):
        """Place a mark and update UI."""
        self.board[idx] = player
        self.buttons[idx].config(text=player, state=tk.DISABLED)

        # Switch turn
        self.current_player = 'O' if player == 'X' else 'X'
        if self.game_active:
            if self.current_player == 'X':
                self.status_label.config(text="Your turn (X)")
            else:
                self.status_label.config(text="AI thinking...")

    def check_game_over(self):
        """Check for win or draw and handle accordingly."""
        winner = self.check_winner_state(self.board)
        if winner:
            self.game_active = False
            if winner == 'X':
                self.status_label.config(text="You win!")
                messagebox.showinfo("Game Over", "Congratulations! You won!")
            else:
                self.status_label.config(text="AI wins!")
                messagebox.showinfo("Game Over", "AI wins! Better luck next time.")
            self.disable_buttons()
            return True
        elif self.is_draw_state(self.board):
            self.game_active = False
            self.status_label.config(text="It's a draw!")
            messagebox.showinfo("Game Over", "It's a draw!")
            self.disable_buttons()
            return True
        return False

    def check_winner_state(self, board):
        """Return 'X' or 'O' if there's a winner, else None."""
        win_patterns = [
            [0,1,2], [3,4,5], [6,7,8],  # rows
            [0,3,6], [1,4,7], [2,5,8],  # columns
            [0,4,8], [2,4,6]            # diagonals
        ]
        for pattern in win_patterns:
            if board[pattern[0]] == board[pattern[1]] == board[pattern[2]] != ' ':
                return board[pattern[0]]
        return None

    def is_draw_state(self, board):
        """Check if board is full and no winner."""
        return ' ' not in board

    def disable_buttons(self):
        """Disable all buttons after game ends."""
        for btn in self.buttons:
            btn.config(state=tk.DISABLED)

    def reset_game(self):
        """Reset the board and enable buttons."""
        self.board = [' '] * 9
        self.current_player = 'X'
        self.game_active = True
        for btn in self.buttons:
            btn.config(text=' ', state=tk.NORMAL)
        self.status_label.config(text="Your turn (X)")

if __name__ == "__main__":
    game = TicTacToeGUI()
