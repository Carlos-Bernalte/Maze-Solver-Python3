#!/usr/bin/python3
# -- coding: utf-8 --

class Node:
    idNode=0
    def __init__(self, idState=(), cost=0, parent=None, action=None, depth=0, heuristic=0, value=0):
        self.idNode = Node.idNode #It will increase with the creation of new nodes (starts in 0)
        Node.idNode+=1
        self.cost = cost #Accumulated cost by the path to that node
        self.idState = idState #Access to the space state in that node
        self.parent = parent #Access to the parent node
        self.action = action #Movement that has generated the node
        self.depth = depth #Level of the node (root node = 0)
        self.heuristic = heuristic #Value of the heuristic. H(row, column)=|currentRow-objetiveRow| + |currentColumn-objectiveColumn|
        self.value = value #Value of the node according to the selected strategy 

    def toString(self):
        if self.parent is None:
            return "["+str(self.idNode)+"]["+str(self.cost)+","+str(self.idState)+",None,  None,"+str(self.depth)+","+str(self.heuristic)+","+str(self.value)+"]"
        else:
            return "["+str(self.idNode)+"]["+str(self.cost)+","+str(self.idState)+","+str(self.parent.idState)+","+str(self.action)+","+str(self.depth)+","+str(self.heuristic)+","+str(self.value)+"]"