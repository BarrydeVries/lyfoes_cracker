import lyfoes
import copy
import sys
from lyfoes_puzzels import puzzel_3 as import_puzzel

''' Make function to input command line arguments, also allow for imports'''

# Check if puzzel is in history, returns true if so, false if not.
def check_history(puzzel, history):
    for item in history:
        if item.config == puzzel.config:
            return True
    return False

# Main solver code.
def solve_puzzel():
    stack = [lyfoes.Lyfoes(import_puzzel)]
    history = []

    while stack:
        print(len(stack), len(history))
        puzzel = stack.pop()
        if not check_history(puzzel, history):
            history.append(puzzel)
            possible_moves = puzzel.valid_moves()
            
            for move in possible_moves:
                copied_puzzel = lyfoes.Lyfoes(copy.deepcopy(puzzel.config))
                copied_puzzel.moves = copy.deepcopy(puzzel.moves)

                copied_puzzel.apply_move(move)
                if copied_puzzel.is_finished():
                    print(copied_puzzel.moves)
                    exit()
                else:
                    stack = [copied_puzzel] + stack

    print("not solvable")


if __name__ == "__main__":
    solve_puzzel()