"""
File: pyopoly.py
Author: Jason Song
Date: 10/18/2020
Lab Section: 22
Email: jason20@umbc.edu
Description:
    Pyopoly is a board game that takes 2 players each taking a turn rolling 2x dice to move around the board and landing on preset board values.
    Players has a turn to purchase purchasable-property and upgrade owned property and charge rent to opponents that land on properties they own.
    Player that loses all their money loses.
"""
# put your header here
from sys import argv
from random import randint, seed
from board_methods import load_map, display_board

# this code can be anywhere from right under the imports to right # above if __name__ == '__main__':
if len(argv) >= 2:
    seed(argv[1])


START_MONEY = 1500
GO_MONEY = 200

def play_game(starting_money, pass_go_money, board_file):
    board = board_file
    for property in board:  #adds additional key words an values to each position in the board
        property['Players'] = []    #stores players at specific property
        property['Owner'] = 'BANK'  #sets default value of key 'Owner' as 'BANK'
        property['Building'] = False    #sets default key value of having 'Building' as False


    #takes user name and user symbol
    p1_name = input('First player, what is your name? ').strip()
    p1_symbol = input('First player, what symbol do you want your character to use?').strip()

    while (len(p1_symbol) != 1) or (p1_symbol.isupper() != True):   #confirms user symbol input is 1 character and capital letter
        p1_symbol = input('First player, what symbol do you want your character to use?').strip()
    p1 = player_profile(p1_name, p1_symbol, starting_money)

    p2_name = input('Second player, what is your name? ').strip()
    p2_symbol = input('Second player, what symbol do you want your character to use?').strip()
    while (len(p2_symbol) != 1) or (p2_symbol.isupper() != True):
        p2_symbol = input('Second player, what symbol do you want your character to use?').strip()
    p2 = player_profile(p2_name, p2_symbol, starting_money)

    #places symbol on starting space
    board[p1['current position']]['Players'].append(p1['psymbol'])
    board[p2['current position']]['Players'].append(p2['psymbol'])


    next_player = players[0] #initializes while loop if statement for first turn
    while p1['Current Money'] > 0 and p2['Current Money'] > 0:  #exits loop if either player returns current money in negative
        if next_player == players[0]:
            player_move(p1, pass_go_money, board)
            next_player = players[1]   #sets next player turn to alternate
        else:
            player_move(p2, pass_go_money, board)
            next_player = players[0]
    winner = next_player['pname']#sets variable winner to player that has not gone yet because condition for exiting while loop has been met assuming the opponent that still has a turn current money > 0

    return winner  #returns winning player back to if-main when exiting the loop with condition that Current money is > 0

def player_move(player, pass_go_money, board):
    #function that initiates to determine new position of current player
    dice_roll = randint(1, 6) + randint(1, 6)
    board[player['current position']]['Players'].remove(player['psymbol'])  #removes current players prior position prior to move
    player['current position'] += dice_roll #updates players position after dice roll


    if player['current position'] > (len(board) - 1):
        #condition to determine player-position if dice roll resulted in a passing go.
        pass_go_multiplier = int(player['current position'] / len(board))  #determines multiplier if in case player passes Go multiple times and correctly give the pass go amount

        player['current position'] = (player['current position'] % len(board))  #takes result of modulus to determine new position of player when dice roll and current position is greater than length of board
        player['Current Money'] += (pass_go_money * pass_go_multiplier)    #add pass go money when passing go
        board[player['current position']]['Players'].append(player['psymbol'])  #appends player to position to key Players to be outputted in display board
    else:
        board[player['current position']]['Players'].append(player['psymbol'])

    format_board = format_display(board)
    display_board(format_board)
    print('{} has rolled a {}'.format(player['pname'], dice_roll))
    take_turn(player, players, board)


def player_profile(p_name, p_symbol, start_money):
    #creates dictionary for player profiles with keys that are relavant throughout the game
    player = {}
    player['pname'] = p_name
    player['psymbol'] = p_symbol
    player['Current Money'] = start_money
    player['current position'] = 0
    player['player owned'] = []
    players.append(player)
    return player


