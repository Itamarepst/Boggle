import sys

import boggle_board_randomizer as bg
import utils as ut
from board import *

DEFULT_TIME = 180


class Controller:
    """The Controller class for the game Boggle manages the
    coordination between the GUI class and the Check Utilities class.
    It receives user input from the GUI in the form of selected coordinates
    and passes them to the Check Utilities for word validation.
    The Controller also updates the GUI with the results of the
    validation and manages the overall flow of the game,
    such as tracking the score and ending the game when necessary.
    Additionally,
    it handles the initialization of the game board
    and manages the game's parameters,
    such as the board size and time limit."""

    def __init__(self):
        """This is the init method for a class that represents a game of Boggle."""

        # An instance of the GameGui class, which handles the graphical user interface for the game
        self.gui = GameGui()

        # calling a method that sets up Play and Exit buttons
        self.__set_important_button()

        # A list that will store the current board state of the game
        self.__board = []

        # an integer that keeps track of the player's current score
        self.__score: int = 0

        # All the word varietals

        # A list that keeps track of the current path taken by the player
        self.__curr_path = []

        # A string that keeps track of the current word spelled by the player
        self.__curr_word = ''

        # A list that keeps track of all successful path taken by the player
        self.__successful_path = []

        # A list that keeps track of all possible moves for the player at a given point in the game
        self.__possible_moves = []

        # a set of all valid words for the game, created from the geven file
        self.__words = ut.create_word_set('boggle_dict.txt')

    def __make_board(self):
        """This method creates the board for the game. """
        self.__board = bg.randomize_board()

    def __set_important_button(self):
        """This method sets up important buttons for the game.
            It sets the play button to call the play method and
            the exit button to close the gui"""

        self.gui.set_play(self.play)
        self.gui.set_exit(self.gui.close)

    def play(self):
        """
            This method controls the behavior of the play button.
            it starts the game,  updates the
            timer and sets the board, letters and word buttons.

            Otherwise, it resets the game to its initial state.
            """

        if self.gui.play_button["text"] == 'Play':
            # If the button says "Play", it initializes the game

            # initializes the board
            self.gui.make_graph()
            self.__make_board()
            self.gui.make_board(self.__board)

            # sets functions for button
            self.__set_letter()
            self.__set_word_button()

            # Starts the timer
            self.gui.update_timer(DEFULT_TIME)

            # changes label
            self.gui.play_button["text"] = 'Restart'



        elif self.gui.play_button["text"] == 'Restart':
            # If the button says "Restart", it restarts the game.
            self.__restart()

        else:
            # When time ran out and started a new game

            # Restart word
            self.__curr_word = ''
            self.__possible_moves = []
            self.__curr_path = []
            self.gui.set_word_display(self.__curr_word)
            self.gui.set_word_list_display('', '')

            self.__successful_path = []

            # Starts score
            self.__score = 0
            self.gui.set_score_display(0)

            # Restart board
            self.__make_board()
            self.gui.make_board(self.__board)
            self.__set_letter()
            self.__set_word_button()

            self.gui.update_timer(DEFULT_TIME)
            self.gui.play_button["text"] = 'Restart'

    def __restart(self):
        """
            This method resets the game to its initial state.
            It prompts the user to confirm the restart, if confirmed it sets
            the current word and path,
            resets the score, redraws the board,
            and sets the letters and word buttons.
            """
        result = self.gui.messages("")
        if result:
            # Restart current word
            self.__set_clear_func()

            # Restart word list
            self.gui.set_word_display(self.__curr_word)

            # Restart score
            self.__score = 0
            self.gui.set_score_display(self.__score)

            # Makes new board
            self.__make_board()
            self.gui.make_board(self.__board)
            self.__set_letter()
            self.__successful_path = []
            self.gui.set_word_list_display('', '')
            self.__set_word_button()

            # Restarts timer
            self.gui.update_timer('')
            self.gui.update_timer(DEFULT_TIME)

    def __check_moves(self):
        """
            This method checks the possible moves for the player at the current
            point in the game.
            It returns a list of all possible moves.
            """
        if self.__curr_path == []:
            # The first move
            return []

        last_tup = self.__curr_path[-1]
        # the last letter chosen

        moves = ut.creats_square(last_tup[0], last_tup[1], len(self.__board))
        # The allowed next moves

        return moves

    def __set_letter_func(self, key):
        """
           This is a nested function, it creates a function that is used
           to handle the behavior of clicking a letter button.
           If the current path is empty, it adds the letter to the current
           word and path, and updates the possible moves.
           If the letter is not in the current path and is a possible move,
           it adds the letter to the current word and path,
           and updates the possible moves.
           """

        def wrapper():
            if self.__curr_path == []:
                # the First letter

                # Adding the letter
                self.__curr_word += self.__board[key[0]][key[1]]
                self.gui.set_word_display(self.__curr_word)

                # Adding path
                self.__curr_path.append(key)

                # Adding next possible moves
                self.__possible_moves = self.__check_moves()


            elif key not in self.__curr_path:
                # Checks tht wasn't already preset

                if key in self.__possible_moves:
                    # Checks that is allowed

                    # Adding the letter
                    self.__curr_word += self.__board[key[0]][key[1]]
                    self.gui.set_word_display(self.__curr_word)

                    # Adding path
                    self.__curr_path.append(key)

                    # Adding next possible moves
                    self.__possible_moves = self.__check_moves()

        return wrapper

    def __set_letter(self):
        """This function sets the letter function for each letter button.
        The function assigns the  result (a function of calling
            __set_letter_func()
        to each key in the button dictionary."""

        bott_dict = self.gui.get_button_dict()
        # a dict with all the buttons

        for key in bott_dict:
            if isinstance(key, tuple):
                # Checks that only the letter buttons.
                # The letter buttons are saved as (i,j)

                self.gui.set_letter_func(key, self.__set_letter_func(key))
                # calls and sets function

    def __set_word_button(self):
        """This function sets the submit, clear, and delete button
        functions for the GUI."""

        self.gui.set_submit(self.__set_submit_func)
        # Set submit

        self.gui.set_clear(self.__set_clear_func)
        # Set Clear

        self.gui.set_delete(self.__set_delete_func)
        # Set Delete

    def __set_submit_func(self):
        """This function first checks if the current path forms a valid word
        using the ut.is_valid_path method, and if it is a valid word,
        it adds the word to the successful path and word list,
        updates the score,
        and plays a sound. It then clears the current word and path."""

        word = ut.is_valid_path(self.__board, self.__curr_path, self.__words)
        # Checks if the word is a valid word
        # will return the word if is , else will return None

        if word is not None:
            # Thw word is valid

            if self.__curr_path not in self.__successful_path:
                # Checks that the word was not done already

                # Updates word list
                self.gui.set_word_list_display(word, 'ADD')

                # Updates score
                self.__score += len(word) ** 2
                self.gui.set_score_display(self.__score)

                # Saves path
                self.__successful_path.append(self.__curr_path[:])

                # Plays a sound
                self.gui.play_sound()

        # Restart current word
        self.__set_clear_func()

    def __set_clear_func(self):
        """This function clears the current word and path if the
            current path is not empty."""

        # restarts word
        self.__curr_word = ''
        self.gui.set_word_display(self.__curr_word)

        # restarts path
        self.__curr_path = []
        self.__possible_moves = []

    def __set_delete_func(self):
        """This function deletes the last character of the current
        word and removes the last
        element from the current path and updates the possible moves
        if the current path is not empty."""


        if self.__curr_path != []:
            # checks that the word is not empty


            self.__curr_word = self.__curr_word[:-1]
            # Removes a letter

            self.gui.set_word_display(self.__curr_word)
            # Updates display

            self.__curr_path.pop()
            # Removes path

            self.__possible_moves = self.__check_moves()
            # Updates next moves


def main():
    """This function creates an instance of the Controller class
        and runs the GUI by calling the run method on the gui attribute
        of the Controller instance."""

    runner = Controller()
    # Creates a object controller

    runner.gui.run()
    # Runs the game


if __name__ == '__main__':

    filename = sys.argv[0]
    # Receives from terminal

    if filename == 'boggle.py':
        # Checks if this games

        main()
        # runs the game
