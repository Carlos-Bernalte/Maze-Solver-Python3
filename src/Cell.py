#!/usr/bin/python3
# -- coding: utf-8 --

class Cell():
    
    def __init__(self, x, y, value):
        self.x = x
        self.y = y
        self.value = value
        self.neighbours = [False, False, False, False]
        self.visited = False
        self.onTrace= False
        self.comeFrom = ""

    def getPosition(self):
        return (self.x, self.y)

    def setVisited(self):
        self.visited=True
        self.onTrace=False

    def setDefault(self):
        self.neighbours = [False, False, False, False]
        self.onTrace= False
        self.comeFrom=""

    def setNeighbours(self, neighbours):
        self.neighbours= neighbours

    def setNeighbour(self, direction):
        if direction == "N":
            self.neighbours[0]=True
        if direction == "E":
            self.neighbours[1]=True
        if direction == "S":
            self.neighbours[2]=True
        if direction == "O":    
            self.neighbours[3]=True
    