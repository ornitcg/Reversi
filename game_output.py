from constants import *
from tkinter import *
import copy
from action import Action
import time
from player import *
from simple_player import *
from state_space import *
import sys

class Game_Output:
    def __init__(self, state_space, size = SIDE_SIZE):
        self.cols = size
        self.rows = size
        self.state_space = state_space
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




    def display_textual_board(self, board , output_file = None):
        for row in board:
            for i in range(SIDE_SIZE):
                print(row[i], end=' ', file=output_file)
            print(file=output_file)
        print()

    def display_graphic_board(self, board, player=None, wait = False):
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
        if wait:
            time.sleep(0.5)


    def legal_moves_output(self, current_node, legal_moves):

        with open('Output.txt', 'a') as output_file:
            original_stdout = sys.stdout  # Save the original stdout
            sys.stdout = output_file
            print("\n\n*************** Display all actions: ***************")
            print("Player 1 - X (red) , Player 2 - O (white)")

            for action in legal_moves:
                print("\nState number: ", current_node.get_total_count() - NUMBER_OF_INITIAL_DISKS)
                board = current_node.get_board()
                self.display_textual_board(board, output_file)

                successor_node = self.state_space.get_successor(current_node, action)
                print(f"State number: {successor_node.get_total_count() - NUMBER_OF_INITIAL_DISKS}", end=' ')
                print(f"\nPlayer {current_node.get_turn().get_color()} moved, Action ADD{action.get_position()}")

                board = successor_node.get_board()
                self.display_textual_board(board, output_file)
                # print each player's disks count
                print(f"Result: Player X:{successor_node.get_red_count()} disks ,Player O: {successor_node.get_white_count()} disks. Total disks = {successor_node.get_total_count()}")
                print("---------------------------------------------------")
            sys.stdout = original_stdout


    def display_methodical_title(self):
        original_stdout = sys.stdout
        with open('Output.txt', 'a') as output_file:
            sys.stdout = output_file
            print("\n\n*************** Methodical: ***************")
        sys.stdout = original_stdout

    def methodical_output(self, current_node, steps_count):
        original_stdout = sys.stdout
        with open('Output.txt', 'a') as output_file:
            sys.stdout = output_file
            print(f"Step number {steps_count}")
            self.display_textual_board(current_node.get_board(), output_file)
            print(f"Red count: {current_node.get_red_count()} White count: {current_node.get_white_count()}")
            print("---------------------------------------------------")
        sys.stdout = original_stdout