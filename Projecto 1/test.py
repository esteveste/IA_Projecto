from solitaire import *
from search import *
b1 = [["_", "O", "O", "O", "_"],
      ["O", "_", "O", "_", "O"],
      ["_", "O", "_", "O", "_"],
      ["O", "_", "O", "_", "_"],
      ["_", "O", "_", "_", "_"]]

compare_searchers([Solitaire(b1)],"IA",searchers=[breadth_first_tree_search,
                                 breadth_first_search,
                                 depth_first_graph_search,
                                 iterative_deepening_search,
                                 depth_limited_search,
                                 recursive_best_first_search])

