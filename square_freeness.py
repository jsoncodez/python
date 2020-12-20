"""
File: square_freeness.py
Author: Jason Song
Date: 10/04/2020
Lab Section: 22
Email: jason20@umbc.edu
Description: Takes number from user and determines if number is square free or outputs lowest square.
"""

if __name__ == "__main__":

    usr_input = int(input('Tell me a number x: '))
    divisible = []

    #checks if usr_input is a positive number
    if usr_input <= 0:
        print('You cannot calculate the square freeness of {}'.format(usr_input))

    else:
        #iterates through num to check if n ** 2 returns a remainder of 0 indicating if a input has a square
        for num in range(2, usr_input):
            if usr_input % (num ** 2) == 0:
                divisible.append(num)

        #checks if number returned back a divisible of squares, if so: then it will outputs lowest square, if not: then it is square free
        if len(divisible) > 0:
            print('{} is not square free {} squared divides it'.format(usr_input, divisible[0]))
        else:
            print('{} is square free'.format(usr_input))





