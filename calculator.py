"""
File: calculator.py
Author: Jason Song
Date: 11/19/2020
Lab Section: 22
Email: jason20@umbc.edu
Description:
Reads user generated files consisting of sequence of commands to generate values,
variables and compute arithmetic and display results.
"""

def calculate(cmd, cmd_split):
    """
    :param cmd: Two arithmetic commands. add/mul
    :param cmd_split: Individual commands.
    :return: None if invalid variable or result of addition/multiplication
    """

    #initializes return
    compute = 0

    if cmd == 'add':

        #iterates through list of value and variables in list after command to calculate addition or multiplication.
        for value in range(1, len(cmd_split) - 1):
            if cmd_split[value].isnumeric() == True:
                #if value is specified integer
                compute += int(cmd_split[value])

            elif cmd_split[value] in variable:
                #if variable, draws data from dictionary of key = variables and associated values
                compute += variable[cmd_split[value]]

            else:
                #error for invalid inputs, values, variables
                print('{} is invalid'.format(cmd_split[value]))
                return None

        return compute

    elif cmd == 'mul':
        compute += 1

        for value in range(1, len(cmd_split) - 1):
            if cmd_split[value].isnumeric() == True:
                compute *= int(cmd_split[value])
            elif cmd_split[value] in variable:
                compute *= variable[cmd_split[value]]
            else:
                print('{} is invalid'.format(cmd_split[value]))
                return None
        return compute


if __name__ == "__main__":
    usr_cmd_file = str(input('What file of commands do you want to open?'))
    #usr_cmd_file = 'calc_cmds'

    # creates new dictionary, key:value pairs of created variables and it corresponding values
    variable = {}

    #opens reads user inputted file name and returns all lines in list format
    with open(usr_cmd_file, 'r') as cmd_file:
        read_list = cmd_file.readlines()


    #modifies each line to remove any string formatting and create individual list for each command
    for line in range(len(read_list)):
        cmd_split = str(read_list[line]).strip('\n').split(' ')
        cmd = cmd_split[0]  #checks first element in list to check the user command.

        #based on command initiated, below are actions for each potential command.
        if cmd == 'create':
            variable[cmd_split[1]] = int(cmd_split[2])
        elif cmd == 'display' and cmd_split[1] == 'all':
            for key, value in variable.items():
                print(key, value)
        elif cmd == 'display':
            print(cmd_split[1], variable[cmd_split[1]])
        else:
            compute = calculate(cmd, cmd_split)
            if compute != None:
                variable[cmd_split[3]] = compute


