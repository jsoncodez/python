from sys import argv
from random import choice
from board_square import BoardSquare, UrPiece



class RoyalGameOfUr:
    STARTING_PIECES = 7

    def __init__(self, board_file_name):
        self.board = None
        self.load_board(board_file_name)
        self.w_pieces_list = []
        self.b_pieces_list = []

    def load_board(self, board_file_name):
        """
        This function takes a file name and loads the map, creating BoardSquare objects in a grid.

        :param board_file_name: the board file name
        :return: sets the self.board object within the class
        """

        import json
        try:
            with open(board_file_name) as board_file:
                board_json = json.loads(board_file.read())
                self.num_pieces = self.STARTING_PIECES
                self.board = []
                for x, row in enumerate(board_json):
                    self.board.append([])
                    for y, square in enumerate(row):
                        self.board[x].append(BoardSquare(x, y, entrance=square['entrance'], _exit=square['exit'],
                                                         rosette=square['rosette'], forbidden=square['forbidden']))

                for i in range(len(self.board)):
                    for j in range(len(self.board[i])):
                        if board_json[i][j]['next_white']:
                            x, y = board_json[i][j]['next_white']
                            self.board[i][j].next_white = self.board[x][y]
                        if board_json[i][j]['next_black']:
                            x, y = board_json[i][j]['next_black']
                            self.board[i][j].next_black = self.board[x][y]
        except OSError:
            print('The file was unable to be opened. ')

    def draw_block(self, output, i, j, square):
        """
        Helper function for the display_board method
        :param output: the 2d output list of strings
        :param i: grid position row = i
        :param j: grid position col = j
        :param square: square information, should be a BoardSquare object
        """
        MAX_X = 8
        MAX_Y = 5
        for y in range(MAX_Y):
            for x in range(MAX_X):
                if x == 0 or y == 0 or x == MAX_X - 1 or y == MAX_Y - 1:
                    output[MAX_Y * i + y][MAX_X * j + x] = '+'
                if square.rosette and (y, x) in [(1, 1), (1, MAX_X - 2), (MAX_Y - 2, 1), (MAX_Y - 2, MAX_X - 2)]:
                    output[MAX_Y * i + y][MAX_X * j + x] = '*'
                if square.piece:
                    # print('sps:',square.piece.symbol)
                    output[MAX_Y * i + 2][MAX_X * j + 3: MAX_X * j + 5] = square.piece.symbol


    def display_board(self):
        """
        Draws the board contained in the self.board object

        """
        if self.board:
            output = [[' ' for _ in range(8 * len(self.board[i // 5]))] for i in range(5 * len(self.board))]
            for i in range(len(self.board)):
                for j in range(len(self.board[i])):
                    if not self.board[i][j].forbidden:
                        self.draw_block(output, i, j, self.board[i][j])

            print('\n'.join(''.join(output[i]) for i in range(5 * len(self.board))))

    def roll_d4_dice(self, n=4):
        """
        Keep this function as is.  It ensures that we'll have the same runs with different random seeds for rolls.
        :param n: the number of tetrahedral d4 to roll, each with one dot on
        :return: the result of the four rolls.
        """
        dots = 0
        for _ in range(n):
            dots += choice([0, 1])
        return dots
    def find_entrances_white(self): #iterates through board spaces to determine enter position
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if self.board[i][j].entrance == "White":
                    self.entrance_white = self.board[i][j]


        return self.entrance_white

    def find_exits_white(self): #iterates through board spaces to determine exit position
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if self.board[i][j].exit == "White":
                    self.exit_white = self.board[i][j]


        return self.exit_white

    def find_entrances_black(self):
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if self.board[i][j].entrance == "Black":
                    self.entrance_black = self.board[i][j]

        return self.entrance_black

    def find_exits_black(self):
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if self.board[i][j].exit == "Black":
                    self.exit_black = self.board[i][j]

        return self.exit_black

    def find_forbidden(self):
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if self.board[i][j].forbidden:
                    self.forbidden_square = self.board[i][j]

        return self.forbidden_square
    def coordinate_helper(self, movable_piece):
        #takes in pieces that are on spaces from movable_pieces and get's coordinate position for output for user selection
        for spaces in self.board:
            for space in spaces:
                if movable_piece == space:
                    return space.position

    def movable_pieces(self, dice_roll, entrance, pieces_list):
        self.movable_pieces_list = []   #list of pieces that pass can_move test

        self.movable_squares_list = []  #list of square locations that pieces will move to if selected

        win_square = self.find_forbidden()  #based on condition in can_move, creates a 'completed' situation for pieces that land in forbidden zones but only if at end and have exact # of moves

        for i in pieces_list:

            piece = i
            if piece.complete != True:  #any situation that have not reached the end and are out of play

                can_move_output = piece.can_move(dice_roll, piece.position, entrance, win_square)

                if can_move_output != False:    #creates list used for user display and selection for piece movement
                    self.movable_pieces_list.append(piece)
                    self.movable_squares_list.append(can_move_output)
                    # self.prior_positions_list.append(piece.position)

        for index in range(len(self.movable_pieces_list)):  #displays pieces that have valid moves
            if self.movable_pieces_list[index].position == None:

                print(index + 1, self.movable_pieces_list[index].symbol, 'Not on board')
            else:
                print(index + 1, self.movable_pieces_list[index].symbol,
                      self.coordinate_helper(self.movable_pieces_list[index].position))

        usr_select = int(input('Which piece do you want to move?'))

        while usr_select != int(usr_select) or usr_select < 1 or usr_select > len(self.movable_pieces_list):
            usr_select = int(input('Which piece do you want to move?'))

        moving_piece = self.movable_pieces_list[usr_select - 1]


        prior_square = moving_piece.position    #stores square piece will be moving from

        moving_square = self.movable_squares_list[usr_select - 1]

        if moving_square.piece != None and moving_square.piece.color != moving_piece.color: #condition if space was occupied by other player pieces and will remove them from the board
            if moving_square.piece.color == "Black":
                for piece in self.b_pieces_list:
                    if piece == moving_square.piece:
                        piece.position = None
            elif moving_square.piece.color == "White":
                for piece in self.w_pieces_list:
                    if piece == moving_square.piece:
                        piece.position = None

        moving_piece.position = moving_square   #placement of new postiion
        moving_square.piece = moving_piece
        if prior_square != None:    #removes prior location
            prior_square.piece = None

        if moving_square == win_square: #checks if piece moved fits "completed" condition
            moving_piece.complete = True

        #if moving_square.rosette == True:   #checks to see if space was a rosette space for a re roll


        return moving_square


    def check_win(self, pieces_list):   #checks if all player pieces hav ereached the end, breaking out of the while loop.
        self.piece_complete_counter = 0
        for piece in pieces_list:
            if piece.complete == True:
                self.piece_complete_counter += 1
        return self.piece_complete_counter

    def play_game(self):

        """CREATE PLAYERS"""

        p1 = input('What is your name? ')

        print('{}, you will play as white'.format(p1))

        p2 = input('What is your name? ')

        print('{}, you will play as black'.format(p2))

        for i in range(RoyalGameOfUr.STARTING_PIECES):  #creates unique pieces for both players
            a_w_piece = UrPiece('White', f'W{i + 1}')
            a_b_piece = UrPiece('Black', f'B{i + 1}')
            self.w_pieces_list.append(a_w_piece)
            self.b_pieces_list.append(a_b_piece)


        self.display_board()


        white_entrance = self.find_entrances_white()    #gets entrance locations for pieces
        black_entrance = self.find_entrances_black()



        # FIND EXIT
        white_exit = self.find_exits_white()     #stored variables for exit locations for pieces
        black_exit = self.find_exits_black()


        # DICE ROLL
        dice_roll = self.roll_d4_dice() #initial dice roll leading into while loop
        print('rolled a:', dice_roll)


        winner_count = 0    #set up variable for counter for while loop
        p1_turn = True  #set player 1 turn to true to make first roll


        starting_pieces = RoyalGameOfUr.STARTING_PIECES #local variable for amount of pieces for win condition in case it's changed for other game play


        while winner_count != starting_pieces:
            if p1_turn == True:
                if dice_roll != 0:

                    move_turn = self.movable_pieces(dice_roll, white_entrance, self.w_pieces_list)
                    #self.movable_pieces(dice_roll, white_entrance, self.w_pieces_list)


                self.display_board()
                dice_roll = self.roll_d4_dice()
                print('rolled a:', dice_roll)

                winner_count = self.check_win(self.w_pieces_list)

                if move_turn.rosette == True:
                    print('landed on rosette, roll again')
                    p1_turn = True
                else:
                    p1_turn = False

            elif p1_turn == False:

                if dice_roll != 0:

                    move_turn = self.movable_pieces(dice_roll, black_entrance, self.b_pieces_list)

                self.display_board()
                dice_roll = self.roll_d4_dice()
                print('rolled a:', dice_roll)
                winner_count = self.check_win(self.b_pieces_list)
                if move_turn.rosette == True:   #takes return of movable_pieces and if position rosette = true, then it will keep players turn
                    print('landed on rosette, roll again')
                    p1_turn = False
                else:
                    p1_turn = True

        if p1_turn != False:
            print('The winner is {}'.format(p1))
        else:
            print('The winner is {}'.format(p2))


if __name__ == '__main__':
    file_name = input('What is the file name of the board json? ') if len(argv) < 2 else argv[1]
    rgu = RoyalGameOfUr(file_name)
    rgu.play_game()