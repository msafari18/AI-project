class healClimbing:

    def __init__(self, problem):
        self.problem = problem
        self.path = []
        self.visited = 0
        self.extend = 0
        self.bestAns = []
        self.value = 0

    def bestNeighbor(self,currentSol):
        """
        :param currentSol : current state
        :return: the best neighbor for current state
        """
        maxValue = self.problem.value(currentSol)
        bestNeighbor = []
        for i in self.problem.neighbors(currentSol):
            self.visited = self.visited + 1
            if (self.problem.value(i) > maxValue) :

                maxValue = self.problem.value(i)
                bestNeighbor = i

        # self.visited = self.visited + len(self.problem.neighbors(currentSol))
        # print(bestNeighbor)
        return bestNeighbor

    def healClimbingAlgorithm(self, start):
        """
        :param start: start state
        :return: path to goal state
        """
        path = []
        currentState = start

        while (True) :
            self.extend = self.extend + 1
            path.append(currentState)
            if not self.bestNeighbor(currentState) :
                self.value = self.problem.value(currentState)
                self.bestAns = currentState[:]

                return path


            currentState = self.bestNeighbor(currentState)[:]


        # return path
