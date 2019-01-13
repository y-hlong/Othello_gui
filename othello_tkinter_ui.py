#Yin Hao Long 49256403
import othello_logic
import check_move_flip
import tkinter 

class settings_window:
    def __init__(self):
        #Sets up the top level window
        self._settings_window = tkinter.Toplevel()
        
        settings_label = tkinter.Label(
            master = self._settings_window, text = 'Set up your Othello game.',
            font = 'Helvetica')

        settings_label.grid(
            row = 0, column = 0, padx = 10, pady = 10,
            sticky = tkinter.W)

        #ROWS--------------------------------------
        #Sets up the label and drop down menu for rows
        rows_label = tkinter.Label(
            master = self._settings_window, text = 'Number of rows: ',
            font = 'Helvetica')

        rows_label.grid(
            row = 1, column = 0, padx = 10, pady = 10,
            sticky = tkinter.W)

        self.number_of_rows = tkinter.IntVar()
        
        rows_menu = tkinter.OptionMenu(self._settings_window, self.number_of_rows,
                                       4, 6, 8, 10, 12, 14, 16)
        
        rows_menu.grid(
            row = 1, column = 1,
            sticky = tkinter.W)

        #COLUMNS------------------------------------
        #sets up the label and drop down menu for rows
        columns_label = tkinter.Label(
            master = self._settings_window, text = 'Number of columns: ',
            font = 'Helvetica')

        columns_label.grid(
            row = 2, column = 0, padx = 10, pady = 10,
            sticky = tkinter.W)

        self.number_of_columns = tkinter.IntVar()
        
        columns_menu = tkinter.OptionMenu(self._settings_window, self.number_of_columns,
                                       4, 6, 8, 10, 12, 14, 16)
        
        columns_menu.grid(
            row = 2, column = 1,
            sticky = tkinter.W)

        #STARTING PLAYER----------------------------
        #sets up the label and drop down menu for the selection of a starting player
        starting_player_label = tkinter.Label(
            master = self._settings_window, text = 'Starting player: ',
            font = 'Helvetica')

        starting_player_label.grid(
            row = 3, column = 0, padx = 10, pady = 10,
            sticky = tkinter.W)

        self.starting_player_input = tkinter.StringVar()
        
        starting_player_menu = tkinter.OptionMenu(self._settings_window, self.starting_player_input,
                                       'B', 'W')
        
        starting_player_menu.grid(
            row = 3, column = 1,
            sticky = tkinter.W)
        
        #TOPLEFT------------------------------------
        #sets up the label and drop down menu for the selection of which tile is at the top left
        topleft_player_label = tkinter.Label(
            master = self._settings_window, text = 'Top-left color at starting position: ',
            font = 'Helvetica')

        topleft_player_label.grid(
            row = 4, column = 0, padx = 10, pady = 10,
            sticky = tkinter.W)

        self.topleft_player_input = tkinter.StringVar()
        
        topleft_player_menu = tkinter.OptionMenu(self._settings_window, self.topleft_player_input,
                                       'B', 'W')
        
        topleft_player_menu.grid(
            row = 4, column = 1,
            sticky = tkinter.W)
        
        #WINNINGCONDITION---------------------------
        #sets up the label and drop down menu for the selection of a winning condition
        winning_condition_label = tkinter.Label(
            master = self._settings_window, text = 'Winning condition: ',
            font = 'Helvetica')

        winning_condition_label.grid(
            row = 5, column = 0, padx = 10, pady = 10,
            sticky = tkinter.W)

        self.winning_condition_input = tkinter.StringVar()
        
        winning_condition_menu = tkinter.OptionMenu(self._settings_window, self.winning_condition_input,
                                       "Fewer tiles win", "More tiles win")
        
        winning_condition_menu.grid(
            row = 5, column = 1,
            sticky = tkinter.W)        

        #BUTTONS------------------------------------
        #sets up the ok and cancel button
        buttons_frame = tkinter.Frame(master = self._settings_window)

        buttons_frame.grid(
            row = 6, column = 1,
            sticky = tkinter.W)
        
        ok_button = tkinter.Button(
            master = buttons_frame, text = 'ok', font = 'Helvetica',
            command = self._on_ok_button)

        ok_button.grid(
            row = 0, column = 0, padx = 10, pady = 10,
            sticky = tkinter.W)
        
        cancel_button = tkinter.Button(
            master = buttons_frame, text = 'cancel', font = 'Helvetica',
            command = self._on_cancel_button)

        cancel_button.grid(
            row = 0, column = 1, padx = 10, pady = 10,
            sticky = tkinter.E)

        self._settings_window.rowconfigure(0, weight = 0)
        self._settings_window.rowconfigure(1, weight = 1)
        self._settings_window.rowconfigure(2, weight = 1)
        self._settings_window.rowconfigure(3, weight = 1)
        self._settings_window.rowconfigure(4, weight = 1)
        self._settings_window.rowconfigure(5, weight = 1)
        self._settings_window.rowconfigure(6, weight = 1)
        self._settings_window.columnconfigure(0, weight = 1)
        self._settings_window.columnconfigure(1, weight = 1)

        self.ok_button_pressed = False

        self._rows = 0
        self._columns = 0
        self._starting_player = ""
        self._topleft_player = ""
        self._winning_condition = ""
        
    def _on_ok_button(self) -> None:
        #puts all selections from the drop down menus into their own variables
        self.ok_button_pressed = True
        self._rows = self.number_of_rows.get()
        self._columns = self.number_of_columns.get()
        self._starting_player = self.starting_player_input.get()
        self._topleft_player = self.topleft_player_input.get()
        if self.winning_condition_input.get() == "Fewer tiles win":
            self._winning_condition = '<'
        elif self.winning_condition_input.get() == "More tiles win":
            self._winning_condition = '>'
        self._settings_window.destroy()

    def _on_cancel_button(self) -> None:
        #closes the window
        self._settings_window.destroy()
    
    def run(self) -> None:
        #runs the top level window
        self._settings_window.grab_set()
        self._settings_window.wait_window()

    def get_game_settings(self) -> tuple:
        #returns a namedtuple with all information needed to set up a game of Othello
        if self.ok_button_pressed:
            return (self._rows, self._columns, self._starting_player, self._topleft_player, self._winning_condition) 
        else:
            return False

