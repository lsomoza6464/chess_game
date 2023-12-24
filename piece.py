#from piece_sets import white_set, black_set, en_passant_pawns
class Piece():
    def __init__(self, color, type, location):
        self.name = color + type
        self.color = color
        self.type = type
        self.location = location
        self.hasMoved = False
        self.firstMove = False
    
    def __eq__(self, other):
        return isinstance(other, Piece) and self.name == other.name and self.location == other.location
    
    def __hash__(self):
        return hash(self.name + self.color + str(self.location))
