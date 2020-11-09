
#!/usr/bin/python3
# -- coding: utf-8 --

import Maze, sys, JsonManager, Drawer, Functions, frontier, Node
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
def prueba3():
    node1=Node.Node(1,(0,4),None,None,None,None,1)
    node2=Node.Node(1,(0,1),None,None,None,None,1)
    node3=Node.Node(1,(1,0),None,None,None,None,1)
    node4=Node.Node(1,(2,0),None,None,None,None,1)

    front=frontier.Frontier()
    front.insertNode(node1)
    front.insertNode(node2)
    front.insertNode(node3)
    front.insertNode(node4)
    for node in front.frontier:
        print(node.idNode)

if __name__ == '__main__':
    print("##### Choose what you want to do: #####\n •(1) Generate a random maze.\n •(2) Create a maze from JSON." )
    answer=int(input(">ANSWER: "))
    if answer == 1:
        subTask1()
    elif answer== 2:
        subTask2()
    elif answer== 3:
        prueba3()
