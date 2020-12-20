"""
File: find_diphthongs.py
Author: Jason Song
Date: 10/04/2020
Lab Section: 22
Email: jason20@umbc.edu
Description: Locates "diphthongs" regardless of sound within a string entered by user.  Prints out each instance and number of instances.
"""

if __name__ == "__main__":

    usr_string = input('Enter a string with a lot of diphthongs: ')

    string_list = list(usr_string)
    vowel_list = ['a', 'e', 'i', 'o', 'u', 'y']


    diphthong_count = 0

    for i in range(0, len(string_list)):
        new_start_index = i + diphthong_count   #adds the increment to determine the start the next index after finding a diphthong pair

        if (new_start_index < len(string_list)) and (string_list[new_start_index] in vowel_list): #while iterate, it fits condition that the current index is in vowel list (or is a vowel) and if the start index doesn't go over length of the usr input
            if string_list[new_start_index + 1] in vowel_list:  #determines if the next element is a vowel as well, if so, prints the vowel pair and adds to the counter of diphthongs
                print(string_list[new_start_index] + string_list[new_start_index + 1])
                diphthong_count += 1

    print(diphthong_count)

