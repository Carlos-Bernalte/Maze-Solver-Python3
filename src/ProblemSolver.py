import Frontier
import Node
from Functions import succerssorFunction
from Drawer import drawSolution
class Problem:
    def __init__(self, initial, objetive,strategy, maze):
        self.initial=(int(initial[1]), int(initial[4]))
        self.objective=(int(objetive[1]), int(objetive[4]))
        self.strategy=strategy
        self.maze=maze
        self.closed=[]
        self.fringe=Frontier.Frontier()

    def searchSolution (self):
        heuristic=abs(self.initial[0]-self.objective[0])+abs(self.initial[1]-self.objective[1])
        self.fringe.insertNode(Node.Node(self.initial,0,None,None,0,heuristic,8))
        while(1):
            if self.fringe.isEmpty():
                print("The frontier is empty.")
                return None
            else:
                currentNode=self.fringe.removeNode()
                if self.goal(currentNode.idState):
                    return solution(currentNode)
                if not isIn(currentNode, self.closed):
                    neighbors=succerssorFunction(currentNode, self.maze)
                    self.fringe.insertList(self.initNodes(currentNode, neighbors, self.objective))
                    self.closed.append(currentNode)
    
    def initNodes(self,currentNode=Node, neighbors=[], objective=()):
        listNode=[]
        for neig in neighbors:
            cost=currentNode.cost+neig[2]+1
            f=self.heuristic(currentNode.idState)
            value=cost+f
            node=Node.Node(neig[1],currentNode.cost+neig[2]+1,currentNode,neig[0], currentNode.depth+1,f, value)
            listNode.append(node)
        return listNode

    



    def heuristic(self,currentNode):
        return abs(currentNode[0]-self.objective[0])+abs(currentNode[1]-self.objective[1])

    def goal(self, state):
        if state == self.objective:
            return True
        else:
            return False

def isIn(currentNode, closed):
    for node in closed:
        if node.idState == currentNode.idState:
            return True
    return False

def solution(nodeSolution):
        sol = []
        node = nodeSolution
        while node is not None:
            sol.insert(0,node)
            node = node.parent
        return sol