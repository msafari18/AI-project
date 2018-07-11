import random


class healClimbingRandom:

    def __init__(self, problem):
        self.problem = problem
        self.visited = 0
        self.extend = 0
        self.bestAns = []
        self.value = 0

    def RNeighbor(self, currentSol):
        """
        :param currentSol : current state
        :return: a random neighbor which is better than current state
        """
        currValue = self.problem.value(currentSol)
        bestNeighbors = []
        for i in self.problem.neighbors(currentSol):
            self.visited = self.visited + 1
            if (self.problem.value(i) > currValue ):
                bestNeighbors.append(i)

        if not bestNeighbors :
            return bestNeighbors

        return random.choice(bestNeighbors)

    def healClimbingRAlgorithm(self, start):
        """
        :param start: start state
        :return: path to goal state
        """
        path = []
        currentState = start


        while (True):
            self.extend = self.extend + 1
            path.append(currentState)
            if not self.RNeighbor(currentState):
                self.bestAns = currentState[:]
                self.value = self.problem.value(currentState)
                return path

            currentState = self.RNeighbor(currentState)

        return path
