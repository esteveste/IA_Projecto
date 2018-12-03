from search import *
from solitaire import *

t1 = [["_","O","O","O","_"], ["O","_","O","_","O"], ["_","O","_","O","_"], ["O","_","O","_","_"],["_","O","_","_","_"]]
t2 = [["O","O","O","X"], ["O","O","O","O"], ["O","_","O","O"], ["O","O","O","O"]]
t3 = [["O","O","O","X","X"], ["O","O","O","O","O"], ["O","_","O","_","O"], ["O","O","O","O","O"]] 
t4 = [["O","O","O","X","X","X"], ["O","_","O","O","O","O"], ["O","O","O","O","O","O"], ["O","O","O","O","O","O"]] 


def greedy_search(problem, h=None):
    """f(n) = h(n)"""
    h = memoize(h or problem.h, 'h')
    return best_first_graph_search(problem, h)

def compare_merdas():
    """Prints a table of search results."""
    compare_searchers(problems=[solitaire(t1),
                                solitaire(t2),
                                solitaire(t3),
                                #solitaire(t4)
],
                      header=['Searcher', 't1',
                              't2', 't3', 't4'],
    				   searchers=[depth_first_tree_search,
                                 greedy_search,
                                 astar_search])


compare_merdas()
    
