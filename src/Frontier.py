#!/usr/bin/python3
# -- coding: utf-8 --


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
                self.insertNode(node)


    def insertNode(self, node):
        if (len(self.frontier)==0):
            self.frontier.append(node)
        else:
            x=len(self.frontier)-1
            while x>=0:
                if((self.frontier[x].value < node.value)):
                    self.frontier.insert(x+1,node)
                    break
                elif(self.frontier[x].value == node.value):
                    if(self.frontier[x].idState[0] < node.idState[0]): 
                        self.frontier.insert(x+1,node)
                        break
                    else:
                        if(self.frontier[x].idState[0] == node.idState[0]):
                            if(self.frontier[x].idState[1] < node.idState[1] ):
                                self.frontier.insert(x+1,node)
                                break
                            elif (self.frontier[x].idState[1] == node.idState[1]):
                                if (self.frontier[x].idNode < node.idNode):
                                    self.frontier.insert(x+1,node)
                                    break
                if (x==0):
                    self.frontier.insert(0,node)
                x= x-1


