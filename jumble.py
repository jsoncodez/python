"""
File: jumble.py
Author: Jason Song
Date: 12/8/2020
Lab Section: 22
Email: jason20@umbc.edu
Description:
Jumbles a string and based on equation ax+b mod L (L = len(a_string)), equation determines indices for which characters
form the new jumbled string.  Indices can't repeat.
"""

def jumble(a_string, a, b):
    """

    :param a_string: user input string
    :param a: user inputted integer
    :param b: user inputted integer
    :return: the jumbled string
    """

    #split to make into list
    split_list = []
    for letter in a_string:
        split_list.append(letter)

    # ax + b mod L
    #   L = len(a_string) = string_len
    str_len = len(usr_string)

    # holds indexes already used
    used_index_list = []
    jumbled_string = ''

    for char_index in range(len(a_string) + 1):
        # calculates next index and checks to see if index has been used
        jumble_index = ((a * char_index) + (b % str_len)) % str_len
        if jumble_index not in used_index_list:
            used_index_list.append(jumble_index)
            jumbled_string += a_string[jumble_index]

    return jumbled_string


if __name__ == '__main__':
    usr_string = input('What string do you want to jumble? ')
    while usr_string != 'quit':
        usr_a = int(input('What is integer a? '))
        usr_b = int(input('What is integer b? '))

        print('jumbled string is: ', jumble(usr_string, usr_a, usr_b))
        usr_string = input('What string do you want to jumble? ')

