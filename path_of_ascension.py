"""
File: path_of_ascension.py
Author: Jason Song
Date: 10/04/2020
Lab Section: 22
Email: jason20@umbc.edu
Description: Obtains number of variables in a sequence of randomly generated numbers from 0, 100.  Prints and iterates through sequence determing the longest ascending subsequence and outputting result.
"""

import sys
from random import seed, randint

# make sure you include this for testing purposes:

if len(sys.argv) >= 2:
   seed(sys.argv[1])


if __name__ == "__main__":

    usr_length_input = int(input('What length of sequence do you want to input? '))

    ascension_list = []
    counter = 0
    stored_counter = 0
    prior_num = 0

    for i in range(usr_length_input):
        ascension_list.append(randint(0, 100))



    if usr_length_input > 0 and usr_length_input <= 1000:   #makes sure user input is between 0 and 1000 inclusively
        print(ascension_list)

        for num in range(0, len(ascension_list)):   #irerates from 0 to length of user list not inclusive at the end.
            if ascension_list[num] > prior_num:     #checks to see if the integer is greater than the prior index integer
                counter += 1
                if stored_counter < counter:    #if condition above is met, it will also check to see if current count is greater and replaces, otherwise does not do anything to maximum counter
                    stored_counter = counter

            elif ascension_list[num] <= prior_num:  #condition if current element integer is less than, acts as reset for the counter to restart a new ascending subsequence
                if stored_counter < counter:

                    stored_counter = counter

                counter = 1
            prior_num = ascension_list[num]

        print('The max ascending length is {}'.format(stored_counter))

    else:
        print('Please select number between 0 and 1000')











