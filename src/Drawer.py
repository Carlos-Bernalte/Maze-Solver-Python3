from PIL import Image, ImageDraw

WALLS=(0, 0, 0)
ASPHALT=(255, 255, 255)
EARTH=(224, 211, 27)
GRASS=(112, 255, 110)
WATER=(110, 214, 255)

PATH=(255, 0, 0)
FRONTIER=(0, 0, 255)
INNER_TREE=(0,255,0)

def drawMaze(maze):
    sizeCell=20
    
    WIDTH = sizeCell * maze.rows + 20
    HIGHT = sizeCell * maze.columns + 20

    im = Image.new("RGB", (HIGHT,WIDTH), (255, 255, 255))
    draw = ImageDraw.Draw(im)
    for i in range(maze.columns):
        for j in range(maze.rows):
            draw.rectangle([(i*sizeCell+10,j*sizeCell+10),(i*sizeCell+sizeCell+10,j*sizeCell+sizeCell+10)], typeOfBox(maze.getMaze()[j][i].value))
    for i in range(maze.columns):
        for j in range(maze.rows):
            if maze.getMaze()[j][i].getNeighbours()[0]==False:
                draw.line((i*sizeCell+10, j*sizeCell+10, i*sizeCell+sizeCell+10, j*sizeCell+10), WALLS, 2) #North
            if maze.getMaze()[j][i].getNeighbours()[1]==False:
                draw.line((i*sizeCell+sizeCell+10, j*sizeCell+10, i*sizeCell+10+sizeCell, j*sizeCell+sizeCell+10), WALLS, 2) #East
            if maze.getMaze()[j][i].getNeighbours()[2]==False:
                draw.line((i*sizeCell+10, j*sizeCell+sizeCell+10, i*sizeCell+sizeCell+10, j*sizeCell+sizeCell+10), WALLS, 2) #South
            if maze.getMaze()[j][i].getNeighbours()[3]==False:
                draw.line((i*sizeCell+10, j*sizeCell+10, i*sizeCell+10, j*sizeCell+sizeCell+10), WALLS, 2) #West

    im.show()
    #im.save("results/Lab_" + str(maze.rows) + "_" + str(maze.columns) + ".jpg")


def drawPath(frontier, maze):
    sizeCell=20
    
    WIDTH = sizeCell * maze.rows + 20
    HIGHT = sizeCell * maze.columns + 20

    im = Image.new("RGB", (HIGHT,WIDTH), (255, 255, 255))
    draw = ImageDraw.Draw(im)
    for node in frontier:
        position=node[1]
        draw.rectangle([(position[0]*sizeCell+10,position[1]*sizeCell+10),(position[0]*sizeCell+sizeCell+10,position[1]*sizeCell+sizeCell+10)], fill=(0, 166, 255))
    
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
    im.show()
    #im.save("results/Resolved_Lab_" + str(maze.columns) + "_" + str(maze.rows) + ".jpg")

def typeOfBox(value):
    if value==0:
        return ASPHALT
    if value==1:
        return EARTH
    if value==2:
        return GRASS
    if value==3:
        return WATER