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
        self.possible_actions = ["M", "C", "MC", "MM", "CC", "MMM", "CCC", "MMC", "MCC"]
        super().__init__(initial, goal)

    # return new state as result of an action
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
        print("state", state)
        # go through all posisble actions
        for a in self.possible_actions:
            print("action", a)
            numMiss, numCann = a.count("M"), a.count("C")
            if b:
                mLeft, cLeft = m - numMiss, c - numCann
            else:
                mLeft, cLeft = m + numMiss, c + numCann
            mRight, cRight = self.N1 - mLeft, self.N2 - cLeft
            print(
                "mLeft",
                mLeft,
                "cLeft",
                cLeft,
                "|",
                "mRight",
                mRight,
                "cRight",
                cRight,
            )
            # check for negative values and if missionaries are outnumbered by cannibals
            if (
                (mLeft >= 0 and cLeft >= 0 and mRight >= 0 and cRight >= 0)
                and (mLeft == 0 or mLeft >= cLeft)
                and (mRight == 0 or mRight >= cRight)
            ):
                print("added", a)
                actions.append(a)
            print("valid actions", actions)
        return actions


if __name__ == "__main__":
    mc = MissCannibalsVariant(4, 4)
    # mc = MissCannibalsVariant(3, 3)
    # print(mc.result((2, 2, False), "M"))
    # print(
    #     mc.actions((3, 3, True))
    # )  # Test your code as you develop! This should return ['MC', 'MMM']
    print(mc.actions((2, 2, False)))
    # path = depth_first_graph_search(mc).solution()
    # print("dfs", path)
    # path = breadth_first_graph_search(mc).solution()
    # print("bfs", path)
