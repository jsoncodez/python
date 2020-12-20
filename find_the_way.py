"""
File: find_the_way.py
Author: Jason Song
Date: 11/19/2020
Lab Section: 22
Email: jason20@umbc.edu
Description:
Based on randomly generated 2d grid and start position,
uses recursion to finds a path avoiding specified spaces.
Outputs the path taken with series of numbers and returns True/False if a path was determined to reach the outer limit of the board to 'exit'.
"""
import sys
import random

ALLOWED = '_'
FORBIDDEN = '*'


def create_map(x, y, p):
    """
    :param x: the number of rows of the grid
    :param y: the number of cols of the grid
    :param p: the probability of a forbidden space
    :return: the grid, the starting location
    """
    the_grid = [[FORBIDDEN if random.random() < p else ALLOWED for j in range(y)] for i in range(x)]
    x = random.randint(0, x - 1)
    y = random.randint(0, y - 1)
    the_grid[x][y] = 's'
    return the_grid, [x, y]


def found_end_check(x, y, the_grid):
    """
    :param x: x-coordinate
    :param y: y- coordinate
    :param the_grid: the current grid with path placements
    :return: returns True or False.
    Based on if condition is met that the current position is on the outer limits of the 2d grid to signal exit position.
    """
    x_outer_bounds = len(the_grid) - 1  #determines length of list of lists
    y_outer_bounds = len(the_grid[x]) - 1 #llength of list
    if x == x_outer_bounds or y == y_outer_bounds or x == 0 or y == 0:
        return True
    else:
        return False


def step_counter(the_grid, x, y):
    """
    :param the_grid:
    :param x:  x coordinate
    :param y:   y coordinate
    :return: integer to place on next moved position
    """
    #places '0' to start the number path if the current position is the starting position
    if the_grid[x][y] == 's':
        return 0
    else:
        next_step = the_grid[x][y] + 1
        return next_step #if not starting position, returns back the next step count



def find_the_way_out(the_grid, starting_position):
    """
    :param the_grid: this is a 2d grid, either the positions will be ALLOWED which is a space, or "*" or "s".  s is the starting position passed as a list
        and * is
    :param starting_position:  the starting list/tuple coordinate for the starting position.
    :return: True if there is a way out, False if not

    You need to implement this function
    You are permitted to add helper functions but you shouldn't change the signature (name and parameters) of this function.
    """

    x, y = starting_position    #separates tuple sent through as a parameter
    next_step = step_counter(the_grid, x, y)

    the_grid[x][y] = next_step   #places next step counter in coordinate
    current_position_step = the_grid[x][y]  #stores the current positions step count

    # BASE CASE - IF WE FIND THE END OF THE BOARD

    if found_end_check(x, y, the_grid) == True:
        #helper func to check to see if current position has landed on a exit position and return True for user to know it's found a path
        return True

    # RECURSIVE CASE -> checks for possible moves based on condition the space is ALLOWED

    if x - 1 >= 0 and the_grid[x - 1][y] == ALLOWED:  # MOVE UP

        the_grid[x-1][y] = next_step
        #sets next step counter in new position

        if find_the_way_out(the_grid, (x - 1, y)):
            return True

        the_grid[x - 1][y] = 'b'
        #position is set to 'b' if recursion was to backtrack

    if y - 1 >= 0 and the_grid[x][y - 1] == ALLOWED:  # MOVE LEFT
        the_grid[x][y - 1] = next_step
        if find_the_way_out(the_grid, (x, y - 1)):
            return True

        the_grid[x][y - 1] = 'b'

    if y + 1 < len(the_grid[x]) and the_grid[x][y + 1] == ALLOWED:  # MOVE RIGHT
        the_grid[x][y + 1] = next_step
        if find_the_way_out(the_grid, (x, y + 1)):
            return True

        the_grid[x][y + 1] = 'b'

    if (x + 1 < len(the_grid)) and (the_grid[x + 1][y] == ALLOWED):  # MOVE DOWN
        the_grid[x+1][y] = next_step

        if find_the_way_out(the_grid, (x + 1, y)):
            return True

        the_grid[x + 1][y] = 'b'

    #returns False if none of the above conditions are met signalling recursion had run out of valid moves.
    the_grid[x][y] = 'b'
    return False


def display(the_grid):
    """
        This should display the grid on the screen.
    :param the_grid: the 2d grid.
    """
    print('\n'.join(''.join([str(x).ljust(3) for x in the_grid[i]]) for i in range(len(the_grid))))


if __name__ == '__main__':
    if len(sys.argv) == 5:
        seed = int(sys.argv[1])
        x_dimension = int(sys.argv[2])
        y_dimension = int(sys.argv[3])
        probability = float(sys.argv[4])
    else:

        seed = input('What is the seed (enter a string): ')

        x_dimension = int(input('Enter the x dimension: '))

        y_dimension = int(input('Enter the y dimension: '))

        probability = float(input('Enter a float between 0 and 1 to represent the probability of a forbidden space: '))

    random.seed(seed)

    while input('Again? ').strip().lower() == 'yes':
        the_grid, starting = create_map(x_dimension, y_dimension, probability)
        display(the_grid)
        print(find_the_way_out(the_grid, starting))
        display(the_grid)
