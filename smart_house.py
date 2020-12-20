"""
File: smart_house.py
Author: Jason Song
Date: 11/18/2020
Lab Section: 22
Email: jason20@umbc.edu
Description:
Takes user inputs: address of a house, devices and on/off status of devices.
Allows user to save devices to a user-specified file and filename for recovery and display purposes.
"""


class Device:
    def __init__(self, name, toggle):
        self.name = name
        self.toggle = toggle


class SmartHouse:
    def __init__(self, address):
        self.address = address
        self.devices_list = []  #list of current devices within file
        self.adding_devices = []    #separate list to determine devices to append to already existing file
        self.file_name = None

    def add_device(self, device):
        """
        :param device: device name
        :return:
        """
        #appends to both lists for either reference later or differentiate file devices vs. newly created devices to be appended to file.
        self.devices_list.append(device)
        self.adding_devices.append(device)
        #print(device.name)

    def get_device(self, the_id):
        """
        :param the_id: user inputted device name
        :return: checks to see if device name is in list of devices from specific file, returns device object
        """
        # search through the ID's for the device with that name/id,
        #returns device and attributes for display or modification

        for device in self.devices_list:
            if device.name == the_id:
                return device

    def save_house(self, file_name):
        """
        :param file_name: takes user entered filename
        :return: creates or appends devices to file
        """
        # take a filename and save all devices into a file - user will create name, no apostrophes etc
        self.file_name = file_name

        #iterates through list of appended devices from using 'add device' command and appends to file_name
        with open(self.file_name, 'a') as save_file:
            for device in self.adding_devices:
                save_file.write(device.name + ';' + str(device.toggle) + '\n')



    def load_house(self, file_name):
        """
        :param file_name: user entered file name
        :return: recreates from file
        """
        # take in filename, reset the devices and load in the devices in the file

        self.file_name = file_name

        #reads file given by user after 'load' command and outputs in list format
        with open(self.file_name, 'r') as load_file:
            reload_list = load_file.readlines()

        #recreates list by appending each item in file to the devices_list
        for item in range(len(reload_list)):
            device_split = reload_list[item].split(';')
            if device_split[1].strip('\n') == 'True':
                self.devices_list.append(Device(device_split[0], True))
            else:
                self.devices_list.append(Device(device_split[0], False))


    def display(self):

        print('For the house at {}'.format(self.address))

        #iterates through devices and prints out devices attributes in proper format
        for device in self.devices_list:
            if device.toggle == True:
                toggle_status = 'on'
            else:
                toggle_status = 'off'
            print('\t\t', device.name, 'is', toggle_status)


if __name__ == '__main__':
    address = input('What is the address of the house?')
    house = SmartHouse(address)

    command = input('What do you want to do? (add device, toggle device, load <file>, save <file>, display) ').lower()
    while command != 'quit':
        if command == 'add' or command == 'add device':
            the_id = input('What is the device id?')
            if not house.get_device(the_id):
                yes_no = input('Is the device on? (yes/no)')
                if yes_no == 'yes':
                    house.add_device(Device(the_id, True))
                elif yes_no == 'no':
                    house.add_device(Device(the_id, False))
            else:
                print('There is no device id: {} in the ')
        elif command == 'toggle' or command == 'toggle device':
            the_id = input('What is the device id?')
            the_device = house.get_device(the_id)
            if the_device:
                on_off_toggle = input('On, Off or Toggle? ').lower()
                if on_off_toggle == 'on':
                    the_device.toggle = True
                elif on_off_toggle == 'off':
                    the_device.toggle = False
                elif on_off_toggle == 'toggle':
                    the_device.toggle = not the_device.toggle
            else:
                print('There is no device id: {} in the ')
        elif command == 'load':
            file_name = input('What is the filename to load from? ')
            house.load_house(file_name)
            print('The house has been loaded from {}'.format(file_name))
        elif command == 'save':
            file_name = input('What is the filename to save as? ')
            house.save_house(file_name)
            print('The house has been saved in {}'.format(file_name))
        elif command == 'display':
            house.display()
        else:
            print('unknown command', command)

        command = input(
            'What do you want to do? (add device, toggle device, load <file>, save <file>, display) ').lower()
