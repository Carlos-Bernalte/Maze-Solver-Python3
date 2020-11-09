
#!/usr/bin/python3
# -- coding: utf-8 --

from typing import final
import Maze, sys, JsonManager, Drawer, Functions, Frontier, Node
import os.path as check
from tkinter import filedialog

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
    my_maze.generateMazeJSON(JsonManager.read(filedialog.askopenfilename()))
    Drawer.drawMaze(my_maze)


def testFrontier():
    node1=Node.Node(1,(0,4),None,None,None,None,5)
    node2=Node.Node(1,(0,1),None,None,None,None,1)
    node3=Node.Node(1,(1,0),None,None,None,None,2)
    node4=Node.Node(1,(2,0),None,None,None,None,1)

    front=Frontier.Frontier()
    front.insertNode(node1)
    front.insertNode(node2)
    front.insertNode(node3)
    front.insertNode(node4)
    
    for node in front.frontier:
        print(node.idNode)

if __name__ == '__main__':
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
                testFrontier()
                