class interactive_game_board:
    def __init__(self, board_state: othello_logic.board_state):
        #sets up root window
        self._state = board_state
        self._root_window = tkinter.Tk()

        #creates a button that starts a new game when clicked
        new_game_button = tkinter.Button(
            master = self._root_window, text = 'New Game', font = 'Helvetica',
            command = self._on_new_game)

        new_game_button.grid(
            row = 0, padx = 10, pady = 10,
            sticky = tkinter.N + tkinter. W)

        #label that shows whose turn it is
        self._text_display_turn = tkinter.StringVar()
        self._text_display_turn.set("")
        
        players_turn_label = tkinter.Label(
            master = self._root_window, textvariable = self._text_display_turn,
            font = 'Helvetica')

        players_turn_label.grid(
            row = 0,
            sticky = tkinter.N)

        #label that shows how much black and white tiles are currently on the board
        self._text_display = tkinter.StringVar()
        self._text_display.set('Black: ' + str(self._state.check_number_of_B()) + '  White: ' + str(self._state.check_number_of_W()))
        
        pieces_count_label = tkinter.Label(
            master = self._root_window, textvariable = self._text_display,
            font = 'Helvetica')

        pieces_count_label.grid(
            row = 0,
            sticky = tkinter.S)
        
        #creates a canvas
        self._canvas = tkinter.Canvas(
            master = self._root_window, width = 600, height = 600,
            background = '#006000')
        
        self._canvas.grid(
            row = 1, column = 0,
            sticky = tkinter.N + tkinter.S + tkinter.E + tkinter.W)

        #EVENTS-------------------------------------------------------------
        #all the event that drives the program
        self._winner_found = False
        
        self._canvas.bind('<Configure>', self._redraw)
        self._canvas.bind('<Enter>', self._redraw)
        self._canvas.bind('<Leave>', self._redraw)
        self._canvas.bind('<Button-1>', self._on_canvas_click)
        self._canvas.bind('<ButtonRelease-1>', self._redraw)
        
        self._root_window.rowconfigure(0, weight = 0)
        self._root_window.rowconfigure(1, weight = 2)
        self._root_window.columnconfigure(0, weight = 1)

    def _on_canvas_click(self, event: tkinter.Event):
        #runs when a click event happens on canvas
        #if winner is found, click will not do anything until a new game is started
        if self._winner_found == False:
            self._make_turn(event)
        
    def _make_turn(self, event: tkinter.Event):
        #checks where the click occured and matches that with the closest [column][row]
        #if move is valid, draw a oval with the current player's color 
        for column in range(len(self._state.current_gamestate())):
            for row in range(len(self._state.current_gamestate()[column])):
                center_x_tile = 1/self._state.number_of_columns() * column + 1/self._state.number_of_columns() * 1/2
                center_x_tile_pixel = center_x_tile * self._canvas.winfo_width()
                center_y_tile = 1/self._state.number_of_rows() * row + 1/self._state.number_of_rows() * 1/2 
                center_y_tile_pixel = center_y_tile * self._canvas.winfo_height()
                if event.x/self._canvas.winfo_width() > center_x_tile - 1/self._state.number_of_columns() * 1/2 and event.x/self._canvas.winfo_width() < center_x_tile + 1/self._state.number_of_columns() * 1/2 and event.y/self._canvas.winfo_height() > center_y_tile - 1/self._state.number_of_rows() * 1/2 and event.y/self._canvas.winfo_height() < center_y_tile + 1/self._state.number_of_rows() * 1/2:
                    if self._state.make_turn(check_move_flip.check_move().test_all_possibilities([row, column], self._state.current_gamestate(), self._state.current_players_turn(), self._state.next_players_turn())[0]) != False:
                        self._text_display.set('Black: ' + str(self._state.check_number_of_B()) + '  White: ' + str(self._state.check_number_of_W()))
                        self._text_display_turn.set("It is Player {}'s turn".format(self._state.current_players_turn()))
                        if self._state.check_no_valid_move():
                            self._text_display_turn.set("It is Player {}'s turn because Player {} had no possible moves".format(self._state.current_players_turn(), self._state.next_players_turn()))
                        if self._state.check_winner()[0] == True:
                            self._text_display_turn.set("{}".format(self._state.check_winner()[1]))
                            self._winner_found = True
                            return
                        
                    
    def _on_new_game(self):
        #sets the winner found to false so click event can happen
        #runs function that runs top level menu
        self._winner_found = False
        self._run_setup()
        
    def _run_setup(self):
        #runs top level menu and sets up the current state of the game
        self._game_settings = settings_window()
        self._game_settings.run()
        
        try:
            self._row, self._column, self._starting_player, self._topleft, self_winning_condition = self._game_settings.get_game_settings()
            self._state = othello_logic.board_state(self._row, self._column, self._starting_player, self._topleft, self_winning_condition)
            self._state.initial_board_setup()
            self._text_display.set('Black: ' + str(self._state.check_number_of_B()) + '  White: ' + str(self._state.check_number_of_W()))
            self._text_display_turn.set("It is Player {}'s turn".format(self._state.current_players_turn()))
        except:
            self._text_display.set('Game not started due to invalid input')
        finally:
            self._canvas.after(10, self._redraw('x'))
            
    
    def run(self):
        #runs the main loop for tkinter
        self._root_window.mainloop()

    def _redraw(self, event: tkinter.Event) -> None:
        #redraws everything on canvas, scaled with fractional and current width and height
        self._canvas.delete(tkinter.ALL)
        canvas_width = self._canvas.winfo_width()
        canvas_height = self._canvas.winfo_height()

        #X lines-----------------------------------------------------------
        #draws the vertical lines of the grid
        pixel_x = 1/self._state.number_of_columns()*self._canvas.winfo_width()
        
        temp_x = pixel_x
        for columns in range(self._state.number_of_columns() - 1):
            self._canvas.create_line(temp_x, 0, temp_x, 1*self._canvas.winfo_height(), fill = 'black')
            temp_x += pixel_x

        #Y lines-----------------------------------------------------------
        #draws the horizontal lines of the grid
        pixel_y = 1/self._state.number_of_rows()*self._canvas.winfo_height()
        
        temp_y = pixel_y
        for row in range(self._state.number_of_rows() - 1):
            self._canvas.create_line(0, temp_y, 1 * self._canvas.winfo_width(), temp_y, fill = 'black')
            temp_y += pixel_y
            
        #Tiles--------------------------------------------------------------
        #draws the tiles according to current game state
        for column in range(len(self._state.current_gamestate())):
            for row in range(len(self._state.current_gamestate()[column])):
                center_x_tile = 1/self._state.number_of_columns() * column + 1/self._state.number_of_columns() * 1/2
                center_x_tile_pixel = center_x_tile * self._canvas.winfo_width()
                center_y_tile = 1/self._state.number_of_rows() * row + 1/self._state.number_of_rows() * 1/2 
                center_y_tile_pixel = center_y_tile * self._canvas.winfo_height()
                if self._state.current_gamestate()[column][row] == 'B':
                    self._canvas.create_oval(center_x_tile_pixel -  1/self._state.number_of_columns() * 1/2 * self._canvas.winfo_width(),
                                             center_y_tile_pixel -  1/self._state.number_of_rows() * 1/2 * self._canvas.winfo_height(),
                                             center_x_tile_pixel +  1/self._state.number_of_columns() * 1/2 * self._canvas.winfo_width(),
                                             center_y_tile_pixel +  1/self._state.number_of_rows() * 1/2 * self._canvas.winfo_height(),
                                             fill = 'black')
                elif self._state.current_gamestate()[column][row] == 'W':
                    self._canvas.create_oval(center_x_tile_pixel -  1/self._state.number_of_columns() * 1/2 * self._canvas.winfo_width(),
                                             center_y_tile_pixel -  1/self._state.number_of_rows() * 1/2 * self._canvas.winfo_height(),
                                             center_x_tile_pixel +  1/self._state.number_of_columns() * 1/2 * self._canvas.winfo_width(),
                                             center_y_tile_pixel +  1/self._state.number_of_rows() * 1/2 * self._canvas.winfo_height(),
                                             fill = 'white')
                                             
                                             
    
    def draw_game_board(self):
        pass

if __name__ == '__main__':
    interactive_game_board(othello_logic.board_state(4, 4, 'B', 'W', '>')).run()
