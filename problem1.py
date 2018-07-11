import random


class Problem1:

    def __init__(self,graph,nodenum,numberOfColor):
        self.gragh = graph
        self.nodenum = nodenum
        self.numberOfColor = numberOfColor
        self.colorGraph = []

    def generateStart(self):

         colorG = [random.randint(1,int(self.numberOfColor)) for x in range(int(self.nodenum))]
         return  colorG

    def neighbors(self,currentSol):
        """
        :param currentSol : current state
        :return: the best neighbor for current state
        """
        neighbors = []
        temp = currentSol[:]

        for i in range(0,int(self.nodenum)) :
            # print(i,'i')
            for j in range(1,int(self.numberOfColor) + 1) :
                if temp[i] != j :
                    temp[i] = j
                    neighbors.append(temp)
                temp = currentSol[:]


        return neighbors


    def value(self,state):
        # print(state)
        v = 0
        for i in range(int(self.nodenum)) :
            for j in range(int(self.nodenum)):
                if self.gragh[i][j] == 1 :
                    if state[i] != state[j] :
                        v += 1
        # print(v)
        return v/2


