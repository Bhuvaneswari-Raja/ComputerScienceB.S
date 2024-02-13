"""
File:    mancala.py
Author:  Avinesh Jangbahadur
Date:    10/29/23
Section: 44
E-mail:  ZL32138@umbc.edu
Description:
This program is a simplified version of the game mancala between two players.
"""

BLOCK_WIDTH = 6
BLOCK_HEIGHT = 5
BLOCK_SEP = "*"
SPACE = ' '
NUM_CUPS = 6
mancala_dict = {0: 0, 1: 4, 2: 4, 3: 4, 4: 4, 5: 4, 6: 4, 7: 0, 8: 4, 9: 4, 10: 4, 11: 4, 12: 4, 13: 4}


def draw_board(top_cups, bottom_cups, mancala_a, mancala_b):
    """
    draw_board is the function that you should call in order to draw the board.
        top_cups and bottom_cups are lists of strings.  Each string should be length BLOCK_WIDTH and each list should be of length BLOCK_HEIGHT.
        mancala_a and mancala_b should be lists of strings.  Each string should be BLOCK_WIDTH in length, and each list should be 2 * BLOCK_HEIGHT + 1

    :param top_cups: This should be a list of strings that represents cups 1 to 6 (Each list should be at least BLOCK_HEIGHT in length, since each string in the list is a line.)
    :param bottom_cups: This should be a list of strings that represents cups 8 to 13 (Each list should be at least BLOCK_HEIGHT in length, since each string in the list is a line.)
    :param mancala_a: This should be a list of 2 * BLOCK_HEIGHT + 1 in length which represents the mancala at position 7.
    :param mancala_b: This should be a list of 2 * BLOCK_HEIGHT + 1 in length which represents the mancala at position 0.
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
        draw_block(board, len(top_cups) - i - 1, 1, bottom_cups[i])

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
    # this function is responsible for obtaining the names of the two players and returning them as an array so that
    # they can be used for output throughout the game
    players = []
    player1 = input("What is the first player's name? ")
    player2 = input("What is the second player's name? ")
    players.append(player1)
    players.append(player2)
    return players


def take_turn(players, turn):
    print_board(players)
    cup = 7
    bad_input = 1
    max_cup = 12
    mancala_cup = 7
    last_top_cup = 5
    max_dict_value = 13
    while bad_input:
        # input validation for the cup selected by the player
        if turn % 2 == 0:
            print(players[0], "what cup do you want to move? ", end="")
        else:
            print(players[1], "what cup do you want to move? ", end="")
        cup = int(input())
        if cup < max_cup and cup >= 0 and cup != mancala_cup:
            bad_input -= 1
            
        else:
            print("invalid cup. try again. ")
    # taking the turn for a pod selected in the upper row of the board
    if cup <= last_top_cup:
        beads = mancala_dict[cup + 1]
    else:
        beads = mancala_dict[cup + 2]
    if cup <= last_top_cup:
        for i in range(beads + 1):

            be = cup + 1 + i
            if be < max_dict_value:
                mancala_dict[be] = (mancala_dict[be] + 1)
            else:
                be = be - max_dict_value
                mancala_dict[be] = (mancala_dict[be] + 1)
            mancala_dict[cup + 1] = 0
    # taking the turn for a pod on the bottom row of the board
    else:
        for i in range(beads):
            be = cup + 3 + i
            if be < max_dict_value:
                mancala_dict[be] = (mancala_dict[be] + 1)
            else:
                if be == max_dict_value:
                    mancala_dict[max_dict_value] = (mancala_dict[max_dict_value] + 1)
                else:
                    be = be - 14
                    mancala_dict[be] = (mancala_dict[be] + 1)
            mancala_dict[cup + 2] = 0

    if (beads + cup + 1) == max_dict_value or (beads + cup + 1) == mancala_cup:
        return 0
    else:
        return 1

    pass


def print_board(players):
    """
    :param players:
    :return: none

    this function is responsible for printing the board throughout the course of the game.
    It produces output reflecting the dictionary "mancala_dict" that keeps track of stone values on the mancala board.
    """
    all_cells = []
    for i in range(12):
        current_cell = []
        current_cell.append(f'Cup {i} ')
        for i in range(BLOCK_HEIGHT - 1):
            current_cell.append(" " * BLOCK_WIDTH)
        current_cell[2] = "Stones"
        all_cells.append(current_cell)

    top_rows = all_cells[0:NUM_CUPS]
    bottom_rows = all_cells[NUM_CUPS:]
    for i in range(1, 7):
        all_cells[i][3] = str(mancala_dict[i + 1])
    for i in range(8, 14):
        all_cells[i - 2][3] = str(mancala_dict[i])

    all_cells[0][3] = str(mancala_dict[1])
    all_cells[11][3] = str(mancala_dict[13])

    first_mancala = []
    second_mancala = []
    for i in range(BLOCK_HEIGHT * 2 + 1):
        first_mancala.append(" " * BLOCK_WIDTH)
        second_mancala.append(" " * BLOCK_WIDTH)
    # section that sets up the output in the mancalas. Displays play names, stones and # of stones
    first_mancala[3] = (players[0])
    second_mancala[3] = (players[1])
    first_mancala[7] = "Stones"
    second_mancala[7] = first_mancala[7]
    first_mancala[8] = str(mancala_dict[0])
    second_mancala[8] = str(mancala_dict[7])
    draw_board(top_rows, bottom_rows, first_mancala, second_mancala)


def run_game():
    turn = 0
    players = get_player()
    while win_condition(players):
        x = take_turn(players, turn)
        if x == 0:
            print("Your last stone landed in a mancala...\nPlease go again")
        turn += x
    pass


def win_condition(players):
    # check if either row is empty
    # total the beads in each mancala
    count_rone = 0
    count_rtwo = 0
    for i in range(1, 7):
        count_rone += mancala_dict[i]
    for i in range(8, 13):
        count_rtwo += mancala_dict[i]
    if count_rone == 0 or count_rtwo == 0:
        # this section of code determines which player is the winner and returns false after in order to stop play
        # (terminates loop in run_game() )
        if mancala_dict[0] > mancala_dict[7]:
            print(players[1], "has won")
        else:
            print(players[1], "has won")
        return False
    else:
        return True


if __name__ == "__main__":
    run_game()
