'''
The Lyfoes class contains:
moves       -A list of previous moves.
move_count  -A counter that counts the number of moves.
tubes       -The number of tubes in the game.
config      -A single list of numbers, 0 for gaps, 1.. for colors.
'''

import sys

class Lyfoes:
    moves = []
    move_count = 0

    def __init__(self, config):
        if( len(config) % 4 == 0):
            self.tubes = int(len(config) / 4)
            self.config = config
        else:
            print("config should be a mutiple of 4.")
            sys.exit()

    # Get tube on given index.
    def get_tube(self, index):
        if(index >= self.tubes):
            return None
        return self.config[4 * index : 4*( index + 1)]

    # Print tube on given index.
    def print_tube(self, index):
        print(self.get_tube(index))

    # Print entire puzzel.
    def print_puzzel(self):
        print(self.config)

    # Verify if game is finished.
    def is_finished(self):
        for index in range(self.tubes):
            tube = self.get_tube(index)
            if(not (tube[0] == tube[1] == tube[2] == tube[3])):
                return False
        return True
    
    # Returns the top vaue of the tube and the next open spot or 0,0,index for empty tube.
    def top_value(self, index):
        if(self.get_tube(index)[0] == 0):
            return 0, 0, index
        for i in range(1,4):
            if(self.get_tube(index)[i] == 0):
                return self.get_tube(index)[i-1], i, index
        return self.get_tube(index)[3], 4, index

    # Determine wheter a move that starts at start and ends at end is valid.
    # Then append it to a list of all possible moves, with the appropriate indexes
    # included.
    def valid_move(self, start, end, moves):
        start_move = self.top_value(start)
        end_move = self.top_value(end)

        # Ensure the start tube is nonempty.
        if(start_move[0] != 0 ):
            if(end_move[0] == 0 or (end_move[1] != 4 and end_move[0] == start_move[0])):
                moves.append((start_move, end_move))

    # Get all valid moves in curren position (as list of tuples).
    def valid_moves(self):
        move_list = []
        for start_index in range(self.tubes):
            for end_index in range(self.tubes):
                if(start_index != end_index):
                    self.valid_move(start_index, end_index, move_list)
        return move_list

    # Apply move to game, moves consist of two 3-tuples, first the value, then
    # the next open spot and then the index of the tube.
    def apply_move(self, move):
        start = move[0]
        end = move[1]

        value = start[0]

        # Set start value to 0, end value to desired value.
        self.config[4 * start[2] + start[1] - 1] = 0
        self.config[4 * end[2] + end[1]] = value
        self.moves.append(move)

