from search import Problem


class solitaire(Problem):
    def __init__(self,board):
        super(self,board)
    def actions(self,state):
        pass
    def result(self,state,action):
        pass
    def goal_test(self,state):
        pass

    def path_cost(self, c, state1, action, state2):
        pass

    def h(self, node):
        """Needed for informed search."""
        pass


class sol_state:
    def __init__(self,board):
        self.board=board

    # for A*, this < other_state
    def __lt__(self, other):
        pass


def board_moves(board):
    pass
def board_perform_move(board,move):
    pass


# CODIGO DADO

# TAI content
def c_peg ():
 return "O"
def c_empty ():
 return "_"
def c_blocked ():
 return "X"
def is_empty (e):
 return e == c_empty()
def is_peg (e):
 return e == c_peg()
def is_blocked (e):
 return e == c_blocked()

# TAI pos
# Tuplo (l, c)
def make_pos (l, c):
 return (l, c)
def pos_l (pos):
 return pos[0]
def pos_c (pos):
 return pos[1]

# TAI move
# Lista [p_initial, p_final]
def make_move (i, f):
 return [i, f]
def move_initial (move):
 return move[0]
def move_final (move):
 return move[1]



if __name__=="__main__":
    # For testing
    b1 = [["_", "O", "O", "O", "_"], ["O", "_", "O", "_", "O"], ["_", "O", "_", "O", "_"],["O", "_", "O", "_", "_"], ["_", "O", "_", "_", "_"]]