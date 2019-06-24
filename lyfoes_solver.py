import lyfoes
from lyfoes_puzzels import puzzel_1

''' Make function to input command line arguments, also allow for imports'''

puzzel = lyfoes.Lyfoes(17, puzzel_1)
print(len(puzzel.valid_moves()))