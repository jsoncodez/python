"""
File: lucky_base.py
Author: Jason Song
Date: 12/8/2020
Lab Section: 22
Email: jason20@umbc.edu
Description:
Converts user inputted number to base 7.
"""

def max_base_place(number):
    """

    :param number:
    :return:

        Helper function to determine the starting largest max base 7 case.
    """

    max_base = 1
    exponent = 0
    while max_base * 7 <= number and number > 0:
        exponent += 1
        max_base = 7 ** exponent

    return max_base

def lucky_base(number, max_base, base_string = ''):
    """

    :param number: number to convert to base of 7
    :param max_base: determines next base of 7's place
    :param base_string: concatenates result of each unit placeholder when applying base 7 for final string output
    :return: string formatted of number in base 7
    """

    print('max base', max_base)
    print('start of func base_string', base_string)

    base_int = int(number / max_base)
    print('base_int', base_int)

    remainder = number % max_base
    print('remainder', remainder)

    # BASE CASE
    if max_base == 1:
        base_string += str(base_int)

        return base_string

    # RECURSIVE CASE
    else:
        base_string += str(base_int)
        return lucky_base(remainder, max_base / 7, base_string)


if __name__ == '__main__':


    usr_integer = int(input('Enter number to convert to base 7: '))

    while usr_integer != 'quit':

        base_seven = lucky_base(usr_integer, max_base_place(usr_integer))

        print('This is base seven of {}: {}'.format(usr_integer, base_seven))
        usr_integer = int(input('What base 7 number would you like to convert?'))


