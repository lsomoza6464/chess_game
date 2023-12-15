#from piece_sets import white_set, black_set, en_passant_pawns
class Piece():
    def __init__(self, color, type, location):
        self.name = color + type
        self.color = color
        self.type = type
        self.location = location
        self.hasMoved = False
    
