import Maze, Cell
def succersorFunction(state, maze):
    successors=[]
    print(state[1][0],state[1][1])
    neighbours=maze[state[1][0]][state[1][1]].getNeighbours()
    if neighbours[0]==True:
        successors.append(["N",(state[1][0], state[1][1]-1), 1])
    if neighbours[1]==True:
        successors.append(["E",(state[1][0]+1, state[1][1]), 1])
    if neighbours[2]==True:
        successors.append(["S",(state[1][0], state[1][1]+1), 1])
    if neighbours[3]==True:
        successors.append(["O",(state[1][0]-1, state[1][1]), 1])

    print(successors)
    return successors
    
