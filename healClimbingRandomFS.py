import random


class healClimbingRandomFS:
    def __init__(self, problem):

        self.problem = problem
        self.visited = 0
        self.extend = 0
        self.bestAns = []
        self.value = 0

    def FSNeighbor(self, currentSol):
        """
        :param currentSol : current state
        :return: the first neighbor which is better than current state
        """

        currValue = self.problem.value(currentSol)
        bestNeighbors = []
        for i in self.problem.neighbors(currentSol):
            self.visited = self.visited + 1
            if (self.problem.value(i) > currValue):
                return i

        return bestNeighbors


    def healClimbingFS(self, start):
        """
        :param start: start state
        :return: path to goal state
        """
        path = []
        currentState = start

        while (True):
            self.extend = self.extend + 1
            path.append(currentState)
            if not self.FSNeighbor(currentState):
                self.bestAns = currentState [:]
                self.value = self.problem.value(currentState)
                return path

            currentState = self.FSNeighbor(currentState)

        return path
