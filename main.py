import pygame
from piece import Piece
from piece_sets import white_set, black_set, captured_pieces_black, captured_pieces_white, white_pieces, black_pieces, white_locations, black_locations, white_king_location, black_king_location, white_en_passant_pawns, black_en_passant_pawns
from moves import Moves
#author of piece images: By en:User:Cburnett - File:Chess kdt45.svg, CC BY-SA 3.0, https://commons.wikimedia.org/w/index.php?curid=20363778

pygame.init()
WIDTH = 800
HEIGHT = 900
screen = pygame.display.set_mode([WIDTH, HEIGHT])
font = pygame.font.Font('freesansbold.ttf', 20)
big_font = pygame.font.Font('freesansbold.ttf', 50)
timer = pygame.time.Clock()
fps = 60
moves = Moves()
en_passant_piece = False
is_pawn = False

#game variables and images

turn_step = 0 #moves between 0 - 3 based off of turns
selection = 100 #index of selected piece
valid_moves = []
#load in game piece images
black_queen = pygame.image.load('images/black_queen.png')
black_queen = pygame.transform.scale(black_queen, (80, 80))
black_queen_small = pygame.transform.scale(black_queen, (40, 40))
white_queen = pygame.image.load('images/white_queen.png')
white_queen = pygame.transform.scale(white_queen, (80, 80))
white_queen_small = pygame.transform.scale(white_queen, (40, 40))
black_king = pygame.image.load('images/black_king.png')
black_king = pygame.transform.scale(black_king, (80, 80))
black_king_small = pygame.transform.scale(black_king, (40, 40))
white_king = pygame.image.load('images/white_king.png')
white_king = pygame.transform.scale(white_king, (80, 80))
white_king_small = pygame.transform.scale(white_king, (40, 40))
black_bishop = pygame.image.load('images/black_bishop.png')
black_bishop = pygame.transform.scale(black_bishop, (80, 80))
black_bishop_small = pygame.transform.scale(black_bishop, (40, 40))
white_bishop = pygame.image.load('images/white_bishop.png')
white_bishop = pygame.transform.scale(white_bishop, (80, 80))
white_bishop_small = pygame.transform.scale(white_bishop, (40, 40))
black_knight = pygame.image.load('images/black_knight.png')
black_knight = pygame.transform.scale(black_knight, (80, 80))
black_knight_small = pygame.transform.scale(black_knight, (40, 40))
white_knight = pygame.image.load('images/white_knight.png')
white_knight = pygame.transform.scale(white_knight, (80, 80))
white_knight_small = pygame.transform.scale(white_knight, (40, 40))
black_rook = pygame.image.load('images/black_rook.png')
black_rook = pygame.transform.scale(black_rook, (80, 80))
black_rook_small = pygame.transform.scale(black_rook, (40, 40))
white_rook = pygame.image.load('images/white_rook.png')
white_rook = pygame.transform.scale(white_rook, (80, 80))
white_rook_small = pygame.transform.scale(white_rook, (40, 40))
black_pawn = pygame.image.load('images/black_pawn.png')
black_pawn = pygame.transform.scale(black_pawn, (80, 80))
black_pawn_small = pygame.transform.scale(black_pawn, (40, 40))
white_pawn = pygame.image.load('images/white_pawn.png')
white_pawn = pygame.transform.scale(white_pawn, (80, 80))
white_pawn_small = pygame.transform.scale(white_pawn, (40, 40))

white_images = [white_rook, white_knight, white_bishop, white_king, white_queen, white_pawn]
small_white_images = [white_rook_small, white_knight_small, white_bishop_small, white_king_small, white_queen_small, white_pawn_small]
black_images = [black_rook, black_knight, black_bishop, black_king, black_queen, black_pawn]
small_black_images = [black_rook_small, black_knight_small, black_bishop_small, black_king_small, black_queen_small, black_pawn_small]

#draw game board
def draw_board():
    for i in range(32):
        column = i % 4
        row = i // 4
        if row % 2 == 0:
            pygame.draw.rect(screen, 'light grey', [600 - (column * 200), row * 100, 100, 100])
        else:
            pygame.draw.rect(screen, 'light grey', [700 - (column * 200), row * 100, 100, 100])
    pygame.draw.rect(screen, 'dimgrey', [0, 800, 800, 100])
    status_text = ['White: select a piece to move', 'White: select a destination', 'Black: select a piece to move', 'Black: select a destination']
    screen.blit(big_font.render(status_text[turn_step], True, 'black'), (20, 820))

