import Maze, pygame, sys, time

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

pygame.init()
clk = pygame.time.Clock()

def parse_argv():
    if len(sys.argv) != 3:
        print("The number of arguments is wrong.")
        sys.exit()
    if(not sys.argv[1].isdigit() or not sys.argv[2].isdigit()):
        print("The arguments must be digits.")
        sys.exit()

def main():
    #rows=sys.argv[1]
    #columns=sys.argv[2]
    rows=10
    columns=10

    
    Width=620
    Hight=620
    sizeCell=600/rows
    screen = pygame.display.set_mode((Width,Hight))
    pygame.display.set_caption("Lab_"+str(rows)+"_"+str(columns))
    screen.fill(WHITE)
    
    my_maze = Maze.Maze(columns,rows)
    my_maze.init_grid()
    my_maze.iterate()
    #my_maze.printMaze()


    while 1:
        for Evento in pygame.event.get():
            if Evento.type == pygame.QUIT:
                #pygame.image.save(screen, "Lab_"+str(rows)+"_"+str(columns)+".jpg")
                sys.exit()

        for i in range(my_maze.rows):
            for j in range(my_maze.columns):
                if my_maze.getMaze()[j][i].getNeigh()[0]==False:
                    pygame.draw.line(screen, BLACK, [i*sizeCell +10,j*sizeCell+10], [i*sizeCell+sizeCell +10,j*sizeCell +10], 2) #North
                if my_maze.getMaze()[j][i].getNeigh()[1]==False:
                    pygame.draw.line(screen, BLACK, [i*sizeCell+sizeCell +10,j*sizeCell+10], [i*sizeCell +10+sizeCell,j*sizeCell+sizeCell +10], 2) #East
                if my_maze.getMaze()[j][i].getNeigh()[2]==False:
                    pygame.draw.line(screen, BLACK, [i*sizeCell +10,j*sizeCell+sizeCell+10], [i*sizeCell+sizeCell +10,j*sizeCell+sizeCell +10], 2) #South
                if my_maze.getMaze()[j][i].getNeigh()[3]==False:
                    pygame.draw.line(screen, BLACK, [i*sizeCell +10,j*sizeCell+10], [i*sizeCell +10,j*sizeCell+sizeCell +10], 2) #West
        pygame.display.flip()
        clk.tick(20)
    pygame.quit()


if __name__ == '__main__':
    # parse_argv()

    main()

