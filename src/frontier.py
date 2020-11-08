class Frontier:
    def __init__(self):
        self.frontier=[]

    def removeNode(self):
        if (self.frontier):
            nodeList = self.frontier.pop(0)
            return nodeList
        else:
            return None

    def isEmpty(self):
        if (self.frontier):
            return False
        else:
            return True

    def insertList(self, nodeList):
        if(nodeList is not None):
            for node in nodeList:
                self.inserNode(node)


    def insertNode(self, node):
        if (len(self.frontier)==0):
            self.frontier.append(node)
        else:
            x=0
            while x< len(self.frontier):
                if (self.frontier[x].idState.equals(node.idState)):
                    break
                x+=1
            if x==len(self.frontier):
                self.frontier.insert(len(self.frontier),node)
