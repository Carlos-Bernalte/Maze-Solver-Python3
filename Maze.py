import Cell, pygame, random
import numpy as np

class Maze():
    def __init__(self,rows, columns):
        self.rows = rows
        self.columns = columns
        self.grid = []

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
                null_cell = Cell.Cell(i, j)
                self.grid[i].append(null_cell)
    def getMaze(self):
        return self.grid

    def show_grid(self):
        for i in range(self.rows):
            for j in range(self.columns):
                print(self.grid[i][j].getPosition())

    def Choose_Starting_Cell(self):
        initialCellX = random.randint(0,columns-1)
        initialCellY = random.randint(0,rows-1)
        print(initialCellX+" "+initialCellY)
        self.grid[initialCellY][initialCellX].visited = True
        return (initialCellX, initialCellY)

    def Choose_Random_Cell(self):
        choosen=False
        while not choosen:
            CellX = random.randint(0,columns-1)
            CellY = random.randint(0,rows-1)
            if grid[CellY][CellX].visited == False:
                grid[CellY][CellX].visited = True
                choosen = True
        return (CellX, CellY)
    def generate_lab(self):
        self.Choose_Starting_Cell