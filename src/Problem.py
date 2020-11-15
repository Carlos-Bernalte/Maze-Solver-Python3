import Node
import Frontier
from Functions import succerssorFunction

class Problem:
    def __init__(self, initial, objetive,strategy):
        self.initial=(int(initial[1]), int(initial[4]))
        self.objective=(int(objetive[1]), int(objetive[4]))
        self.strategy=strategy

    def goal(self, state):
        if state == self.objective:
            return True
        else:
            return False



