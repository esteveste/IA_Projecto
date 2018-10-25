from search import Problem
from copy import deepcopy
import math


# CODIGO DADO

# TAI content
def c_peg():
    return "O"


def c_empty():
    return "_"


def c_blocked():
    return "X"


def is_empty(e):
    return e == c_empty()


def is_peg(e):
    return e == c_peg()


def is_blocked(e):
    return e == c_blocked()


# TAI pos
# Tuplo (l, c)
def make_pos(l, c):
    return (l, c)


def pos_l(pos):
    return pos[0]


def pos_c(pos):
    return pos[1]


# TAI move
# Lista [p_initial, p_final]
def make_move(i, f):
    return [i, f]


def move_initial(move):
    return move[0]


def move_final(move):
    return move[1]


# estrura de dados board
def get_board_size(board):
    return (len(board), len(board[0]))



class solitaire(Problem):
    """Models a Solitaire problem as a satisfaction problem.
    A solution cannot have more than 1 peg left on the board."""

    def __init__(self, board):
        super().__init__(sol_state(board))

    def actions(self, state):
        return board_moves(state.board)

    def result(self, state, action):
        return sol_state(board_perform_move(state.board, action))

    def goal_test(self, state):
        return state.nr_pieces == 1
        # return False

    def path_cost(self, c, state1, action, state2):
        """All moves have same cost"""
        return c + 1

    def h(self, node):
        """Needed for informed search."""
        return node.state.h
        # return 0


class sol_state:
    def __init__(self, board):
        self.board = board
        self.nr_pieces, self.h = self.calculate_heuristic()

    # for A*, this < other_state
    def __lt__(self, other):
        return self.h > other.h
        # return self.nr_pieces > other.nr_pieces

    def calculate_heuristic(self):

        line_nr,col_nr  = get_board_size(self.board)

        count_pieces = 0
        distance_h=0
        # Manhatam distance + count peg

        for i in range(line_nr):
            for j in range(col_nr):
                if is_peg(self.board[i][j]):
                    count_pieces+=1
                    for ii in range(line_nr):
                        for jj in range(col_nr):
                            if  is_peg(self.board[ii][jj]):
                                distance_h+=abs(i-ii)+abs(j-jj)

        # pegs sem move
        peg_sem_move=0
        pieces = [i[0] for i in board_moves(self.board)]
        for i in range(line_nr):
            for j in range(col_nr):
                if is_peg(self.board[i][j]) and not make_pos(i,j) in pieces:
                    peg_sem_move+=1

        return (count_pieces, peg_sem_move+distance_h/ (2 * count_pieces))


def board_moves(board):
    line_nr,col_nr = get_board_size(board)

    total_moves = []
    for i in range(line_nr):
        for j in range(col_nr):

            if (is_peg(board[i][j])):
                # comer para esquerda
                if j >= 2 and is_peg(board[i][j - 1]) and is_empty(board[i][j - 2]):
                    total_moves.append(make_move(make_pos(i, j), make_pos(i, j - 2)))
                # verifica comer para cima
                if i >= 2 and is_peg(board[i - 1][j]) and is_empty(board[i - 2][j]):
                    total_moves.append(make_move(make_pos(i, j), make_pos(i - 2, j)))

                # direita
                if j < col_nr - 2 and is_peg(board[i][j + 1]) and is_empty(board[i][j + 2]):
                    total_moves.append(make_move(make_pos(i, j), make_pos(i, j + 2)))

                # comer para baixo
                if i < line_nr - 2 and is_peg(board[i + 1][j]) and is_empty(board[i + 2][j]):
                    total_moves.append(make_move(make_pos(i, j), make_pos(i + 2, j)))


    return total_moves


def board_perform_move(board, move):
    b_aux = deepcopy(board)

    i_l=pos_l(move_initial(move))
    i_c=pos_c(move_initial(move))
    f_l=pos_l(move_final(move))
    f_c=pos_c(move_final(move))

    b_aux[i_l][i_c] = c_empty()
    b_aux[f_l][f_c] = c_peg()

    b_aux[int((i_l+f_l)/2)][int((i_c+f_c)/2)] = c_empty()

    return b_aux

