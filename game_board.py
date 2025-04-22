from constants import *
from tkinter import *

class Game_Board:
    def __init__(self, size = SIDE_SIZE):
        self.board = []
        self.cols = size
        self.rows = size
        self.init_board(size)
        self.winner = None
        self.game_over = False


    def init_board(self, size):
        for i in range(size):
            row = []
            for j in range(size):
                row.append(EMPTY)
            self.board.append(row)
        self.board[3][3] = TURN_BLACK
        self.board[3][4] = TURN_WHITE
        self.board[4][3] = TURN_WHITE
        self.board[4][4] = TURN_BLACK

    def display_board(self):
        for row in self.board:
            for i in range(SIDE_SIZE):
                print(row[i], end=' ')
            print()


    def display_GUI_board(self, board):
        rows = SIDE_SIZE
        cols = rows
        cell_size = 60
        width = cols * cell_size
        height = rows * cell_size

        # Create the main window
        root = Tk()
        root.title("Reversi")

        # Create a canvas to draw on
        canvas = Canvas(root, width=width, height=height, bg="light blue")
        canvas.pack()

        # Draw the grid and pieces
        for row in range(rows):
            for col in range(cols):
                # Calculate position
                x1 = col * cell_size
                y1 = row * cell_size
                x2 = x1 + cell_size
                y2 = y1 + cell_size

                # Draw cell border
                canvas.create_rectangle(x1, y1, x2, y2, outline="black")

                # Draw the piece based on cell value
                cell_value = board[row][col]
                if cell_value == TURN_BLACK:  # Player 1 (black)
                    canvas.create_oval(
                        x1 + 5, y1 + 5,
                        x2 - 5, y2 - 5,
                        fill="black"
                    )
                elif cell_value == TURN_WHITE:  # Player 2 (white)
                    canvas.create_oval(
                        x1 + 5, y1 + 5,
                        x2 - 5, y2 - 5,
                        fill="white", outline="black"
                    )

        # # Add row and column labels
        # for i in range(rows):
        #     canvas.create_text(
        #         5, i * cell_size + cell_size // 2,
        #         text=str(i), fill="white", anchor=W
        #     )

        # for j in range(cols):
        #     canvas.create_text(
        #         j * cell_size + cell_size // 2, 5,
        #         text=str(j), fill="white", anchor=N
        #     )

        # Start the GUI event loop
        root.mainloop()