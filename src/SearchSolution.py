#!/usr/bin/python3
# -- coding: utf-8 --

import Frontier
import Node
from Drawer import drawSolution

def searchAlgorithm(problem, maze):
    depth=0
    sol=None
    closed=[]
    fringe=Frontier.Frontier()

    initial_node=Node.Node()
    initial_node.idState=problem.initial
    initial_node.cost=0
    initial_node.parent=None
    initial_node.action=None
    initial_node.depth=0
    initial_node.heuristic=heuristic(problem.initial, problem.objective)
    initial_node.value=calcValue(initial_node, problem.strategy)
    fringe.insertNode(initial_node)

    while(1):
        if depth==1000000:
            print("The algorithm arrrives to the limit of iteractions")
            break
        elif fringe.isEmpty():
            print("The frontier is empty.")
            break
        else:
            currentNode=fringe.removeNode()
            if problem.goal(currentNode.idState):
                sol=solution(currentNode)
                break
            if not isIn(currentNode, closed):
                neighbors=succerssorFunction(currentNode, maze.grid)
                fringe.insertList(initNodes(currentNode, neighbors, problem.objective, problem.strategy,maze.grid))
                closed.append(currentNode)
                depth+=1
    writeSolution(sol,problem.strategy, maze)
    drawSolution(sol,fringe.frontier,closed, maze,problem.strategy)

def writeSolution(solution,strategy,maze):
    solution_txt = open("results/solution_"+str(maze.rows)+"x"+str(maze.columns)+"_"+strategy+".txt","w")
    solution_txt.write("[id][cost,state,father_id,action,depth,h,value]")     
    for n in solution:
        solution_txt.write("\n"+n.toString())
    solution_txt.close() 

def calcValue(node: Node,strategy: str):

    if strategy == "BREADTH":
        return node.depth
    elif strategy == "DEPTH":
        return 1/(node.depth+1)
    elif strategy == "GREEDY":
        return node.heuristic
    elif strategy == "UNIFORM":
        return node.cost
    elif strategy =="A":
        return node.cost+node.heuristic

def initNodes(currentNode=Node, neighbors=[], objective=(), s="",maze=[]):
    listNode=[]
    for neig in neighbors:
        node=Node.Node()
        node.idState=neig[1]
        #node.cost=currentNode.cost+neig[2]+1
        # node.cost=currentNode.cost+abs(maze[currentNode.idState[0]][currentNode.idState[1]].value-maze[node.idState[0]][node.idState[1]].value)+1
        node.cost=currentNode.cost+((currentNode.idState[1] % 2)+1)*(maze[node.idState[0]][node.idState[1]].value + 1)
        node.parent=currentNode
        node.action=neig[0]
        node.depth=currentNode.depth+1
        node.heuristic=heuristic(neig[1], objective)
        node.value=calcValue(node, s)
        
        listNode.append(node)
    return listNode

def isIn(currentNode, closed):
    for node in closed:
        if node.idState == currentNode.idState:
            return True
    return False

def heuristic(currentNode, objective):
    return abs(currentNode[0]-objective[0])+abs(currentNode[1]-objective[1])

def solution(nodeSolution):
    sol = []
    node = nodeSolution
    while node is not None:
        sol.insert(0,node)
        node = node.parent
    return sol
        
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
