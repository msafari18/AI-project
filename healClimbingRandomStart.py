class healClimbing:

    def __init__(self, problem):
        self.problem = problem
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

        return bestNeighbor

    def healClimbingRS(self, start):
        """
        :param start: start state
        :return:
        """
        solution = []
        Lastsolution = []
        currentState = start
        m = 0
        while(not Lastsolution in solution and m < 15 ) :
            m = m + 1
            path = []
            solution.append(currentState)
            currentState = self.problem.generateStart()
            while (True) :
                self.extend = self.extend + 1
                if not self.bestNeighbor(currentState) :
                    Lastsolution = currentState

                    break

                path.append(currentState)
                currentState = self.bestNeighbor(currentState)

        self.bestAns = Lastsolution[:]
        self.value = self.problem.value(Lastsolution)
        return solution
