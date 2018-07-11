import random
from healClimbingAlgorithm import  healClimbing
from healClimbingRandom import healClimbingRandom
from healClimbingRandomFS import healClimbingRandomFS
# from healClimbingRandomStart import healClimbing
from problem1 import Problem1
from problem2 import Problem2
from SimulatedAnnealing import SimulatedAnnealing
from problem3 import Problem3
from genetic import Genetic
from matplotlib import pyplot as plt


#---------------------------------------------------- PROBLEM1 INPUT AND IMPLEMENTION

# graph = [[1,0,1,0,1,1,1,0,1,0,1,0,1,0,1],
#          [0,1,1,1,1,0,0,0,0,0,0,0,1,0,1],
#          [1,1,1,0,0,0,0,1,0,1,0,1,1,1,0],
#          [0,1,0,1,1,1,0,0,1,1,1,1,0,0,0],
#          [1,1,0,1,1,0,0,0,0,0,0,0,0,1,1],
#          [1,0,0,1,0,1,1,1,1,1,1,0,0,0,0],
#          [1,0,0,0,0,1,1,0,0,0,0,1,1,1,1],
#          [0,0,1,0,0,1,0,1,0,0,0,0,0,0,0],
#          [1,0,0,1,0,1,0,0,1,1,1,1,0,0,1],
#          [0,0,1,1,0,1,0,0,1,1,0,0,0,1,0],
#          [1,0,0,1,0,1,0,0,1,0,1,1,0,0,0],
#          [0,0,1,1,0,0,1,0,1,0,1,1,1,1,0],
#          [1,1,1,0,0,0,1,0,0,0,0,1,1,0,1],
#          [0,0,1,0,1,0,1,0,0,1,0,1,0,1,1],
#          [1,1,0,0,1,0,1,0,1,0,0,0,1,1,1]]
#
# nodenum = input("number of graph node")
# # for i in range(0, int(nodenum)):
# #     graph.append([int(x) for x in input("graph").split()])
# numberOfColor = input("number of color")
#

# prob1 = Problem1(graph,nodenum,numberOfColor)

# hc = healClimbing (prob1)
# path = hc.healClimbingAlgorithm(prob1.generateStart())
# print (path)
# print(hc.bestAns)
# print(hc.value)
# print(hc.extend)
# print(hc.visited)

# hc = healClimbingRandom (prob1)
# path = hc.healClimbingRAlgorithm(prob1.generateStart())
# print (path)
# print(hc.bestAns)
# print(hc.value)
# print(hc.extend)
# print(hc.visited)

# hc = healClimbingRandomFS (prob1)
# path = hc.healClimbingFS(prob1.generateStart())
# print (path)
# print(hc.bestAns)
# print(hc.value)
# print(hc.extend)
# print(hc.visited)

# hc = healClimbing (prob1)
# path = hc.healClimbingRS(prob1.generateStart())
# print (path)
# print(hc.bestAns)
# print(hc.value)
# print(hc.extend)
# print(hc.visited)


#---------------------------------------------------- PROBLEM2 INPUT AND IMPLEMENTION

# table = []
# dictionary = []
# dictionary = ([x for x in input("dictionary").split()])
# # print(dictionary)
# row = input("number of row")
# col = input("number of col")
#
# for i in range(0, int(row)):
#     table.append([x for x in input("letter").split()])
#
# prob2 = Problem2(table,col,row,dictionary)
# s = SimulatedAnnealing(prob2)
# path = s.SimulatedAnnealingAlgorithm(prob2.generateStart())
# print(s.extend)
# print(s.visited)




#---------------------------------------------------- PROBLEM3 INPUT AND IMPLEMENTION
x = input("mutation rate ")
y = input("end condition")
z = input("population size ")
mut = []
child = []
pop = []
for j in range (20) :
    pop = []
    for i in range(1,50) :
        prob3 = Problem3(int(x),int(y))
        g = Genetic(prob3,int(x),int(y),int(z),i)
        m = g.geneticAlgorithm1()
        pop.append(g.iterateNum)
    plt.plot(pop,'-c')
    plt.suptitle('child size effect')
    plt.xlabel(' number of child')
    plt.ylabel('number of generation')
    plt.show()



print(m)
print(g.iterateNum)
l = []
r = []
if m[0][0] == 0 : l.append('E')
else : r.append('E')
if m[0][1] == 0 : l.append('T')
else : r.append('T')
if m[0][2] == 0 : l.append('A')
else : r.append('A')
if m[0][3] == 0 : l.append('I')
else : r.append('I')
if m[0][4] == 0 : l.append('N')
else : r.append('N')
if m[0][5] == 0 : l.append('O')
else : r.append('O')
if m[0][6] == 0 : l.append('S')
else : r.append('S')
if m[0][7] == 0 : l.append('H')
else : r.append('H')
if m[0][8] == 0 : l.append('R')
else : r.append('R')
if m[0][9] == 0 : l.append('D')
else : r.append('D')

others = ['B','C','F','G','J','K','L','M','P','Q','U','V','W','X','Y','Z']

print('keyboard :) ')

for i in range (5) :
    if r :
        print(r[0],' ', end='', flush=True)

        r.remove(r[0])
    else :
        n= random.choice(others)
        print(n,' ', end='', flush=True)
        others.remove(n)
for i in range(5):
    if l:
        print(l[0],' ', end='', flush=True)
        l.remove(l[0])
    else:
        n = random.choice(others)
        print(n,' ', end='', flush=True)
        others.remove(n)
print()
print('  ', end='', flush=True)
for i in range(4):
    if r:
        print(r[0],' ', end='', flush=True)
        r.remove(r[0])
    else:
        n = random.choice(others)
        print(n,' ', end='', flush=True)
        others.remove(n)
for i in range(4):
    if l:
        print(l[0],' ', end='', flush=True)
        l.remove(l[0])
    else:
        n = random.choice(others)
        print(n,' ', end='', flush=True)
        others.remove(n)

print()
print('  ', end='', flush=True)
for i in range(4):
    if r:
        print(r[0],' ', end='', flush=True)
        r.remove(r[0])
    else:
        n = random.choice(others)
        print(n,' ', end='', flush=True)
        others.remove(n)
for i in range(4):
    if l:
        print(l[0],' ', end='', flush=True)
        l.remove(l[0])
    else:
        n = random.choice(others)
        print(n,' ', end='', flush=True)
        others.remove(n)


i = 0

# plt.plot(g.bests,'ob')
# plt.suptitle('bests value')
# plt.xlabel('populations')
# plt.ylabel('values')
# plt.show()
#
# plt.plot(g.average,'ob')
# plt.suptitle('average of values')
# plt.xlabel('populations')
# plt.ylabel('values')
# plt.show()
#
# plt.plot(g.worste,'ob')
# plt.suptitle(' worst values')
# plt.xlabel('populations')
# plt.ylabel('values')
# plt.show()
#
# plt.plot(g.bests,'og',g.average,'ob' , g.worste,'or')
# plt.suptitle('all in one')
#
# plt.xlabel('populations')
# plt.ylabel('values')
# plt.show()

# plt.plot(child,'-c')
# plt.suptitle('miutation rate effect')
# plt.xlabel('number of child')
# plt.ylabel('number of generation')
# plt.show()

