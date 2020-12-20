"""
File: knights_move_sum.py
Author: Jason Song
Date: 10/04/2020
Lab Section: 22
Email: jason20@umbc.edu
Description: Creates a 4x4 virtual chessboard with each space containing a randomly generated number and sums the spaces a knight piece could move to.
"""
import sys
from random import seed, randint

# make sure you include this for testing purposes:
if len(sys.argv) >= 2:
    seed(sys.argv[1])

if __name__ == "__main__":

    #creates the matrix - 'chess board'
    the_matrix = []
    for row in range(4):
        new_row = []
        for column in range(4):
            new_row.append(randint(0, 100))
        the_matrix.append(new_row)
        print(new_row)



    usr_row = int(input('What is the row that you want to start at? '))
    usr_column = int(input('What is the column that you want to start at? '))
    sum_moves = 0

    #list of all potential moves the knight can take
    all_move_list = [
        [usr_row + 2, usr_column + 1],
        [usr_row + 2, usr_column - 1],
        [usr_row - 2, usr_column + 1],
        [usr_row - 2, usr_column - 1],
        [usr_row + 1, usr_column + 2],
        [usr_row - 1, usr_column + 2],
        [usr_row + 1, usr_column - 2],
        [usr_row - 1, usr_column - 2]
    ]



    for move in all_move_list:  #iterates through all the potential moves in all_move_list
        if (move[0] >= 0) and (move[0] < len(new_row)) and (move[1] >= 0) and (move[1] < len(the_matrix)):  #only initiates if condition is met that the move is valid (falls within the range of the matrix)

            valid_coord = []
            for coordinate in move: #takes the row and column of the new positon of the night from the move
                valid_coord.append(coordinate)

            sum_moves += the_matrix[valid_coord[0]][valid_coord[1]] #takes the element in the position created by the for loop above and sums value


    print('The sum of the chess moves is', sum_moves)
