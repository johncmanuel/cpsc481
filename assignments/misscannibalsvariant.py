from search import *


class MissCannibalsVariant(Problem):
    """
    The problem of Missionaries and Cannibals.
    N1 and N2 are the total number of missionaries and cannibals starting from the
    left bank.

    A state is represented as a 3-tuple, two numbers and a boolean:
    state[0] is the number of missionaries on the left bank (note: the number of
    missionaries on the right bank is N1-m)

    state[1] is the number of cannibals on the left bank (note: the number of
    cannibals on the right bank is N2-c)

    state[2] is true if boat is at the left bank, false if at the right bank

    boat capacity is 3
    """

    def __init__(self, N1=4, N2=4, goal=(0, 0, False)):
        initial = (N1, N2, True)
        self.N1 = N1
        self.N2 = N2
        # assumes boat capacity is 3, so number of possible actions is 3^2 -> 9
        self.possible_actions = ["M", "C", "MC", "MM", "CC", "MMM", "CCC", "MCM", "MCC"]
        super().__init__(initial, goal)

    # return new state as result of an action
    # TODO: account for cases when n1 or n2 exceeds boat capac or below 0
    def result(
        self, state: tuple[int, int, bool], action: str
    ) -> tuple[int, int, bool]:
        m, c, b = state
        numMiss, numCann = action.count("M"), action.count("C")
        # add missionaries and/or cannibals if going back to left bank
        return (
            (max(m - numMiss, 0), max(c - numCann, 0), not b)
            if b
            else (min(m + numMiss, self.N1), min(c + numCann, self.N2), not b)
        )

    # Should return list of actions
    def actions(self, state: tuple[int, int, bool]) -> list[str]:
        (
            m,
            c,
            b,
        ) = state
        actions = []
        # go through all posisble actions
        for a in self.possible_actions:
            numMiss, numCann = a.count("M"), a.count("C")
            if b:
                newM, newC = m - numMiss, c - numCann
            else:
                newM, newC = m + numMiss, c + numCann
            if (
                (newM >= 0 and newC >= 0)
                and (newM == 0 or newM >= newC)
                and ((self.N1 - newM == 0 or self.N1 - newM >= self.N2 - newC))
            ):
                actions.append(a)
        print("actions at state", state, ":", actions)
        return actions


if __name__ == "__main__":
    mc = MissCannibalsVariant(4, 4)
    print(mc.result((2, 2, False), "M"))
    print(
        mc.actions((3, 3, True))
    )  # Test your code as you develop! This should return ['MC', 'MMM']
    path = depth_first_graph_search(mc).solution()
    print("dfs", path)
    path = breadth_first_graph_search(mc).solution()
    print("bfs", path)
