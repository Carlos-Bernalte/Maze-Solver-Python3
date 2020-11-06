
#!/usr/bin/python3
# -- coding: utf-8 --

import Maze, sys, time, jsonManager
from PIL import Image, ImageDraw
import os.path as check

def parse_argv():
    if len(sys.argv) == 3:
        if  sys.argv[1] == "-f" and check.exists(sys.argv[2]):
            if check.exists(sys.argv[2]):
                return 1
            else:
                print("File not found.")
                sys.exit()
        else:
            print("Option not found.")
            sys.exit()


    elif len(sys.argv) ==4:
        if  sys.argv[1] == "-g":
            if sys.argv[2].isdigit() and sys.argv[3].isdigit():
                return 2

            else:
                print("Impossible to generate.")
                sys.exit()
        else:
            print("Option not found.")
            sys.exit()
    else:
        print("The number of arguments is wrong!\n"
        + "Remember, the correct formats are:\n"
        + "1.- python ./main.py -g numRows numCols\n"
        + "2.- python ./main.py -f fileSelected.json")
        sys.exit()


def drawMaze(maze):

    sizeCell=20
    WIDTH = sizeCell * maze.rows + 20
    HIGHT = sizeCell * maze.columns + 20

    im = Image.new("RGB", (WIDTH, HIGHT), (255, 255, 255))
    draw = ImageDraw.Draw(im)

    #--Here the maze will be drawn
    for i in range(maze.columns):
        for j in range(maze.rows):
            
            if maze.getMaze()[j][i].getNeighbours()[0]==False:
                draw.line((i*sizeCell+10, j*sizeCell+10, i*sizeCell+sizeCell+10, j*sizeCell+10), fill=0) #North
            if maze.getMaze()[j][i].getNeighbours()[1]==False:
                draw.line((i*sizeCell+sizeCell+10, j*sizeCell+10, i*sizeCell+10+sizeCell, j*sizeCell+sizeCell+10), fill=0) #East
            if maze.getMaze()[j][i].getNeighbours()[2]==False:
                draw.line((i*sizeCell+10, j*sizeCell+sizeCell+10, i*sizeCell+sizeCell+10, j*sizeCell+sizeCell+10), fill=0) #South
            if maze.getMaze()[j][i].getNeighbours()[3]==False:
                draw.line((i*sizeCell+10, j*sizeCell+10, i*sizeCell+10, j*sizeCell+sizeCell+10), fill=0) #West

    im.save("results/Lab_" + str(maze.columns) + "_" + str(maze.rows) + ".jpg")

def generateLab():
    rows = int(sys.argv[2])
    columns= int(sys.argv[3])

    my_maze = Maze.Maze()
    my_maze.generateRandomMaze(rows, columns)
    my_maze.iterate()
    drawMaze(my_maze)
    
    myJsonManager= jsonManager.jsonManager()
    myJsonManager.write(my_maze)


def uploadJson():
    myJsonManager= jsonManager.jsonManager()
    my_maze = Maze.Maze()
    my_maze.generateMazeJSON(myJsonManager.read(sys.argv[2]))
    drawMaze(my_maze)  

if __name__ == '__main__':
    option=parse_argv()
    if option == 1:
        uploadJson()
    elif option== 2:
        generateLab()

