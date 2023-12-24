from piece_sets import white_set, black_set, white_en_passant_pawns, black_en_passant_pawns, white_king_location, black_king_location, white_pieces, black_pieces
class Moves():
    def __init__(self):
        self.currentPiece = None
        self.opponentSet = None
        self.mySet = None
        self.whiteKingLoc = white_king_location
        self.blackKingLoc = black_king_location

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
            #print(moves_list)
            print()
            self.remove_moves_in_check(moves_list, piece, current_color)
        return moves_list
    
    def remove_moves_in_check(self, moves_list, piece, color):
        if color == 'white':
            current_set = white_set
            opponent_set = black_set
            #pieces = white_pieces
            opponent_pieces = black_pieces
        else:
            current_set = black_set
            opponent_set = white_set
            #pieces = black_pieces
            opponent_pieces = white_pieces
        current_location = piece.location
        current_set.remove(current_location)
        removedArr = []
        temp_pieces = set()
        for temp_location in moves_list:
            current_set.add(temp_location)
            if temp_location in opponent_set:
                opponent_set.remove(temp_location)
                #temp_pieces = []
                for elem in opponent_pieces:
                    if elem.location != temp_location and not(elem in temp_pieces):
                        temp_pieces.add(elem)
                    #else:
                        #print("elem" + str(elem.location))
                #print("temp pieces for " + str(temp_location))
                #for elem in temp_pieces:
                    #print(str(elem.location))
                opponent_set.add(temp_location)
            else:
                temp_pieces = opponent_pieces
            #for elem in temp_pieces:
                #print(str(elem.location))
            #print(temp_pieces)
            if color == 'white':
                if piece.type == 'king':
                    real_white_king = self.whiteKingLoc
                    self.whiteKingLoc = temp_location
                if self.in_check(color, self.whiteKingLoc, temp_pieces):
                    removedArr.append(temp_location)
            else:
                if piece.type == 'king':
                    real_black_king = self.blackKingLoc
                    self.blackKingLoc = temp_location
                if self.in_check(color, self.blackKingLoc, temp_pieces):
                    removedArr.append(temp_location)
            current_set.remove(temp_location)
            if color == 'white' and piece.type == 'king':
                self.whiteKingLoc = real_white_king
            elif piece.type == 'king' and color == 'black':
                self.blackKingLoc = real_black_king
            #print(piece.name)
            #print(temp_location)
            #print(opponent_set)
            #print(current_set)
        current_set.add(current_location)
        #print(removedArr)
        for location in removedArr:
            moves_list.remove(location)
        return moves_list
    
    def is_mate(self, color):
        print(self.get_all_moves(white_pieces))
        if color == 'white' and len(self.get_all_moves(white_pieces)) == 0:#change to 'if not none instead of if len
            return True
        if color == 'black' and len(self.get_all_moves(black_pieces)) == 0:
            return True
        return False
        """if color == 'white':
            my_list = white_pieces
            current_set = white_set
        else:
            my_list = black_pieces
            current_set = black_set
        for piece in my_list:
            current_location = piece.location
            current_set.remove(current_location)
            for move in self.get_moves(piece, "not my"):#not my turn
                current_set.add(move)
                if not self.in_check(color):
                    return False
                current_set.remove(move)
            current_set.add(current_location)
        return True"""
                
                
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
            if  0 <= y + direction <= 7 and 0 <= x + i <= 7 and (x + i, y + direction) not in self.mySet and ((x + i, y + direction) in self.opponentSet or 
                (self.currentPiece.color == 'w' and (x + i, y + direction) in black_en_passant_pawns) or (self.currentPiece.color == 'b' and (x + i, y + direction) in white_en_passant_pawns)):
                moves.add((x + i, y + direction))
        if self.currentPiece.hasMoved == False and (direction == 1 and (x, 3) not in self.mySet and (x, 3) not in self.opponentSet):
            moves.add((x, 3))
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

    def in_check(self, color, king, pieces = None):
        #print("white king" + str(white_king_location))
        if pieces:
            opponent_list = pieces
        else:
            if color == 'white':
                opponent_list = black_pieces
            else:
                opponent_list = white_pieces
        #if king:
            #my_king_location = king
        #else:
            #if color == 'white':
                #my_king_location = white_king_location
           # else:
                #my_king_location = black_king_location
        return king in self.get_all_moves(opponent_list)
        
        
