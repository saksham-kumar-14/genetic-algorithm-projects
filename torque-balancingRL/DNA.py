import numpy as np
import math 
import random

class DNA:
    def __init__(self):
        # self.actions = np.zeros(100)
        self.max_capability = 50
        self.actions = []
        self.n_actions = 100

        for i in range(self.n_actions):
            x = random.randrange(-self.max_capability * 100, self.max_capability * 100)
            x /=  100
            self.actions.append(x)

    def evolution(self, new_action, idx):
        self.actions[idx] = new_action

