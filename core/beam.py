import numpy as np
import matplotlib.pyplot as plt

class GaussianBeam:
    def __init__(self, wavelength, waist, z0=0.0):
        self.wavelength = wavelength
        self.waist = waist
        self.z0 = z0
        self.zR = np.pi * waist**2 / wavelength  # Rayleigh range

    def w(self, z):
        return self.waist * np.sqrt(1 + ((z - self.z0) / self.zR) ** 2)

    def plot_profile(self, z_min=0, z_max=0.5, num=200):
        z = np.linspace(z_min, z_max, num)
        w = self.w(z)
        plt.plot(z, w * 1e3)
        plt.xlabel("z (m)")
        plt.ylabel("Beam radius (mm)")
        plt.title("Gaussian Beam Envelope")
        plt.grid(True)
        plt.show()
