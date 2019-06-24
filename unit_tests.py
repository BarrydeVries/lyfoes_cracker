from lyfoes import Lyfoes

game = Lyfoes(2,[1, 0, 0, 0, 1, 1, 1, 0])
game.print_puzzel()
game.print_tube(1)
print(game.get_tube(1))
print(game.is_finished())
print(game.valid_moves())
