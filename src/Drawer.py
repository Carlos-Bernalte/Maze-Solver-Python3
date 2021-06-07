#!/usr/bin/python3
# -- coding: utf-8 --


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
    displ=10
    im = Image.new("RGB", (HIGHT,WIDTH), (255, 255, 255))
    draw = ImageDraw.Draw(im)
    for i in range(maze.columns):
        for j in range(maze.rows):
            draw.rectangle([(i*sizeCell+displ,j*sizeCell+displ),(i*sizeCell+sizeCell+displ,j*sizeCell+sizeCell+displ)], typeOfBox(maze.grid[j][i].value))
    displ=9
    for i in range(maze.columns):
        for j in range(maze.rows):
            neighs=maze.grid[j][i].neighbours
            if neighs[0]==False:
                draw.line((i*sizeCell+displ, j*sizeCell+displ, i*sizeCell+sizeCell+displ, j*sizeCell+displ), WALLS, 2) #North
            if neighs[1]==False:
                draw.line((i*sizeCell+sizeCell+displ, j*sizeCell+displ, i*sizeCell+sizeCell+displ, j*sizeCell+sizeCell+displ), WALLS, 2) #East
            if neighs[2]==False:
                draw.line((i*sizeCell+displ, j*sizeCell+sizeCell+displ, i*sizeCell+sizeCell+displ, j*sizeCell+sizeCell+displ), WALLS, 2) #South
            if neighs[3]==False:
                draw.line((i*sizeCell+displ, j*sizeCell+displ, i*sizeCell+displ, j*sizeCell+sizeCell+displ), WALLS, 2) #West
    
    im.save("results/Lab_" + str(maze.rows) + "_" + str(maze.columns) + ".png")



def drawSolution(solution,frontier,inner_tree, maze, strategy):
    sizeCell=20
    WIDTH = sizeCell * maze.rows + 20
    HIGHT = sizeCell * maze.columns + 20
    displ=10
    im = Image.new("RGB", (HIGHT,WIDTH), (255, 255, 255))
    draw = ImageDraw.Draw(im)

    for i in range(maze.columns):
        for j in range(maze.rows):
            draw.rectangle([(i*sizeCell+displ,j*sizeCell+displ),(i*sizeCell+sizeCell+displ,j*sizeCell+sizeCell+displ)], typeOfBox(maze.grid[j][i].value))
    for node in frontier:
        position=node.idState
        draw.rectangle([(position[1]*sizeCell+displ,position[0]*sizeCell+displ),(position[1]*sizeCell+sizeCell+displ,position[0]*sizeCell+sizeCell+displ)], FRONTIER)
    
    for node in inner_tree:
        position=node.idState
        draw.rectangle([(position[1]*sizeCell+displ,position[0]*sizeCell+displ),(position[1]*sizeCell+sizeCell+displ,position[0]*sizeCell+sizeCell+displ)], INNER_TREE)

    for node in solution:
        position=node.idState
        draw.rectangle([(position[1]*sizeCell+displ,position[0]*sizeCell+displ),(position[1]*sizeCell+sizeCell+displ,position[0]*sizeCell+sizeCell+displ)], PATH)
    displ=9
    for i in range(maze.columns):
        for j in range(maze.rows):
            neighs=maze.grid[j][i].neighbours
            if neighs[0]==False:
                draw.line((i*sizeCell+displ, j*sizeCell+displ, i*sizeCell+sizeCell+displ, j*sizeCell+displ), WALLS, 2) #North
            if neighs[1]==False:
                draw.line((i*sizeCell+sizeCell+displ, j*sizeCell+displ, i*sizeCell+sizeCell+displ, j*sizeCell+sizeCell+displ), WALLS, 2) #East
            if neighs[2]==False:
                draw.line((i*sizeCell+displ, j*sizeCell+sizeCell+displ, i*sizeCell+sizeCell+displ, j*sizeCell+sizeCell+displ), WALLS, 2) #South
            if neighs[3]==False:
                draw.line((i*sizeCell+displ, j*sizeCell+displ, i*sizeCell+displ, j*sizeCell+sizeCell+displ), WALLS, 2) #West

    im.save("results/Resolved_Lab_" + str(maze.rows) + "_" + str(maze.columns) + "_"+strategy+".png")

def typeOfBox(value):
    if value==0:
        return ASPHALT
    if value==1:
        return EARTH
    if value==2:
        return GRASS
    if value==3:
        return WATER