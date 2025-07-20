import numpy as np

class Lens:
    def __init__(self, focal_length, position=0.0):
        self.focal_length = focal_length
        self.position = position

    def transfer_matrix(self):
        # Thin lens: [1, 0; -1/f, 1]
        return np.array([[1, 0], [-1/self.focal_length, 1]])
