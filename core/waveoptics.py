import numpy as np

def fresnel_diffraction_1d(x, z, wavelength, aperture_func):
    # Simple 1D Fresnel integral
    k = 2 * np.pi / wavelength
    dx = x[1] - x[0]
    u0 = aperture_func(x)
    U = np.zeros_like(x, dtype=complex)
    for i, xi in enumerate(x):
        U[i] = np.sum(u0 * np.exp(1j * k * (xi - x)**2 / (2*z))) * dx
    return U
