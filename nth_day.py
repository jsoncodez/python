"""
File: nth_day.py
Author: Jason Song
Date: 12/8/2020
Lab Section: 22
Email: jason20@umbc.edu
Description:
Recursively determines the accrued presents based on the amount of days until Christmas.
"""

def nth_day_of_christmas(day):
    #must be recursive
    """

    :param day: how many days until christmas
    :return: accumulated amount of presents
    """

    print('day', day)
    print('day+1', day + 1)

    #next_day = day+1

    # BASE CASE
    if day == 0:
        return 0

    # RECURSIVE CASE
    else:
        per_day_gifts = int((day * (day + 1)) / 2)
        print('per day gifts', per_day_gifts)

        return per_day_gifts + nth_day_of_christmas(day - 1)



if __name__ == '__main__':

    usr_days = int(input('how many days of christmas is there? '))
    while usr_days != 'quit':
        print(type(usr_days))
        total_gifts = nth_day_of_christmas(usr_days)
        print('total gifts = ', total_gifts)

        usr_days = int(input('how many days of christmas is there? '))