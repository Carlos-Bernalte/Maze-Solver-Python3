class Cell():

    def __init__(self, x, y):
        self.position = (x, y)
        self.value = 0
        self.neighbours = [False, False, False, False]
        #self.neighbours = [True, True, True, True]
        self.visited = False
        self.onTrace= False
        self.come_from = ""
    def getNeigh(self):
        return self.neighbours

    def setNeigh(self, newNeigh):
        self.neighbours = newNeigh

    def getDirection(self):
        return self.come_from

    def getPosition(self):
        return self.position

    def setVisited(self):
        self.visited=True

    def setOnTrace(self):
        self.onTrace= True

    def setNotOnTrace(self):
        self.onTrace= False

    def isOnTrace(self):
        return onTrace