#!/path/to/python 
import random

list = ["aromao", "mreis", "rsilva", "jsaias","tsantos","psalgueiro","mmourao","hvieira","hfernandes","hramos"]
list.sort()

print "Lista de candidatos: " + str(list)

winnerList = random.sample(list, 3) 
winnerList.sort

print "and the winner List is : " + str(winnerList)
