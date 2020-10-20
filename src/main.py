#!/usr/bin/python3
# -- coding: utf-8 --

import Maze, pygame, sys, time, jsonManager
import os.path as check
#---Global Variables---#
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

def parse_argv():
    if len(sys.argv) == 3: #Option using .json file
        if  sys.argv[1] == "-f" and check.exists(sys.argv[2]):
            if check.exists(sys.argv[2]):
                return 1
            else:
                print("File not found.")
                sys.exit()
        else:
            print("Option not found.")
            sys.exit()

    elif len(sys.argv) ==4: #Option typing Maze size
        if  sys.argv[1] == "-g":
            if sys.argv[2].isdigit() and sys.argv[3].isdigit():
                return 2
            else:
                print("Impossible to generate.")
                sys.exit()
        else:
            print("Option not found.")
            sys.exit()

        #python ./main.py -g 10 8
        #python ./main.py -f puzzle_10x10.json
    else:
        print("The number of arguments is wrong!\n"
        + "Remember, the correct formats are:\n"
        + "1.- python ./main.py -g numRows numCols\n"
        + "2.- python ./main.py -f fileSelected.json")
        sys.exit()


def drawmaze(maze):

    sizeCell=20
    WIDTH = sizeCell * maze.rows + 20
    HIGHT = sizeCell * maze.columns + 20
    
    screen = pygame.display.set_mode((HIGHT,WIDTH))
    screen.fill(WHITE)

    #--Here the maze will be drawn
    for i in range(maze.columns):
        for j in range(maze.rows):
            
            if maze.getMaze()[j][i].getNeigh()[0]==False:
                pygame.draw.line(screen, BLACK, [i * sizeCell + 10, j * sizeCell + 10], [i * sizeCell + sizeCell + 10, j * sizeCell + 10], 2) #North
            if maze.getMaze()[j][i].getNeigh()[1]==False:
                pygame.draw.line(screen, BLACK, [i * sizeCell + sizeCell + 10, j * sizeCell + 10], [i * sizeCell + 10 + sizeCell, j * sizeCell + sizeCell + 10], 2) #East
            if maze.getMaze()[j][i].getNeigh()[2]==False:
                pygame.draw.line(screen, BLACK, [i * sizeCell + 10, j * sizeCell + sizeCell + 10], [i * sizeCell + sizeCell +10,j * sizeCell + sizeCell + 10], 2) #South
            if maze.getMaze()[j][i].getNeigh()[3]==False:
                pygame.draw.line(screen, BLACK, [i * sizeCell + 10,j * sizeCell + 10], [i * sizeCell + 10, j * sizeCell + sizeCell + 10], 2) #West

    pygame.image.save(screen, "results/Lab_" + str(maze.rows) + "_" + str(maze.columns) + ".jpg")

def main():
    rows = int(sys.argv[2])
    columns= int(sys.argv[3])

    my_maze = Maze.Maze()
    my_maze.generateRandomMaze(rows, columns)
    my_maze.iterate()
    drawmaze(my_maze)

def main2():
    json = jsonManager.read(sys.argv[2])

    my_maze = Maze.Maze()
    my_maze.generateMazeJSON(json)
    drawmaze(my_maze)  

if __name__ == '__main__':

    if parse_argv() == 1:
        main2()
    elif parse_argv()== 2:
        main()
