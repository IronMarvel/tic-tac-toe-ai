# Tic‑Tac‑Toe with AI (Minimax + Alpha‑Beta Pruning)

A classic Tic‑Tac‑Toe game built with Python's `tkinter` library. You play against an unbeatable AI opponent powered by the **Minimax algorithm** with **alpha‑beta pruning**. The AI always makes the optimal move, making it impossible to win – you can only hope for a draw!

---

## Features

- 🎮 **Graphical user interface** (GUI) using `tkinter`
- 🤖 **Unbeatable AI** – uses minimax with alpha‑beta pruning to choose the best move
- 🧠 **Turn‑based gameplay** – you are `X`, AI is `O`
- 🔁 **New Game** button to reset the board at any time
- 📢 **Game over notifications** with winner/draw messages

---

## AI Algorithm

The AI uses the **Minimax algorithm**, a recursive search that simulates all possible future moves. It assigns scores to each board state:
- **+10** for an AI win (with depth penalty to prefer faster wins)
- **–10** for a human win
- **0** for a draw

The algorithm alternates between maximizing (AI) and minimizing (human) scores. To make it efficient, **alpha‑beta pruning** is added, which cuts off branches that cannot affect the final decision. This allows the AI to evaluate the game tree quickly, even though the full game tree is small (9! possible games).

---

## Requirements

- **Python 3.x** (built‑in `tkinter` is included with standard Python installations on Windows, macOS, and most Linux distributions)
- No external packages required – just Python!

---

## How to Run

1. **Clone or download** this repository to your local machine.
2. Open a terminal / command prompt in the project folder.
3. Run the script:

   ```bash
   python tic_tac_toe.py
