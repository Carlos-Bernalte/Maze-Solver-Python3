class Cell():

    def __init__(self, x, y):
        self.position = (x, y)
        self.value = 0
        self.neighbours = [False, False, False, False]
        #self.neighbours = [True, True, True, True]
        self.visited = False
        self.come_from = ""
    def getNeigh(self):
        return self.neighbours

    def setNeigh(self, newNeigh):
        self.neighbours = newNeigh

    def getPosition(self):
        return self.position