from search import *

eight_puzzle = EightPuzzle((1, 2, 3, 5, 7, 4, 8, 6, 0))

astar = astar_search(eight_puzzle, h=None, display=True).solution()

# dfs = depth_first_graph_search(eight_puzzle).solution()
# print("dfs", dfs)
bfs = breadth_first_graph_search(eight_puzzle).solution()
print("bfs", bfs)
# print("astar", astar)
