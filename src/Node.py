#!/usr/bin/python3
# -- coding: utf-8 --

class Node:
    idNode=0
    def __init__(self, cost, idState, idParent, action, depth, heuristic, value):
        self.idNode = Node.idNode #It will increase with the creation of new nodes (starts in 0)
        Node.idNode+=1
        self.cost = cost #Accumulated cost by the path to that node
        self.idState = idState #Access to the space state in that node
        self.idParent = idParent #Access to the parent node
        self.action = action #Movement that has generated the node
        self.depth = depth #Level of the node (root node = 0)
        self.heuristic = heuristic #Value of the heuristic
        self.value = value #Value of the node according to the selected strategy

    
'''
The String which must be generated is:
    [<idNode>] [<cost>, <idState>, <idParent>, <action>, <depth>, <heuristic>, <value>]
'''