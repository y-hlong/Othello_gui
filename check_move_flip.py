#Yin Hao Long 49256403
class check_move:
    def __init__(self):
        self._coordinates_to_flip = []
        
    def test_all_possibilities(self, move_coordinates: list, game_board: list, current_players_turn: str, next_players_turn: str):
        '''
        Runs all methods that check in every direction for tiles that should be flipped.
        If no tiles are found that can be flipped, return an empty list signifying that the move is invalid.
        '''
        try:
            if game_board[move_coordinates[1]][move_coordinates[0]] != '.':
                return (self._coordinates_to_flip, 'INVALID')
        except:
            raise OutOfRange('Input is larger than board limit')
        self.check_top_left(move_coordinates, game_board, current_players_turn, next_players_turn) 
        self.check_top_right(move_coordinates, game_board, current_players_turn, next_players_turn) 
        self.check_bottom_right(move_coordinates, game_board, current_players_turn, next_players_turn) 
        self.check_bottom_left(move_coordinates, game_board, current_players_turn, next_players_turn) 
        self.check_top(move_coordinates, game_board, current_players_turn, next_players_turn) 
        self.check_bottom(move_coordinates, game_board, current_players_turn, next_players_turn) 
        self.check_right(move_coordinates, game_board, current_players_turn, next_players_turn) 
        self.check_left(move_coordinates, game_board, current_players_turn, next_players_turn)
        if self._coordinates_to_flip != []:
            return (self._coordinates_to_flip, 'VALID')
        else:
            return (self._coordinates_to_flip, 'INVALID')
    
    def check_top_left(self, move_coordinates: list, game_board: list, current_players_turn: str, next_players_turn: str):
        '''
        Checks diagnally top left from the user input coordinate to either the end of row and column
        or when it hits the tile of the current player's turn. If there are no tiles that belong
        to the other player in said direction, return None.
        '''
        try:
            if game_board[move_coordinates[1] - 1][move_coordinates[0] - 1] != next_players_turn:
                return None
        except:
            return
        temp_column = move_coordinates[1]
        temp_row = move_coordinates[0]
        potential_flip_coordinates = []
        potential_flip_coordinates.append([temp_column, temp_row])
        while True:
            temp_column -= 1
            temp_row -= 1
            if temp_column < 0 or temp_row < 0 or temp_row >= len(game_board[0]) or temp_column >= len(game_board):
                return None   
            if game_board[temp_column][temp_row] == next_players_turn:
                potential_flip_coordinates.append([temp_column, temp_row])
            if game_board[temp_column][temp_row] == current_players_turn:
                self._coordinates_to_flip.extend(potential_flip_coordinates)
                return
    def check_top_right(self, move_coordinates: list, game_board: list, current_players_turn: str, next_players_turn: str):
        '''
        Checks diagnally top right from the user input coordinate to either the end of row and column
        or when it hits the tile of the current player's turn. If there are no tiles that belong
        to the other player in said direction, return None.
        '''
        try:
            if game_board[move_coordinates[1] + 1][move_coordinates[0] - 1] != next_players_turn:
                return None
        except:
            return
        temp_column = move_coordinates[1]
        temp_row = move_coordinates[0]
        potential_flip_coordinates = []
        potential_flip_coordinates.append([temp_column, temp_row])
        while True:
            temp_column += 1
            temp_row -= 1
            if temp_column < 0 or temp_row < 0  or temp_row >= len(game_board[0]) or temp_column >= len(game_board):
                return None   
            if game_board[temp_column][temp_row] == next_players_turn:
                potential_flip_coordinates.append([temp_column, temp_row])
            if game_board[temp_column][temp_row] == current_players_turn:
                self._coordinates_to_flip.extend(potential_flip_coordinates)
                return            
    def check_bottom_right(self, move_coordinates: list, game_board: list, current_players_turn: str, next_players_turn: str):
        '''
        Checks diagnally bottom right from the user input coordinate to either the end of row and column
        or when it hits the tile of the current player's turn. If there are no tiles that belong
        to the other player in said direction, return None.
        '''
        try:
            if game_board[move_coordinates[1] + 1][move_coordinates[0] + 1] != next_players_turn:
                return None
        except:
            return
        temp_column = move_coordinates[1]
        temp_row = move_coordinates[0]
        potential_flip_coordinates = []
        potential_flip_coordinates.append([temp_column, temp_row])
        while True:
            temp_column += 1
            temp_row += 1
            if temp_column < 0 or temp_row < 0  or temp_row >= len(game_board[0]) or temp_column >= len(game_board):
                return None   
            if game_board[temp_column][temp_row] == next_players_turn:
                potential_flip_coordinates.append([temp_column, temp_row])
            if game_board[temp_column][temp_row] == current_players_turn:
                self._coordinates_to_flip.extend(potential_flip_coordinates)
                return
    def check_bottom_left(self, move_coordinates: list, game_board: list, current_players_turn: str, next_players_turn: str):
        '''
        Checks diagnally bottom left from the user input coordinate to either the end of row and column
        or when it hits the tile of the current player's turn. If there are no tiles that belong
        to the other player in said direction, return None.
        '''
        try:
            if game_board[move_coordinates[1] - 1][move_coordinates[0] + 1] != next_players_turn:
                return None
        except:
            return
        temp_column = move_coordinates[1]
        temp_row = move_coordinates[0]
        potential_flip_coordinates = []
        potential_flip_coordinates.append([temp_column, temp_row])
        while True:
            temp_column -= 1
            temp_row += 1
            if temp_column < 0 or temp_row < 0  or temp_row >= len(game_board[0]) or temp_column >= len(game_board):
                return None   
            if game_board[temp_column][temp_row] == next_players_turn:
                potential_flip_coordinates.append([temp_column, temp_row])
            if game_board[temp_column][temp_row] == current_players_turn:
                self._coordinates_to_flip.extend(potential_flip_coordinates)
                return

    def check_top(self, move_coordinates: list, game_board: list, current_players_turn: str, next_players_turn: str):
        '''
        Checks top of the user input coordinate to either the end of row
        or when it hits the tile of the current player's turn. If there are no tiles that belong
        to the other player in said direction, return None.
        '''
        try:   
            if game_board[move_coordinates[1]][move_coordinates[0] - 1] != next_players_turn:
                return None
        except:
            return 
        temp_column = move_coordinates[1]
        temp_row = move_coordinates[0]
        potential_flip_coordinates = []
        potential_flip_coordinates.append([temp_column, temp_row])
        while True:
            temp_row -= 1 
            if temp_column < 0 or temp_row < 0  or temp_row >= len(game_board[0]) or temp_column >= len(game_board):
                return None   
            if game_board[temp_column][temp_row] == next_players_turn:
                potential_flip_coordinates.append([temp_column, temp_row])
            if game_board[temp_column][temp_row] == current_players_turn:
                self._coordinates_to_flip.extend(potential_flip_coordinates)
                return
    def check_bottom(self, move_coordinates: list, game_board: list, current_players_turn: str, next_players_turn: str):
        '''
        Checks bottom of the user input coordinate to either the end of row
        or when it hits the tile of the current player's turn. If there are no tiles that belong
        to the other player in said direction, return None.
        '''
        try:
            if game_board[move_coordinates[1]][move_coordinates[0] + 1] != next_players_turn:
                return None
        except:
            return
        temp_column = move_coordinates[1]
        temp_row = move_coordinates[0]
        potential_flip_coordinates = []
        potential_flip_coordinates.append([temp_column, temp_row])
        while True:
            temp_row += 1 
            if temp_column < 0 or temp_row < 0  or temp_row >= len(game_board[0]) or temp_column >= len(game_board):
                return None   
            if game_board[temp_column][temp_row] == next_players_turn:
                potential_flip_coordinates.append([temp_column, temp_row])
            if game_board[temp_column][temp_row] == current_players_turn:
                self._coordinates_to_flip.extend(potential_flip_coordinates)
                return
    def check_right(self, move_coordinates: list, game_board: list, current_players_turn: str, next_players_turn: str):
        '''
        Checks the right of the user input coordinate to either the end of column
        or when it hits the tile of the current player's turn. If there are no tiles that belong
        to the other player in said direction, return None.
        '''
        try:
            if game_board[move_coordinates[1] + 1][move_coordinates[0]] != next_players_turn:
                return None
        except:
            return
        temp_column = move_coordinates[1]
        temp_row = move_coordinates[0]
        potential_flip_coordinates = []
        potential_flip_coordinates.append([temp_column, temp_row])
        while True:
            temp_column += 1 
            if temp_column < 0 or temp_row < 0  or temp_row >= len(game_board[0]) or temp_column >= len(game_board):
                return None   
            if game_board[temp_column][temp_row] == next_players_turn:
                potential_flip_coordinates.append([temp_column, temp_row])
            if game_board[temp_column][temp_row] == current_players_turn:
                self._coordinates_to_flip.extend(potential_flip_coordinates)
                return
    def check_left(self, move_coordinates: list, game_board: list, current_players_turn: str, next_players_turn: str):
        '''
        Checks the left of the user input coordinate to either the end of column
        or when it hits the tile of the current player's turn. If there are no tiles that belong
        to the other player in said direction, return None.
        '''
        try:
            if game_board[move_coordinates[1] -1][move_coordinates[0]] != next_players_turn:
                return None
        except:
            return
        temp_column = move_coordinates[1]
        temp_row = move_coordinates[0]
        potential_flip_coordinates = []
        potential_flip_coordinates.append([temp_column, temp_row])
        while True:
            temp_column -= 1 
            if temp_column < 0 or temp_row < 0  or temp_row >= len(game_board[0]) or temp_column >= len(game_board):
                return None   
            if game_board[temp_column][temp_row] == next_players_turn:
                potential_flip_coordinates.append([temp_column, temp_row])
            if game_board[temp_column][temp_row] == current_players_turn:
                self._coordinates_to_flip.extend(potential_flip_coordinates)
                return
class OutOfRange(Exception):
    pass
