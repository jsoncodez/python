"""
File: pickets_problem.py
Author: Jason Song
Date: 12/9/2020
Lab Section: 22
Email: jason20@umbc.edu
Description:
Determines if board of pickets are able to capture any other picket on the board.
If any pickets are mutually attacking pairs, board will return False.
"""

# REMEMBER TO CHANGE CODE TO TAKE PROJECT BOARD TEST NOT MY OWN

PICKET = 'P'
def board():
    board = []
    usr_row = 10
    usr_col = 5
    #for row in range(len(usr_row)):
    for row in range(usr_row):
        row = []
        #for col in range(len(usr_col)):
        for col in range(usr_col):
            row.append('S')
        #print(row)
        board.append(row)

    board[1][2] = PICKET
    #board[3][0] = PICKET
    board[2][0] = PICKET
    board[2][3] = PICKET
    board[3][2] = PICKET

    for row in board:
        print(' '.join(row))
    #print('board', board)

    return board


def pickets_problem(board):
    #list of all moves a picket can make in relation to a 2d grid
    direction_list = [[-1, 1], [1, 1], [1, -1], [-1, -1]]

    print(board[0])
    print(len(board))
    for row in range(len(board)):
        if PICKET in board[row]:
            p_coord = [row, board[row].index(PICKET)]


            for direction in direction_list:

                # creates deep copy of coord to default original coordinate for iteration in other possible directions
                moving_coord = list(p_coord)

                print('direction moving', direction)
                spaces_list = []

                #conditions are limiting iteration (moves) to the boundaries of the board
                # appends the values of all spaces in each diagonal direction.
                while moving_coord[0] < len(board) - 1 and moving_coord[0] > 0 and moving_coord[1] < len(board[row]) - 1 and moving_coord[1] > 0:
                    for move in range(len(direction)):
                        moving_coord[move] += direction[move]
                    spaces_list.append(board[moving_coord[0]][moving_coord[1]])

                    print('spacelist', spaces_list)
                    #checks to see if a picket has attacking pair, removing invalid 1st block space.
                    if PICKET in spaces_list[1:]:
                        return False
                    print('moving_coord after move', moving_coord)

    return True



if __name__ == '__main__':

    #input_rows = int(input('How many rows on the board? '))
    #input_cols = int(input('How many columns on the board? '))

    board = board()

    print(pickets_problem(board))
    #print(pickets_problem(board))
