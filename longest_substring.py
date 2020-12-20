"""
File: longest_substring.py
Author: Jason Song
Date: 12/8/2020
Lab Section: 22
Email: jason20@umbc.edu
Description:
Takes two strings, uses one to determine the longest length of substring in the other string.
"""

def longest_substring(total_string, find_string):
    """
    determines longest length substring of find_string that's inside total_string
    :param total_string: string to find substring in
    :param find_string: substring comparison
    :return: returns longest running sub string within total_string
    """

    print(len(total_string))
    print(len(find_string))
    total_string += ' '
    longest_sub = 0

    for char in range(len(total_string)):

        sub_slice = total_string[char]
        slice_stop = char

        # counts number of matching characters in the sub string and total string.
        # until condition that next character in sequence does not match.

        while sub_slice in find_string and slice_stop <= (len(total_string)):
            slice_check = slice(char, slice_stop)
            sub_slice = total_string[slice_check]
            slice_stop += 1

        # replaces the current longest substring if greater
        if len(sub_slice[:-1]) > longest_sub:
            longest_sub = len(sub_slice[:-1])

    return longest_sub


if __name__ == '__main__':

    usr_total_str = input('Enter total string: ')
    while usr_total_str != 'quit':
        usr_find_str = input('Enter search sub-string: ')

        print(longest_substring(usr_total_str, usr_find_str))
        usr_total_str = input('Enter total string: ')