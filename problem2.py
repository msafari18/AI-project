import random


class Problem2:

    def __init__(self,table,col,row,dictionary):
        self.table = table
        self.dictionary = dictionary
        self.row = row
        self.col = col
        self.v = 0

    def generateStart(self):
         return  self.table

    def maxLen(self) :
        max = len(self.dictionary[0])
        for i in self.dictionary :
            if max < len(i) :
                max = len(i)
        return max

    def neighbors(self,currentSol):
        """
        :param currentSol : current state
        :return: the best neighbor for current state
        """

        neighbors = []

        m = random.randint(0,int(self.row) - 1)
        n = random.randint(0, int(self.col) - 1)
        x = random.randint(0, int(self.row) - 1)
        y = random.randint(0, int(self.col) - 1)

        o = currentSol[m][n]
        currentSol[m][n] = currentSol[x][y]
        currentSol[x][y] = o
        neighbors.append(currentSol)

        return neighbors

    def actions(self,i,j):

        actions = ['r', 'u', 'l', 'd']
        if i == 0:
            if 'u' in actions:
                actions.remove('u')
        if i == int(self.row) - 1 :
            if 'd' in actions:
                actions.remove('d')
        if j == 0:
            if 'l' in actions:
                actions.remove('l')
        if j == int(self.col) - 1:
            if 'r' in actions:
                actions.remove('r')
        # print(i,j,actions)
        return actions

    word = ""
    def value(self,state):
        self.v = 0
        for i in range(len(state)) :
            for j in range(len(state[i])) :
                self.word = ""
                # print(i,j)
                self.findWord(state,i,j,0,"")
        # print(self.v)

        return self.v

    def findWord(self,state,x,y,v,word):


        act = self.actions(x,y)
        word = word + state[x][y]
        # print(word)

        if word in self.dictionary:
            # print(state)
            # print('yesssssss')
            # print(word)
            self.v+=1
            # return

        # if self.v >= len(self.dictionary) :
        #     return
        if len(word) >= self.maxLen():
            return
        for a in act:
            if a == 'r':
                self.findWord(state, x, y + 1,v,word)
            if a == 'l':
                # print(x, y)
                self.findWord(state, x, y - 1,v,word)
            if a == 'u':
                # print(x, y)
                self.findWord(state, x - 1, y,v,word)
            if a == 'd':
                # print(x, y)
                self.findWord(state, x + 1, y,v,word)



