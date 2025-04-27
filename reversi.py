from game_board import *
from state_space import *
from argparse import *
from min_max import *
from transition_model import *
from heuristic import *


def main():
    parser = ArgumentParser(description="Reversi Game")
    parser.add_argument('--displayAllActions', type = int, metavar = 'num', help='Display all legal moves for a board state with NUM disks')
    parser.add_argument('--methodical', type = int, metavar = 'n', help='Run a methodical game showing N first states')
    parser.add_argument('--ahead', type=int, default=None, help='Look ahead specified number of moves')
    args = parser.parse_args()

    transition_model = Transition_Model()
    state_space = State_Space( transition_model, SIDE_SIZE)
    initial_state = state_space.get_initial_state()
    heuristic = Heuristic()
    minmax = Min_Max(initial_state,  state_space) # default depth is 1 ,default player is MAX, default heuristic is None
    minmax.play()

    if args.displayAllActions is not None:
        # Generate a board with this many disks and show all legal moves
        print(f"Displaying all actions for board with {args.displayAllActions} disks")
        # Your implementation here
    elif args.methodical is not None:
        print(f"Running methodical game showing first {args.methodical} states")
        # Your implementation here
    elif args.ahead is not None:# Default behavior
        pass



if __name__ == "__main__":
    main()