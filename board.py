import tkinter as tk
from tkinter import messagebox

from PIL import ImageTk, Image

MAIN_FRAME = '#F4D983'
#
# '#B3D0D4'
BUTTON_COLOR = '#8CB8BB'
LABEL_COLOR = '#8CB8BB'
# '#C35C5C'
ACTIVE_COLOR = '#8CB8BB'

DEFULT_FONT = 'Segoe UI Black'
DEFULT_SIZE = 18
BG_BUTTON = '#8CB8BB'
FG_BUTTON = '#8CB8BB'

rules = ["Welcome to the Boggle game!",
         "1.In this game, your goal is to find as many words",
         " as possible by connecting adjacent letters",
         "on the grid.Each letter after the first must",
         "be a horizontal, vertical, or diagonal neighbor"
    , "of the one before it and no individual letter",
         "cube may be used more than once in a word",
         "2. The game board is a 4x4 grid of letters.",
         "Each cell is worth 2 points"
    , "3. You have 3 minutes to find as many",
         "words as possible.",
         "4.  Your score will be displayed on the",
         "left corner screen.",
         "5. If you want to play again,",
         "click on the restart button.",
         "6. Remember, the game is not about",
         "winning or losing, it's about having",
         " fun and improving your vocabulary",
         "and word-finding skills.",
         "7. Have fun and enjoy the game!"]


