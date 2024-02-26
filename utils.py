##############################################################################
#                                   Imports                                  #
##############################################################################

from typing import Iterable
from typing import List, Tuple
from typing import Optional

#########################################################################
#                           Meseges
#########################################################################


##############################################################################
#                                  global                                    #
##############################################################################

Board = List[List[str]]
Path = List[Tuple[int, int]]


# Board = list[list[str]]
# Path = list[tuple[int, int]]


##############################################################################
#                                  Functions                                 #
##############################################################################


def opens_file(file_path):
    """this function opens a file path in a 'r' mode """
    with open(file_path, 'r') as file:
        f = file.readlines()
        return f


def create_word_set(file_path) -> dict:
    """this function creates a set of all the words from a given file """
    file = opens_file(file_path)
    word_set = set()
    for word in file:
        word = word.strip('\n')
        word_set.add(word)

    return word_set


def creats_sub_words_set(words: set) -> set:
    """ this function creates a set of all the sub words in the main set"""
    sub_set = set()
    for word in words:
        for i in range(1, len(word) + 1):
            sub_set.add(word[:i])
            # Adds all the sub words

    return sub_set


def legal_word(words, word) -> bool:
    """ this function returns True if a word is in the main set, else - False"""
    word_len = len(word)
    if word in words:
        # Checks if the word is in the dict in the right length
        return True
    return False


def in_board(path: Path, board_size: int) -> bool:
    """ this function receives a path and a board size, and returns True if the tuples in path are inside the board"""
    for tup in path:
        row, col = tup
        if 0 > row or row >= board_size or 0 > col or col >= board_size:
            # Checks that the tupele size is legal
            return False
    return True


def not_twice(path: list):
    for tup in path:
        times = path.count(tup)
        if times > 1:
            return False
    return True


def creats_square(row, col, board_size):
    """ this function creates a list of tuples, representing legal cells"""
    lst_sqr = []
    for r in range(row - 1, row + 2):
        for c in range(col - 1, col + 2):
            if 0 > r or r >= board_size or 0 > c or c >= board_size:
                # Checks that the tuple size is legal
                continue
            else:
                tup = (r, c)
                lst_sqr.append(tup)

    tup = (row, col)
    lst_sqr.remove(tup)
    return lst_sqr


def checks_next(tup: tuple, next_tup: tuple, board_size: int) -> bool:
    row, col = tup
    legal_moves = creats_square(row, col, board_size)
    if next_tup in legal_moves:
        return True
    return False


def legal_move(path, board_size):
    i = 0
    while i < len(path) - 1:
        if not checks_next(path[i], path[i + 1], board_size):
            return False
        i += 1
    return True


def legal_path(path, board_size) -> bool:
    if in_board(path, board_size) and not_twice(path):
        if legal_move(path, board_size):
            return True
    return False


def create_word(path, board) -> str:
    """ this function creates a word from a given path in the board"""
    word: str = ''
    for tup in path:
        row, col = tup
        letter: str = board[row][col]
        word += letter
    return word


def is_valid_path(board: Board, path: Path, words: Iterable[str]) -> Optional[
    str]:
    """
    this function receives a board, path, and a set of valid words,
     and returns the word if the path&word are valid

    """
    if legal_path(path, len(board)):
        # Checks that the path is legal (in the board, in a row )
        word = create_word(path, board)
        # The word from the board with the path
        if legal_word(words, word):
            return word
    return None


def _helper_find_length_n_paths(n, board, old_tup, sub_word, words, paths, move_lst, func):
    """
    this function is a helper for 2 functions. it uses backtracking approach,
     for finding all valid paths under different constraints
    """
    size = len(board)
    row, col = old_tup[0], old_tup[1]
    word = create_word(move_lst, board)

    if func == 'path':
        # Checks if it needs to count the amount of pathes
        if word in words and len(move_lst) == n:
            paths.append(move_lst[:])
            return paths

    elif func == 'words':
        # Checks if it needs to count the amount of words
        if word in words and len(word) == n:
            paths.append(move_lst[:])
            return paths

    pos_moves = creats_square(row, col, size)
    # creates
    for tup in pos_moves:
        if tup in move_lst:
            continue
        move_lst.append(tup)
        cur_word = create_word(move_lst, board)
        if cur_word not in sub_word:
            move_lst.pop()
            continue

        _helper_find_length_n_paths(n, board, tup, sub_word, words, paths,
                                    move_lst, func)

        move_lst.pop()


def find_length_n_paths(n: int, board: Board, words: Iterable[str]) -> List[
    Path]:
    """
    this function returns a list of all possible paths in length 'n'
    """
    if n == 0:
        return []

    sub_word = creats_sub_words_set(words)
    size = len(board)
    paths = []
    for row in range(size):
        for col in range(size):
            _helper_find_length_n_paths(n, board, (row, col), sub_word, words, paths, [(row, col)], 'path')
    return paths


def find_length_n_words(n: int, board: Board, words: Iterable[str]) -> List[
    Path]:
    """
    his function returns a list of all possible paths for a valid words in length 'n'
    """
    if n == 0:
        return []

    sub_word = creats_sub_words_set(words)
    size = len(board)
    paths = []
    for row in range(size):
        for col in range(size):
            _helper_find_length_n_paths(n, board, (row, col), sub_word, words,
                                        paths, [(row, col)], 'words')
    return paths


def max_score_paths(board: Board, words: Iterable[str]) -> List[Path]:
    """
    this function receives a board and a set of all valid words,
    and returns the max score path for each valid name in the board
    """
    word_dict = {}
    paths: list = []
    max_length_word = max(words, key=len)
    for i in range(len(max_length_word), 0, -1):
        word_path: list = find_length_n_paths(i, board, words)
        for path in word_path:
            word: str = create_word(path, board)
            if word not in word_dict:
                word_dict[word] = path
    return list(word_dict.values())
