import Cell, pygame, random
import numpy as np

class Maze():
    def __init__(self,rows, columns):
        self.rows = rows
        self.columns = columns
        self.grid = []
        self.path=[]

    def generate_maze_sol(self, rows, columns, n_neighbours, movements, movements_id):
        self.rows = rows
        self.columns = columns
        self.n_neighbours = n_neighbours
        self.movements = movements
        self.movements_id = movements_id

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

    def Choose_Starting_Cell(self):
        initialCellX = random.randint(0, self.columns - 1)
        initialCellY = random.randint(0, self.rows - 1)
        print(initialCellX+" "+initialCellY)
        self.grid[initialCellY][initialCellX].visited = True
        return (initialCellX, initialCellY)

    def Choose_Random_Cell(self):
        choosen=False
        while not choosen:
<<<<<<< HEAD
            self.CurrentCellX = random.randint(0,columns-1)
            self.CurrentCellY = random.randint(0,rows-1)
            if grid[CurrentCellY][CurrentCellX].visited == False:
                grid[CellY][CellX].visited = True
=======
            CellX = random.randint(0, self.columns - 1)
            CellY = random.randint(0, self.rows - 1)
            if self.grid[CellY][CellX].visited == False:
                self.grid[CellY][CellX].visited = True
>>>>>>> 2c3f5ffa5a03c119c97b3d4b0e4eb75efa80b50f
                choosen = True

    def randomize_dir(self):
        choosen=False
        while not choosen:
            direction=random.randint(0,3)
            if direction==0 and self.grid[self.CurrentCellX][self.CurrentCellY].getDirection() != "N" and self.CurrentCellX-1<0:
                self.CurrentCellY-=1
                self.grid[self.CurrentCellX][self.CurrentCellY].visited==:
                choosen = True
            if direction==1 and self.grid[self.CurrentCellX][self.CurrentCellY].getDirection() != "E" and self.CurrentCellY+1<self.columns:
                self.CurrentCellX+=1
                choosen = True
            if direction==2 and self.grid[self.CurrentCellX][self.CurrentCellY].getDirection() != "S" and self.CurrentCellX+1<self.rows:
                self.CurrentCellY+=1
                choosen = True
            if direction==3 and self.grid[self.CurrentCellX][self.CurrentCellY].getDirection() != "W" and self.CurrentCellY-1<0:
                self.CurrentCellX-=1
                choosen = True

    def generate_lab(self):
        self.path.append(self.grid[self.CurrentCellX][self.CurrentCellY])
        while self.grid[self.CurrentCellX][self.CurrentCellY].visited==False:
            randomize_dir()
            path.append(self.grid[self.CurrentCellX][self.CurrentCellY])
            if self.grid[self.CurrentCellX][self.CurrentCellY].isOnTrace()==True:
                cellPopped=self.path.pop()
                while cellPopped.getPosition==() != (self.CurrentCellX,self.CurrentCellY):
                    cellPopped.setNotOnTrace()
                    cellPopped=path.pop()
            
            
            
    def iterate(self):
        Choose_Random_Cell()
        generate_lab(Choose_Random_Cell())
        