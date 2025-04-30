from game_board import *
from state_space import *
from argparse import *
from min_max import *
from transition_model import *
from heuristic import *
from game_engine import *
from constants import *
from simple_player import *


def main():
    parser = ArgumentParser(description="Reversi Game")
    parser.add_argument('--displayAllActions', type = int, metavar = 'num', help='Display all legal moves for a board state with NUM disks')
    parser.add_argument('--methodical', type = int, metavar = 'n', help='Run a methodical game showing N first states')
    parser.add_argument('--ahead', type=int, default=None, help='Look ahead specified number of moves')
    args = parser.parse_args()


    # Initialize players
    # player_red = Simple_Player(RED)
    # player_white = Simple_Player(WHITE)
    # players = [player_red, player_white]
    # game = Game_Engine(players)
    # game.play()
    # max_disks = 7
    # player_red = Simple_Player(RED)
    # player_white = Simple_Player(WHITE)
    # players = [player_red, player_white]
    # game = Game_Engine(players)
    # game.play(max_disks=max_disks)

    # heuristic = Heuristic()
    # minmax = Min_Max(initial_state,  state_space) # default depth is 1 ,default player is MAX, default heuristic is None
    # minmax.play()

    if args.displayAllActions is not None:
        max_disks = args.displayAllActions
        player_red = Simple_Player(RED)
        player_white = Simple_Player(WHITE)
        players = [player_red, player_white]
        game = Game_Engine(players)
        game.play(max_disks=max_disks)
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