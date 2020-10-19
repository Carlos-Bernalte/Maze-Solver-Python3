#!/usr/bin/python3
# -- coding: utf-8 --

import Maze, pygame, sys, time 
from jsonManager import jsonManager

#---Global Variables---#
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


WIDTH=620
HIGHT=620
screen = pygame.display.set_mode((WIDTH,HIGHT))

pygame.init()
screen.fill(WHITE)

def parse_argv():
    if len(sys.argv) != 3:
        print("The number of arguments is wrong.")
        sys.exit()
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
    #parse_argv()
    main()

