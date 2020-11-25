import Problem
import Frontier
import Node
from Functions import succerssorFunction
from Drawer import drawSolution

def searchAlgorithm(problem, maze):
    depth=0
    sol=None
    closed=[]
    fringe=Frontier.Frontier()
    f=heuristic(problem.initial, problem.objective)
    initial_node=Node.Node(problem.initial,0,None,None,0,f,0)
    initial_node.value=calcValue(initial_node,0,f,problem.strategy)
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
                neighbors=succerssorFunction(currentNode, maze.getMaze())
                fringe.insertList(initNodes(currentNode, neighbors, problem.objective, problem.strategy))
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

def calcValue(node,cost,f,strategy=""):
    value=0
    if strategy == "BREADTH":
        value=node.depth+1
    elif strategy == "DEPTH":
        value=1/(node.depth+1)
    elif strategy == "GREEDY":
        value=f
    elif strategy == "UNIFORM":
        value=node.cost
    elif strategy =="A":
        value=cost+f
    return value

def initNodes(currentNode=Node, neighbors=[], objective=(), s=""):
    listNode=[]
    for neig in neighbors:
        cost=currentNode.cost+neig[2]+1
        f=heuristic(neig[1], objective)
        value=calcValue(currentNode, cost, f, s)
    
        node=Node.Node(neig[1],currentNode.cost+neig[2]+1,currentNode,neig[0], currentNode.depth+1,f, value)
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
        

