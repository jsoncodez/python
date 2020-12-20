"""
File: phone.py
Author: Jason Song
Date: 12/3/2020
Lab Section: 22
Email: jason20@umbc.edu
Description: Phone Class - created phone objects and performs various functions specific to phones.
Reads user generated files consisting of sequence of commands to generate values,
variables and compute arithmetic and display results.
"""


#CAN ADD MORE METHODS IF YOU NEED BUT NEED THE 3 CORES: init, connect, disconnect

class Phone:
    def __init__(self, number, switchboard):
        """
        :param number: the phone number without area code
        :param switchboard: the switchboard to which the number is attached.
        """

        self.number = number
        self.switchboard = switchboard
        self.connected_status = False

    def connect(self, area_code, other_phone_number):
        """
        :param area_code: passed on switchboard with specified area code
        :param other_phone_number: the other phone number without the area code
        :return: True or false - if phone exists in specified switchboards and both phones are currently not connected to another phone.
        """

        for phone in area_code.switchboard_phone_list:

            if phone.number == other_phone_number and phone.connected_status == False and self.connected_status == False:
                phone.connected_status = self
                self.connected_status = phone

                return True

        return False


    def disconnect(self):
        """
        You should also make sure to disconnect the other phone on the other end of the line.
        :return: result output if it's been disconnected or unable to
        """



        print('Hanging up...')

        #check to see if the phone obj linked matches the itself
        if self == self.connected_status.connected_status:
            self.connected_status.connected_status = False
            self.connected_status = False
            return True
        else:
            return False
