import Cell, random
import numpy as np

class Maze():

    grid = []
    path = []

    def __init__(self,rows, columns):
        self.rows = rows
        self.columns = columns
        self.init_grid()

    def init_grid(self):
        for i in range(self.rows):
            self.grid.append([])
            for j in range(self.columns):
                self.grid[i].append(Cell.Cell(i, j))
    
    def getMaze(self):
        return self.grid

    def check_maze(self):
        complete=True
        for i in range(self.rows):
            for j in range(self.columns):
                if self.grid[i][j].visited== False:
                    complete = False
        return complete

    def choose_starting_cell(self):
        initialCellX = random.randint(0, self.columns - 1)
        initialCellY = random.randint(0, self.rows - 1)
        self.grid[initialCellX][initialCellY].setVisited()
        print("Tengo que llegar a: ", initialCellX, " ",initialCellY)
        return (initialCellX, initialCellY)

    def choose_random_cell(self):
        choosen=False
        while not choosen:
            self.CurrentCellX = random.randint(0, self.columns - 1)
            self.CurrentCellY = random.randint(0, self.rows - 1)
            if self.grid[self.CurrentCellX][self.CurrentCellY].getVisited() == False:
                self.grid[self.CurrentCellX][self.CurrentCellY].setOnTrace()
                choosen = True
        print()
        print("Empiezo en: ", self.grid[self.CurrentCellX][self.CurrentCellY].getPosition())

    def randomize_dir(self):
        choosen=False
        while not choosen:
            direction=random.randint(0,3)
            
            if direction==0 and self.grid[self.CurrentCellX][self.CurrentCellY].getDirection() != "N" and self.CurrentCellX-1!=-1:
                print("Voy para el Norte")
                self.grid[self.CurrentCellX][self.CurrentCellY].setNeighbour("N")
                self.CurrentCellX-=1
                self.grid[self.CurrentCellX][self.CurrentCellY].setNeighbour("S")
                choosen = True
            elif direction==1 and self.grid[self.CurrentCellX][self.CurrentCellY].getDirection() != "E" and self.CurrentCellY+1!=self.columns:
                print("Voy para el Este")
                self.grid[self.CurrentCellX][self.CurrentCellY].setNeighbour("E")
                self.CurrentCellY+=1
                self.grid[self.CurrentCellX][self.CurrentCellY].setNeighbour("W")
                choosen = True
            elif direction==2 and self.grid[self.CurrentCellX][self.CurrentCellY].getDirection() != "S" and self.CurrentCellX+1!=self.rows:
                print("Voy para el Sur")
                self.grid[self.CurrentCellX][self.CurrentCellY].setNeighbour("S")
                self.CurrentCellX+=1
                self.grid[self.CurrentCellX][self.CurrentCellY].setNeighbour("N")
                choosen = True
            elif direction==3 and self.grid[self.CurrentCellX][self.CurrentCellY].getDirection() != "W" and self.CurrentCellY-1!=-1:
                print("Voy para el Oeste")
                self.grid[self.CurrentCellX][self.CurrentCellY].setNeighbour("W")
                self.CurrentCellY-=1
                self.grid[self.CurrentCellX][self.CurrentCellY].setNeighbour("E")
                choosen = True

    def generate_lab(self):
        self.path=[]
        self.path.append(self.grid[self.CurrentCellX][self.CurrentCellY])
        while self.grid[self.CurrentCellX][self.CurrentCellY].getVisited()==False:
            self.randomize_dir()
            print("Estoy ahora en: ", self.grid[self.CurrentCellX][self.CurrentCellY].getPosition())
            if self.grid[self.CurrentCellX][self.CurrentCellY].isOnTrace()==True:
                
                print("Loop")
                cellPopped=self.path.pop()
                print(cellPopped.getPosition(), " ", (self.CurrentCellX,self.CurrentCellY))
                while cellPopped.getPosition() != (self.CurrentCellX,self.CurrentCellY):
                    self.grid[cellPopped.getPosition()[0]][cellPopped.getPosition()[1]].setDefault()
                    print("La celda ", cellPopped.getPosition()[0], " ", cellPopped.getPosition()[1]," funada")
                    cellPopped=self.path.pop()
                self.grid[cellPopped.getPosition()[0]][cellPopped.getPosition()[1]].setDefault()
            self.grid[self.CurrentCellX][self.CurrentCellY].setOnTrace()
            self.path.append(self.grid[self.CurrentCellX][self.CurrentCellY])
        print("He llegado a un camino en: ", self.grid[self.CurrentCellX][self.CurrentCellY].getPosition())
            
            
    def iterate(self):
        self.choose_starting_cell()
        while self.check_maze()==False:
            self.choose_random_cell()
            self.generate_lab()
            for cell in self.path:
                cell.setVisited()

    def printMaze(self):
        for x in self.grid:
            for y in x:
                print(y.getNeigh(), end=" ")
            print()