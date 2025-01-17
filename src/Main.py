
#!/usr/bin/python3
# -- coding: utf-8 --


from os import listdir

import Drawer
import JsonManager
import Maze
from Problem import Problem
from SearchSolution import searchAlgorithm


def subTask1():
    rows, columns=-1,-1
    while rows<0 or columns<0:
        try:
            rows = int(input("\t•Number of rows: "))
            columns= int(input("\t•Number of columns: "))
        except ValueError:
            print("##ERROR: Please write a positive number for both variables.")

    my_maze = Maze.Maze()
    my_maze.generateRandomMaze(rows, columns)
    Drawer.drawMaze(my_maze)
    JsonManager.write(my_maze)
    print("Maze generated on \\mazes folder.\n")
    
def subTask2():
    my_maze=Maze.Maze()
    my_maze.generateMazeJSON(JsonManager.read(choose_file("./mazes")))
    Drawer.drawMaze(my_maze)
    print("Solution storage on \\results folder.")

def subTask3():
    my_maze=Maze.Maze()
    problem=JsonManager.read(choose_file("./problems"))
    try:
        my_maze.generateMazeJSON(JsonManager.read("./mazes/"+str(problem["MAZE"])))
    except:
        print("Incorrect format of the JSON file.")
        return 0
    strategy=-1
    while strategy != "BREADTH" and strategy != "DEPTH" and strategy != "GREEDY" and strategy != "UNIFORM" and strategy != "A":
        print("Strategies available: [BREADTH, DEPTH, GREEDY, UNIFORM, A]")
        strategy=input("• Choose your stratrgy to solve: \n")

    prob=Problem(problem["INITIAL"][1:-1].split(","),problem["OBJETIVE"][1:-1].split(","),strategy)
    searchAlgorithm(prob,my_maze)
    print("Solution storage on \\results folder.")

def defineProblem():
    print("Choose the maze you would want to solve: ")
    my_maze=Maze.Maze()
    try:
        file_maze=choose_file("./mazes")
        my_maze.generateMazeJSON(JsonManager.read(file_maze))
    except:
        print("Incorrect format of the JSON file.")
        return 0
    
    initial=[-1,-1]
    while initial[0]<0 or initial[0]>my_maze.rows-1 or initial[1]<0 or initial[1]>my_maze.columns-1:
        print("Select the initial cell: ")
        initial[0]=int(input("  Initial cell row: "))
        initial[1]=int(input("  Initial cell column: "))
    
    objective=[-1,-1]
    while objective[0]<0 or objective[0]>my_maze.rows-1 or objective[1]<0 or objective[1]>my_maze.columns-1:
        print("Select the objective cell: ")
        objective[0]=int(input("  Objective cell row: "))
        objective[1]=int(input("  Obejctive cell column: "))
    file=file_maze.split("/")

    JsonManager.writeProblem(initial, objective, file[len(file)-1], [my_maze.rows,my_maze.columns])
    print("Problem storage on \\problems folder.")

def choose_file(path: str):
    files=listdir(path)
    answer=-1;
    while answer<0 or answer>len(files)-1:
        print("\nAvailable files: ")
        i=0;
        for file in files:
            print("\t[",i,"]",file)
            i=i+1
        answer=int(input("\nSelect the file you want: "))
    return path+"/"+files[answer]


if __name__ == '__main__':
    answer=-1
    print("##### Choose what you want to do: #####\n •(0) Exit.\n •(1) Generate a random maze.\n •(2) Create a maze from JSON.\n •(3) Solve a problem.\n •(4) Define a problem." )
    try:
        answer=int(input(">ANSWER: "))
        if answer == 1:
            subTask1()
        elif answer== 2:
            subTask2()
        elif answer== 3:
            subTask3()
        elif answer== 4:
            defineProblem()
        elif answer==0:
            print(">>Exit")
        else:
            print("Please write an available number")

    except ValueError:
        print("##ERROR: Please write an available number.")
    except KeyboardInterrupt:
        print("Program finished")
    except FileNotFoundError:
        print("Path not founded")


