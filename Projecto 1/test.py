from solitaire import *
from search import *

from collections import Counter
import linecache
import os
import tracemalloc


def display_top(snapshot, key_type='lineno', limit=10):
    snapshot = snapshot.filter_traces((
        tracemalloc.Filter(False, "<frozen importlib._bootstrap>"),
        tracemalloc.Filter(False, "<unknown>"),
    ))
    top_stats = snapshot.statistics(key_type)

    print("Top %s lines" % limit)
    for index, stat in enumerate(top_stats[:limit], 1):
        frame = stat.traceback[0]
        # replace "/path/to/module/file.py" with "module/file.py"
        filename = os.sep.join(frame.filename.split(os.sep)[-2:])
        print("#%s: %s:%s: %.1f KiB"
              % (index, filename, frame.lineno, stat.size / 1024))
        line = linecache.getline(frame.filename, frame.lineno).strip()
        if line:
            print('    %s' % line)

    other = top_stats[limit:]
    if other:
        size = sum(stat.size for stat in other)
        print("%s other: %.1f KiB" % (len(other), size / 1024))
    total = sum(stat.size for stat in top_stats)
    print("Total allocated size: %.1f KiB" % (total / 1024))


tracemalloc.start()

b1 = [["_", "O", "O", "O", "_"],
      ["O", "_", "O", "_", "O"],
      ["_", "O", "_", "O", "_"],
      ["O", "_", "O", "_", "_"],
      ["_", "O", "_", "_", "_"]]


b2 = [["_", "O", "O", "O", "_","_", "_"],
      ["O", "_", "O", "_", "O","O", "X"],
      ["_", "O", "_", "O", "O","O", "X"],
      ["O", "X", "O", "_", "_","_", "_"],
      ["_", "O", "_", "_", "_","_", "X"]]

# b1=[["X","X","O","O","O","O","O","X","X"],
#      ["X","X","O","O","O","O","O","X","X"],
#      ["O","O","O","O","O","O","O","O","O"],
#      ["O","O","O","O","O","O","O","O","O"],
#      ["O","O","O","O","_","O","O","O","O"],
#      ["O","O","O","O","O","O","O","O","O"],
#      ["O","O","O","O","O","O","O","O","O"],
#      ["X","X","O","O","O","O","O","X","X"],
#      ["X","X","O","O","O","O","O","X","X"]]

#
# b2=[["O","O","O","X","X","X"],
#  ["O","_","O","O","O","O"],
#  ["O","O","O","O","O","O"],
#  ["O","O","O","O","O","O"]]
board4 = [["O", "O", "O", "X", "X", "X"],
          ["O", "_", "O", "O", "O", "O"],
          ["O", "O", "O", "O", "O", "O"],
          ["O", "O", "O", "O", "O", "O"]]
compare_searchers([solitaire(b2),solitaire(board4)],["Algoritms","Board","B2"],searchers=[
    # breadth_first_tree_search,
    #                              breadth_first_search,
    #                              depth_first_graph_search,
    #                              iterative_deepening_search,
    #                              depth_limited_search,
    #                              recursive_best_first_search,
                                 astar_search])

print("\nMemory use:\n")
snapshot = tracemalloc.take_snapshot()
display_top(snapshot)

