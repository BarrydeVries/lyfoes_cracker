import lyfoes
import copy
import sys
from lyfoes_puzzels import puzzel_1 as import_puzzel

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
        print(len(history))
        [print(item.config) for item in history]
        puzzel = stack.pop()
        if not check_history(puzzel, history):
            history.append(puzzel)
            possible_moves = puzzel.valid_moves()
            
            for move in possible_moves:
                copied_puzzel = copy.deepcopy(puzzel)
                copied_puzzel.apply_move(move)

                if copied_puzzel.is_finished():
                    print(copied_puzzel.moves)
                else:
                    stack.append(copied_puzzel)

    print("not solvable")


if __name__ == "__main__":
    solve_puzzel()