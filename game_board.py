from constants import *
from tkinter import *

class Game_Board:
    def __init__(self, size = SIDE_SIZE):
        self.cols = size
        self.rows = size
        self.canvas = None
        self.root = None

    def initialize_GUI(self):
        rows = SIDE_SIZE
        cols = rows
        cell_size = CELL_SIZE
        width = cols * cell_size
        height = rows * cell_size

        # Create the main window
        self.root = Tk()
        self.root.title("Reversi")

        # Create a canvas to draw on
        self.canvas = Canvas(self.root, width=width, height=height + EXTRA, bg=BACKGROUND_COLOR)
        self.canvas.pack()




    def display_textual_board(self, board):
        for row in board:
            for i in range(SIDE_SIZE):
                print(row[i], end=' ')
            print()
        print('\n\n')



    def display_GUI_board(self, board):
        if self.canvas is None or self.root is None:
            self.initialize_GUI()

        self.canvas.delete("all")  # Clear the canvas before redrawing



        # Draw the grid and pieces
        for row in range(self.rows):
            for col in range(self.cols):
                # Calculate position
                x1 = col * CELL_SIZE
                y1 = row * CELL_SIZE
                x2 = x1 + CELL_SIZE
                y2 = y1 + CELL_SIZE

                # Draw cell border
                self.canvas.create_rectangle(x1, y1, x2, y2, outline="black")

                # Draw the cells content based on cells values
                cell_value = board[row][col]
                if cell_value == TURN_RED:
                    self.canvas.create_oval(
                        x1 + PADDING, y1 + PADDING,
                        x2 - PADDING, y2 - PADDING,
                        fill=FILL_COLOR_PLAYER1
                    )
                elif cell_value == TURN_WHITE:  # Player 2 (white)
                    self.canvas.create_oval(
                        x1 + PADDING, y1 + PADDING,
                        x2 - PADDING, y2 - PADDING,
                        fill=FILL_COLOR_PLAYER2, outline=OUTLINE_COLOR
                    )

        self.root.update_idletasks()
        self.root.update()




