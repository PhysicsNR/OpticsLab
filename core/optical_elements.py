import numpy as np

class FreeSpace:
    def __init__(self, length):
        self.length = length

    def transfer_matrix(self):
        return np.array([[1, self.length], [0, 1]])

class Lens:
    def __init__(self, focal_length):
        self.focal_length = focal_length

    def transfer_matrix(self):
        return np.array([[1, 0], [-1/self.focal_length, 1]])

class Mirror:
    def __init__(self):
        pass  # Flat mirror for ABCD is identity

    def transfer_matrix(self):
        return np.array([[1, 0], [0, 1]])

# Add more as needed (Prism, Curved Mirror, etc.)
