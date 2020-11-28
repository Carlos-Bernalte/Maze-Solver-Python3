#!/usr/bin/python3
# -- coding: utf-8 --

import Cell, random

class Maze:

    def __init__(self):
        self.grid = []       

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
                self.grid[i][j].value=JSON["cells"]["(" + str(i) + ", " + str(j) + ")"]["value"]


    def initLab(self):
        for i in range(self.rows):
            self.grid.append([])
            for j in range(self.columns):
                self.grid[i].append(Cell.Cell(i, j, random.randint(0, 3)))

    #--Checks if the maze is completed (all the cells are visited)
    def checkMaze(self):
        complete=True
        for i in range(self.rows):
            for j in range(self.columns):
                if self.grid[i][j].visited== False:
                    complete = False
        return complete
    #--Choose the starting cell we must to arrive
    def chooseVisitedCell(self):
        initialCellX = random.randint(0, self.rows - 1)
        initialCellY = random.randint(0, self.columns - 1)
        self.grid[initialCellX][initialCellY].setVisited()

    #--Is to choose a cell where we are going to start on the maze to build a path
    def chooseRandomCell(self):
        choosen=False
        x,y=0,0
        while not choosen:
            x = random.randint(0, self.rows - 1)
            y = random.randint(0, self.columns - 1)
            if self.grid[x][y].visited == False:
                choosen = True

        return x, y
    
    def navigateMaze(self):
        path=[]
        x,y=self.chooseRandomCell()
        path.append([(x,y),"",""])
        while self.grid[x][y].visited == False:
            path=self.randomizeDirection(x,y,path)
            x,y = path[-1][0]
            if self.isIn((x,y),path[0:-1])==True:
                path=self.deleteLoop((x,y),path)
        return path

    def deleteLoop(self,cellRepeated,path):
        path.pop()
        cellPoped=path.pop()
        while cellPoped[0] != cellRepeated:
            cellPoped=path.pop()
        cellPoped[2]=""
        path.append(cellPoped)
        return path

    def isIn(self,cell, path):
        for cellInPath in path:
            if cellInPath[0] == cell:
                return True
        return False
    
    def randomizeDirection(self, x,y,path):
        choosen=False
        direction=""
        while not choosen:
            direction=random.choice(["N","E","S","O"])
            if direction=="N" and x-1>-1 and path[-1][0]!= (x+1,y):
                path[-1][2]="N"
                x-=1
                path.append([(x,y),"S",""])
                choosen=True
            elif direction=="E" and y+1<self.columns-1 and path[-1][0]!= (x,y-1):
                path[-1][2]="E"
                y+=1
                path.append([(x,y),"O",""])
                choosen=True
            elif direction=="S" and x+1<self.rows-1 and path[-1][0]!= (x-1,y):
                path[-1][2]="S"
                x+=1
                path.append([(x,y),"N",""])
                choosen=True
            elif direction=="O" and y-1>-1 and path[-1][0]!= (x,y+1):
                path[-1][2]="O"
                y-=1
                path.append([(x,y),"E",""])
                choosen=True
        return path

    def iterate(self):
        self.chooseVisitedCell()
        while self.checkMaze() == False:
            path=self.navigateMaze()

            for i in range(len(path)):
                x,y = path[i][0]
                self.grid[x][y].visited=True
                self.grid[x][y].setNeighbour(path[i][1])
                self.grid[x][y].setNeighbour(path[i][2])

"""
        for i in range(self.rows):
            for j in range(self.columns):
                print(self.grid[i][j].neighbours, end="")
            print()
"""