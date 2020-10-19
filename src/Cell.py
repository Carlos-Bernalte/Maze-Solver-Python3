#!/usr/bin/python3
# -- coding: utf-8 --

class Cell:

    def __init__(self, x, y, neighbours = None, value = 0 ):
        self.position = (x, y)
        self.value = value
        if neighbours is not None: self.neighbours=neighbours
        else: self.neighbours = [False, False, False, False]
        self.visited = False
        self.onTrace = False 
        self.come_from = ""
        

    def getNeigh(self):
        return self.neighbours

    def getDirection(self):
        return self.come_from

    def getPosition(self):
        return self.position

    def getVisited(self):
        return self.visited

    def setVisited(self):
        self.visited=True
        self.onTrace=False

    def setOnTrace(self):
        self.onTrace= True

    def isOnTrace(self):
        return self.onTrace

    def setDefault(self):
        self.neighbours = [False, False, False, False]
        self.onTrace= False
    
    def setNeighbour(self, direction):
        self.come_from=direction
        if direction == "N":
            self.neighbours[0]=True
        if direction == "E":
            self.neighbours[1]=True
        if direction == "S":
            self.neighbours[2]=True
        if direction == "O":    #Dijo Luis que pusieramos O en vez de W para que no se rayara con su JSON
            self.neighbours[3]=True
    