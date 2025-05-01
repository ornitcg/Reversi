from constants import *
from tkinter import *
import copy
from action import Action
import time
from player import *
from simple_player import *

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


    def display_graphic_board(self, board, player=None):
        if self.canvas is None or self.root is None:
            self.initialize_GUI()

        self.canvas.delete("all")  # Clear the canvas before redrawing

        if player is not None:
            if  player.get_color() == RED:
                player_color = "red"
            else:
                player_color = "white"

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
                if cell_value == RED:
                    self.canvas.create_oval(
                        x1 + PADDING, y1 + PADDING,
                        x2 - PADDING, y2 - PADDING,
                        fill=FILL_COLOR_PLAYER1
                    )
                elif cell_value == WHITE:  # Player 2 (white)
                    self.canvas.create_oval(
                        x1 + PADDING, y1 + PADDING,
                        x2 - PADDING, y2 - PADDING,
                        fill=FILL_COLOR_PLAYER2, outline=OUTLINE_COLOR
                    )
                elif cell_value == LEGAL:
                    self.canvas.create_oval(
                        x1 + LEGAL_PADDING, y1 + LEGAL_PADDING,
                        x2 - LEGAL_PADDING, y2 - LEGAL_PADDING,
                        fill = BACKGROUND_COLOR  , outline=player_color, width=5
                    )

        self.root.update_idletasks()
        self.root.update()


    def legal_moves_output(self, current_node, legal_moves):
        print("********* Display all actions: ***************")
        print("Player 1 - X (red) , Player 2 - O (white)")

        for action in legal_moves:
            successor_node = self.state_space.get_successor(current_node, action)
            print("\nState number: ", current_node.get_total_count() - NUMBER_OF_INITIAL_DISKS)
            self.game_board.display_textual_board(current_node.get_board())

            print(f"State number: {successor_node.get_total_count() - NUMBER_OF_INITIAL_DISKS}", end=' ')

            print(f"\nPlayer {current_node.get_turn().get_color()} moved, Action ADD{action.get_position()}")
            self.game_board.display_textual_board(successor_node.get_board())
            #print each player's disks
            print(f"Result: Player X:{successor_node.get_red_count()} disks ,Player O: {successor_node.get_white_count()} disks. Total disks = {successor_node.get_total_count()}")

    def methodical_output(self, current_node, steps_count):
        print(f"Step number {steps_count}")
        self.game_board.display_textual_board(current_node.get_board())
        print(f"Red count: {current_node.get_red_count()} White count: {current_node.get_white_count()}")
