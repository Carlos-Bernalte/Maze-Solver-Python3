import Maze, pygame, sys, time, jsonManager

#---Glogal Variables---#
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


WIDTH=620
HIGHT=620
screen = pygame.display.set_mode((WIDTH,HIGHT))

jsonM= jsonManager.jsonManager()
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
    pygame.display.set_caption("Lab_"+str(maze.rows)+"_"+str(maze.columns))
    while 1:
        for Evento in pygame.event.get():
            if Evento.type == pygame.QUIT:
                pygame.image.save(screen, "results/Lab_"+str(maze.rows)+"_"+str(maze.columns)+".jpg")
                sys.exit()
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
        pygame.display.flip()
    pygame.quit()

def generateFromJson():
    #rows=sys.argv[1]
    #columns=sys.argv[2]
    rows = jsonM.get_nrows()
    columns= jsonM.get_ncols()

    pygame.display.set_caption("Lab_"+str(rows)+"_"+str(columns))

    if rows>columns:
        sizeCell=600/rows
    else:
        sizeCell=600/columns
    
    my_maze = Maze.Maze(columns,rows)
    my_maze.iterate()
    drawMaze(my_maze, sizeCell)

def main():
    #rows=sys.argv[1]
    #columns=sys.argv[2]
    rows = 100
    columns= 100
    sizeCell=600/rows
    
    my_maze = Maze.Maze(columns,rows)
    my_maze.iterate()
    drawMaze(my_maze, sizeCell)

if __name__ == '__main__':
    #parse_argv()
    main()