class GameGui:
    """
    "The GUI class for the game Boggle is responsible for
    displaying the game board,
    accepting user input, and displaying game information such as score
    and time remaining.
    It communicates with the Controller class to receive updates on the
    game state and to send user input.
    The GUI also provides visual feedback to the user on the
    status of the game,
    such as highlighting valid words or indicating the end of the game.
    It can be customized with different themes and colors to provide an
    immersive gaming experience."
    """

    def __init__(self):
        """The init function of the Graphic class is the constructor of
        the class.
        It sets up the main window using the tkinter library,
        initializes the start menu, frame, and graphic elements of the game.
        It also sets up the main loop for the game to run."""
        # Stars the main loop
        self.__root = tk.Tk()

        # Starts The main constractor of the game
        self.__init__start()
        self.__init__frame()
        self.__init__grap()

    def __init__start(self):
        """Initializes the instance variables with their initial values.
        This includes setting the time to 0 and creating a timer ID."""
        # Starts the time variable
        self.__time = 0
        self.__timer_id = 0

    def __init__frame(self):
        """This function creates the main frame, outer frame, right frame,
        and left frame, and sets their properties.
        It also sets the title, size, and resizability of the main window,
        and calls other functions to further initialize the frames."""
        # Main window
        self.__root.title('BOGGLE')
        self.__root.resizable(width=False, height=False)
        self.__root.geometry('{}x{}'.format(600, 500))

        # Main frame
        self.__outer_frame = tk.Frame(self.__root, bg='WHITE',
                                      highlightbackground='black')

        self.__outer_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        # Right frame (that will have all the button)
        self.__right_frame = tk.Frame(self.__outer_frame, bg=MAIN_FRAME,
                                      width=300, pady=0,
                                      highlightbackground=MAIN_FRAME,
                                      highlightthickness=0)
        self.__right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True,
                                anchor='e')

        # Left frame (that will contain all the labels )
        self.__left_frame = tk.Frame(self.__outer_frame, width=300,
                                     bg=MAIN_FRAME, pady=1,
                                     highlightbackground="white",
                                     highlightthickness=0)
        self.__left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True,
                               anchor='w')

        # Call function
        self.__init_in_frame()
        self.__frame_grid()

    def __init_in_frame(self):
        """ this function creates the inner frames for the game,
        including the bottom right frame, bottom left frame, top right frame,
        and top left frame.
        It sets their properties such as background color, size, and highlight
        thickness.
        It also uses the pack geometry manager to position the frames
        within the main frame.
        The frames are anchored to the specific corners of the main frame  """

        # The frame that will have the letters buttons
        self.__bottom_right_frame = tk.Frame(self.__right_frame, bg=MAIN_FRAME,
                                             width=300, height=300,
                                             highlightthickness=0)
        self.__bottom_right_frame.pack(side=tk.BOTTOM, fill=tk.BOTH,
                                       expand=True,
                                       anchor='se')

        # The frame that will have the word list
        self.__bottom_left_frame = tk.Frame(self.__left_frame, bg=MAIN_FRAME,
                                            height=300, width=300,
                                            highlightthickness=0)
        self.__bottom_left_frame.pack(side=tk.BOTTOM, fill=tk.BOTH,
                                      expand=True,
                                      anchor='sw')

        # The frame that will have the game control buttons
        self.__top_right_frame = tk.Frame(self.__right_frame, bg=MAIN_FRAME,

                                          highlightthickness=0, width=300,
                                          height=100)
        self.__top_right_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=False,
                                    anchor='ne')

        # The frame that will have all the display labels
        self.__top_left_frame = tk.Frame(self.__left_frame, bg=MAIN_FRAME,

                                         highlightthickness=0, width=300,
                                         height=100)
        self.__top_left_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=False,
                                   anchor='nw')

    def __frame_grid(self):
        """This function applies grid in the top right and top left
        frames using tkinter's grid geometry manager.
        It sets the row and column weights and minimum sizes for the frames."""

        # Divides the frame in to a grid
        for ind in range(1):
            self.__top_right_frame.rowconfigure(ind, weight=1, minsize=74)

        for index in range(1):
            self.__top_right_frame.columnconfigure(index, weight=1, minsize=20)

        # Divides the frame in to a grid
        for ind in range(1):
            self.__top_left_frame.rowconfigure(ind, weight=1, minsize=20)

        for index in range(1):
            self.__top_left_frame.columnconfigure(index, weight=1, minsize=20)

    def __init_image(self):
        """This function displays an image in the bottom left frame
        using the PIL library and tkinter's PhotoImage class.
        It also displays a list of instructions in the bottom right frame
        using a tkinter Listbox widget. """

        # Boggle image
        # Loads the image
        self.__image1 = Image.open("Sand_image_2.jpg")

        # Loads the image to tkinter
        self.__boggle_image = ImageTk.PhotoImage(self.__image1)

        # Creates a label for the image
        self.__image_label = tk.Label(self.__bottom_left_frame,
                                      image=self.__boggle_image, width=500,
                                      height=500, background=MAIN_FRAME)

        # packs the image
        self.__image_label.pack(expand=True, fill=tk.BOTH, side=tk.TOP)

        # instructions

        # Creates a Listbox for the successful words
        self.__rules = tk.Listbox(self.__bottom_right_frame,
                                  width=50, height=25,
                                  background=MAIN_FRAME,
                                  font=(DEFULT_FONT, 14), borderwidth=0,
                                  justify='center')

        # Packs the Listbox
        for i, rule in enumerate(rules):
            self.__rules.insert(i, rule)
        self.__rules.pack(side=tk.BOTTOM)

    def __init__grap(self):
        """function is responsible for initializing the main graphics
            for the game.
            It calls other functions to create the basic home page,
            including the play button, exit button and the instructions
             """

        # Calls the constractor for the start button
        self.__init__main_buttons()

        # Calls the constractor for the home screen
        self.__init_image()

    def __init__main_buttons(self):
        """The function creates the main buttons
            for the game,
            including the play button and exit button."""

        # Starts the button dict
        self.__buttons = {}

        # Calls the constractor for the play button
        self.__init_play_button()

        # Calls the constractor for the exit button
        self.__init_exit_button()

    def __init_word_graphic(self):
        """ This function initializes the graphic objects related to the
        successful words in the game.
        It creates a tkinter Listbox widget for displaying the
        list of successful words,
         """

        # The list of successful word
        self.word_box = tk.Listbox(self.__bottom_left_frame, width=30,
                                   height=21,
                                   font=(DEFULT_FONT, 15), bg=MAIN_FRAME,
                                   highlightbackground=LABEL_COLOR,
                                   highlightthickness=1, justify='center')
        self.word_box.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        # Adding a title
        self.word_box.insert(3, 'THE SUCCESSFUL WORDS:')

    def __init_exit_button(self):
        """ this function creates and sets up the exit button for the game.
        It creates the button, sets its properties such as text, font,
        background color and state. It then binds the button to two events,
        <Leave> and <Enter>
        that change the background color of the button when the cursor
        leaves or enters the button.
        The button is positioned in the top right frame
        using the grid geometry manager."""

        # The constructor of the Exit button
        self.exit_button = tk.Button(self.__top_right_frame, text='Exit',
                                     bg='white',
                                     font=(DEFULT_FONT, DEFULT_SIZE),
                                     state='normal',
                                     highlightbackground=LABEL_COLOR)

        # Adding the button to the dict
        self.__buttons['Exit'] = self.exit_button

        # hover over the button
        self.exit_button.bind("<Leave>",
                              lambda event: self.exit_button.configure(
                                  bg="gray"))
        self.exit_button.bind("<Enter>",
                              lambda event: self.exit_button.configure(
                                  bg=ACTIVE_COLOR))
        # pack the button
        self.exit_button.grid(row=0, column=0, sticky='e', columnspan=1)

    def __init_play_button(self):
        """ The __init_play_button function creates and sets up
        the play button for the game.
        It creates the button, sets its properties such as text, font,
        background color and state. It then binds the button to two events,
        <Leave> and <Enter>
        that change the background color of the button when the cursor leaves
        or enters the button.
        The button is positioned in the top right frame using the
        grid geometry manager."""

        # The constructor of the play button
        self.play_button = tk.Button(self.__top_right_frame, text='Play',
                                     font=(DEFULT_FONT, DEFULT_SIZE),
                                     state='normal',
                                     highlightbackground=LABEL_COLOR)

        # Adding the button to the dict
        self.__buttons['play'] = self.play_button

        # hover over the button
        self.play_button.bind("<Leave>",
                              lambda event: self.play_button.configure(
                                  bg="gray"))
        self.play_button.bind("<Enter>",
                              lambda event: self.play_button.configure(
                                  bg=ACTIVE_COLOR))

        # pack the button
        self.play_button.grid(row=0, column=1, columnspan=1, sticky='e')

    def __init__label(self):
        """ This function initializes the label objects that display information
        to the player regarding the game.
        It creates four labels: the time label title, the time label display,
        the score label title, and the score label display. Additionally,
        it creates two labels for the current word being formed:
        """

        # Creates the time label tittle
        self.__time_title_label = tk.Label(self.__top_left_frame, text='Time:',
                                           highlightbackground=LABEL_COLOR,
                                           borderwidth=3, relief="groove",
                                           font=(DEFULT_FONT, DEFULT_SIZE),
                                           bg=LABEL_COLOR)
        self.__time_title_label.grid(row=0, column=2, sticky='NSEW', pady=2,
                                     padx=2)

        # Creates the time label display
        self.__show_time_label = tk.Label(self.__top_left_frame,
                                          text=self.__time,
                                          highlightbackground=LABEL_COLOR,
                                          borderwidth=3, relief="groove",
                                          font=(DEFULT_FONT, DEFULT_SIZE)
                                          )
        self.__show_time_label.grid(row=1, column=2, sticky='NSEW', pady=2,
                                    padx=2)

        # Creates the score label tittle
        self.__score_title_label = tk.Label(self.__top_left_frame,
                                            text='Score',
                                            highlightbackground=LABEL_COLOR,
                                            borderwidth=3, relief="groove",
                                            bg=LABEL_COLOR,
                                            font=(DEFULT_FONT, DEFULT_SIZE))
        self.__score_title_label.grid(row=0, column=1, sticky='NSEW', pady=2,
                                      padx=2)

        # Creates the score label display
        self.__show_score_label = tk.Label(self.__top_left_frame,
                                           text='0',
                                           highlightbackground=LABEL_COLOR,

                                           font=(DEFULT_FONT, DEFULT_SIZE),
                                           relief="groove")
        self.__show_score_label.grid(row=1, column=1, pady=2,
                                     padx=2, sticky='nsew')

        # Creates the current word label tittle
        self.word_in_progress_title = tk.Label(self.__top_left_frame,
                                               text='Word:',
                                               width=9, height=1,
                                               font=(DEFULT_FONT, DEFULT_SIZE),
                                               bg=LABEL_COLOR,
                                               highlightbackground=LABEL_COLOR,
                                               relief="groove")
        self.word_in_progress_title.grid(row=0, column=0, sticky='NSEW',
                                         pady=2,
                                         padx=2)

        # Creates the current word display
        self.__show_cur_word = tk.Label(self.__top_left_frame, width=9,
                                        height=1,
                                        pady=1,
                                        highlightbackground=LABEL_COLOR,
                                        relief="groove")
        self.__show_cur_word.grid(row=1, column=0, sticky='NSEW', pady=2,
                                  padx=2)

    def __init_word_button(self):
        """Initializes the buttons for the user interface:
        'Clear', 'Delete', and 'Submit'.  """

        # The constructor of the Submit button
        self.submit_button = tk.Button(self.__top_right_frame, text='Submit',
                                       activebackground=ACTIVE_COLOR,
                                       font=(DEFULT_FONT, DEFULT_SIZE),
                                       highlightbackground=LABEL_COLOR,
                                       bg=LABEL_COLOR)

        # The constructor of the Clear button
        self.clear = tk.Button(self.__top_right_frame, text='Clear',
                               activebackground=LABEL_COLOR,
                               font=(DEFULT_FONT, DEFULT_SIZE),
                               highlightbackground=LABEL_COLOR, bg=LABEL_COLOR)

        # The constructor of the Delete button
        self.delete_button = tk.Button(self.__top_right_frame, text='Delete',
                                       activebackground=ACTIVE_COLOR,
                                       font=(DEFULT_FONT, DEFULT_SIZE),
                                       highlightbackground=LABEL_COLOR,
                                       bg=LABEL_COLOR)
        # packing
        self.play_button.grid(row=0, column=5, sticky='nsew', pady=1,
                              padx=1)
        self.exit_button.grid(row=0, column=4, sticky='nsew', pady=1,
                              padx=1)
        self.delete_button.grid(row=0, column=0, columnspan=1, sticky='nsew',
                                pady=1,
                                padx=1)
        self.submit_button.grid(row=0, column=2, columnspan=1, sticky='nsew',
                                pady=1,
                                padx=1)
        self.clear.grid(row=0, column=1, columnspan=1, sticky='nsew', pady=1,
                        padx=1)

        # Adding to button dict
        self.__buttons['Clear'] = self.clear
        self.__buttons['submit'] = self.submit_button
        self.__buttons['Delete'] = self.delete_button

    def __init_letters_button(self, row, col, name):
        """This function initializes the buttons for the letters of the game.
        It creates a button for each letter using
        The button's text is set to the input parameter 'name',
        The buttons are also added to the buttons dictionary,
        with their respective row and column as keys."""

        #  Creating a button for each letter
        self.button = tk.Button(self.__bottom_right_frame, text=name,
                                activebackground=ACTIVE_COLOR,
                                font=(DEFULT_FONT, DEFULT_SIZE))
        self.button.bind("<Leave>",
                         lambda event: self.button.configure(bg=BUTTON_COLOR))
        self.button.bind("<Enter>",
                         lambda event: self.button.configure(bg=ACTIVE_COLOR))

        # packing the button
        self.button.grid(row=row, column=col, rowspan=1, sticky=tk.NSEW)

        # Adding to dict
        self.__buttons[(row, col)] = self.button

    def set_play(self, func):
        """this function sets the play button command"""
        self.play_button.configure(command=func)

    def set_exit(self, func):
        """this function sets the exit button command"""
        self.exit_button.configure(command=func)

    def set_submit(self, func):
        """this function sets the submit button command"""
        self.submit_button.configure(command=func)

    def set_clear(self, func):
        """this function sets the clear button command"""
        self.clear.configure(command=func)

    def set_delete(self, func):
        """this function sets the delete button command"""
        self.delete_button.configure(command=func)

    def set_letter_func(self, name, func):
        """this function sets the letter function command"""
        self.__buttons[name].configure(command=func)

    def set_score_display(self, score: int):
        """this function sets the score display"""
        self.__show_score_label["text"] = score

    def set_word_display(self, word: str):
        """this function sets the current word display"""
        self.__show_cur_word['text'] = word

    def set_word_list_display(self, word: str, func):
        """this function sets the word list display"""
        if func == 'ADD':
            # checks the needs to add a word
            self.word_box.insert(tk.END, '\n' + word)
        else:
            # Restarts the List
            self.word_box.delete(1, tk.END)

    def __hide_image(self):
        """this function forgets the image & rules from the main window"""
        self.__image_label.forget()
        self.__rules.forget()

    def make_graph(self):
        """This function initializes the graphics of the ehrn game is started.
        by calling , several other functions. It hides an image, initializes labels,
        initializes the graphic objects related to the words being used,
        and initializes the buttons for the user interface"""

        # clears the frames
        self.__hide_image()

        # initializes the labels
        self.__init__label()

        # initializes the list
        self.__init_word_graphic()

        # initializes the buttons
        self.__init_word_button()

    def make_board(self, board):
        """
        This function creates the letter buttons for the game. It takes a 2D board as an input,
        and loops through the rows and columns of the board.
        For each cell in the board, it calls the __init_letters_button function
        to create a button with the letter in that cell.
        The function also configures the rows and columns of the
        frame
        """

        size = len(board)
        # Dividing the board in to a grid
        for ind in range(size):
            self.__bottom_right_frame.rowconfigure(ind, weight=1, minsize=50)

        for index in range(len(board[0])):
            self.__bottom_right_frame.columnconfigure(index, weight=1,
                                                      minsize=50)
        # initialize a button for each slot
        for row in range(size):
            for col in range(len(board[0])):
                self.__init_letters_button(row, col, board[row][col])

    def play_sound(self):
        """this function plays a sound"""
        self.__root.bell()

    def get_button_dict(self):
        """this function return the button dict """
        return self.__buttons

    def messages(self, score):
        """tThis function is used to display messages to the user when the game is over.
        It takes a score as an input and checks if the input is an integer.
        If it is, it shows a message box with the user's score and asks if they
        want to play again.
        If the input is not an integer, it asks if the user wants to restart
        the game"""

        # the messages was called because the is over
        if isinstance(score, int):
            result = tk.messagebox.askyesno('GAME OVER ',
                                            "Your score is: " + str(
                                                score) + " do you want to play again?")
        else:
            # the messages were called because of restart
            result = tk.messagebox.askyesno('RESTART',
                                            "Are you sure you want to restart?")
        return result

    def update_timer(self, time):
        """unction that updates the timer and starts counting down from the
        input time in seconds.
         It displays the time in minutes and seconds format and when the time
         is less than 11 seconds,
        it changes the background color of the label.
        When the time reaches 0 seconds, it displays 'Time's up' and calls
        the messages
        function to ask the user if they want to play again or close the game."""


        if isinstance(time, str):
            # Checks if it needs to restart
            self.__top_left_frame.after_cancel(self.__timer_id)
            return

        minutes, seconds = divmod(time, 60)
        # Changing to display

        self.__time = time
        self.__show_time_label.config(
            text="{}:{:02d}".format(minutes, seconds))
        # Updating Display label

        if time < 11:
            # if 10 sec left
            self.__show_time_label.config(background='red')

        if time >= 0:
            # recursive call every 100 mil
            self.__timer_id = self.__root.after(1000, self.update_timer,
                                                time - 1)
        else:
            # No more time updates label
            self.__show_time_label['text'] = 'TIMES UP!'

            # Asks message
            result = self.messages(int(self.__show_score_label['text']))

            # Checks the anser of the player
            if result:
                # Starts new game

                self.play_button['text'] = 'new'
                self.__show_time_label.config(background=MAIN_FRAME)
                self.play_button.invoke()

            else:
                # End game
                self.close()

    def run(self):
        """this function runs the Gui Class"""
        self.__root.tk.mainloop()

    def close(self):
        """this function closes the Gui Class"""
        self.__root.destroy()
