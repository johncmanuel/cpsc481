from games import *


class GameOfNim(Game):

    def __init__(self, board: list[int]):
        self.board = board
        self.moves = self.make_moves(board)
        self.initial = GameState(to_move="MAX", utility=0, board=board, moves=self.moves)

    # create new state as result of an action
    # this assumes its a valid move, so no need to check
    def result(self, state, move: tuple[int, int]):
        state[move[0]] -= move[1]
        return state

    # action: (r, n) where r = row num and n = number of objs to remove
    def actions(self, state):
        return state.moves

    def terminal_test(self, state):
        """A state is terminal if there are no objects left"""
        return state.board == [0, 0, 0, 0]

    def utility(self, state, player):
        """Return the value to player; 1 for win, -1 for loss, 0 otherwise."""
        pass

    def display(self, state):
        board = state.board
        print("board: ", board)

    # generate all possible moves for a given state
    def make_moves(self, board: list[int]):
        return [(i, j) for i in range(1, len(board)) for j in range(1, board[i] + 1)]


if __name__ == "__main__":
    nim = GameOfNim(board=[0, 5, 3, 1])  # Creating the game instance
    # nim = GameOfNim(board=[7, 5, 3, 1]) # a much larger tree to search
    # print(nim.initial.board) # must be [0, 5, 3, 1]
    # print(nim.initial.moves) # must be [(1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (2,1), (2, 2), (2, 3), (3, 1)]
    # print(nim.result(nim.initial, (1,3) ))
    # utility = nim.play_game(alpha_beta_player, query_player) # computer moves first
    # if (utility < 0):
    #     print("MIN won the game")
    # else:
    #     print("MAX won the game")
    #
