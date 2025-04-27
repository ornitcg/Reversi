from constants import *
from tkinter import *

class Game_Board:
    def __init__(self, size = SIDE_SIZE, board = None):
        self.board = board
        self.cols = size
        self.rows = size
        if self.board is None:
            self.init_board(size)
        self.winner = None
        self.game_over = False
        self.black_count = 0
        self.white_count = 0



    def init_board(self, size):
        self.board = []
        for i in range(size):
            row = []
            for j in range(size):
                row.append(EMPTY)
            self.board.append(row)

        self.board[MIDDLE-1][MIDDLE-1] = TURN_RED
        self.board[MIDDLE-1][MIDDLE] = TURN_WHITE
        self.board[MIDDLE][MIDDLE-1] = TURN_WHITE
        self.board[MIDDLE][MIDDLE] = TURN_RED

    def display_board(self):
        for row in self.board:
            for i in range(SIDE_SIZE):
                print(row[i], end=' ')
            print()


    def display_GUI_board(self, board):
        rows = SIDE_SIZE
        cols = rows
        cell_size = CELL_SIZE
        width = cols * cell_size
        height = rows * cell_size

        # Create the main window
        root = Tk()
        root.title("Reversi")

        # Create a canvas to draw on
        canvas = Canvas(root, width=width, height=height+EXTRA, bg=BACKGROUND_COLOR)
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

                # Draw the cells content based on cells values
                cell_value = board[row][col]
                if cell_value == TURN_RED:
                    canvas.create_oval(
                        x1 + PADDING, y1 + PADDING,
                        x2 - PADDING, y2 - PADDING,
                        fill=FILL_COLOR_PLAYER1
                    )
                elif cell_value == TURN_WHITE:  # Player 2 (white)
                    canvas.create_oval(
                        x1 + PADDING, y1 + PADDING,
                        x2 - PADDING, y2 - PADDING,
                        fill=FILL_COLOR_PLAYER2, outline=OUTLINE_COLOR
                    )


        # Start the GUI event loop
        root.mainloop()






    def get_board(self):
        return self.board