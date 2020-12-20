"""
File: norgard.py
Author: Jason Song
Date: 11/18/2020
Lab Section: 22
Email: jason20@umbc.edu
Description:
Replicates Norgard's Sequence.  Takes in integer input from the user and computes the sequence.
"""



def norgard(n):
    """

    :param n: user inputted integer
    :return:
    """
    even_odd_check = int(n % 2)
    """
    Checks to see if user's input and through recursion process results in an even or odd number.
    If even (modulus = 0) uses -a_n. 
    If odd (modulus != 0) uses (a_n) + 1
    """

    # BASE CASE - a_0 = 0
    if n == 0:
        return 0

    #RECURSIVE CASE
    else:

        if even_odd_check == 1:
        #condition that number n is odd in the current recursion step

            return (norgard(int(n)/2)+1)

        elif even_odd_check == 0:
        #condition that number n is odd in the current recursion step

            return (-1) * norgard(int(n)/2)



if __name__ == "__main__":
    usr_int_input = int(input('What value do you want to calculate? '))
    print(norgard(usr_int_input))


