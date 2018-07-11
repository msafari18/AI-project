import random
import math
import numpy as np

class SimulatedAnnealing :

    def __init__(self, problem):

        self.problem = problem
        self.visited = 0
        self.extend = 0
        self.bestAns = []
        self.value = 0


    def randomNeighbor(self,currentSol):
        """
        :param currentSol: current state
        :return: a random neighbor for current state
        """
        neighbor = self.problem.neighbors(currentSol)
        self.visited= self.visited + 1

        return neighbor[0]

    def acceptance_probability (self,oldCost,newCost,T) :
        """
        :param oldCost: old solution cost
        :param newCost: new solution cost
        :param T: temerature
        :return: a value that decrease depends on time and solution
        if the new solution is worse than the old solution it decreases
        """

        return (math.exp((newCost - oldCost) / T))


    def SimulatedAnnealingAlgorithm (self,start) :
        """
        :param start: start state
        :return: path to goal state
        """
        path = []
        sol =[]
        oldCost = self.problem.value(start)
        T = 1.0
        T_min = 0.0001
        # alpha = 0.9
        alpha = 0.001
        # alpha = 20

        currentSol = start[:]
        iterateNumber = 0
        while iterateNumber < 1000 and T > T_min :

            iterateNumber = iterateNumber + 1
            path.append([currentSol,oldCost])
            newSol = self.randomNeighbor(currentSol)[:]

            # print("hereeeee",newSol)
            newCost = self.problem.value(newSol)

            p = self.acceptance_probability(oldCost,newCost,T)
            r = random.random()
            # print(p,r,newCost,oldCost,newSol)
            # print()
            if p > r :
                # if( newCost > oldCost ) :
                print(newSol,'value :' , newCost)
                sol.append([newSol,newCost])
                self.extend  = self.extend + 1
                currentSol = newSol[:]
                oldCost = newCost

            # decrease T by passing time in every iterate
            T = T - alpha
            # T = T * alpha
        max = -1
        finalSol = []
        self.bestAns = currentSol
        self.value = self.problem.value(currentSol)


        return finalSol





