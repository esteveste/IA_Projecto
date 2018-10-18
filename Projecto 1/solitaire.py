from search import Problem

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

# estrura de dados board
def get_board_size(board):
    return (len(board),len(board[0]))
# def get_piece(board,)


class solitaire(Problem):
    def __init__(self,board):
        # super(self,board)
        super().__init__(board)
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
    col_nr,line_nr=get_board_size(board)

    total_moves=[]
    for i in range(line_nr):
        for j in range(col_nr):
            #verifica comer para cima

            piece = board[i][j]

            if i>=2 and is_peg(board[i][j]) and is_peg(board[i - 1][j]) and is_empty(board[i - 2][j]):
                total_moves.append(make_move(make_pos(i,j),make_pos(i-2,j)))

            # comer para baixo
            if i<line_nr-2 and is_peg(board[i][j]) and is_peg(board[i + 1][j]) and is_empty(board[i + 2][j]):
                total_moves.append(make_move(make_pos(i,j),make_pos(i+2,j)))
            #comer para esquerda
            if j>=2 and is_peg(board[i][j]) and is_peg(board[i][j-1]) and is_empty(board[i][j-2]):
                total_moves.append(make_move(make_pos(i,j),make_pos(i,j-2)))
            #direita
            if j<col_nr-2 and is_peg(board[i][j]) and is_peg(board[i][j+1]) and is_empty(board[i][j+2]):
                total_moves.append(make_move(make_pos(i,j),make_pos(i,j+2)))

    return total_moves


def board_perform_move(board,move):
    pass




if __name__=="__main__":
    # For testing
    b1 = [["_", "O", "O", "O", "_"],
          ["O", "_", "O", "_", "O"],
          ["_", "O", "_", "O", "_"],
          ["O", "_", "O", "_", "_"],
          ["_", "O", "_", "_", "_"]]