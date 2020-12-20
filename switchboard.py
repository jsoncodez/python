"""
File: switchboard.py
Author: Jason Song
Date: 12/3/2020
Lab Section: 22
Email: jason20@umbc.edu
Description:
Switchboard Class - creates, modify, manages basic functions within a switch.
Connects paths among switch sequences.
"""


from phone import Phone


#CAN ADD MORE METHODS IF NEEDED- STARTER METHODS: add_phone, add_trunk_connection, connect_call,
class Switchboard:
    def __init__(self, area_code):
        """
        :param area_code: the area code to which the switchboard will be associated.
        """

        self.area_code = area_code
        self.trunk_line_list = []
        self.switchboard_phone_list = []

    def add_phone(self, phone_number):
        """
        This function should add a local phone connection by creating a phone object
        and storing it in this class.  How you do that is up to you.

        :param phone_number: phone number without area code
        :return: depends on implementation / None
        """

        self.phone_number = phone_number

        for phone in self.switchboard_phone_list:

            if phone.number == self.phone_number:

                return print('Phone number already exist in switchboard')

        self.switchboard_phone_list.append(Phone(self.phone_number, self))


    def add_trunk_connection(self, switchboard):
        """
        Connect the switchboard (self) to the switchboard (switchboard)

        :param switchboard: should be either the area code or switchboard object to connect.
        :return: success/failure, None, or it's up to you
        """

        #check to see if switchboard is already connected
        if switchboard in self.trunk_line_list:
            print('Switch is already connected')

        else:
            # adds switchboard obj to trunk lines
            switchboard.trunk_line_list.append(self)
            self.trunk_line_list.append(switchboard)


    def connect_call(self, area_code, number, previous_codes):
        """
        :param area_code: the area code to which the destination phone belongs
        :param number: the phone number of the destination phone without area code.
        :param previous_codes: path of switchboards during recursion
        :return: returns a list of the switchboard path to it's final destination.
                returned previous_path list determine if destination has been reached or if it found end of switchboard sequence
        """


        current_switchboard = previous_codes[len(previous_codes) - 1]

        # iterates through available connected switchboards of specified switchboard
        # recurse if hits dead end, checks switchboards unused trunk connections etc etc
        for trunk_switchboard in current_switchboard.trunk_line_list:

            # BASE CASE
            if previous_codes[len(previous_codes) - 1].area_code == area_code:
                return previous_codes

            # RECURSIVE CASE
            if trunk_switchboard not in previous_codes:
                previous_codes.append(trunk_switchboard)
                self.connect_call(area_code, number, previous_codes)

        return previous_codes










