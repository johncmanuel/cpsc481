from games import *


class GameOfNim(Game):

    def __init__(self, board: list[int]):
        self.board = board
        self.moves = []
        self.initial = GameState(to_move="MAX", utility=0, board=board, moves=self.moves)

    # create new state as result of an action
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
