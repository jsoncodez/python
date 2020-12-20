"""
File: apostrophes.py
Author: Jason Song
Date: 11/18/2020
Lab Section: 22
Email: jason20@umbc.edu
Description:
Adds apostrophes in appropriate places to a given string via recursion.
"""

def apost(string_list, index_count):
    """
    :param string_list: takes list version of string inputted by user
    :param index_count: counter to determine base case and index position within list
    :return: Base case returns amended string with apostrophes added.
    Recursive part returns individual words and checks specified conditions to add or forgo adding apostrophes.
    """

    # BASE CASE
    if index_count == len(string_list):
        #converts final amended list of words back into string
        string_sentence = ' '.join(string_list)
        return string_sentence

    #RECURSIVE CASE
    else:

        #condition to forgo adding an apostrophy in the case where word is not alphanumeric or word does not end in an 's'
        if string_list[index_count].isalnum() == False or string_list[index_count][-1] != 's' and string_list[index_count][-1] != 's'.upper():
            return apost(string_list, index_count + 1)

        #condition left over are words that are alphanumeric and end in 's'.
        else:
            #Isolates word by the string in specific index count,
            #takes first character in the word to 2nd last letter(removing the 's') and concatenates the "'s".
            #Replaces modified word into same index
            if string_list[index_count][-1].islower():
                string_list[index_count] = string_list[index_count][0:len(string_list[index_count])-1] + "'s"
            else:
                string_list[index_count] = string_list[index_count][0:len(string_list[index_count])-1] + "'s".upper()

            return apost(string_list, index_count + 1)


if __name__ == "__main__":
    usr_input = str(input('Input a string: '))
    #converts user string to list format for recursion purposes and isolating individual word segments
    string_list = list(usr_input.split(" "))
    print(apost(string_list, 0))
