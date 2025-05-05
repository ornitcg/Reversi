from game_output import *
from state_space import *
from argparse import *
from min_max import *
from transition_model import *
from heuristic import *
from game_engine import *
from constants import *
from simple_player import *
from smart_player import *

def simulate_game(transition_model,state_space,  steps = None, max_disks=None, mode=None, heuristic = None, tree =None , wait = False):
    game = Game_Engine(transition_model ,state_space, heuristic=heuristic, tree=tree)
    game.play(steps=steps, max_disks=max_disks, mode=mode, wait=wait)
    if wait:
        time.sleep(3) # Delay to view the final state


def main():
    parser = ArgumentParser(description="Reversi Game")
    parser.add_argument('--displayAllActions', type = int, metavar = 'num', help='Display all legal moves for a board state with NUM disks')
    parser.add_argument('--methodical', type = int, metavar = 'n', help='Run a methodical game showing N first states')
    parser.add_argument('--ahead', type=int, default=None, help='Look ahead specified number of moves')
    parser.add_argument('command', nargs='?', choices=['H'], help='Use H to run game with heuristic evaluation')

    args = parser.parse_args()
    players = [Simple_Player(RED), Simple_Player(WHITE)]
    tm = Transition_Model(players)
    sp = State_Space(tm)

    if args.displayAllActions is not None:
        if args.displayAllActions < NUMBER_OF_INITIAL_DISKS:
            print(f"Number of disks must be greater than {NUMBER_OF_INITIAL_DISKS}")
            return
        max_disks = args.displayAllActions
        print(f"max disks: {max_disks}")
        simulate_game(tm, sp, max_disks=max_disks, mode=DISPLAY_ALL_ACTIONS)


    elif args.methodical is not None:
        n = args.methodical
        simulate_game(tm, sp, steps=n, mode=METHODICAL)
        print(f"Running methodical game showing first {args.methodical} states")


    elif args.command == 'H' and args.ahead is not None:
       players = [Smart_Player(RED), Smart_Player(WHITE)]
       tm = Transition_Model(players)
       sp = State_Space(tm)
       heuristic = Heuristic(tm)
       min_max = Min_Max(tm, sp, heuristic=heuristic)
       simulate_game(tm, sp, mode=H, heuristic=min_max, steps=args.ahead)


    elif args.command == 'H':
        # Running game with heuristic evaluation
        players = [Smart_Player(RED), Smart_Player(WHITE)]
        tm = Transition_Model(players)
        sp = State_Space(tm)
        heuristic = Heuristic(tm)
        simulate_game(tm, sp , mode=H, heuristic= heuristic)




if __name__ == "__main__":
    main()

    print(f"Running game with heuristic evaluation")
    players = [Smart_Player(RED), Smart_Player(WHITE)]
    tm = Transition_Model(players)
    sp = State_Space(tm)
    heuristic = Heuristic(tm)
    # simulate_game(tm, sp, mode=H, heuristic=heuristic, wait = False)


