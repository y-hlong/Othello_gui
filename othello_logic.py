#Yin Hao Long 49256403
import check_move_flip


class board_state:
    def __init__(self, rows: int, columns: int, starting_color: str, top_left_color: str, winning_condition: str):
        '''
        Sets all variable needed to be displayed or manipulated for the game board.
        '''
        self._rows = rows
        self._columns = columns
        if self._rows % 2 == 1 or self._columns % 2 == 1 or type(self._rows) != int or type(self._columns) != int:
            raise InvalidRowColumnException("Row and column must be an even integer between 4 - 16")

        self._current_player = starting_color
        self._top_left_color = top_left_color
        if self._current_player != 'B' and self._current_player != 'W' or self._top_left_color != 'W' and self._top_left_color != 'B':
            raise InvalidColor("Only B and W are accepted input for colors")

        self._winning_condition = winning_condition
        if self._winning_condition !=  '<' and self._winning_condition !=  '>':
            raise InvalidWinCondition("Only < and > accepted as win conditions")

        if self._current_player == 'B':
            self._next_player = 'W'
        else:
            self._next_player = 'B'
        if self._top_left_color == 'B':
            self._top_right_color = 'W'
            
        else:
            self._top_right_color = 'B'
            
        self.game_board = []
        self.invalid_count = 0

    def number_of_rows(self) -> int:
        return self._rows

    def number_of_columns(self) -> int:
        return self._columns
    
    def current_gamestate(self) -> list:
        '''
        Returns the current gamestate in a 2d list format.
        '''
        return self.game_board

    def current_players_turn(self) -> str:
        '''
        Returns a str that represents the current player's turn.
        '''
        return self._current_player

    def next_players_turn(self) -> str:
        '''
        Returns a str representing the next player's turn.
        '''
        return self._next_player

    def check_number_of_B(self) -> int:
        '''
        Returns the amount of B tile on the board.
        '''
        b_count = 0
        for column in self.game_board:
            for row in column:
                if row == 'B':
                    b_count += 1
        return b_count

    def check_number_of_W(self) -> int:
        '''
        Returns the amount of W tile on the board.
        '''
        w_count = 0
        for column in self.game_board:
            for row in column:
                if row == 'W':
                    w_count += 1
        return w_count
    
    def initial_board_setup(self):
        '''
        Creates a board according to info when creating board_state object.
        '''
        for column in range(self._columns):
            self.game_board.append([])
        for row in range(self._rows):
            for column in range(self._columns):
                if column == self._columns/2 - 1 and row == self._rows/2 - 1 or column == self._columns/2 and row == self._rows/2:
                    self.game_board[column].append(self._top_left_color)
                    continue
                if column == self._columns/2 and row == self._rows/2 - 1 or column == self._columns/2 - 1 and row == self._rows/2:
                    self.game_board[column].append(self._top_right_color)
                    continue
                self.game_board[column].append('.')
                
    def display_board(self):
        '''
        Displays the board in a user_friendly way.
        '''
        for row in range(self._rows):
            for column in range(self._columns):
                print(self.game_board[column][row] + " ", end ="")
            print("")
            
    def make_turn(self, coordinates_to_change):
        '''
        Takes in a pair of coordinates (column, row) and checks if the move is valid.
        If valid, tiles are changed according to othello rules.
        '''
        if coordinates_to_change == []:
            return False
        for coordinate in coordinates_to_change:
            self.game_board[coordinate[0]][coordinate[1]] = self._current_player
        self._current_player, self._next_player = self._next_player, self._current_player    
        return True
               
    def check_no_valid_move(self):
        '''
        Check whether or not a player can make a move. If not, the turn reverts back to previous player.
        If there are two turns where there are no moves available, a end game condition is met
        since no players can make a move.
        '''
        possible_moves = []
        for columns in range(len(self.game_board)):
            for rows in range(len(self.game_board[columns])):
                if self.game_board[columns][rows] == '.':
                    possible_moves.extend(check_move_flip.check_move().test_all_possibilities([rows, columns], self.current_gamestate(), self.current_players_turn(), self.next_players_turn())[0])
        if possible_moves == []:
            self._current_player, self._next_player = self._next_player, self._current_player
            self.invalid_count += 1
            return True
        else:
            self.invalid_count = 0
            return False
        
    def check_winner(self):
        '''
        Checks if any winning conditions are met according to initial input.
        
        '''
        x = '1'
        if self.invalid_count >= 2:
            if self._winning_condition == '>':
                if self.check_number_of_B() > self.check_number_of_W():
                    x = 'WINNER: B'
                    return True, x
                elif self.check_number_of_B() == self.check_number_of_W():
                    x = 'WINNER: NONE'
                    return True, x
                else:
                    x = 'WINNER: W'
                    return True, x
            if self._winning_condition == '<':
                if self.check_number_of_B() < self.check_number_of_W():
                    x = 'WINNER: B'
                    return True, x
                elif self.check_number_of_B() == self.check_number_of_W():
                    x = 'WINNER: NONE'
                    return True, x
                else:
                    x = 'WINNER: W'
                    return True, x
        if self._winning_condition == '>' and self.check_number_of_B() + self.check_number_of_W() == self._rows * self._columns:
            if self.check_number_of_B() > self.check_number_of_W():
                x = 'WINNER: B'
                return True, x
            elif self.check_number_of_B() == self.check_number_of_W():
                x = 'WINNER: NONE'
                return True, x
            else:
                x = 'WINNER: W'
                return True, x
        if self._winning_condition == '<' and self.check_number_of_B() + self.check_number_of_W() == self._rows * self._columns:
            if self.check_number_of_B() < self.check_number_of_W():
                x = 'WINNER: B'
                return True, x
            elif self.check_number_of_B() == self.check_number_of_W():
                x = 'WINNER: NONE'
                return True, x
            else:
                x = 'WINNER: W'
                return True, x
        return False, x

class InvalidRowColumnException(Exception):
    pass

class InvalidColor(Exception):
    pass

class InvalidWinCondition(Exception):
    pass

class InvalidMove(Exception):
    pass                                   
                                          
