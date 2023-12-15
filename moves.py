from piece_sets import white_set, black_set, en_passant_pawns, white_king_location, black_king_location, white_pieces, black_pieces
class Moves():
    def __init__(self):
        self.currentPiece = None
        self.opponentSet = None
        self.mySet = None

    def get_moves(self, piece, notMyTurn = None):
        self.currentPiece = piece
        if self.currentPiece.color == 'w':
            self.opponentSet = black_set
            self.mySet = white_set
            current_color = 'white'
        else:
            self.opponentSet = white_set
            self.mySet = black_set
            current_color = 'black'
        if piece.type == 'rook':
            moves_list =  self.rook_moves()
        elif piece.type == 'knight':
            moves_list = self.knight_moves()
        elif piece.type == 'bishop':
            moves_list = self.bishop_moves()
        elif piece.type == 'king':
            moves_list = self.king_moves()
        elif piece.type == 'queen':
            moves_list = self.queen_moves()
        else:
            moves_list = self.pawn_moves()
        """This checks to see if making this move will put the king in check"""
        if(not(notMyTurn)):
            self.remove_moves_in_check(moves_list, piece, current_color)
        return moves_list
    
    def remove_moves_in_check(self, moves_list, piece, color):
        if color == 'white':
            current_set = white_set
        else:
            current_set = black_set
        current_location = piece.location
        current_set.remove(current_location)
        removedArr = []
        for temp_location in moves_list:
            current_set.add(temp_location)
            if self.in_check(color):
                removedArr.append(temp_location)
            self.mySet = current_set #maybe not needed
            current_set.remove(temp_location)
        current_set.add(current_location)
        for location in removedArr:
            moves_list.remove(location)
        return moves_list
    
    def is_checkmate(self, color):
        if color == 'white':
            my_list = white_pieces
            current_set = white_set
        else:
            my_list = black_pieces
            current_set = black_set
        for piece in my_list:
            current_location = piece.location
            current_set.remove(current_location)
            for move in self.get_moves(piece, "Not my turn"):
                current_set.add(move)
                if not self.in_check(color):
                    return False
                current_set.remove(move)
            current_set.add(current_location)
        return True
                
                
    def diagonal_moves(self):
        moves = set()
        for i in range(4):
            if i == 0:
                r = 1
                c = 1
            elif i == 1:
                r = 1
                c = -1
            elif i == 2:
                r = -1
                c = 1
            else:
                r = -1
                c = -1
            x = self.currentPiece.location[0] + r
            y = self.currentPiece.location[1] + c
            while 0 <= x <= 7 and 0 <= y <= 7 and (x, y) not in self.opponentSet and (x, y) not in self.mySet:
                moves.add((x, y))
                x += r
                y += c
            if (x, y) in self.opponentSet:
                moves.add((x, y))
        return moves

    def horizontal_moves(self):
        moves = set()
        for i in range(4):
            if i == 0:
                r = 1
                c = 0
            elif i == 1:
                r = -1
                c = 0
            elif i == 2:
                r = 0
                c = 1
            else:
                r = 0
                c = -1
            x = self.currentPiece.location[0] + r
            y = self.currentPiece.location[1] + c
            while 0 <= x <= 7 and 0 <= y <= 7 and (x, y) not in self.opponentSet and (x, y) not in self.mySet:
                moves.add((x, y))
                x += r
                y += c
            if (x, y) in self.opponentSet:
                moves.add((x, y))
        return moves

    def knight_moves(self):
        moves = set()
        for i in range(2):
            for j in range(4):
                if(i == 0):
                    r = 2
                    c = 1
                else:
                    r = 1
                    c = 2
                if j <= 1:
                    r *= -1
                if 1 <= j <= 2:
                    c *= -1
                x = self.currentPiece.location[0] + r
                y = self.currentPiece.location[1] + c
                if 0 <= x <= 7 and 0 <= y <= 7 and (x, y) not in self.mySet:
                    moves.add((x, y)) #could also do x, y and y, x
        #print(moves)
        return moves

    def bishop_moves(self):
        return self.diagonal_moves()

    def rook_moves(self):
        return self.horizontal_moves()

    def queen_moves(self):
        output = self.diagonal_moves()
        for elem in self.horizontal_moves():
            output.add(elem)
        return output

    def king_moves(self):
        moves = set()
        x = self.currentPiece.location[0]
        y = self.currentPiece.location[1]
        for i in range(-1, 2):
            if 0 <= x + i <= 7 and 0 <= y - 1 <= 7 and (x + i, y - 1) not in self.mySet:
                moves.add((x + i, y - 1))
        for i in range(-1, 2):
            if 0 <= x + i <= 7 and 0 <= y + 1 <= 7 and (x + i, y + 1) not in self.mySet:
                moves.add((x + i, y + 1))
        for i in range(-1, 2, 2):
            if 0 <= x + i <= 7 and 0 <= y <= 7 and (x + i, y) not in self.mySet:
                moves.add((x + i, y))
        return moves

    def pawn_moves(self):
        moves = set()
        x = self.currentPiece.location[0]
        y = self.currentPiece.location[1]
        direction = 1
        if self.currentPiece.color == 'b':
            direction = -1
        if  0 <= y + direction <= 7 and (x, y + direction) not in self.mySet and (x, y + direction) not in self.opponentSet:
            moves.add((x, y + direction))
        for i in range(-1, 2, 2):
            if  0 <= y + direction <= 7 and 0 <= x + i <= 7 and (x + i, y + direction) not in self.mySet and ((x + i, y + direction) in self.opponentSet or (x + i, y + direction) in en_passant_pawns):
                moves.add((x + i, y + direction))
        if self.currentPiece.hasMoved == False and (direction == 1 and (x, 3) not in self.mySet and (x, 3) not in self.opponentSet):
            moves.add((x, 3))
            #en_passant_pawns.add((x, 2))
        if self.currentPiece.hasMoved == False and (direction == -1 and (x, 4) not in self.mySet and (x, 4) not in self.opponentSet):
            moves.add((x, 4))
        return moves
    
    def get_all_moves(self, pieces):
        allMoves = set()
        for piece in pieces:
            for move in self.get_moves(piece, "Not my turn"):
                if move not in allMoves:
                    allMoves.add(move)
        return allMoves

    def in_check(self, color):
        if color == 'white':
            opponent_list = black_pieces
            my_king_location = white_king_location
        else:
            opponent_list = white_pieces
            my_king_location = black_king_location
        return my_king_location in self.get_all_moves(opponent_list)
        
        
