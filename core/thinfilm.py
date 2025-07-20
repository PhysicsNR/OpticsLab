import numpy as np

def thin_film_reflectance(n1, n2, n3, d, wavelength):
    # n1=incident, n2=film, n3=substrate; d=thickness
    r12 = (n1 - n2) / (n1 + n2)
    r23 = (n2 - n3) / (n2 + n3)
    delta = 2 * np.pi * n2 * d / wavelength
    r = (r12 + r23 * np.exp(2j * delta)) / (1 + r12 * r23 * np.exp(2j * delta))
    R = np.abs(r)**2
    return R
