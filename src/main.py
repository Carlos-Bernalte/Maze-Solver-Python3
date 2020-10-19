import Maze, pygame, sys, time
import os.path as check
#---Glogal Variables---#
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

WIDTH=620
HIGHT=620



def parse_argv():
    if len(sys.argv) == 3:
        if  sys.argv[1] == "-f" and check.exists(sys.argv[2]):
            return 1
    elif len(sys.argv) ==4:
        if  sys.argv[1] == "-g":
            if sys.argv[2].isdigit() and sys.argv[3].isdigit():
                return 2
        
    else:
        print("The number of arguments is wrong.")
        sys.exit()


def drawmaze(maze):
    screen = pygame.display.set_mode((WIDTH,HIGHT))
    screen.fill(WHITE)
    sizeCell=600/maze.rows
    #--Here the maze will be draw
    for i in range(maze.rows):
        for j in range(maze.columns):
            
            if maze.getMaze()[j][i].getNeigh()[0]==False:
                pygame.draw.line(screen, BLACK, [i*sizeCell +10,j*sizeCell+10], [i*sizeCell+sizeCell +10,j*sizeCell +10], 2) #North
            if maze.getMaze()[j][i].getNeigh()[1]==False:
                pygame.draw.line(screen, BLACK, [i*sizeCell+sizeCell +10,j*sizeCell+10], [i*sizeCell +10+sizeCell,j*sizeCell+sizeCell +10], 2) #East
            if maze.getMaze()[j][i].getNeigh()[2]==False:
                pygame.draw.line(screen, BLACK, [i*sizeCell +10,j*sizeCell+sizeCell+10], [i*sizeCell+sizeCell +10,j*sizeCell+sizeCell +10], 2) #South
            if maze.getMaze()[j][i].getNeigh()[3]==False:
                pygame.draw.line(screen, BLACK, [i*sizeCell +10,j*sizeCell+10], [i*sizeCell +10,j*sizeCell+sizeCell +10], 2) #West

    pygame.image.save(screen, "results/Lab_"+str(maze.rows)+"_"+str(maze.columns)+".jpg")


def main():
    rows=int(sys.argv[2])
    columns=int(sys.argv[3])
    
    my_maze = Maze.Maze(rows,columns)
    my_maze.iterate()
    drawmaze(my_maze)

if __name__ == '__main__':

    if parse_argv() == 1:
        print("Opción json")
    elif parse_argv()== 2:
        main()

