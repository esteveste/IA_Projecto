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


# def get_piece(board,)


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
        return is_goal_state(state.board)
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
        # return True

    def calculate_heuristic(self):

        line_nr,col_nr  = get_board_size(self.board)

        # count until next piece

        total_heuristic = 0
        count_pieces = 0
        # center_heuristic=0

        for i in range(line_nr):

            line_heuristic = 0
            found_piece = False

            for j in range(col_nr):
                if is_peg(self.board[i][j]):

                    # count_pieces+=1
                    # center_heuristic+= abs((i-line_nr/2)+(j-col_nr/2))
                    if (found_piece):
                        total_heuristic += line_heuristic
                        line_heuristic = 1
                    else:
                        found_piece = True
                        line_heuristic += 1
        #
        for i in range(line_nr):

            line_heuristic = 0
            found_piece = False

            for j in range(col_nr):
                if is_peg(self.board[i][j]):
                    if (found_piece):
                        total_heuristic += line_heuristic
                        line_heuristic = 1
                    else:
                        found_piece = True
                        line_heuristic += 1

        # peg_isolada = 0
        # for i in range(line_nr):
        #
        #     for j in range(col_nr):
        #         if is_peg(self.board[i][j]):
        #             count_pieces += 1
        #             if (i == 0 or not is_peg(self.board[i - 1][j])) and (
        #                     i == line_nr-1 or not is_peg(self.board[i + 1][j])) and (
        #                     j == 0 or not is_peg(self.board[i][j - 1])) and (
        #                     j == col_nr-1 or not is_peg(self.board[i][j + 1])):
        #                 peg_isolada += 1
        distance_h=0
        l=[]
        for i in range(line_nr):
            for j in range(col_nr):
                if is_peg(self.board[i][j]):
                    count_pieces+=1
                    for ii in range(line_nr):
                        for jj in range(col_nr):
                            if  is_peg(self.board[ii][jj]):
                                distance_h+=abs(i-ii)+abs(j-jj)

        # ManHatan distance
        self.nr_pieces = count_pieces
        # return (count_pieces, count_pieces-1 + peg_isolada)
        return (count_pieces,len(board_moves(self.board))+count_pieces+distance_h/ (2 * count_pieces))


def board_moves(board):
    line_nr,col_nr = get_board_size(board)

    total_moves = []
    for i in range(line_nr):
        for j in range(col_nr):
            # verifica comer para cima
            if (is_peg(board[i][j])):

                if i >= 2 and is_peg(board[i - 1][j]) and is_empty(board[i - 2][j]):
                    total_moves.append(make_move(make_pos(i, j), make_pos(i - 2, j)))

                # comer para baixo
                if i < line_nr - 2 and is_peg(board[i + 1][j]) and is_empty(board[i + 2][j]):
                    total_moves.append(make_move(make_pos(i, j), make_pos(i + 2, j)))
                # comer para esquerda
                if j >= 2 and is_peg(board[i][j - 1]) and is_empty(board[i][j - 2]):
                    total_moves.append(make_move(make_pos(i, j), make_pos(i, j - 2)))
                # direita
                if j < col_nr - 2 and is_peg(board[i][j + 1]) and is_empty(board[i][j + 2]):
                    total_moves.append(make_move(make_pos(i, j), make_pos(i, j + 2)))

    return total_moves


def board_perform_move(board, move):
    new_board = deepcopy(board)  # clone board (could be optim)
    new_board[move[0][0]][move[0][1]] = c_empty()
    new_board[move[1][0]][move[1][1]] = c_peg()
    if (move[0][0] != move[1][0]):
        # ent movemos para cima ou baixo
        midle_jump = 1 if move[0][0] < move[1][0] else -1
        new_board[move[0][0] + midle_jump][move[0][1]] = c_empty()
    else:
        # ent movemos para esquerda ou direita
        midle_jump = 1 if move[0][1] < move[1][1] else -1
        new_board[move[0][0]][move[0][1] + midle_jump] = c_empty()
    return new_board


def is_goal_state(board):
    # returns True if board in final state
    line_nr,col_nr  = get_board_size(board)
    peg_nr = 0
    for i in range(line_nr):
        for j in range(col_nr):
            if is_peg(board[i][j]):
                peg_nr += 1
    return peg_nr == 1

# if __name__=="__main__":
#     # For testing
# b1 = [["_", "O", "O", "O", "_","_", "O", "O", "O", "_"],
#       ["O", "_", "O", "_", "O","O", "X", "O", "_", "_"],
#       ["_", "O", "_", "O", "O","O", "X", "O", "_", "_"],
#       ["O", "X", "O", "_", "_","_", "O", "O", "O", "_"],
#       ["_", "O", "_", "_", "_","_", "X", "_", "_", "_"]]
