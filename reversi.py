from game_board import *
from state_space import *
from argparse import *
from min_max import *


def main():
    parser = ArgumentParser(description="Reversi Game")
    parser.add_argument('--displayAllActions', type = int, metavar = 'num', help='Display all legal moves for a board state with NUM disks')
    parser.add_argument('--methodical', type = int, metavar = 'n', help='Run a methodical game showing N first states')
    parser.add_argument('--ahead', type=int, default=None, help='Look ahead specified number of moves')
    args = parser.parse_args()

    game_board = Game_Board()
    state_space = State_Space(game_board)
    initial_state = state_space.get_initial_state()
    minmax = Min_Max(initial_state,  state_space)

    if args.displayAllActions is not None:
        # Generate a board with this many disks and show all legal moves
        print(f"Displaying all actions for board with {args.displayAllActions} disks")
        # Your implementation here
    elif args.methodical is not None:
        print(f"Running methodical game showing first {args.methodical} states")
        # Your implementation here
    elif args.ahead is not None:# Default behavior
        game_board.display_board()
        game_board.display_GUI_board(game_board.board)

    # start_state = state_space.get_initial_state()
    game_board.display_board()
    game_board.display_GUI_board(game_board.board)

if __name__ == "__main__":
    main()