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
    fringe.insertNode(Node.Node(problem.initial,0,None,None,0,heuristic(problem.initial, problem.objective),heuristic(problem.initial, problem.objective)))
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
    drawSolution(sol,fringe.frontier,closed, maze)

def initNodes(currentNode=Node, neighbors=[], objective=(), s=""):
    listNode=[]
    for neig in neighbors:
        cost=currentNode.cost+neig[2]+1
        f=heuristic(neig[1], objective)
        value=cost+f
        
        if s == "BREADTH":
            value=currentNode.depth+1
        elif s == "DEPTH":
            value=1/(currentNode.depth+1)
        elif s == "GREEDY":
            value=f
        elif s == "UNIFORM":
            value=currentNode.cost
        elif s =="'A":
            value=cost+f

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
        
