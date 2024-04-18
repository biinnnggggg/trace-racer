import numpy as np 

# Constants
INF : float = 10e12
PI : float = 3.1415926535897932385

RNG = np.random.default_rng()

# Utility functions

def deg_to_rad(degrees : float) -> float:
    """Converts an angle from degrees to radians.
    """
    return degrees * PI / 180.0

def rand_in_unit_sphere():
        while True:
            p = RNG.random(3)
            if np.linalg.norm(p) < 1: return p

def rand_unit_vector():
        vec = rand_in_unit_sphere()
        return vec / np.linalg.norm(vec)