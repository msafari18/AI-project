import random
import math
class Problem3:

    def __init__(self,mutationRate,endCondition):
        self.mutationRate = mutationRate
        self.endCondition = endCondition
        self.populationSize = 0
        self.state = []
        self.allV = []

    def genPop(self,populationSize):
         population = []
         self.populationSize = populationSize
         for i in range(0,populationSize) :
            p = [random.randint(0,1) for x in range(10)]
            population.append(p) 
         return  population


    def values(self,popultion):

        values = []
        secval = 0

        for i in popultion :
            left = 0
            right = 0
            secval = 0
            for j in range(9) :
                # print(i[j])
                if i[j] == 0 :
                    left = left + 1
                if i[j] == 1 :
                    right = right + 1
            firstval = abs(right - left)
            # print ("ddd",i)
            if i[1] != i[7]:
                secval = secval + 1
            if i[0] != i[8]:
                secval = secval + 1
            if i[5] != i[4]:
                secval = secval + 1
            if i[2] != i[4]:
                secval = secval + 1
            if i[8] != i[0]:
                secval = secval + 1
            if i[7] != i[0]:
                secval = secval + 1
            if i[3] != i[4]:
                secval = secval + 1
            if i[0] != i[9]:
                secval = secval + 1
            values.append(secval - firstval)
            # if secval - firstval < 0 :
                # print(secval - firstval , secval , firstval)
                # print(i)
        if len(values) == self.populationSize :
            self.allV.append(values)

        return values

    def goalTest(self,values):
        for i in values :
            if i == 7 :
                return True

        return False
