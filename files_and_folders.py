"""
File: files_and_folders.py
Author: Jason Song
Date: 12/11/2020
Lab Section: 22
Email: jason20@umbc.edu
Description:
Simulates creation of file directory.  Based on commands, creating/nesting/modifying and
navigating through set of folders and files
"""

class CommandLine:
    def __init__(self):

        self.root = Directory('root', None)
        self.current_path = self.root

    def run(self):

        command = input('>>> ')
        while command.strip().lower() != 'exit':
            split_command = command.split()
            if len(split_command):
                if split_command[0] == 'ls':
                    self.current_path.display()
            if len(split_command) >= 2:
                if split_command[0] == 'cd':
                    self.change_directory(split_command[1])
                elif split_command[0] == 'makedir':
                    self.current_path.create_directory(split_command[1])
                elif split_command[0] == 'fcreate':
                    self.current_path.create_file(split_command[1])
                elif split_command[0] == 'fwrite':
                    self.current_path.file_write(split_command[1])
                elif split_command[0] == 'fread':
                    self.current_path.file_read(split_command[1])
                elif split_command[0] == 'fclose':
                    self.current_path.close_file(split_command[1])
                elif split_command[0] == 'fopen':
                    self.current_path.open_file(split_command[1])

            command = input('>>> ')

    def change_directory(self, dir_name):

        if dir_name == '..':
            self.current_path = self.current_path.parent
        else:
            for directory in self.current_path.sub_dir:
                if directory.name == dir_name:
                    self.current_path = directory


class Directory:
    def __init__(self, name, parent):

        self.name = name
        self.parent = parent
        self.sub_dir = []
        self.sub_file_list = []


    def display(self):

        print('ls for directory: {}'.format(self.name))

        sub_dir_display = []
        for dir in self.sub_dir:
            sub_dir_display.append(dir.name)
        print('\t\t'.join(sub_dir_display))

        sub_file_display = []
        for file in self.sub_file_list:
            sub_file_display.append(file.file_name)
        print('\t\t'.join(sub_file_display))
        print()


    def create_file(self, file_name):

        found_file = self.file_search(file_name)
        if found_file == False:
            new_file = File(file_name)
            self.sub_file_list.append(new_file)
        else:
            print('File already exists in directory.')


    def create_directory(self, dir_name):

        for dir in self.sub_dir:
            if dir.name == dir_name:
                return print('Directory name already exists.')

        self.sub_dir.append(Directory(dir_name, self))


    def file_write(self, file_name):

        found_file = self.file_search(file_name)
        if found_file != False and found_file.open_status == True:
            usr_write = input('Enter file contents for {}: '.format(file_name))
            found_file.file_content.append(usr_write)
        elif found_file.open_status == False:
            print('You cannot write to a closed file.')


    def file_read(self, file_name):

        print('Contents of {}:'.format(file_name))
        found_file = self.file_search(file_name)

        if found_file != False:
            for write_entry in found_file.file_content:
                print(write_entry)


    def close_file(self, file_name):

        found_file = self.file_search(file_name)
        if found_file != False and found_file.open_status != False:
            found_file.open_status = False
        elif found_file.open_status == False:
            print('Cannot close a closed file')
        elif found_file == False:
            print('File does not exist')


    def open_file(self, file_name):

        found_file = self.file_search(file_name)
        if found_file != False and found_file.open_status != True:
            found_file.open_status = True
            found_file.file_content = []
        elif found_file.open_status == True:
            print('Cannot open an opened file')
        elif found_file == False:
            print('File does not exist')

    def file_search(self, file_name):
        # helper function to determine if files within directory exists, outputting the file for use or return False
        for file in self.sub_file_list:
            if file.file_name == file_name:
                return file
        return False

class File:
    def __init__(self, file_name):
        self.file_name = file_name
        self.open_status = False
        # create a list of entries for read command
        self.file_content = []


if __name__ == '__main__':

    cmd_line = CommandLine()
    cmd_line.run()
