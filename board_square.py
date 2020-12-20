class UrPiece:
    def __init__(self, color, symbol):
        self.color = color
        self.position = None
        self.complete = False
        self.symbol = symbol

    def can_move(self, num_moves, current_square, starting_square, win_square):

        a_board_square = self.position

        if a_board_square == None:
            a_board_square = starting_square

            num_moves -= 1
        else:
            a_board_square = current_square

        for i in range(num_moves):
            if a_board_square.exit == self.color and num_moves - i > 1:
                return False
            elif a_board_square.exit == self.color and num_moves - i == 1:
                a_board_square = win_square
                return a_board_square
            else:
                if self.color == "White":
                    a_board_square = a_board_square.next_white
                else:
                    a_board_square = a_board_square.next_black

        if a_board_square.piece == None:
            return a_board_square

        elif a_board_square.piece != None:
            if a_board_square.piece.color == self.color:
                return False

            else:
                if a_board_square.rosette == True:
                    return False
                else:
                    return a_board_square

class BoardSquare:
    def __init__(self, x, y, entrance=False, _exit=False, rosette=False, forbidden=False):
        self.piece = None
        self.position = (x, y)
        self.next_white = None
        self.next_black = None
        self.exit = _exit
        self.entrance = entrance
        self.rosette = rosette
        self.forbidden = forbidden

    def load_from_json(self, json_string):
        import json
        loaded_position = json.loads(json_string)
        self.piece = None
        self.position = loaded_position['position']
        self.next_white = loaded_position['next_white']
        self.next_black = loaded_position['next_black']
        self.exit = loaded_position['exit']
        self.entrance = loaded_position['entrance']
        self.rosette = loaded_position['rosette']
        self.forbidden = loaded_position['forbidden']

    def jsonify(self):
        next_white = self.next_white.position if self.next_white else None
        next_black = self.next_black.position if self.next_black else None
        return {'position': self.position, 'next_white': next_white, 'next_black': next_black, 'exit': self.exit,
                'entrance': self.entrance, 'rosette': self.rosette, 'forbidden': self.forbidden}
