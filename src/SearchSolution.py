import Problem
import Frontier
import Node
from Functions import succerssorFunction
def searchAlgorithm(problem=Problem, maze=[]):
    ite=0
    closed=[]
    fringe=Frontier.Frontier()
    heuristic=abs(problem.initial[0]-problem.objective[0])+abs(problem.initial[1]-problem.objective[1])
    fringe.insertNode(Node.Node(problem.initial,0,None,None,0,heuristic,8))
    while(1):
        if fringe.isEmpty():
            print("The frontier is empty.")
            return None
        else:
            currentNode=fringe.removeNode()
            print(currentNode.idState)
            if problem.goal(currentNode.idState):
                print("SOLUCION CON ", ite, "ITERACCIONES")
                return solution(currentNode)
            if isIn(currentNode, closed):
                print("CUT")
            else:
                neighbors=succerssorFunction(currentNode, maze)
                fringe.insertList(initNodes(currentNode, neighbors, problem.objective))
                closed.append(currentNode)
        ite+=1

def initNodes(currentNode=Node, neighbors=[], objective=()):
    listNode=[]
    for neig in neighbors:
        cost=currentNode.cost+neig[2]+1
        heuristic=abs(neig[1][0]-objective[0])+abs(neig[1][1]-objective[1])
        value=cost+heuristic
        node=Node.Node(neig[1],currentNode.cost+neig[2]+1,currentNode,neig[0], currentNode.depth+1, heuristic, value)
        listNode.append(node)
    return listNode


def isIn(currentNode, closed):
    for node in closed:
        if node.idState == currentNode.idState:
            return True
    return False

def heuristic(self, currentNode):
    return abs(currentNode[0]-self.objetive[0])+abs(currentNode[1]-self.objetive[1])

def solution(nodeSolution):
    sol = []
    node = nodeSolution
    while node is not None:
        sol.append(node)
        node = node.parent
    return sol
        

