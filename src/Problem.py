import Node
import Frontier
from Functions import succerssorFunction

class Problem:
    def __init__(self, initial, objetive,strategy):
        self.initial=(int(initial[0]),int(initial[1]))
        self.objective=(int(objetive[0]),int(objetive[1]))
        self.strategy=strategy
        

    def goal(self, state):
        if state == self.objective:
            return True
        else:
            return False



