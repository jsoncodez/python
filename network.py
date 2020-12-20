"""
File: network.py
Author: Jason Song
Date: 12/3/2020
Lab Section: 22
Email: jason20@umbc.edu
Description:
Network Class - container for switchboard objects and manages functions that bridges the classes attributes and methods.
Able to save/load container for later use.
"""

from phone import Phone
from switchboard import Switchboard
import json



HYPHEN = "-"
QUIT = 'quit'
SWITCH_CONNECT = 'switch-connect'
SWITCH_ADD = 'switch-add'
PHONE_ADD = 'phone-add'
NETWORK_SAVE = 'network-save'
NETWORK_LOAD = 'network-load'
START_CALL = 'start-call'
END_CALL = 'end-call'
DISPLAY = 'display'


class Network:
    def __init__(self):
        """
            Construct a network by creating the switchboard container object

            You are free to create any additional data/members necessary to maintain this class.
        """

        self.network_switchboard_list = []

    def load_network(self, filename):
        """
        :param filename: the name of the file to be loaded.  Assume it exists and is in the right format.
                If not, it's ok if your program fails.
        :return: success?
        """

        self.filename = filename

        # stores list of switches that have loaded and available to be connected
        completed_load_switches = []
        with open(self.filename) as load_network_file:

            for switch in load_network_file:
                switch_profile = json.loads(switch)

                # recreates switchboard using add_switchboard method
                self.add_switchboard(switch_profile['area_code'])

                # recreates phone numbers in switchboard
                for phone_num in switch_profile["switch_phones"]:
                    self.create_phone(phone_num, switch_profile['area_code'])

                completed_load_switches.append(switch_profile["area_code"])

                #runs to see if current switch can connect to any of its trunk connections
                for trunk_switch in switch_profile["trunk_connects"]:
                    if trunk_switch in completed_load_switches:
                        self.connect_switchboards(switch_profile["area_code"], trunk_switch)

        print('loading of switches and phones complete')


    def save_network(self, filename):
        """
        :param filename: the name of your file to save the network.  Remember that you need to save all the
            connections, but not the active phone calls (they can be forgotten between save and load).
            You must invent the format of the file, but if you wish you can use either json or csv libraries.
        :return: success?
        """
        self.filename = filename

        with open(self.filename, 'w') as save_network_file:

            # creating json objects for creating of json file,
            # iterating through switches within network and associated data to recreate network
            for switch in self.network_switchboard_list:
                switch_profile = {}
                switch_profile['area_code'] = switch.area_code

                switch_phone_list = []
                for phone in switch.switchboard_phone_list:
                    switch_phone_list.append(phone.number)
                switch_profile['switch_phones'] = switch_phone_list

                switch_trunk_list = []
                for trunk in switch.trunk_line_list:
                    switch_trunk_list.append(trunk.area_code)
                switch_profile['trunk_connects'] = switch_trunk_list

                save_network_file.write(json.dumps(switch_profile) + '\n')


    def add_switchboard(self, area_code):
        """
        add switchboard should create a switchboard and add it to your network.

        By default it is not connected to any other boards and has no phone lines attached.
        :param area_code: the area code for the new switchboard
        :return: switchboard exist/new unique switchboard obj in current network
        """

        #check to see if switchboard already exists
        for switch in self.network_switchboard_list:
            if switch.area_code == area_code:
                return print('Switchboard area code already exists')

        #creates switchboard obj and appends to list of switchboard objects in the network
        self.network_switchboard_list.append(Switchboard(area_code))


    def create_phone(self, phone_number, area_code):
        """
        :param phone_number: new phone number
        :param area_code: area code of the desired switchboard
        :return: results in add_phone of switchboard with area_code or Failure if area_code does not exist
        """

        for switch in self.network_switchboard_list:
            if switch.area_code == area_code:
                return switch.add_phone(phone_number)
        return print('Area code does not exist')


    def connect_switchboards(self, area_1, area_2):
        """
            Connect switchboards should connect the two switchboards (creates a trunk line between them)
            so that long distance calls can be made.

        :param area_1: area-code 1
        :param area_2: area-code 2
        :return: results in connection of switchboards or False
        """

        switch1 = None
        switch2 = None

        # checks to see if user inputted valid area codes, cross referencing the network
        # stores variables and used under the condition that both area codes exist
        for switchboard in self.network_switchboard_list:
            if area_2 != area_1:
                if switchboard.area_code == area_1:
                    switch1 = switchboard

                elif switchboard.area_code == area_2:
                    switch2 = switchboard

        #validates source area code and dest area code, prior to entering into attempt to connect
        if switch1 == None or switch2 == None:
            print('Invalid area_code(s)')
            return False
        else:
            return switch1.add_trunk_connection(switch2)


    def start_end_call(self, src_area_code, src_number, dest_area_code, dest_number, cmd):
        """
        :param src_area_code: phone's area code that initialized the call
        :param src_number: phone's number that initialized the call
        :param dest_area_code: destination's area code
        :param dest_number: destination's phone number
        :param cmd: takes in user inputted command sharing the process to validate user input and parse necessary data to start or end calls
        :return: returns False if failed to validate the person who initiated the call area code and phone number
            if it passes conditions, function is run and ouput of either connecting/disconnecting/failed
        """

        for switch in self.network_switchboard_list:

            # checks if the src phone number requesting connection is a valid phone number
            if switch.area_code == src_area_code:
                for phone in switch.switchboard_phone_list:
                    if phone.number == src_number:

                        #validation and parsed data used to initiate user command start/end call
                        if cmd == START_CALL:
                            switch_path = switch.connect_call(dest_area_code, dest_number, previous_codes = [switch])

                            # recursion path list returned from connect_call,
                            # if succesful connection to dest area code, last element of path would be the destion switchboard
                            dest_switch = switch_path[-1]
                            if dest_switch.area_code == dest_area_code:

                                # if destination switchboard has been reached, next attempt to connect between phones
                                return phone.connect(dest_switch, dest_number)

                        elif cmd == END_CALL:
                            print('enter endcall')
                            return phone.disconnect()

                return False
        return False


    def display(self):

        for switchboard in self.network_switchboard_list:

            print('Switchboard with area code:', switchboard.area_code)

            print('\tTrunk lines are:')
            for trunk_line in switchboard.trunk_line_list:
                print('\t\tTrunk line connection to:', trunk_line.area_code)

            print('\tLocal phone numbers are:')
            #print('phone numbers list', switchboard.switchboard_phone_list)
            for phone in switchboard.switchboard_phone_list:
                if phone.connected_status == False:
                    print('\t\tPhone with number: {} is not in use'.format(phone.number))
                else:
                    print('\t\tPhone with number: {} is connected to {}-{}'.format(phone.number, phone.connected_status.switchboard.area_code, phone.connected_status.number))

            print()


