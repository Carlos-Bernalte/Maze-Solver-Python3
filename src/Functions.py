#!/usr/bin/python3
# -- coding: utf-8 --

def succerssorFunction(node, maze):
    successors=[]
    neighbours=maze[node.idState[0]][node.idState[1]].neighbours
    if neighbours[0]==True:
        successors.append(("N",(node.idState[0]-1, node.idState[1]), maze[node.idState[0]-1][node.idState[1]].value))
    if neighbours[1]==True:
        successors.append(("E",(node.idState[0], node.idState[1]+1), maze[node.idState[0]][node.idState[1]+1].value))
    if neighbours[2]==True:
        successors.append(("S",(node.idState[0]+1, node.idState[1]), maze[node.idState[0]+1][node.idState[1]].value))
    if neighbours[3]==True:
        successors.append(("O",(node.idState[0], node.idState[1]-1), maze[node.idState[0]][node.idState[1]-1].value))
    return successors
    
