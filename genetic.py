import random
import math
class Genetic() :

    def __init__(self, problem,mutattionRate,endCondition,populationSize,nc):
        self.problem = problem
        self.path = []
        self.mutattionRate = mutattionRate
        self.endCondition = endCondition
        self.populationSize = populationSize
        self.population = self.problem.genPop(self.populationSize)
        self.parents = []
        self.child = []
        self.values = []
        self.iterateNum = 0
        self.bests = []
        self.worste = []
        self.average = []
        self.nc = nc

        self.childValues = []


    def geneticAlgorithm1(self):
        """
        :return: the best neighbor for current state
        """
        nPop = []
        self.iterateNum = 0
        flag = True
        while (self.iterateNum <= self.endCondition and flag ) :
            # print(iterateNum)
            self.values = []
            # print(len(self.population))
            self.values = self.problem.values(self.population)
            if (self.problem.goalTest(self.values)) :
                flag = False
            val = self.values
            max2 = max(self.values)
            min2 = min(self.values)
            # print(self.values,max2,min2)
            self.bests.append(max2)
            self.worste.append(min2)
            sum = 0
            for i in self.values :

                if i > 0 :
                    sum = sum + i
            self.average.append(sum/len(self.values))

            self.selectParents()
            self.makeChild()
            self.mutation()


            self.childValues = self.problem.values(self.child)

            for n,i in enumerate(self.population ):
                # print(self.values)
                nPop.append([i,self.values[n]])
            for n,i in enumerate(self.child ):
                nPop.append([i,self.childValues[n]])

            sortedPopulation = sorted(nPop, key=lambda m: m[1],reverse=True)
            self.population = self.nextGeneration(sortedPopulation)
            self.iterateNum = self.iterateNum + 1

        # val = self.problem.values(self.population)
        bestInThisPopulation = []
        max1 = -1000
        for n,i in enumerate(val) :
            if  i > max1 :
                max1 = i
                bestInThisPopulation = [self.population[n],max1]

        return bestInThisPopulation

    def nextGeneration(self,sp):
        nextGeneration = []
        # s = math.ceil(self.populationSize/2)

        for i in range(self.populationSize) :
            # print(len(sp))
            nextGeneration.append(sp[i][0])
            # sp.remove(sp[i])
        # for i in range(self.populationSize - s) :
        #     nextGeneration.append(random.choice(sp)[0])
        return nextGeneration


    def mutation(self):
        """
        :param start: start state
        :return: path to goal state
        """
        for i in range(self.mutattionRate) :
            whichChild = random.randint(0,len(self.child) - 1)
            whichFeatures = random.randint(0,9)
            # print(self.child[whichChild][whichFeatures],self.child[whichChild])
            if self.child[whichChild][whichFeatures] == 0 :
                self.child[whichChild][whichFeatures] = 1
            else :
                self.child[whichChild][whichFeatures] = 0


        return

    def makeChild(self):
        """
        :param start: start state
        :return: path to goal state
        """
        while (len(self.child) < self.nc):
            x = random.randint(0, len(self.parents) - 1)
            y = random.randint(0, len(self.parents) - 1)
            if x != y:
                newChild = self.parents[x][0:5] + self.parents[y][5:10]
                self.child.append(newChild)

        return

    def selectParents(self):
        """
        :param start: start state
        :return: path to goal state
        """
        parentsSize = math.ceil(self.populationSize / 2)
        for i in range(parentsSize):
            m = random.randint(0, len(self.population) - 1)
            self.parents.append(self.population[m])

        return