if __name__ == '__main__':
    the_network = Network()
    s = input('Enter command: ')
    while s.strip().lower() != QUIT:
        split_command = s.split()
        if len(split_command) == 3 and split_command[0].lower() == SWITCH_CONNECT:
            area_1 = int(split_command[1])
            area_2 = int(split_command[2])
            the_network.connect_switchboards(area_1, area_2)
        elif len(split_command) == 2 and split_command[0].lower() == SWITCH_ADD:
            the_network.add_switchboard(int(split_command[1]))
        elif len(split_command) == 2 and split_command[0].lower() == PHONE_ADD:
            number_parts = split_command[1].split(HYPHEN)
            area_code = int(number_parts[0])
            phone_number = int(''.join(number_parts[1:]))

            the_network.create_phone(phone_number, area_code)

        elif len(split_command) == 2 and split_command[0].lower() == NETWORK_SAVE:
            the_network.save_network(split_command[1])
            print('Network saved to {}.'.format(split_command[1]))
        elif len(split_command) == 2 and split_command[0].lower() == NETWORK_LOAD:
            the_network.load_network(split_command[1])
            print('Network loaded from {}.'.format(split_command[1]))

        elif len(split_command) == 3 and split_command[0].lower() == START_CALL:
            src_number_parts = split_command[1].split(HYPHEN)
            src_area_code = int(src_number_parts[0])
            src_number = int(''.join(src_number_parts[1:]))

            dest_number_parts = split_command[2].split(HYPHEN)
            dest_area_code = int(dest_number_parts[0])
            dest_number = int(''.join(dest_number_parts[1:]))

            connect_result = the_network.start_end_call(src_area_code, src_number, dest_area_code, dest_number, START_CALL)

            if connect_result == True:
                print('{}-{} and {}-{} are now connected.'.format(src_area_code, src_number, dest_area_code, dest_number))
            else:
                print('{}-{} and {}-{} were not connected.'.format(src_area_code, src_number, dest_area_code, dest_number))


        elif len(split_command) == 2 and split_command[0].lower() == END_CALL:
            number_parts = split_command[1].split('-')
            area_code = int(number_parts[0])
            number = int(''.join(number_parts[1:]))

            disc_result = the_network.start_end_call(area_code, number, None, None, END_CALL)

            if disc_result is True:
                print('Connection Terminated.')
            else:
                print('Unable to disconnect.')


        elif len(split_command) >= 1 and split_command[0].lower() == DISPLAY:
            the_network.display()

        s = input('Enter command: ')