def draw_pieces():
    if moves.in_check('white', white_king_location):
        pygame.draw.rect(screen, 'red', [white_king_location[0] * 100, white_king_location[1] * 100, 100, 100])
    if moves.in_check('black', black_king_location):
        pygame.draw.rect(screen, 'red', [black_king_location[0] * 100, black_king_location[1] * 100, 100, 100])
    for i in range(len(white_pieces)):
        if selection == i and turn_step < 2:
            pygame.draw.rect(screen, 'light blue', [white_locations[i][0] * 100, white_locations[i][1] * 100, 100, 100])
        index = piece_list.index(white_pieces[i].type)
        screen.blit(white_images[index], (white_locations[i][0] * 100 + 10, white_locations[i][1] * 100 + 10))
    for i in range(len(black_pieces)):
        if selection == i and turn_step > 1:
            pygame.draw.rect(screen, 'light blue', [black_locations[i][0] * 100, black_locations[i][1] * 100, 100, 100])
        index = piece_list.index(black_pieces[i].type)
        screen.blit(black_images[index], (black_locations[i][0] * 100 + 10, black_locations[i][1] * 100 + 10)) 
piece_list = ['rook', 'knight', 'bishop', 'king', 'queen', 'pawn']

#main game loop
run = True
while run:
    timer.tick(fps)
    screen.fill('grey')
    draw_board()
    draw_pieces()

    def piece_is_pawn(self, piece):
        if piece.type == 'pawn':
            return True
        return False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            x_coord = pygame.mouse.get_pos()[0]
            y_coord = pygame.mouse.get_pos()[1]
            selected_cell = (x_coord // 100, y_coord // 100)
            if turn_step <= 1:
                if selected_cell in white_locations:
                    selection = white_locations.index(selected_cell)
                    valid_moves = moves.get_moves(white_pieces[selection])
                    selected_piece_cell = selected_cell
                    if turn_step == 0:
                        turn_step = 1
                    if piece_is_pawn:
                        is_pawn = True
                        if (white_locations[selection][0], white_locations[selection][1] - 1) in white_en_passant_pawns:
                            en_passant_piece = (white_locations[selection][0], white_locations[selection][1] - 1)
                        else:
                            en_passant_piece = False
                    else:
                        en_passant_piece = False
                        is_pawn = False
                if selected_cell in valid_moves and selection != 100:
                    white_locations[selection] = selected_cell
                    white_pieces[selection].location = selected_cell
                    if white_pieces[selection].hasMoved == False:
                        white_pieces[selection].firstMove = True
                    else:
                        white_pieces[selection].firstMove = False
                    white_pieces[selection].hasMoved = True
                    white_set.add(selected_cell)
                    white_set.remove(selected_piece_cell)
                    selected_piece_cell = None
                    if en_passant_piece:
                        white_en_passant_pawns.remove(en_passant_piece)
                    #if white_pieces[selection].type == 'pawn' and (white_locations[selection][0], white_locations[selection][1] - 2) in en_passant_pawns and white_locations[selection][1] == 4:
                     #   print("does it")
                      #  en_passant_pawns.remove((white_locations[selection][0], white_locations[selection][1] - 2))
                    if white_pieces[selection].type == 'pawn' and white_locations[selection][1] == 3 and white_pieces[selection].firstMove:
                        white_en_passant_pawns.add((white_locations[selection][0], 2))
                    if white_pieces[selection].type == 'king':
                        white_king_location = white_locations[selection]
                    if selected_cell in black_locations:
                        removed_index = black_locations.index(selected_cell)
                        captured_pieces_black.add(black_pieces[removed_index])
                        black_set.remove(black_locations.pop(removed_index))
                        black_pieces.pop(removed_index)
                    if selected_cell in black_en_passant_pawns and selected_cell[1] == 5 and is_pawn:
                        removed_index = black_locations.index((selected_cell[0], selected_cell[1] - 1))
                        captured_pieces_black.add(black_pieces[removed_index])
                        black_set.remove(black_locations.pop(removed_index))
                        black_pieces.pop(removed_index)
                        black_en_passant_pawns.remove(selected_cell)
                    #black_options = check_options(black_pieces, black_locations, 'black')
                    #white_options = check_options(white_pieces, white_locations, 'white')
                    #white_pieces[selection].hasMoved = True
                    turn_step = 2
                    selection = 100
                    valid_moves = []
                    if moves.is_mate('black'):
                        if moves.in_check('black', black_king_location):
                            print("white wins")
                        else:
                            print('stalemate')
            if turn_step > 1:
                if selected_cell in black_locations:
                    selection = black_locations.index(selected_cell)
                    valid_moves = moves.get_moves(black_pieces[selection]) 
                    """need to edit valid moves to see if king is in check after making the move (check if each move puts the king in check)"""
                    selected_piece_cell = selected_cell
                    if turn_step == 2:
                        turn_step = 3
                    if piece_is_pawn:
                        is_pawn = True
                        if (black_locations[selection][0], black_locations[selection][1] + 1) in black_en_passant_pawns:
                            en_passant_piece = (black_locations[selection][0], black_locations[selection][1] + 1)
                        else:
                            en_passant_piece = False
                    else:
                        en_passant_piece = False
                        is_pawn = False
                if selected_cell in valid_moves and selection != 100:
                    black_locations[selection] = selected_cell
                    black_pieces[selection].location = selected_cell
                    if black_pieces[selection].hasMoved == False:
                        black_pieces[selection].firstMove = True
                    else:
                        black_pieces[selection].firstMove = False
                    black_pieces[selection].hasMoved = True
                    black_set.add(selected_cell)
                    black_set.remove(selected_piece_cell)
                    selected_piece_cell = None
                    if en_passant_piece:
                        black_en_passant_pawns.remove(en_passant_piece)
                    #if black_pieces[selection].type == 'pawn' and (black_locations[selection][0], black_locations[selection][1] + 2) in en_passant_pawns and black_locations[selection][1] == 3:
                    #    en_passant_pawns.remove((black_locations[selection][0], black_locations[selection][1] + 2))
                    if black_pieces[selection].type == 'pawn' and black_locations[selection][1] == 4 and black_pieces[selection].firstMove:
                        black_en_passant_pawns.add((black_locations[selection][0], 5))
                    if black_pieces[selection].type == 'king':
                        black_king_location = black_locations[selection]
                    if selected_cell in white_locations:
                        removed_index = white_locations.index(selected_cell)
                        captured_pieces_white.add(white_pieces[removed_index])
                        white_set.remove(white_locations.pop(removed_index))
                        white_pieces.pop(removed_index)
                    if selected_cell in white_en_passant_pawns and selected_cell[1] == 2 and is_pawn:
                        removed_index = white_locations.index((selected_cell[0], selected_cell[1] + 1))
                        captured_pieces_white.add(white_pieces[removed_index])
                        white_set.remove(white_locations.pop(removed_index))
                        white_pieces.pop(removed_index)
                        white_en_passant_pawns.remove(selected_cell)
                    #print('white check: ' + str(moves.in_check('white')))
                    #print('black check: ' + str(moves.in_check('black')))
                    #white_options = check_options(white_pieces, white_locations, 'white')
                    #black_options = check_options(black_pieces, black_locations, 'black')
                    turn_step = 0
                    selection = 100
                    valid_moves = []
                    if moves.is_mate('white'):
                        if moves.in_check('white', white_king_location):
                            print("black wins")
                        else:
                            print('stalemate')
                    else:
                        print('noooo')
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
            x_coord = pygame.mouse.get_pos()[0]
            y_coord = pygame.mouse.get_pos()[1]
            print('white enpassant' + str(white_en_passant_pawns))
            print('black enpassant' + str(black_en_passant_pawns))
            temp_selected_cell = (x_coord // 100, y_coord // 100)
            if temp_selected_cell in white_locations or temp_selected_cell in black_locations:
                if temp_selected_cell in white_locations:
                    current_piece_list = white_pieces
                    selection = white_locations.index(temp_selected_cell)
                else:
                    current_piece_list = black_pieces
                    selection = black_locations.index(temp_selected_cell)

                temp_valid_moves = moves.get_moves(current_piece_list[selection])
                print(temp_valid_moves) # dont delete
    pygame.display.flip()
pygame.quit()