def take_turn(player, players, board):
    usr_position = player['current position']

    print('{} has landed on {}'.format(player['pname'], board[usr_position]['Place']))
    #checks to see if current player lands on opponent's owned property.  If so, confirms if property has building or not and subtracts appropriate rent.
    if board[usr_position]['Owner'] != 'BANK' and board[usr_position]['Owner'] != player['pname']:
        print("You have landed on {}'s property, you must pay the rent".format(board[usr_position]['Owner']))
        if board[usr_position]['Building'] == True:
            player['Current Money'] -= int(board[usr_position]['BuildingRent'])
            print('You have paid {} to {}'.format(board[usr_position]['BuildingRent'], board[usr_position]['Owner']))
        else:
            player['Current Money'] -= int(board[usr_position]['Rent'])
            print('You have paid {} to {}'.format(board[usr_position]['Rent'], board[usr_position]['Owner']))


    if player['Current Money'] >= 0:    #condition prior to entering in the user selections, otherwise will skip and return back to play_game function, ultimately ending the game
        print('\t1) Buy Property \n\t2) Get Property Info  \n\t3) Get Player Info  \n\t4) Build a Building  \n\t5) End Turn')
        usr_select = input('\tWhat do you want to do?').strip()

        while usr_select != '5':# and player['Current Money'] > 0:
            if usr_select == '1':   #current player buy property option
                if int(board[usr_position]['Price']) < 0:   #condition to check if property is purchasable property
                    print('You cannot buy this property.  It cannot be bought or sold.')
                elif board[usr_position]['Owner'] != 'BANK':  # board[usr_position]:    #if not non-purchasable property, checks to see if property has already been purchased by either players
                    print('{} is the owner of the property, you cannot buy it.'.format(board[usr_position]['Owner']))
                else:   #otherwise prompts if user wants to purchase
                    usr_buy = input('The property is unowned, do you want to buy it?').lower().strip()
                    if usr_buy == 'y' or usr_buy == 'yes':
                        if player['Current Money'] > int(board[usr_position]['Price']):

                            player['player owned'].append(usr_position)

                            player['Current Money'] -= int(board[int(player['current position'])]['Price']) #subtracts current users money by Price
                            board[usr_position]['Owner'] = player['pname']  #sets owner key value to current player on the property

                            print('You have bought {}.'.format(board[usr_position]['Place']))

                        else:
                            print('You do not have enough funds')
                    else:
                        print('You did not buy it')

            elif usr_select == '2':  # Get property info
                usr_property_info = input('For which property do you want to get the information? ').strip()
                for property in board:  #iterates through all properties on board and outputs property info if user input matches either Abbrev or Place name
                    if property.get('Abbrev') == usr_property_info or property.get('Place') == usr_property_info:
                        print('\t\t{}'.format(property['Place']))
                        for key in ('Price', 'Owner', 'Building', 'Rent'):  #formats output of specific keys of the property
                            if key == 'Building':
                                if property['Building'] == False:

                                    print('\t\t{}:'.format(key), 'No')
                                else:
                                    print('\t\t{}:'.format(key), 'Yes')
                            elif key == 'Rent':
                                print('\t\tRent {}, {} (with building)'.format(property['Rent'], property['BuildingRent']))
                            else:
                                print('\t\t{}: {}'.format(key, property[key]))


            elif usr_select == '3':  # get player info
                print('Players are:')
                for name in players:
                    print('\t{}'.format(name['pname']))
                usr_player_info = input('Which player do you wish to know about? ').strip()

                for player_num in range(len(players)):  # range(len(players)): #iterates through players and outputs correct player by matching condition if either the player name or player symbol exists to ou
                    if usr_player_info == players[player_num]['pname'] or usr_player_info == players[player_num]['psymbol']:

                        for key in ('pname', 'psymbol', 'Current Money'): #formats output of specific keys of the player
                            print(key, ':', players[player_num][key])

                        print('Properties Owned:')
                        if len(players[player_num]['player owned']) > 0:
                            for property in players[player_num]['player owned']:
                                print('\t\t', board[property]['Place'], 'with a building:', board[property]['Building'])
                        else:
                            print('\t\t', 'No Properties Yet')


            elif usr_select == '4':

                upgrade_properties = []
                # creates local list of relevant Abbrev & Place names, that reflect any upgradable position the current player owns and does not currently have a building
                for owned_property in player['player owned']:
                    if (board[owned_property]['Owner'] in player['pname']) and (board[owned_property]['Building'] != True):
                        upgrade_properties.append(board[owned_property]['Abbrev'])
                        upgrade_properties.append(board[owned_property]['Place'])
                        print(board[owned_property]['Place'], board[owned_property]['Abbrev'], board[owned_property]['BuildingCost'])

                usr_building = input('For which property do you want to build a building on? ').strip()
                #cross references users input to valid upgradeable properties
                if usr_building not in upgrade_properties:
                    print("The property either has a building, isn't yours, or doesn't exist.")
                else:
                    for valid_properties in player['player owned']:
                        if (usr_building == board[valid_properties]['Abbrev']) or (usr_building == board[valid_properties]['Place']) and (board[valid_properties]['Building'] != True):
                            board[valid_properties]['Building'] = True
                            player['Current Money'] -= int(board[valid_properties]['BuildingCost'])
                    print('You have built the building for {}.'.format(board[valid_properties]['Place']))
            print()

            print('\t1) Buy Property \n\t2) Get Property Info  \n\t3) Get Player Info  \n\t4) Build a Building  \n\t5) End Turn')
            usr_select = input('\tWhat do you want to do?').strip()


def format_display(board):

    format_board = []
    for property in board:
        abbrev_str = str(property['Abbrev'])

        if len(property['Players']) > 0:
            box_str = '{}\n{}'.format(abbrev_str.ljust(5), ''.join(property['Players']).ljust(5))
            format_board.append(box_str)
        else:
            box_str = '{}\n{}'.format(abbrev_str.ljust(5), ' '.ljust(5))
            format_board.append(box_str)


    return format_board



if __name__ == "__main__":
    players = []
    board_map = load_map(input('Enter board file: '))
    outcome = play_game(START_MONEY, GO_MONEY, board_map)
    print('You have been knocked out of the game.')
    print('The game has finally ended.  {} is the winner and now we can all go home.'.format(outcome))