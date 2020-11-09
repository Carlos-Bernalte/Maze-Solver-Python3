#!/usr/bin/python3
# -- coding: utf-8 --

import Cell, random

class Maze:

    def __init__(self):
        self.grid = []
        self.path = []        

    def generateRandomMaze(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.initLab()
        self.iterate()

    def generateMazeJSON(self, JSON):
        self.rows = JSON['rows']
        self.columns = JSON['cols']
        self.initLab()
        for i in range(self.rows):
            for j in range(self.columns):
                self.grid[i][j].neighbours=JSON["cells"]["(" + str(i) + ", " + str(j) + ")"]["neighbors"]
                self.grid[i][j].neighbours=JSON["cells"]["(" + str(i) + ", " + str(j) + ")"]["value"]


    def initLab(self):
        for i in range(self.rows):
            self.grid.append([])
            for j in range(self.columns):
                self.grid[i].append(Cell.Cell(i, j))
    
    def getMaze(self):
        return self.grid

    #--Checks if the maze is completed (all the cells are visited)
    def checkMaze(self):
        complete=True
        for i in range(self.rows):
            for j in range(self.columns):
                if self.grid[i][j].visited== False:
                    complete = False
        return complete
    #--Choose the starting cell we must to arrive
    def chooseStartingCell(self):
        initialCellX = random.randint(0, self.rows - 1)
        initialCellY = random.randint(0, self.columns - 1)
        self.grid[initialCellX][initialCellY].setVisited()

    #--Is to choose a cell where we are going to start on the maze to build a path
    def chooseRandomCell(self):
        choosen=False
        while not choosen:
            self.CurrentCellX = random.randint(0, self.rows - 1)
            self.CurrentCellY = random.randint(0, self.columns - 1)
            if self.grid[self.CurrentCellX][self.CurrentCellY].getVisited() == False:
                self.grid[self.CurrentCellX][self.CurrentCellY].setOnTrace()
                choosen = True
    #--Choose the direction you come from, checking that you cannot go back to the direction you came from, as well as you cannot go out of bounds
    def randomizeDir(self):
        choosen=False
        while not choosen:
            direction=random.randint(0,3)

            if direction==0 and self.grid[self.CurrentCellX][self.CurrentCellY].getDirection() != "N" and self.CurrentCellX-1!=-1:

                self.grid[self.CurrentCellX][self.CurrentCellY].setNeighbour("N")
                self.CurrentCellX-=1
                self.grid[self.CurrentCellX][self.CurrentCellY].setNeighbour("S")
                choosen = True
            elif direction==1 and self.grid[self.CurrentCellX][self.CurrentCellY].getDirection() != "W" and self.CurrentCellY+1!=self.columns:
                self.grid[self.CurrentCellX][self.CurrentCellY].setNeighbour("E")
                self.CurrentCellY+=1
                self.grid[self.CurrentCellX][self.CurrentCellY].setNeighbour("O")
                choosen = True
            elif direction==2 and self.grid[self.CurrentCellX][self.CurrentCellY].getDirection() != "N" and self.CurrentCellX+1!=self.rows:
                self.grid[self.CurrentCellX][self.CurrentCellY].setNeighbour("S")
                self.CurrentCellX+=1
                self.grid[self.CurrentCellX][self.CurrentCellY].setNeighbour("N")
                choosen = True

            elif direction==3 and self.grid[self.CurrentCellX][self.CurrentCellY].getDirection() != "O" and self.CurrentCellY-1!=-1:
                self.grid[self.CurrentCellX][self.CurrentCellY].setNeighbour("O")

                self.CurrentCellY-=1
                self.grid[self.CurrentCellX][self.CurrentCellY].setNeighbour("E")
                choosen = True

    def deleteLoop(self):
        if self.grid[self.CurrentCellX][self.CurrentCellY].isOnTrace()==True:
            cellPopped=self.path.pop()
            while cellPopped.getPosition() != (self.CurrentCellX,self.CurrentCellY):
                self.grid[cellPopped.getPosition()[0]][cellPopped.getPosition()[1]].setDefault()
                cellPopped=self.path.pop() 

    def generateLab(self):
        self.path=[]
        self.path.append(self.grid[self.CurrentCellX][self.CurrentCellY])
        while self.grid[self.CurrentCellX][self.CurrentCellY].getVisited()==False:
            self.randomizeDir()
            self.deleteLoop()
            self.grid[self.CurrentCellX][self.CurrentCellY].setOnTrace()
            self.path.append(self.grid[self.CurrentCellX][self.CurrentCellY])

    def iterate(self):
        self.chooseStartingCell()
        while self.checkMaze()==False:
            self.chooseRandomCell()
            self.generateLab()
            for cell in self.path:
                cell.setVisited()

