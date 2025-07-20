import numpy as np
from core.beam import GaussianBeam

class System:
    def __init__(self, elements):
        self.elements = elements

    def propagate(self, beam, dz=0.001):
        z_positions = [0]
        waists = [beam.waist]
        R_curvatures = [np.inf]
        z = 0
        q = 1j * np.pi * beam.waist**2 / beam.wavelength
        all_z = []
        all_w = []
        all_R = []

        for elem in self.elements:
            # Propagate continuously through free space
            if hasattr(elem, 'length'):
                steps = int(elem.length / dz)
                M_step = np.array([[1, dz], [0, 1]])
                for _ in range(steps):
                    q = (M_step[0,0] * q + M_step[0,1]) / (M_step[1,0] * q + M_step[1,1])
                    z += dz
                    waist = np.sqrt(-beam.wavelength / (np.pi * np.imag(1/q)))
                    if np.imag(1/q) != 0:
                        R = 1/np.real(1/q)
                    else:
                        R = np.inf
                    all_z.append(z)
                    all_w.append(waist)
                    all_R.append(R)
            # Apply ABCD of lens or mirror instantly at one z
            else:
                M = elem.transfer_matrix()
                q = (M[0,0] * q + M[0,1]) / (M[1,0] * q + M[1,1])
                waist = np.sqrt(-beam.wavelength / (np.pi * np.imag(1/q)))
                if np.imag(1/q) != 0:
                    R = 1/np.real(1/q)
                else:
                    R = np.inf
                # Mark this as a discontinuity (instantaneous change)
                all_z.append(z)
                all_w.append(waist)
                all_R.append(R)
        return np.array(all_z), np.array(all_w), np.array(all_R)
