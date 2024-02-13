"""
File: mancala.py
Author: Pooja Rajamanikandan
Date: 10/24/2023
Section: 54
E-mail: le64534@umbc.edu
Description: This program implements a game of Mancala
"""

BLOCK_WIDTH = 6
BLOCK_HEIGHT = 5
BLOCK_SEP = "*"
SPACE = ' '


def draw_board(top_cups, bottom_cups, mancala_a, mancala_b):
    """
    draw_board is the function that you should call in order to draw the board.
    top_cups and bottom_cups are lists of strings.  Each string should be length BLOCK_WIDTH and each list should be of length BLOCK_HEIGHT.
    mancala_a and mancala_b should be 2d lists of strings.  Each string should be BLOCK_WIDTH in length, 
        and each list should be 2 * BLOCK_HEIGHT + 1

        :param top_cups: This should be a list of strings that represents cups 1 to 6 (Each list should be at 
            least BLOCK_HEIGHT in length, since each string in the list is a line.)
        :param bottom_cups: This should be a list of strings that represents cups 8 to 13 (Each list should be at 
            least BLOCK_HEIGHT in length, since each string in the list is a line.)
        :param mancala_a: This should be a list of 2 * BLOCK_HEIGHT + 1 in length which represents the 
            mancala at position 7.
        :param mancala_b: This should be a list of 2 * BLOCK_HEIGHT + 1 in length which represents the 
            mancala at position 0.
    """
    board = [[SPACE for _ in range((BLOCK_WIDTH + 1) * (len(top_cups) + 2) + 1)] for _ in range(BLOCK_HEIGHT * 2 + 3)]
    for p in range(len(board)):
        board[p][0] = BLOCK_SEP
        board[p][len(board[0]) - 1] = BLOCK_SEP

    for q in range(len(board[0])):
        board[0][q] = BLOCK_SEP
        board[len(board) - 1][q] = BLOCK_SEP

    # draw midline
    for p in range(BLOCK_WIDTH + 1, (BLOCK_WIDTH + 1) * (len(top_cups) + 1) + 1):
        board[BLOCK_HEIGHT + 1][p] = BLOCK_SEP

    for i in range(len(top_cups)):
        for p in range(len(board)):
            board[p][(1 + i) * (1 + BLOCK_WIDTH)] = BLOCK_SEP

    for p in range(len(board)):
        board[p][1 + BLOCK_WIDTH] = BLOCK_SEP
        board[p][len(board[0]) - BLOCK_WIDTH - 2] = BLOCK_SEP

    for i in range(len(top_cups)):
        draw_block(board, i, 0, top_cups[i])
        draw_block(board, i, 1, bottom_cups[i])

    draw_mancala(0, mancala_a, board)
    draw_mancala(1, mancala_b, board)
    
    print('\n'.join([''.join(board[i]) for i in range(len(board))]))


def draw_mancala(fore_or_aft, mancala_data, the_board):
    """
    Draw_mancala is a helper function for the draw_board function.
        :param fore_or_aft: front or back (0, or 1)
        :param mancala_data: a list of strings of length 2 * BLOCK_HEIGHT + 1 each string of length BLOCK_WIDTH
        :param the_board: a 2d-list of characters which we are creating to print the board.
    """
    if fore_or_aft == 0:
        for i in range(len(mancala_data)):
            data = mancala_data[i][0: BLOCK_WIDTH].rjust(BLOCK_WIDTH)
            for j in range(len(mancala_data[0])):
                the_board[1 + i][1 + j] = data[j]
    else:
        for i in range(len(mancala_data)):
            data = mancala_data[i][0: BLOCK_WIDTH].rjust(BLOCK_WIDTH)
            for j in range(len(mancala_data[0])):
                the_board[1 + i][len(the_board[0]) - BLOCK_WIDTH - 1 + j] = data[j]


def draw_block(the_board, pos_x, pos_y, block_data):
    """
    Draw block is a helper function for the draw_board function.
        :param the_board: the board is the 2d grid of characters we're filling in
        :param pos_x: which cup it is
        :param pos_y: upper or lower
        :param block_data: the list of strings to put into the block.
    """
    for i in range(BLOCK_HEIGHT):
        data = block_data[i][0:BLOCK_WIDTH].rjust(BLOCK_WIDTH)
        for j in range(BLOCK_WIDTH):
            the_board[1 + pos_y * (BLOCK_HEIGHT + 1) + i][1 + (pos_x + 1) * (BLOCK_WIDTH + 1) + j] = data[j]

def get_player():
    player_1_name = input("Player 1 please tell me your name: ")
    player_2_name = input("Player 2 please tell me your name: ")
    players = (player_1_name, player_2_name)
    
    return players


def take_turn(player, cups):
    coin = 1
    
def move_stones(cup):
    cup_values = {0:0, 1:5,2:5,3:5,4:5,5:5,6:5,7:0,8:5,9:5,10:5,11:5,12:5,13:5}

    if cup in cup_values:
        while cup_values[cup] > 0:
            cup_values[cup + 1] += 1
            cup -= 1


def run_game():
    list_of_players = get_player()
    player_1 = list_of_players[0]
    player_2 = list_of_players[1]

    x = "Cup".ljust(BLOCK_WIDTH)
    top_rows = [
        [x, "1", "Stones", str(5), SPACE],
        [x, "2", "Stones", str(5), SPACE],
        [x, "3", "Stones", str(5), SPACE],
        [x, "4", "Stones", str(5), SPACE],
        [x, "5", "Stones", str(5), SPACE],
        [x, "6", "Stones", str(5), SPACE]
    ]

    bottom_rows = [
        [x, "7", "Stones", str(5), SPACE],
        [x, "8", "Stones", str(5), SPACE],
        [x, "9", "Stones", str(5), SPACE],
        [x, "10", "Stones", str(5), SPACE],
        [x, "11", "Stones", str(5), SPACE],
        [x, "12", "Stones", str(5), SPACE]

    ]

    empty_space = SPACE.ljust(BLOCK_WIDTH)
    first_mancala = [empty_space,empty_space, empty_space,player_2.ljust(BLOCK_WIDTH), empty_space, empty_space, "Stones".ljust(BLOCK_WIDTH), str(0).ljust(BLOCK_WIDTH), empty_space,empty_space,empty_space,empty_space]
    second_mancala = [empty_space,empty_space, empty_space,player_1.ljust(BLOCK_WIDTH), empty_space, empty_space, "Stones".ljust(BLOCK_WIDTH), str(0).ljust(BLOCK_WIDTH), empty_space,empty_space,empty_space,empty_space]
    
    draw_board(top_rows,bottom_rows,first_mancala,second_mancala)

    while winner != True:


if __name__ == "__main__":
    run_game()