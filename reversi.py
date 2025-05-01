from game_board import *
from state_space import *
from argparse import *
from min_max import *
from transition_model import *
from heuristic import *
from game_engine import *
from constants import *
from simple_player import *

def simulate_game_with_simple_players(steps = None, max_disks=None, mode=None):
    player_red = Simple_Player(RED)
    player_white = Simple_Player(WHITE)
    players = [player_red, player_white]
    game = Game_Engine(players)
    game.play(steps=steps, max_disks=max_disks, mode=mode)
    time.sleep(5) # Delay for 5 seconds to view the final state
def main():

    parser = ArgumentParser(description="Reversi Game")
    parser.add_argument('--displayAllActions', type = int, metavar = 'num', help='Display all legal moves for a board state with NUM disks')
    parser.add_argument('--methodical', type = int, metavar = 'n', help='Run a methodical game showing N first states')
    parser.add_argument('--ahead', type=int, default=None, help='Look ahead specified number of moves')
    args = parser.parse_args()


    # heuristic = Heuristic()
    # minmax = Min_Max(initial_state,  state_space) # default depth is 1 ,default player is MAX, default heuristic is None
    # minmax.play()

    if args.displayAllActions is not None:
        if args.displayAllActions < NUMBER_OF_INITIAL_DISKS:
            print(f"Number of disks must be greater than {NUMBER_OF_INITIAL_DISKS}")
            return
        max_disks = args.displayAllActions
        print(f"max disks: {max_disks}")
        current_node, legal_moves = simulate_game_with_simple_players(max_disks=max_disks, mode=DIESLAY_ALL_ACTIONS)
        Game_Board().legal_moves_output(current_node, legal_moves)

    elif args.methodical is not None:
        n = args.methodical
        simulate_game_with_simple_players(steps=n, mode=METHODICAL)
        print(f"Running methodical game showing first {args.methodical} states")

    elif args.ahead is not None:# Default behavior
        pass



if __name__ == "__main__":
    main()