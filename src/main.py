import Maze, pygame, sys, time

#---Glogal Variables---#
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
def size_window():
    print()

def main():
    #rows=sys.argv[1]
    #columns=sys.argv[2]
    rows=100
    columns=100
    pygame.display.set_caption("Lab_"+str(rows)+"_"+str(columns))

    sizeCell=600/rows
    
    my_maze = Maze.Maze(columns,rows)
    my_maze.iterate()


    while 1:
        for Evento in pygame.event.get():
            if Evento.type == pygame.QUIT:
                pygame.image.save(screen, "results/Lab_"+str(rows)+"_"+str(columns)+".jpg")
                sys.exit()
        #--Here the maze will be draw
        for i in range(rows):
            for j in range(columns):
                if my_maze.getMaze()[j][i].getNeigh()[0]==False:
                    pygame.draw.line(screen, BLACK, [i*sizeCell +10,j*sizeCell+10], [i*sizeCell+sizeCell +10,j*sizeCell +10], 2) #North
                if my_maze.getMaze()[j][i].getNeigh()[1]==False:
                    pygame.draw.line(screen, BLACK, [i*sizeCell+sizeCell +10,j*sizeCell+10], [i*sizeCell +10+sizeCell,j*sizeCell+sizeCell +10], 2) #East
                if my_maze.getMaze()[j][i].getNeigh()[2]==False:
                    pygame.draw.line(screen, BLACK, [i*sizeCell +10,j*sizeCell+sizeCell+10], [i*sizeCell+sizeCell +10,j*sizeCell+sizeCell +10], 2) #South
                if my_maze.getMaze()[j][i].getNeigh()[3]==False:
                    pygame.draw.line(screen, BLACK, [i*sizeCell +10,j*sizeCell+10], [i*sizeCell +10,j*sizeCell+sizeCell +10], 2) #West
        pygame.display.flip()
    pygame.quit()


if __name__ == '__main__':
    #parse_argv()
    main()

