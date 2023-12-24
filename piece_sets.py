from piece import Piece
white_pieces = [Piece('w', 'rook', (0,0)), Piece('w', 'knight', (1,0)), Piece('w', 'bishop', (2,0)), Piece('w', 'king', (3,0)), Piece('w', 'queen', (4,0)), Piece('w', 'bishop', (5,0)), Piece('w', 'knight', (6,0)), Piece('w', 'rook', (7,0)), Piece('w', 'pawn', (0,1)), Piece('w', 'pawn', (1,1)), Piece('w', 'pawn', (2,1)), Piece('w', 'pawn', (3,1)), Piece('w', 'pawn', (4,1)), Piece('w', 'pawn', (5,1)), Piece('w', 'pawn', (6,1)), Piece('w', 'pawn', (7,1))]
black_pieces = [Piece('b', 'rook', (0,7)), Piece('b', 'knight', (1,7)), Piece('b', 'bishop', (2,7)), Piece('b', 'king', (3,7)), Piece('b', 'queen', (4,7)), Piece('b', 'bishop', (5,7)), Piece('b', 'knight', (6,7)), Piece('b', 'rook', (7,7)), Piece('b', 'pawn', (0,6)), Piece('b', 'pawn', (1,6)), Piece('b', 'pawn', (2,6)), Piece('b', 'pawn', (3,6)), Piece('b', 'pawn', (4,6)), Piece('b', 'pawn', (5,6)), Piece('b', 'pawn', (6,6)), Piece('b', 'pawn', (7,6))]
white_locations = [(0,0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0), (0,1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1)]
black_locations = [(0,7), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7), (0,6), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (7, 6)]
white_set = {(0,0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0), (0,1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1)}
black_set = {(0,7), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7), (0,6), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (7, 6)}
captured_pieces_white = set()
captured_pieces_black = set()
white_en_passant_pawns = set()
black_en_passant_pawns = set()
black_king_location = (3, 7)
white_king_location = (3, 0)
"""
for x in range(8):
    all_moves_white.add((x, 2))
    all_moves_white.add((x, 3))
    all_moves_black.add((x, 4))
    all_moves_black.add((x, 5))
"""
