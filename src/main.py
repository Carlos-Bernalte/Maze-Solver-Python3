
#!/usr/bin/python3
# -- coding: utf-8 --

import Maze, sys, JsonManager, Drawer, Functions
import os.path as check

def subTask1():
    rows = int(input("\t •Number of rows: "))
    columns= int(input("\t •Number of columns: "))

    my_maze = Maze.Maze()
    my_maze.generateRandomMaze(rows, columns)
    Drawer.drawMaze(my_maze)

    JsonManager.write(my_maze)

def subTask2():
    my_maze=Maze.Maze()
    my_maze.generateMazeJSON(JsonManager.read("results/Lab_5_5.json"))
    Drawer.drawMaze(my_maze)
    frontier=Functions.succersorFunction(["N",(0,0),1], my_maze.getMaze())
    #Drawer.drawPath(frontier,my_maze)

if __name__ == '__main__':
    print("##### Choose what you want to do: #####\n •(1) Generate a random maze.\n •(2) Create a maze from JSON." )
    answer=int(input(">ANSWER: "))
    if answer == 1:
        subTask1()
    elif answer== 2:
        subTask2()
