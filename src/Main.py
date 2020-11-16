
#!/usr/bin/python3
# -- coding: utf-8 --

import Maze, JsonManager, Drawer
from Problem import Problem
from SearchSolution import searchAlgorithm

from tkinter.filedialog import askopenfilename
from tkinter import Tk

Tk().withdraw()

def subTask1():
    rows, columns=-1,-1
    while rows>0 and columns>0:
        try:
            rows = int(input("\t•Number of rows: "))
            columns= int(input("\t•Number of columns: "))
        except:
            print("##ERROR: Please write a positive number for both variables.")

    my_maze = Maze.Maze()
    my_maze.generateRandomMaze(rows, columns)
    Drawer.drawMaze(my_maze)

    JsonManager.write(my_maze)

def subTask2():

    my_maze=Maze.Maze()
    my_maze.generateMazeJSON(JsonManager.read(askopenfilename()))
    Drawer.drawMaze(my_maze)

def subTask3():
    my_maze=Maze.Maze()
    problem=JsonManager.read(askopenfilename())
    my_maze.generateMazeJSON(JsonManager.read("examples/"+str(problem["MAZE"])))

    strategy=-1
    while strategy != "BREADTH" and strategy != "DEPTH" and strategy != "GREEDY" and strategy != "UNIFORM" and strategy != "'A":
        print("Strategies available: [BREADTH, DEPTH, GREEDY, UNIFORM, 'A]")
        strategy=input("• Choose your stratrgy to solve: ")
        print()


    prob=Problem(problem["INITIAL"][1:-1].split(","),problem["OBJETIVE"][1:-1].split(","),strategy)
    searchAlgorithm(prob,my_maze)

if __name__ == '__main__':

    subTask3()
    """
    answer=-1
    while answer < 0 or answer >3:
        print("##### Choose what you want to do: #####\n •(1) Generate a random maze.\n •(2) Create a maze from JSON.\n •(3) Test insertion on frontier." )
        try:
            answer=int(input(">ANSWER: "))
        except:
            print("##ERROR: Please write an available option.")
        finally:
            if answer == 1:
                subTask1()
            elif answer== 2:
                subTask2()
            elif answer== 3:
                subTask3()
    """
