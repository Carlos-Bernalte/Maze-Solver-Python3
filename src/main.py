#!/usr/bin/python3
# -- coding: utf-8 --

import Maze, pygame, sys, time, jsonManager
import os.path as check
#---Glogal Variables---#
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

WIDTH=620
HIGHT=620

def parse_argv():
    if len(sys.argv) == 3:
        if  sys.argv[1] == "-f" and check.exists(sys.argv[2]):
            if check.exists(sys.argv[2]):
                return 1
            else:
                print("File not found")
                sys.exit()
        else:
            print("Option not found")
            sys.exit()

    elif len(sys.argv) ==4:
        if  sys.argv[1] == "-g":
            if sys.argv[2].isdigit() and sys.argv[3].isdigit():
                return 2
            else:
                print("Impossible to generate")
                sys.exit()
        else:
            print("Option not found")
            sys.exit()

        """python ./main.py -g 10 8"""
        """python ./main.py -f puzzle_10x10.json"""
    else:
        print("The number of arguments is wrong.")
        sys.exit()
<<<<<<< HEAD
    elif(not sys.argv[1].isdigit() or not sys.argv[2].isdigit()):
        print("The arguments must be digits.")
        sys.exit()
        
def drawMaze(maze, sizeCell):
    pygame.display.set_caption("Lab_" + str(maze.rows) + "_" + str(maze.columns))

    while 1:
        #--Here the maze will be draw
        for i in range(maze.rows):
            for j in range(maze.columns):
                if maze.getMaze()[j][i].getNeigh()[0]==False:
                    pygame.draw.line(screen, BLACK, [i * sizeCell + 10, j * sizeCell + 10], [i * sizeCell + sizeCell + 10, j * sizeCell + 10], 2) #North
                if maze.getMaze()[j][i].getNeigh()[1]==False:
                    pygame.draw.line(screen, BLACK, [i * sizeCell + sizeCell + 10, j * sizeCell + 10], [i * sizeCell + 10 + sizeCell, j * sizeCell + sizeCell + 10], 2) #East
                if maze.getMaze()[j][i].getNeigh()[2]==False:
                    pygame.draw.line(screen, BLACK, [i * sizeCell + 10, j * sizeCell + sizeCell + 10], [i * sizeCell + sizeCell + 10, j * sizeCell + sizeCell + 10], 2) #South
                if maze.getMaze()[j][i].getNeigh()[3]==False:
                    pygame.draw.line(screen, BLACK, [i * sizeCell + 10, j * sizeCell + 10], [i * sizeCell + 10, j * sizeCell + sizeCell + 10], 2) #West
        pygame.display.flip()
    pygame.quit()
=======


def drawmaze(maze):
    screen = pygame.display.set_mode((WIDTH,HIGHT))
    screen.fill(WHITE)
    sizeCell=600/maze.rows
    #--Here the maze will be draw
    for i in range(maze.columns):
        for j in range(maze.rows):
            
            if maze.getMaze()[j][i].getNeigh()[0]==False:
                pygame.draw.line(screen, BLACK, [i*sizeCell +10,j*sizeCell+10], [i*sizeCell+sizeCell +10,j*sizeCell +10], 2) #North
            if maze.getMaze()[j][i].getNeigh()[1]==False:
                pygame.draw.line(screen, BLACK, [i*sizeCell+sizeCell +10,j*sizeCell+10], [i*sizeCell +10+sizeCell,j*sizeCell+sizeCell +10], 2) #East
            if maze.getMaze()[j][i].getNeigh()[2]==False:
                pygame.draw.line(screen, BLACK, [i*sizeCell +10,j*sizeCell+sizeCell+10], [i*sizeCell+sizeCell +10,j*sizeCell+sizeCell +10], 2) #South
            if maze.getMaze()[j][i].getNeigh()[3]==False:
                pygame.draw.line(screen, BLACK, [i*sizeCell +10,j*sizeCell+10], [i*sizeCell +10,j*sizeCell+sizeCell +10], 2) #West

    pygame.image.save(screen, "results/Lab_"+str(maze.rows)+"_"+str(maze.columns)+".jpg")

>>>>>>> ada2f9009888012e26934ca008286823f023a567

def main():
    rows=8
    columns=8
    
    my_maze = Maze.Maze()
    my_maze.generateRandomMaze(rows, columns)
    my_maze.iterate()
    drawmaze(my_maze)

def main2():
    json = jsonManager.read("jsonInput/puzzle_10x10.json")

    my_maze = Maze.Maze()
    my_maze.generateMazeJSON(json.getData())
    drawmaze(my_maze) 

def main():
    json = jsonManager.read()
    maze = Maze.Maze(json)

    if maze.rows > maze.columns:
        sizeCell = 600/maze.rows
    else:
        sizeCell = 600/maze.columns

    maze.iterate()
    drawMaze(maze, sizeCell)    

if __name__ == '__main__':
    main2()
    """
    if parse_argv() == 1:
        print("Opción json")
    elif parse_argv()== 2:
        main()
    """
