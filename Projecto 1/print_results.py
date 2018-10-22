from solitaire import *
from os import walk
from search import (Problem, depth_limited_search, breadth_first_search, depth_first_tree_search,
                    astar_search, greedy_best_first_graph_search)
import timeit
from utils import print_table

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


# Directory Format
# |- yourProject.py
# |- search.py
# |- utils.py
# |- print_results.py
# |- tests
#     |- test01
#         |- input
#         |- output
#     etc

board = [["X", "X", "O", "O", "O", "O", "O", "X", "X"],
         ["X", "X", "O", "O", "O", "O", "O", "X", "X"],
         ["O", "O", "O", "O", "O", "O", "O", "O", "O"],
         ["O", "O", "O", "O", "O", "O", "O", "O", "O"],
         ["O", "O", "O", "O", "_", "O", "O", "O", "O"],
         ["O", "O", "O", "O", "O", "O", "O", "O", "O"],
         ["O", "O", "O", "O", "O", "O", "O", "O", "O"],
         ["X", "X", "O", "O", "O", "O", "O", "X", "X"],
         ["X", "X", "O", "O", "O", "O", "O", "X", "X"]]

small_board = [["X", "X", "O", "O"],
               ["X", "X", "O", "O"],
               ["O", "O", "O", "_"],
               ["O", "O", "O", "O"]]

rect_small_board = [["X", "X", "O", "O"],
                    ["X", "X", "O", "O"],
                    ["O", "O", "O", "_"],
                    ["O", "O", "O", "O"],
                    ["X", "X", "O", "O"],
                    ["X", "X", "O", "O"]]

board1 = [["_", "O", "O", "O", "_"],
          ["O", "_", "O", "_", "O"],
          ["_", "O", "_", "O", "_"],
          ["O", "_", "O", "_", "_"],
          ["_", "O", "_", "_", "_"]]

board2 = [["O", "O", "O", "X"],
          ["O", "O", "O", "O"],
          ["O", "_", "O", "O"],
          ["O", "O", "O", "O"]]


board3 = [["O", "O", "O", "X", "X"],
          ["O", "O", "O", "O", "O"],
          ["O", "_", "O", "_", "O"],
          ["O", "O", "O", "O", "O"]]

board4 = [["O", "O", "O", "X", "X", "X"],
          ["O", "_", "O", "O", "O", "O"],
          ["O", "O", "O", "O", "O", "O"],
          ["O", "O", "O", "O", "O", "O"]]


def main():
    mooshakTests("tests") # tests is the directory name

    test_dic = test_algorithms(board3, astar=True,greedy=True,depth=True)
    print_results_table(test_dic)


def xx_invalid_solution(a, b):
    return False


def greedy_search(solitaire):
    greedy_best_first_graph_search(solitaire, solitaire.h)

# -------------------------------
#  Test Multiple Search:
#  Greedy
#  Depth
#  A*
# -------------------------------


def test_algorithms(board, greedy=False, depth=False, astar=False):
    greedy_game = solitaire(board)
    depth_game = solitaire(board)
    astar_game = solitaire(board)

    start_time, greedy_time, depth_time, astar_time = 0, 0, 0, 0

    if greedy:
        start_time = timeit.default_timer()
        greedy_best_first_graph_search(greedy_game, greedy_game.h)
        greedy_time = round(timeit.default_timer() - start_time, 3)
    if depth:
        start_time = timeit.default_timer()
        depth_limited_search(depth_game)
        depth_time = round(timeit.default_timer() - start_time, 3)
    if astar:
        start_time = timeit.default_timer()
        astar_search(astar_game, astar_game.h)
        astar_time = round(timeit.default_timer() - start_time, 3)

    result_dic = {"greedy": {
        "game": greedy_game,
        "exe": ("N", "Y")[greedy],
        "time": greedy_time
    },
        "depth": {
        "game": depth_game,
        "exe": ("N", "Y")[depth],
        "time": depth_time
    },
        "astar": {
        "game": astar_game,
        "exe": ("N", "Y")[astar],
        "time": astar_time
    }
    }
    return result_dic


# -------------------------------
# End Search tests
# -------------------------------

def print_results_table(test_dic):
    headers = ("Algorithm", "Executed", "Time", "Generated", "Expanded")
    data = []
    for i in test_dic:
        lst = []
        # Edit as you like :)
        lst.append(i)
        lst.append(test_dic[i]["exe"])
        lst.append(str(test_dic[i]["time"]))
        # lst.append(str(test_dic[i]["game"].n_generated_nodes))
        # lst.append(str(test_dic[i]["game"].n_expanded_nodes))

        data += [lst]

    table = [headers] + data

    print("")
    for i, d in enumerate(table):
        line = '| '.join(str(x).ljust(10) for x in d)
        print(line)
        if i == 0:
            print('-' * len(line))


# -------------------------------
#  Mooshak Tests
#  tests_dir - tests directory name
# -------------------------------


def mooshakTests(tests_dir):
    inputFiles = []
    outputFiles = []
    for (dirpath, dirnames, filenames) in walk(tests_dir):
        for i in range(len(dirnames)):
            for (dpt, drn, iofiles) in walk(dirpath + "/" + dirnames[i]):
                new_inputfile = [dirpath + "/" + dirnames[i] +
                                 "/" + s for s in iofiles if s == "input"]
                new_outputfile = [dirpath + "/" + dirnames[i] +
                                  "/" + s for s in iofiles if s == "output"]
                inputFiles.extend(new_inputfile)
                outputFiles.extend(new_outputfile)
        break
    print(inputFiles)

    for i in range(len(inputFiles)):
        inputFile = open(inputFiles[i], "r")
        outputFile = open(outputFiles[i], "r")

        print(f"Test {inputFiles[i]}\n")

        content = inputFile.read()
        exec(content)
        print(outputFile.read())

        inputFile.close()
        outputFile.close()


if __name__ == "__main__":
    main()
    print("\nMemory use:\n")
    snapshot = tracemalloc.take_snapshot()
    display_top(snapshot)
