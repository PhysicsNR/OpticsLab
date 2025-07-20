import numpy as np

class FreeSpace:
    def __init__(self, length):
        self.length = length

    def transfer_matrix(self):
        # Free-space propagation: [1, d; 0, 1]
        return np.array([[1, self.length], [0, 1]])
